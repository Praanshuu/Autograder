# Analysis of "Srivatsanb123/Coderunner"

## Architecture Overview
*   **Language**: Go (Golang) v1.x
*   **Framework**: Gin (Web Framework)
*   **Execution Model**: Local Subprocess (`os/exec`)
*   **Concurrency Model**: Goroutines

## How it Execution Logic Works

### 1. Request Handling (Gin)
The server accepts HTTP POST requests. Go's `net/http` (used by Gin) creates a **lightweight Goroutine** for every single incoming request.
*   **Comparison**: Python (Django/Flask) typically uses a Thread per request. A thread consumes ~1MB-8MB RAM. A Goroutine consumes ~2KB.
*   **Impact**: This allows the server to *accept* 1000s of requests instantly without running out of RAM, whereas a standard Python server might choke after a few hundred concurrent threads.

### 2. The Execution Function (`runner.go`)
When a request comes in:
1.  **Unique Workspace**: It generates a UUID (`jobID = uuid.New().String()`) and creates a folder `jobs/<uuid>`.
2.  **File Creation**: Writes the code to disk (e.g., `program.py`).
3.  **Compilation (If needed)**: Runs `exec.Command("gcc", ...)` and waits.
4.  **Parallel Test Cases**:
    *   It loops through all inputs (`inputs []string`).
    *   It enters a **WaitGroup** (`wg.Add(1)`).
    *   It launches a **new Goroutine** for each test case (`go func(...)`).
    *   Inside that Goroutine, it spawns a subprocess `exec.Command("python", ...)`.

### 3. Why it handles "100s of users"
The key is **Non-Blocking I/O** managed by the Go scheduler.
*   In Python, if you have 10 workers and 10 students submit code, the 11th waits.
*   In Go + this architecture, if 100 students submit code:
    *   The server accepts ALL 100 requests immediately.
    *   It spawns 100 x (Test Cases) Goroutines.
    *   Each Goroutine tries to spawn a OS Process (Python/GCC).
    *   **The Bottleneck**: The operating system. The *server* code handles the load fine, but the *CPU* will eventually hit 100% trying to switch between 500 active Python processes.

## Strengths vs Weaknesses

### Strengths
*   **High Throughput**: Can accept traffic bursts much better than Python.
*   **Parallel Execution**: Running test cases in parallel reduces the *latency* perceived by the student (total wait time).
*   **Simplicity**: No complex queue (Redis/RabbitMQ) needed for medium loads because Go buffers the complexity.

### Weaknesses (Critical)
*   **Security risks**: Code runs on the *host machine*. If I submit `os.removeAll("/")`, I could potentially damage the server (execution user permissions are key).
*   **Resource Exhaustion**: There is no apparent "Queue" or "Limit". If 1000 users submit simultaneously, it creates 1000 processes. This can crash the server (Fork Bomb).
*   **No Isolation**: All processes share the same OS kernel namespace directly.

## Recommendation for Autograder
We can adopt the **Parallel Test Case** strategy using Python's `ThreadPoolExecutor`. While Python threads are heavier than Goroutines, for 5-10 local users or 150 Docker users, the architectural bottleneck is the *Docker Container overhead*, not the Python thread overhead.
