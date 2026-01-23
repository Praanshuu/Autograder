# src/modules/dynamic_analyzer.py
from __future__ import annotations

import ast
import contextlib
import io
import json
import math
import os
import tarfile
import threading
from pathlib import Path
from typing import Any

import docker


# --- Constants ---
CONTAINER_WORKING_DIR = "/usr/src/app"
CONTAINER_TEMP_DIR = "/tmp"
INPUT_FILE_NAME = "input.txt"
RUNNER_FILE_NAME = "runner.py"

PYTHON_IMAGE = "python:3.10-slim"
C_IMAGE = "gcc:13-bookworm"
JAVA_IMAGE = "eclipse-temurin:21-jdk"

EXECUTION_TIMEOUT_SECONDS = 5


class DynamicAnalyzer:
    def __init__(self):
        self.client = None
        try:
            self.client = docker.from_env()
            self.client.ping()
            print("[DYNAMIC] Docker client initialized.")
        except Exception as e:
            print(f"[DYNAMIC] Docker init error: {e}")

    # ----------------------------
    # Common helpers
    # ----------------------------
    def _create_tar_from_string(self, content_str: str, filename: str) -> io.BytesIO:
        tar_stream = io.BytesIO()
        with tarfile.open(fileobj=tar_stream, mode="w:") as tar:
            data = content_str.encode("utf-8", errors="ignore")
            tarinfo = tarfile.TarInfo(name=filename)
            tarinfo.size = len(data)
            tar.addfile(tarinfo, io.BytesIO(data))
        tar_stream.seek(0)
        return tar_stream

    def _normalize_output(self, output: str):
        output = (output or "").strip()
        if not output:
            return ""
        # Try JSON
        try:
            return json.loads(output)
        except Exception:
            pass
        # Try Python literal
        try:
            return ast.literal_eval(output)
        except Exception:
            pass
        # Try numeric
        try:
            if "." in output:
                return float(output)
            return int(output)
        except Exception:
            pass
        return output

    def _compare_outputs(self, actual, expected) -> bool:
        """Comparison tolerant to floats, otherwise strict-ish string compare."""
        # numbers
        if isinstance(actual, (int, float)) and isinstance(expected, (int, float)):
            return math.isclose(float(actual), float(expected), rel_tol=1e-6, abs_tol=1e-6)
        # strings
        return str(actual).strip() == str(expected).strip()

    def _exec_with_timeout(self, container, cmd: list[str]) -> tuple[int | None, str, str]:
        exit_code_ref = [None]
        out_ref = [(b"", b"")]
        err_ref = [None]

        def target():
            try:
                ec, out = container.exec_run(cmd, demux=True)
                exit_code_ref[0] = ec
                out_ref[0] = out if out else (b"", b"")
            except Exception as e:
                err_ref[0] = e

        t = threading.Thread(target=target, daemon=True)
        t.start()
        t.join(EXECUTION_TIMEOUT_SECONDS)

        if t.is_alive():
            return None, "", "Execution timed out."

        if err_ref[0]:
            return None, "", f"System exec error: {err_ref[0]}"

        stdout_b, stderr_b = out_ref[0]
        stdout = (stdout_b or b"").decode("utf-8", errors="ignore").strip()
        stderr = (stderr_b or b"").decode("utf-8", errors="ignore").strip()
        return exit_code_ref[0], stdout, stderr

    # ----------------------------
    # Python runner (program + function mode)
    # ----------------------------
    def _generate_python_runner(self, module_name: str, mode: dict, input_path: str) -> str:
        """
        Runner reads input_path. If program mode: redirects stdin and executes module as __main__.
        If function mode: loads JSON input and calls entry_point.
        """
        exec_type = mode.get("type", "program")
        entry_point = mode.get("entry_point")
        output_map = mode.get("output_map", None)

        # We keep this runner self-contained (no external deps)
        return f"""
import sys
import os
import json
import importlib
import runpy
import contextlib
import io

WORKDIR = {CONTAINER_WORKING_DIR!r}
INPUT_PATH = {input_path!r}
MODULE = {module_name!r}
EXEC_TYPE = {exec_type!r}
ENTRY = {entry_point!r}
OUTPUT_MAP = {output_map!r}

if WORKDIR not in sys.path:
    sys.path.insert(0, WORKDIR)

def _read_input_text():
    try:
        with open(INPUT_PATH, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception:
        return ""

def _read_input_json():
    txt = _read_input_text().strip()
    if not txt:
        return None
    try:
        return json.loads(txt)
    except Exception:
        # If not JSON, pass raw string
        return txt

def _call_function(func, inp):
    # Common conventions:
    # - dict => **kwargs
    # - list/tuple => *args
    # - other => single argument
    if isinstance(inp, dict):
        return func(**inp)
    if isinstance(inp, (list, tuple)):
        return func(*inp)
    return func(inp)

error_occurred = False

try:
    if EXEC_TYPE == "program":
        # redirect stdin from input file
        txt = _read_input_text()
        buf_in = io.StringIO(txt)
        sys.stdin = buf_in
        runpy.run_module(MODULE, run_name="__main__")
        # Any prints from student program are already on stdout
    else:
        if not ENTRY:
            raise ValueError("Function mode requires execution_mode.entry_point in config.")
        mod = importlib.import_module(MODULE)
        if not hasattr(mod, ENTRY):
            raise AttributeError(f"Function '{{ENTRY}}' not found in module '{{MODULE}}'")
        func = getattr(mod, ENTRY)

        inp = _read_input_json()

        out_buf = io.StringIO()
        with contextlib.redirect_stdout(out_buf):
            result = _call_function(func, inp)

        printed = out_buf.getvalue().strip()

        if result is not None:
            if isinstance(result, bool) and OUTPUT_MAP:
                print(OUTPUT_MAP.get("true_value","True") if result else OUTPUT_MAP.get("false_value","False"))
            else:
                print(result)
        else:
            if printed:
                print(printed)

except Exception as e:
    print(f"[RUNNER ERROR] {{e.__class__.__name__}}: {{e}}", file=sys.stderr)
    error_occurred = True

sys.exit(1 if error_occurred else 0)
"""

    def _run_python_test_case(self, code_path: Path, mode_config: dict, input_str: str) -> tuple[int | None, str, str]:
        """
        Runs one test case for Python using a runner in a container.
        Keeps the same concept you already use (runner + input file per test).
        """
        module_name = code_path.stem
        volume_mount = {str(code_path.parent.resolve()): {"bind": CONTAINER_WORKING_DIR, "mode": "ro"}}
        container = None

        try:
            container = self.client.containers.run(
                PYTHON_IMAGE,
                command=["/bin/sh", "-c", "sleep infinity"],
                detach=True,
                volumes=volume_mount,
                working_dir=CONTAINER_WORKING_DIR,
                mem_limit="4096m",
                network_disabled=True,
                pids_limit=1024,
            )

            input_target = f"{CONTAINER_TEMP_DIR}/{INPUT_FILE_NAME}"
            runner_target = f"{CONTAINER_TEMP_DIR}/{RUNNER_FILE_NAME}"

            runner_code = self._generate_python_runner(module_name, mode_config, input_target)

            # Copy runner.py and input.txt into container /tmp
            container.put_archive(CONTAINER_TEMP_DIR, self._create_tar_from_string(input_str, INPUT_FILE_NAME))
            container.put_archive(CONTAINER_TEMP_DIR, self._create_tar_from_string(runner_code, RUNNER_FILE_NAME))

            # Execute runner
            cmd = ["bash", "-lc", f"python3 -u {runner_target}"]
            return self._exec_with_timeout(container, cmd)

        finally:
            if container:
                try:
                    container.remove(force=True)
                except Exception:
                    pass

    # ----------------------------
    # C / Java (compile once per submission, run many tests)
    # ----------------------------
    def _analyze_c_submission(self, submission: dict) -> list[dict]:
        config = submission["config"]
        code_path = Path(submission["code_path"])
        volume_mount = {str(code_path.parent.resolve()): {"bind": CONTAINER_WORKING_DIR, "mode": "ro"}}
        results: list[dict] = []
        container = None

        try:
            container = self.client.containers.run(
                C_IMAGE,
                command=["bash", "-lc", "sleep infinity"],
                detach=True,
                volumes=volume_mount,
                working_dir=CONTAINER_WORKING_DIR,
                mem_limit="4096m",
                network_disabled=True,
                pids_limit=1024,
            )

            container_src = f"{CONTAINER_WORKING_DIR}/{code_path.name}"

            # Compile once
            build_cmd = [
                "bash",
                "-lc",
                "set -e; mkdir -p /tmp/work; "
                f"cp {container_src} /tmp/work/main.c; "
                "gcc -std=c11 -O2 -pipe /tmp/work/main.c -o /tmp/work/a.out -lm",
            ]
            ec, so, se = self._exec_with_timeout(container, build_cmd)
            if ec is None:
                return [{"name": "build", "status": "timeout", "error": se or "Build timed out"}]
            if ec != 0:
                return [{"name": "build", "status": "compile_error", "error": se or so or "C compilation failed"}]

            # Run tests
            for test in config.get("test_cases", []):
                name = test.get("name", "test")
                input_raw = test.get("input", "")
                expected = test.get("expected_output", "")
                expected_str = str(expected).strip()

                input_str = json.dumps(input_raw) if isinstance(input_raw, (list, dict)) else str(input_raw)

                # Put input
                container.put_archive(CONTAINER_TEMP_DIR, self._create_tar_from_string(input_str, INPUT_FILE_NAME))
                input_target = f"{CONTAINER_TEMP_DIR}/{INPUT_FILE_NAME}"

                run_cmd = ["bash", "-lc", f"/tmp/work/a.out < {input_target}"]
                ec, out, err = self._exec_with_timeout(container, run_cmd)

                if ec is None:
                    results.append({"name": name, "status": "timeout", "error": err or "Timed out"})
                    continue
                if ec != 0:
                    results.append({"name": name, "status": "runtime_error", "error": err or "Runtime error"})
                    continue

                actual_norm = self._normalize_output(out)
                expected_norm = self._normalize_output(expected_str)

                if self._compare_outputs(actual_norm, expected_norm):
                    results.append({"name": name, "status": "pass"})
                else:
                    results.append(
                        {
                            "name": name,
                            "status": "fail",
                            "expected": expected_str,
                            "actual": out,
                            "stderr_on_fail": err,
                        }
                    )

            return results

        finally:
            if container:
                try:
                    container.remove(force=True)
                except Exception:
                    pass

    def _analyze_java_submission(self, submission: dict) -> list[dict]:
        config = submission["config"]
        code_path = Path(submission["code_path"])
        volume_mount = {str(code_path.parent.resolve()): {"bind": CONTAINER_WORKING_DIR, "mode": "ro"}}
        results: list[dict] = []
        container = None

        try:
            container = self.client.containers.run(
                JAVA_IMAGE,
                command=["bash", "-lc", "sleep infinity"],
                detach=True,
                volumes=volume_mount,
                working_dir=CONTAINER_WORKING_DIR,
                mem_limit="4096m",
                network_disabled=True,
                pids_limit=1024,
            )

            container_src = f"{CONTAINER_WORKING_DIR}/{code_path.name}"

            # Compile once (MVP assumes Main.java / class Main)
            build_cmd = [
                "bash",
                "-lc",
                "set -e; mkdir -p /tmp/work; "
                f"cp {container_src} /tmp/work/Main.java; "
                "javac -encoding UTF-8 -d /tmp/work /tmp/work/Main.java",
            ]
            ec, so, se = self._exec_with_timeout(container, build_cmd)
            if ec is None:
                return [{"name": "build", "status": "timeout", "error": se or "Build timed out"}]
            if ec != 0:
                return [{"name": "build", "status": "compile_error", "error": se or so or "Java compilation failed"}]

            # Run tests
            for test in config.get("test_cases", []):
                name = test.get("name", "test")
                input_raw = test.get("input", "")
                expected = test.get("expected_output", "")
                expected_str = str(expected).strip()

                input_str = json.dumps(input_raw) if isinstance(input_raw, (list, dict)) else str(input_raw)

                container.put_archive(CONTAINER_TEMP_DIR, self._create_tar_from_string(input_str, INPUT_FILE_NAME))
                input_target = f"{CONTAINER_TEMP_DIR}/{INPUT_FILE_NAME}"

                run_cmd = ["bash", "-lc", f"java -cp /tmp/work Main < {input_target}"]
                ec, out, err = self._exec_with_timeout(container, run_cmd)

                if ec is None:
                    results.append({"name": name, "status": "timeout", "error": err or "Timed out"})
                    continue
                if ec != 0:
                    results.append({"name": name, "status": "runtime_error", "error": err or "Runtime error"})
                    continue

                actual_norm = self._normalize_output(out)
                expected_norm = self._normalize_output(expected_str)

                if self._compare_outputs(actual_norm, expected_norm):
                    results.append({"name": name, "status": "pass"})
                else:
                    results.append(
                        {
                            "name": name,
                            "status": "fail",
                            "expected": expected_str,
                            "actual": out,
                            "stderr_on_fail": err,
                        }
                    )

            return results

        finally:
            if container:
                try:
                    container.remove(force=True)
                except Exception:
                    pass

    # ----------------------------
    # Main entry
    # ----------------------------
    def analyze(self, submission: dict) -> dict:
        student_id = submission.get("student_id", "Unknown")
        print(f"\n[🔍] Dynamic analysis for: {student_id}")

        if not self.client:
            submission["analysis"]["dynamic"] = [{"name": "all_tests", "status": "skipped", "error": "Docker unavailable"}]
            return submission

        config = submission.get("config", {})
        language = (config.get("language") or submission.get("language") or "python").strip().lower()
        mode_config = config.get("execution_mode", {"type": "program"})

        # --- Multilingual dispatch (Python remains program + function mode) ---
        if language == "c":
            submission["analysis"]["dynamic"] = self._analyze_c_submission(submission)
            print(f"[✅] Completed dynamic analysis for {student_id}")
            return submission

        if language == "java":
            submission["analysis"]["dynamic"] = self._analyze_java_submission(submission)
            print(f"[✅] Completed dynamic analysis for {student_id}")
            return submission

        # --- Python path (existing behavior conceptually preserved) ---
        code_path = Path(submission["code_path"])
        results: list[dict] = []

        for test in config.get("test_cases", []):
            name = test.get("name", "test")
            input_data_raw = test.get("input", "")
            expected = test.get("expected_output", "")

            expected_str = str(expected).strip()

            # Input becomes text; for dict/list we JSON dump (works for both program stdin and function JSON)
            try:
                input_str = json.dumps(input_data_raw) if isinstance(input_data_raw, (list, dict)) else str(input_data_raw)
            except Exception:
                input_str = str(input_data_raw)

            print(f"  [TEST] {name} (python, mode={mode_config.get('type','program')})")

            ec, out, err = self._run_python_test_case(code_path, mode_config, input_str)

            if ec is None:
                results.append({"name": name, "status": "timeout", "error": err or "Timed out"})
                continue
            if ec != 0:
                results.append({"name": name, "status": "runtime_error", "error": err or "Runtime error"})
                continue

            actual_norm = self._normalize_output(out)
            expected_norm = self._normalize_output(expected_str)

            if self._compare_outputs(actual_norm, expected_norm):
                results.append({"name": name, "status": "pass"})
            else:
                results.append(
                    {
                        "name": name,
                        "status": "fail",
                        "expected": expected_str,
                        "actual": out,
                        "stderr_on_fail": err,
                    }
                )

        submission["analysis"]["dynamic"] = results
        print(f"[✅] Completed dynamic analysis for {student_id}")
        return submission
