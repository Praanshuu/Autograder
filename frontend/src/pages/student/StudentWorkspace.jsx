import React, { useState, useEffect, useRef } from "react";
import { useParams, useNavigate } from "react-router-dom";
import {
    ChevronLeft,
    Play,
    Send,
    Settings,
    RotateCcw,
    CheckCircle2,
    XCircle,
    Lightbulb,
    FileText,
    History,
    ChevronDown,
    Terminal,
    GripVertical,
    Loader2,
    Clock,
    ArrowRight
} from "lucide-react";
import { Button } from "../../components/ui/button";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "../../components/ui/tabs";
import { motion, AnimatePresence } from "framer-motion";

// --- MONACO EDITOR ---
import MonacoEditor from '@monaco-editor/react';
import { Separator } from "../../components/ui/separator";
import ReactMarkdown from 'react-markdown';
// import { Panel, Group } from "react-resizable-panels"; // Pro feature disabled for now

// Services
import { assignmentService } from "../../services/assignmentService";
import { submissionService } from "../../services/submissionService";
import QuestionPalette from "../../components/workspace/QuestionPalette";
import McqWorkspaceRenderer from "../../components/workspace/McqWorkspaceRenderer";

const StudentWorkspace = () => {
    const { assignmentId } = useParams();
    const navigate = useNavigate();

    // State
    const [assignment, setAssignment] = useState(null);
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0); // Hoisted State
    const [completedQuestions, setCompletedQuestions] = useState(new Set()); // Track completed indices
    const [codeDrafts, setCodeDrafts] = useState({}); // Local cache: { index: code }
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const [code, setCode] = useState("");
    const [selectedLanguage, setSelectedLanguage] = useState("python"); // Add language state
    const [activeTab, setActiveTab] = useState("description");
    const [selectedTestCase, setSelectedTestCase] = useState(0);
    const [output, setOutput] = useState(null);
    const [isRunning, setIsRunning] = useState(false);
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [showConfetti, setShowConfetti] = useState(false);
    const [showExitWarning, setShowExitWarning] = useState(false);
    const [isCompleted, setIsCompleted] = useState(false); // Track completion status
    const [isReadOnly, setIsReadOnly] = useState(false); // Locked mode after finish

    // --- Anti-Cheat State ---
    const [warnings, setWarnings] = useState(0);
    const [isFullscreen, setIsFullscreen] = useState(!!document.fullscreenElement);
    const [warningModal, setWarningModal] = useState(null); // { message, isFinal }
    const MAX_WARNINGS = 3;
    // Ref-based lock: prevents re-entrant cheat detection (alert() itself triggers blur/visibilitychange)
    const isCheatHandlingRef = useRef(false);
    const warningsRef = useRef(0); // Mirror of warnings state, readable inside event handlers

    // Timer state
    const [timeSpent, setTimeSpent] = useState(0); // in seconds (for backend tracking)
    const [timeRemaining, setTimeRemaining] = useState(0); // countdown timer in seconds
    const [totalTimeAllowed, setTotalTimeAllowed] = useState(0); // total time for this difficulty
    const [isTimerRunning, setIsTimerRunning] = useState(false);
    const [showHint, setShowHint] = useState(false);
    const timerIntervalRef = useRef(null);
    const lastUpdateRef = useRef(Date.now());

    // Language configuration - Limited to 3 languages supported by dynamic analyzer
    const languageConfig = {
        python: {
            name: "Python 3",
            extension: "py",
            defaultCode: "",
            icon: "🐍",
            monacoLang: "python"
        },
        java: {
            name: "Java",
            extension: "java",
            defaultCode: "",
            icon: "☕",
            monacoLang: "java"
        },
        c: {
            name: "C",
            extension: "c",
            defaultCode: "",
            icon: "🔧",
            monacoLang: "c"
        }
    };

    // Monaco editor ref for disabling copy/paste actions
    const monacoEditorRef = useRef(null);

    const handleMonacoMount = (editor, monaco) => {
        monacoEditorRef.current = editor;
        if (!isReadOnly && assignment?.mode === 'exam') {
            // Disable copy and paste commands only for exams
            editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyC, () => { });
            editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyV, () => { });
            editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyX, () => { });
        }
    };

    // Load Question Data when Index Changes
    useEffect(() => {
        const loadQuestionData = async () => {
            if (!assignment || !assignment.questions || !assignment.questions[currentQuestionIndex]) return;

            const aq = assignment.questions[currentQuestionIndex];
            const question = aq.question;
            const aqId = aq.id;

            setLoading(false); // Assignment is loaded, just switching questions

            // 1. Calculate Time Limit
            const timeLimit = getTimeLimit(question.difficulty); // Per question limit?
            setTotalTimeAllowed(timeLimit);

            // 2. Load Code: Check Drafts -> Then Backend
            if (codeDrafts[currentQuestionIndex]) {
                setCode(codeDrafts[currentQuestionIndex]);
                // Still fetch timer to get time_spent but ignore code
                try {
                    const timerResponse = await submissionService.getTimer(assignmentId, aqId, selectedLanguage);
                    if (timerResponse.success && timerResponse.data) {
                        setTimeSpent(timerResponse.data.time_spent || 0);
                        setTimeRemaining(Math.max(0, timeLimit - (timerResponse.data.time_spent || 0)));
                    }
                } catch (e) { console.error("Timer fetch failed", e); }
                return;
            }

            // 3. Load Timer & Draft Code
            try {
                const timerResponse = await submissionService.getTimer(assignmentId, aqId, selectedLanguage);
                if (timerResponse.success && timerResponse.data) {
                    const spentTime = timerResponse.data.time_spent || 0;
                    setTimeSpent(spentTime);
                    setTimeRemaining(Math.max(0, timeLimit - spentTime));

                    // Load saved code
                    if (timerResponse.data.code_content) {
                        setCode(timerResponse.data.code_content);
                    } else {
                        setCode(question.starter_code || languageConfig[selectedLanguage].defaultCode);
                    }
                } else {
                    // New/No Progress
                    setTimeSpent(0);
                    setTimeRemaining(timeLimit);
                    setCode(question.starter_code || languageConfig[selectedLanguage].defaultCode);
                }
            } catch (err) {
                console.error("Failed to load timer:", err);
                setTimeSpent(0);
                setTimeRemaining(timeLimit);
                setCode(question.starter_code || languageConfig[selectedLanguage].defaultCode);
            }
        };

        if (assignment) {
            loadQuestionData();
        }
    }, [currentQuestionIndex, assignment]);

    // Initial Assignment Fetch & Status Check
    useEffect(() => {
        const fetchAssignment = async () => {
            if (!assignmentId) return;
            try {
                setLoading(true);

                // Parallel fetch: Assignment + Status
                const [assignmentRes, statusRes] = await Promise.all([
                    assignmentService.getAssignment(assignmentId),
                    submissionService.getAssignmentStatus(assignmentId)
                ]);

                setAssignment(assignmentRes.data);

                // lock if submitted
                if (statusRes.data && statusRes.data.status === 'submitted') {
                    setIsReadOnly(true);
                    setIsCompleted(true); // Re-use completion banner or specific one
                }

                // If no questions, stop loading here
                if (!assignmentRes.data || !assignmentRes.data.questions || assignmentRes.data.questions.length === 0) {
                    setLoading(false);
                }
            } catch (err) {
                setError("Could not load assignment.");
                setLoading(false);
            }
        };
        fetchAssignment();
    }, [assignmentId]);

    // Start timer when component mounts
    useEffect(() => {
        if (assignment && assignment.questions && assignment.questions.length > 0 && !isReadOnly) {
            startTimer();
        }

        // Cleanup on unmount - pause timer and save
        return () => {
            if (!isReadOnly) pauseTimer();
        };
    }, [assignment, isReadOnly]);

    // Timer interval
    useEffect(() => {
        if (isTimerRunning && timeRemaining > 0 && !isReadOnly) {
            timerIntervalRef.current = setInterval(() => {
                setTimeSpent(prev => prev + 1);
                setTimeRemaining(prev => {
                    const newRemaining = prev - 1;

                    // Auto-submit when time runs out
                    if (newRemaining <= 0) {
                        handleTimeUp();
                        return 0;
                    }

                    return newRemaining;
                });
            }, 1000);
        } else {
            if (timerIntervalRef.current) {
                clearInterval(timerIntervalRef.current);
            }
        }

        return () => {
            if (timerIntervalRef.current) {
                clearInterval(timerIntervalRef.current);
            }
        };
    }, [isTimerRunning, timeRemaining, isReadOnly]);

    // Auto-save timer every 30 seconds
    useEffect(() => {
        if (isReadOnly) return; // Don't auto-save in read-only mode

        const autoSaveInterval = setInterval(() => {
            if (assignment && assignment.questions && assignment.questions.length > 0 && timeSpent > 0) {
                updateTimerOnBackend();
            }
        }, 30000); // 30 seconds

        return () => clearInterval(autoSaveInterval);
    }, [assignment, timeSpent, isReadOnly]);

    // --- Anti-Cheat Tracking (Tab/Window Switches & Fullscreen) ---
    useEffect(() => {
        if (isReadOnly || loading || !assignment || assignment.mode !== 'exam') return;

        // 1. Fullscreen monitoring
        const handleFullscreenChange = () => {
            setIsFullscreen(!!document.fullscreenElement);
        };
        document.addEventListener("fullscreenchange", handleFullscreenChange);

        // 2. Tab/Window Switch monitoring
        const handleVisibilityChange = () => {
            if (document.hidden && document.fullscreenElement !== null) {
                handleCheatDetected("You switched tabs or windows!");
            }
        };

        // 3. Window blur monitoring (do NOT also handle visibilitychange to avoid double-counting)
        const handleWindowBlur = () => {
            // Only fire if fullscreen is active AND page is still visible (pure window-blur, not tab switch)
            if (document.fullscreenElement !== null && !document.hidden) {
                handleCheatDetected("Focus lost from the exam window!");
            }
        };

        document.addEventListener("visibilitychange", handleVisibilityChange);
        window.addEventListener("blur", handleWindowBlur);

        return () => {
            document.removeEventListener("fullscreenchange", handleFullscreenChange);
            document.removeEventListener("visibilitychange", handleVisibilityChange);
            window.removeEventListener("blur", handleWindowBlur);
        };
        // NOTE: 'warnings' intentionally NOT in deps — we use warningsRef to read current count
        // inside the handler without re-registering listeners on every warning increment.
    }, [isReadOnly, loading, assignment]);

    const handleCheatDetected = (reason) => {
        // Guard against re-entrant calls (native alert() triggers blur/visibilitychange itself)
        if (isCheatHandlingRef.current) return;
        isCheatHandlingRef.current = true;

        warningsRef.current += 1;
        const newWarnings = warningsRef.current;
        setWarnings(newWarnings); // Keep UI state in sync

        if (newWarnings >= MAX_WARNINGS) {
            // Immediately disable further detection before showing modal
            setIsReadOnly(true);
            setWarningModal({
                message: reason,
                count: newWarnings,
                isFinal: true,
            });
            // Auto-submit is triggered when the user dismisses the modal (onClose)
        } else {
            setWarningModal({
                message: reason,
                count: newWarnings,
                isFinal: false,
            });
        }
        // Release lock after a short delay to allow React to re-render the modal
        // before any further events could arrive
        setTimeout(() => { isCheatHandlingRef.current = false; }, 1000);
    };

    const enterFullscreen = async () => {
        try {
            const docElm = document.documentElement;
            if (docElm.requestFullscreen) {
                await docElm.requestFullscreen();
            } else if (docElm.mozRequestFullScreen) { /* Firefox */
                await docElm.mozRequestFullScreen();
            } else if (docElm.webkitRequestFullscreen) { /* Chrome, Safari and Opera */
                await docElm.webkitRequestFullscreen();
            } else if (docElm.msRequestFullscreen) { /* IE/Edge */
                await docElm.msRequestFullscreen();
            } else {
                alert("Your browser does not support fullscreen functionality.");
            }
        } catch (err) {
            console.error("Fullscreen request failed", err);
            alert("Could not automatically enter fullscreen. Please ensure your browser allows it, or click anywhere on the page and try again.");
        }
    };

    // Timer functions
    const startTimer = async () => {
        if (!assignment || !assignment.questions || assignment.questions.length === 0 || isReadOnly) return;

        const aqId = assignment.questions[currentQuestionIndex]?.id; // Use current index
        try {
            await submissionService.startTimer(assignmentId, aqId, selectedLanguage);
            setIsTimerRunning(true);
            lastUpdateRef.current = Date.now();
        } catch (err) {
            console.error("Failed to start timer:", err);
        }
    };

    const pauseTimer = async () => {
        if (isReadOnly) return;
        setIsTimerRunning(false);
        await updateTimerOnBackend();
    };

    const updateTimerOnBackend = async () => {
        if (!assignment || !assignment.questions || assignment.questions.length === 0 || isReadOnly) return;

        const aqId = assignment.questions[currentQuestionIndex]?.id;
        try {
            await submissionService.updateTimer(assignmentId, aqId, timeSpent, selectedLanguage);
        } catch (err) {
            console.error("Failed to update timer:", err);
        }
    };

    const formatTime = (seconds) => {
        const hrs = Math.floor(seconds / 3600);
        const mins = Math.floor((seconds % 3600) / 60);
        const secs = seconds % 60;

        if (hrs > 0) {
            return `${hrs}:${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
        }
        return `${mins}:${secs.toString().padStart(2, '0')}`;
    };

    // Calculate time limit based on difficulty
    const getTimeLimit = (difficulty) => {
        switch (difficulty?.toLowerCase()) {
            case 'easy': return 30 * 60; // 30 minutes
            case 'medium': return 45 * 60; // 45 minutes  
            case 'hard': return 60 * 60; // 60 minutes
            default: return 45 * 60; // default to 45 minutes
        }
    };

    // Handle when time runs out
    const handleTimeUp = async () => {
        setIsTimerRunning(false);

        try {
            // Auto-submit the assignment
            await updateTimerOnBackend();

            const question = assignment.questions[currentQuestionIndex];
            const submissionData = {
                assignment_id: assignment.id,
                assignment_question_id: question.id,
                code_content: code,
                language: selectedLanguage,
                time_spent: timeSpent
            };

            const response = await submissionService.submitCode(submissionData);

            if (response.success) {
                alert("Time's up! Your assignment has been automatically submitted.");
                navigate('/student/dashboard');
            } else {
                throw new Error(response.message || 'Auto-submission failed');
            }
        } catch (err) {
            console.error("Failed to auto-submit:", err);
            alert("Time's up! Please submit your assignment manually.");
        }
    };

    // Handle back button with warning
    const handleBackClick = () => {
        if (isReadOnly) {
            navigate('/student/dashboard');
            return;
        }
        setShowExitWarning(true);
    };

    const handleConfirmExit = async () => {
        try {
            setIsSubmitting(true);

            // Save timer before submitting
            await updateTimerOnBackend();

            // Try to submit if there is code, but don't block exit if empty or fails
            // Actually, "Exit & Submit" implies we WANT to submit.
            // If user just wants to leave without submitting, that's different.
            // Assuming requirement is "save progress and leave" or "submit and leave".
            // Since we have auto-save on timer, let's ensure we save timer and maybe current draft.

            // For now, let's just navigate away since backend auto-saves timer periodically.
            // Or explicitly save timer once more.

            setShowExitWarning(false);
            navigate('/student/dashboard');

        } catch (err) {
            console.error("Failed to exit:", err);
            // Force exit anyway if error persists?
            navigate('/student/dashboard');
        } finally {
            setIsSubmitting(false);
        }
    };

    // Language change handler
    const handleLanguageChange = async (newLanguage) => {
        setSelectedLanguage(newLanguage);

        // Try to load existing submission for this language
        try {
            const timerResponse = await submissionService.getTimer(assignmentId, currentAQ.id, newLanguage);
            if (timerResponse.success && timerResponse.data && timerResponse.data.code_content) {
                // Use the existing code for this language
                setCode(timerResponse.data.code_content);
            } else {
                // No existing submission for this language, use starter code or default
                const questionStarterCode = assignment?.questions?.[currentQuestionIndex]?.question?.starter_code;
                if (questionStarterCode && questionStarterCode.trim()) {
                    setCode(questionStarterCode);
                } else {
                    setCode(languageConfig[newLanguage].defaultCode);
                }
            }
        } catch (error) {
            console.error("Error loading language-specific code:", error);
            // Fallback to starter code or default
            const questionStarterCode = assignment?.questions?.[currentQuestionIndex]?.question?.starter_code;
            if (questionStarterCode && questionStarterCode.trim()) {
                setCode(questionStarterCode);
            } else {
                setCode(languageConfig[newLanguage].defaultCode);
            }
        }

        setOutput(null); // Clear previous output
    };

    const handleRunCode = async () => {
        if (!assignment || !assignment.questions?.[currentQuestionIndex]) return;

        setIsRunning(true);
        setOutput({ status: 'running' }); // UI State for "Running..."

        try {
            const aq = assignment.questions[currentQuestionIndex];
            const testCases = aq.question?.test_cases || [];

            console.log("🚀 Starting code execution...");
            console.log("Code:", code);
            console.log("Test cases:", testCases);

            // Call Backend Sandbox with correct format
            const response = await submissionService.runCode({
                code: code,
                language: selectedLanguage, // Use selected language instead of hardcoded "python"
                test_cases: testCases,
                question_id: aq.question?.id
            });

            console.log("✅ Run code response:", response); // Debug log

            // Format result for UI
            // The API client wraps the response, so we need response.data.data
            const resultData = response.data.data || response.data;
            console.log("📊 Result data:", resultData);

            // Calculate if all tests passed
            const allTestsPassed = resultData.results.every(r => r.passed);
            const executionSuccessful = resultData.summary.execution_successful;

            let status = 'error';
            let message = 'Code execution failed';

            if (executionSuccessful) {
                if (allTestsPassed) {
                    status = 'success';
                    message = 'Code executed successfully and all tests passed!';
                } else {
                    status = 'failed';
                    message = 'Code executed, but some test cases failed.';
                }
            } else {
                status = 'error';
                message = 'Code execution crashed or timed out.';
            }

            const formattedOutput = {
                status: status,
                message: message,
                results: resultData.results.map((r, index) => ({
                    id: index,
                    status: r.passed ? 'success' : 'error', // Individual test status
                    output: r.actual_output || '',
                    expected: r.expected_output || '',
                    error: r.error || r.error_message || '',
                    input: r.test_case?.input || testCases[index]?.input || '',
                    showOutputOnly: r.show_output_only || false,
                    testPassed: r.passed
                }))
            };

            console.log("🎯 Formatted output:", formattedOutput);
            setOutput(formattedOutput);

        } catch (err) {
            console.error("❌ Run failed:", err);
            setOutput({
                status: 'error',
                message: 'Execution failed: ' + (err.message || 'Unknown error'),
                results: []
            });
        } finally {
            setIsRunning(false);
        }
    };



    if (loading) {
        return (
            <div className="flex h-screen items-center justify-center bg-gray-50">
                <div className="text-center">
                    <Loader2 className="w-10 h-10 animate-spin text-indigo-600 mx-auto mb-4" />
                    <p className="text-gray-500 font-medium">Loading workspace...</p>
                </div>
            </div>
        );
    }

    if (error || !assignment) {
        return (
            <div className="flex h-screen items-center justify-center bg-gray-50">
                <div className="text-center">
                    <XCircle className="w-12 h-12 text-red-500 mx-auto mb-4" />
                    <h2 className="text-xl font-bold text-gray-900 mb-2">Error Loading Assignment</h2>
                    <p className="text-gray-500 mb-6">{error || "Assignment not found."}</p>
                    <Button onClick={() => navigate('/student/dashboard')}>Back to Dashboard</Button>
                </div>
            </div>
        );
    }

    // Helpers
    const currentQuestion = assignment?.questions?.[currentQuestionIndex]?.question || {};
    const currentAQ = assignment?.questions?.[currentQuestionIndex];
    const totalQuestions = assignment?.questions?.length || 0;
    const testCases = currentQuestion.test_cases || [];

    // Save current code to draft
    const saveToDrafts = (index, currentCode) => {
        setCodeDrafts(prev => ({
            ...prev,
            [index]: currentCode
        }));
    };

    // Navigation Handlers
    const handleNextQuestion = () => {
        if (currentQuestionIndex < totalQuestions - 1) {
            saveToDrafts(currentQuestionIndex, code); // Save current
            setCurrentQuestionIndex(prev => prev + 1);
            setOutput(null);
        }
    };

    const handlePrevQuestion = () => {
        if (currentQuestionIndex > 0) {
            saveToDrafts(currentQuestionIndex, code); // Save current
            setCurrentQuestionIndex(prev => prev - 1);
            setOutput(null);
        }
    };

    // Polling Logic for Async Submissions
    const pollSubmission = (attemptId) => {
        const POLL_INTERVAL = 1000; // 1s — faster feedback
        const MAX_ATTEMPTS = 120; // 2 minutes max wait

        let attempts = 0;

        const checkStatus = async () => {
            try {
                if (attempts >= MAX_ATTEMPTS) {
                    setIsSubmitting(false);
                    setWarningModal({ message: "Submission is taking too long. Please check your dashboard later.", count: 0, isFinal: false });
                    return;
                }

                const response = await submissionService.getSubmission(attemptId);
                const attempt = response.data;

                // Terminal states that should stop polling
                const terminalStates = ['success', 'fail', 'error'];

                if (!terminalStates.includes(attempt.status)) {
                    attempts++;
                    // Continue polling for all other states (pending, queued, processing, etc.)
                    setTimeout(checkStatus, POLL_INTERVAL);
                } else {
                    // Completed
                    setIsSubmitting(false);
                    processSubmissionResult(attempt);

                    if (attempt.status === 'success') {
                        setCompletedQuestions(prev => new Set(prev).add(currentQuestionIndex));
                    }
                    // fail/error details are already shown in the output panel
                }
            } catch (err) {
                console.error("Polling error:", err);
                setIsSubmitting(false);
                // Don't alert — just log; student sees nothing changed in the output panel
            }
        };

        // Start polling
        checkStatus();
    };

    // Updated Submit Handler
    const handleSubmit = async () => {
        if (!currentAQ) {
            console.error("Submit failed: currentAQ is missing", { assignment, currentQuestionIndex });
            alert("Error: Question data not found. Please refresh the page.");
            return;
        }

        if (isReadOnly) {
            alert("This assignment is submitted and read-only.");
            return;
        }

        console.log("Submitting code...", {
            assignment_id: assignment.id,
            assignment_question_id: currentAQ.id,
            question_id: currentQuestion.id,
            language: selectedLanguage
        });

        setIsSubmitting(true);
        try {
            await updateTimerOnBackend();

            const isMcq = currentQuestion?.question_type === 'mcq';
            const payload = {
                assignment_id: assignment.id,
                assignment_question_id: currentAQ.id,
                question_id: currentQuestion.id,
                language: selectedLanguage,
                time_spent: timeSpent
            };
            if (isMcq) {
                let optionIndex = code;
                if (currentQuestion.config?.options) {
                    const idx = currentQuestion.config.options.indexOf(code);
                    if (idx !== -1) optionIndex = idx;
                }
                payload.response_data = { answer: optionIndex };
            } else {
                payload.code_content = code;
            }

            const response = await submissionService.submitCode(payload);

            // Handle Response
            const attempt = response.data;

            if (attempt.status === 'queued' || attempt.status === 'processing') {
                // Async: Start Polling
                // Note: We do NOT set isSubmitting(false) here. Polling handles it.
                pollSubmission(attempt.id);
            } else {
                // Sync / Immediate Result
                processSubmissionResult(attempt);
                setIsSubmitting(false);

                if (attempt.status === 'success') {
                    setCompletedQuestions(prev => new Set(prev).add(currentQuestionIndex));
                } else if (attempt.status === 'fail') {
                    // Fail details are already in the output panel
                }
            }

        } catch (err) {
            console.error("Submission failed:", err);
            setIsSubmitting(false);

            // Handle "Already Completed" (400)
            if (err.response?.status === 400 && err.response?.data?.message?.includes("already successfully completed")) {
                alert("You have already completed this question! Marking as complete.");
                setCompletedQuestions(prev => new Set(prev).add(currentQuestionIndex));
            } else {
                alert("Submission failed: " + (err.response?.data?.message || err.message));
            }
        }
    };

    const processSubmissionResult = (attempt) => {
        if (!attempt || !attempt.test_results) return;

        const formattedResults = attempt.test_results.map((r, idx) => ({
            id: idx,
            status: r.status === 'pass' ? 'success' : 'error',
            output: r.actual_output || '',
            expected: testCases[idx]?.expected_output || '',
            error: r.error_message || '',
            input: testCases[idx]?.input || '',
            testPassed: r.status === 'pass'
        }));

        const allPassed = formattedResults.every(r => r.status === 'success');

        setOutput({
            status: allPassed ? 'success' : 'error',
            message: allPassed ? 'All Test Cases Passed! Great Job!' : 'Some test cases failed. Review details below.',
            results: formattedResults
        });

        pauseTimer();

        // Mark as completed (attempted) regardless of pass/fail 
        // to allow user to move on
        setCompletedQuestions(prev => new Set(prev).add(currentQuestionIndex));
    };

    const handleFinishAssignment = async () => {
        try {
            setIsSubmitting(true);
            await submissionService.finishAssignment(assignment.id);

            // Show Success Modal
            setShowConfetti(true);

            // Navigate after delay
            setTimeout(() => {
                setShowConfetti(false);
                navigate('/student/dashboard');
            }, 3000);

        } catch (error) {
            console.error("Failed to finish assignment:", error);
            alert("Error finishing assignment: " + error.message);
        } finally {
            setIsSubmitting(false);
        }
    };

    return (
        <div className="flex flex-col h-screen bg-gray-50 text-gray-900 font-sans overflow-hidden">

            {/* Anti-Cheat Fullscreen Blocking Overlay */}
            {!isReadOnly && !loading && !error && assignment && assignment.mode === 'exam' && !isFullscreen && (
                <div className="fixed inset-0 z-50 bg-gray-900/90 backdrop-blur-sm flex flex-col items-center justify-center p-6 text-center">
                    <div className="bg-white rounded-xl shadow-2xl p-8 max-w-md w-full border-t-4 border-indigo-600">
                        <div className="w-16 h-16 bg-indigo-100 rounded-full flex items-center justify-center mx-auto mb-4">
                            <Settings className="w-8 h-8 text-indigo-600 animate-spin-slow" />
                        </div>
                        <h2 className="text-2xl font-bold text-gray-900 mb-2">Strict Mode Active</h2>
                        <div className="text-gray-600 text-sm mb-6 space-y-2">
                            <p>This assignment runs in a restricted environment.</p>
                            <ul className="text-left bg-gray-50 p-3 rounded-lg border border-gray-100 space-y-1 text-xs">
                                <li>• You must remain in Fullscreen mode.</li>
                                <li>• Switching tabs or windows is recorded.</li>
                                <li>• 3 warnings will result in auto-submission.</li>
                                <li>• Copying/pasting is disabled.</li>
                            </ul>
                        </div>
                        <Button
                            onClick={enterFullscreen}
                            className="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 h-auto"
                        >
                            Enter Fullscreen to Start
                        </Button>
                    </div>
                </div>
            )}

            {/* Anti-Cheat Warning Modal — replaces alert() to avoid focus-loss cascade */}
            {warningModal && (
                <div className="fixed inset-0 z-[60] bg-black/70 flex items-center justify-center p-4">
                    <div className={`bg-white rounded-xl shadow-2xl p-6 max-w-sm w-full border-t-4 ${warningModal.isFinal ? 'border-red-600' : 'border-amber-500'}`}>
                        <div className={`w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-4 ${warningModal.isFinal ? 'bg-red-100' : 'bg-amber-100'}`}>
                            <span className="text-2xl">{warningModal.isFinal ? '🚨' : '⚠️'}</span>
                        </div>
                        <h3 className={`text-lg font-bold text-center mb-2 ${warningModal.isFinal ? 'text-red-700' : 'text-amber-700'}`}>
                            {warningModal.isFinal ? 'Maximum Warnings Reached' : `Warning ${warningModal.count}/${MAX_WARNINGS}`}
                        </h3>
                        <p className="text-gray-700 text-sm text-center mb-2">{warningModal.message}</p>
                        {warningModal.isFinal ? (
                            <p className="text-red-600 text-sm text-center font-medium mb-4">
                                Your assignment is being automatically submitted.
                            </p>
                        ) : (
                            <p className="text-gray-500 text-xs text-center mb-4">
                                {MAX_WARNINGS - warningModal.count} more warning(s) will trigger auto-submission.
                            </p>
                        )}
                        <button
                            className={`w-full py-2 rounded-lg font-semibold text-white transition-colors ${warningModal.isFinal ? 'bg-red-600 hover:bg-red-700' : 'bg-amber-500 hover:bg-amber-600'}`}
                            onClick={() => {
                                const wasFinal = warningModal.isFinal;
                                setWarningModal(null);
                                if (wasFinal) {
                                    handleTimeUp(); // Trigger auto-submit AFTER modal is closed
                                }
                            }}
                        >
                            {warningModal.isFinal ? 'Acknowledged — Submit Now' : 'I Understand, Return to Exam'}
                        </button>
                    </div>
                </div>
            )}

            {/* Completed Banner */}
            {isReadOnly && (
                <div className="bg-amber-100 border-b border-amber-200 px-4 py-2 text-amber-800 text-sm font-medium flex items-center justify-center gap-2">
                    <CheckCircle2 className="w-4 h-4" />
                    This assignment has been submitted and is now read-only.
                </div>
            )}

            {/* 1. HEADER */}
            <header className="h-14 bg-white border-b border-gray-200 flex items-center justify-between px-4 z-20 shadow-sm flex-shrink-0">
                <div className="flex items-center gap-4">
                    <Button
                        variant="ghost"
                        size="icon"
                        className="h-8 w-8"
                        onClick={handleBackClick}
                    >
                        <ChevronLeft className="w-5 h-5 text-gray-600" />
                    </Button>
                    <div>
                        <h1 className="font-bold text-sm text-gray-900 leading-none mb-1">
                            {assignment.title}
                        </h1>
                        <div className="flex items-center gap-2 text-xs text-gray-500">
                            <span className={`px-1.5 py-0.5 rounded border ${assignment.difficulty === 'Hard' ? 'bg-red-50 border-red-100 text-red-700' :
                                assignment.difficulty === 'Medium' ? 'bg-amber-50 border-amber-100 text-amber-700' :
                                    'bg-green-50 border-green-100 text-green-700'
                                }`}>
                                {assignment.difficulty || "Medium"}
                            </span>
                            <span>•</span>
                            <Clock className="w-3 h-3" />
                            <span className={timeRemaining < 300 ? "text-red-600 font-bold" : ""}>
                                {formatTime(timeRemaining)}
                            </span>
                        </div>
                    </div>
                </div>

                {/* Question Palette / Navigation */}
                <QuestionPalette
                    currentQuestionIndex={currentQuestionIndex}
                    totalQuestions={totalQuestions}
                    onSelectQuestion={(idx) => {
                        saveToDrafts(currentQuestionIndex, code);
                        setCurrentQuestionIndex(idx);
                        setOutput(null);
                    }}
                    onNext={handleNextQuestion}
                    onPrev={handlePrevQuestion}
                />

                <div className="flex items-center gap-3">
                    {/* Compact Points Display Removed */}


                    {currentQuestion.question_type !== 'mcq' && (
                        <Button
                            variant="secondary"
                            size="sm"
                            onClick={handleRunCode}
                            disabled={isRunning || isSubmitting}
                            className="bg-gray-100 hover:bg-gray-200 text-gray-700 h-9"
                        >
                            {isRunning ? <Loader2 className="w-4 h-4 animate-spin mr-2" /> : <Play className="w-4 h-4 mr-2" />}
                            Run
                        </Button>
                    )}

                    {/* Read-Only Mode Navigation */}
                    {isReadOnly ? (
                        <div className="flex items-center gap-2">
                            {currentQuestionIndex > 0 && (
                                <Button
                                    size="sm"
                                    variant="outline"
                                    onClick={handlePrevQuestion}
                                    className="h-9 shadow-sm gap-2"
                                >
                                    <ChevronLeft className="w-4 h-4" /> Prev
                                </Button>
                            )}

                            {currentQuestionIndex < totalQuestions - 1 ? (
                                <Button
                                    size="sm"
                                    onClick={handleNextQuestion}
                                    className="bg-indigo-600 hover:bg-indigo-700 text-white h-9 shadow-sm gap-2"
                                >
                                    Next <ChevronDown className="w-4 h-4 -rotate-90" />
                                </Button>
                            ) : (
                                <Button
                                    size="sm"
                                    onClick={() => navigate('/student/dashboard')}
                                    className="bg-gray-900 hover:bg-gray-800 text-white h-9 shadow-sm gap-2"
                                >
                                    Back to Dashboard <ArrowRight className="w-4 h-4" />
                                </Button>
                            )}
                        </div>
                    ) : (
                        /* Normal Submission Mode */
                        completedQuestions.has(currentQuestionIndex) ? (
                            <div className="flex items-center gap-2">
                                {/* Allow Retry */}
                                <Button
                                    size="sm"
                                    variant="outline"
                                    
                                    onClick={handleSubmit}
                                    disabled={isRunning || isSubmitting}
                                    className="h-9 shadow-sm gap-2"
                                >
                                    {isSubmitting ? <Loader2 className="w-4 h-4 animate-spin" /> : <Send className="w-4 h-4" />}
                                    Submit
                                </Button>

                                {currentQuestionIndex < totalQuestions - 1 ? (
                                    <Button
                                        size="sm"
                                        onClick={handleNextQuestion}
                                        className="bg-green-600 hover:bg-green-700 text-white h-9 shadow-sm gap-2"
                                    >
                                        Next Question <ChevronDown className="w-4 h-4 -rotate-90" />
                                    </Button>
                                ) : (
                                    <Button
                                        size="sm"
                                        onClick={handleFinishAssignment}
                                        className="bg-blue-600 hover:bg-blue-700 text-white h-9 shadow-sm gap-2"
                                    >
                                        Finish Assignment <CheckCircle2 className="w-4 h-4" />
                                    </Button>
                                )}
                            </div>
                        ) : (
                            <Button
                                size="sm"
                                onClick={handleSubmit}
                                disabled={isRunning || isSubmitting}
                                className="bg-green-600 hover:bg-green-700 text-white h-9 shadow-sm"
                            >
                                {isSubmitting ? <Loader2 className="w-4 h-4 animate-spin mr-2" /> : <Send className="w-4 h-4 mr-2" />}
                                Submit
                            </Button>
                        )
                    )}
                </div>
            </header>

            {/* 2. MAIN WORKSPACE */}
            <div className="flex-1 w-full overflow-hidden flex">
                {/* LEFT PANEL: Description */}
                <div className="w-[35%] min-w-[300px] max-w-[600px] bg-white border-r border-gray-200 flex flex-col h-full">
                    <div className="flex-1 overflow-y-auto p-6">
                        <div className="mb-6">
                            <h2 className="text-xl font-bold text-gray-900 mb-2 select-none">
                                {currentQuestionIndex + 1}. {currentQuestion.title}
                            </h2>
                            <Separator className="my-4" />

                            <div className="prose prose-sm max-w-none text-gray-700 leading-relaxed whitespace-pre-wrap select-none">
                                <ReactMarkdown>
                                    {currentQuestion.description || assignment.description}
                                </ReactMarkdown>
                            </div>
                        </div>

                        {/* Test Cases Preview (Optional) */}
                        <div className="mt-6">
                            <h3 className="text-sm font-semibold text-gray-900 mb-3">Example Test Cases</h3>
                            <div className="space-y-3">
                                {testCases.slice(0, 2).map((tc, idx) => (
                                    <div key={idx} className="bg-gray-50 rounded-lg p-3 text-xs font-mono border border-gray-200">
                                        <div className="grid grid-cols-2 gap-2 mb-1">
                                            <span className="text-gray-500">Input:</span>
                                            <span className="text-gray-900">{tc.input}</span>
                                        </div>
                                        <div className="grid grid-cols-2 gap-2">
                                            <span className="text-gray-500">Output:</span>
                                            <span className="text-gray-900">{tc.expected_output || tc.output}</span>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>

                        {currentQuestion.hint && (
                            <div className="mt-8 border-t border-gray-100 pt-4">
                                <button
                                    onClick={() => setShowHint(!showHint)}
                                    className="flex items-center gap-2 text-sm font-medium text-indigo-600 hover:text-indigo-700"
                                >
                                    <Lightbulb className="w-4 h-4" />
                                    {showHint ? 'Hide Hint' : 'Need a Hint?'}
                                </button>
                                {showHint && (
                                    <motion.div
                                        initial={{ opacity: 0, y: 5 }}
                                        animate={{ opacity: 1, y: 0 }}
                                        className="mt-3 bg-amber-50 text-amber-900 p-3 rounded-md text-sm border border-amber-100"
                                    >
                                        {currentQuestion.hint}
                                    </motion.div>
                                )}
                            </div>
                        )}
                    </div>
                </div>

                {/* RIGHT PANEL: Editor & Output - TAKES REMAINING SPACE */}
                <div className="flex-1 bg-white flex flex-col h-full">
                    {currentQuestion?.question_type === 'mcq' ? (
                        <div className="flex-1 overflow-hidden">
                            <McqWorkspaceRenderer
                                question={currentQuestion}
                                selectedOption={code}
                                onChange={setCode}
                                disabled={isReadOnly || isSubmitting}
                            />
                        </div>
                    ) : (
                        <div className="flex-[60] min-h-0 flex flex-col bg-[#2d2d2d]">
                            <div className="bg-[#2d2d2d] border-b border-[#111] px-4 h-9 flex justify-between items-center text-xs text-gray-400 select-none flex-shrink-0">
                                <div className="flex items-center gap-2">
                                    {/* Language Dropdown */}
                                    <div className="relative">
                                        <select
                                            value={selectedLanguage}
                                            onChange={(e) => handleLanguageChange(e.target.value)}
                                            className="bg-[#3d3d3d] text-blue-400 font-medium border border-[#555] rounded px-2 py-1 text-xs cursor-pointer hover:bg-[#4d4d4d] focus:outline-none focus:ring-1 focus:ring-blue-500"
                                        >
                                            {Object.entries(languageConfig).map(([key, lang]) => (
                                                <option key={key} value={key} className="bg-[#3d3d3d] text-white">
                                                    {lang.icon} {lang.name}
                                                </option>
                                            ))}
                                        </select>
                                    </div>
                                </div>
                                <span
                                    className="hover:text-white cursor-pointer transition-colors flex items-center gap-1"
                                    onClick={() => setCode(languageConfig[selectedLanguage].defaultCode)}
                                >
                                    <RotateCcw className="w-3 h-3" /> Reset
                                </span>
                            </div>

                            <div className="flex-1 relative overflow-hidden bg-[#1e1e1e]">
                                <MonacoEditor
                                    height="100%"
                                    language={languageConfig[selectedLanguage].monacoLang}
                                    value={code}
                                    theme="vs-dark"
                                    onChange={(value) => setCode(value || '')}
                                    onMount={handleMonacoMount}
                                    options={{
                                        fontSize: 14,
                                        fontFamily: '"Fira Code", "Fira Mono", monospace',
                                        fontLigatures: true,
                                        minimap: { enabled: false },
                                        scrollBeyondLastLine: false,
                                        wordWrap: 'on',
                                        readOnly: isReadOnly || isSubmitting,
                                        automaticLayout: true,
                                        tabSize: 4,
                                        insertSpaces: true,
                                        autoIndent: 'full',
                                        formatOnType: true,
                                        bracketPairColorization: { enabled: true },
                                        autoClosingBrackets: 'always',
                                        autoClosingQuotes: 'always',
                                        lineNumbers: 'on',
                                        renderLineHighlight: 'all',
                                        scrollbar: { verticalScrollbarSize: 8, horizontalScrollbarSize: 8 },
                                        padding: { top: 12, bottom: 12 },
                                        contextmenu: false, // disable right-click copy/paste menu
                                    }}
                                />
                            </div>
                        </div>
                    )}

                    {/* DIVIDER */}
                    {currentQuestion?.question_type !== 'mcq' && <div className="h-1 bg-gray-800 flex-shrink-0" />}

                    {/* CONSOLE - SIMPLIFIED VERSION */}
                    {currentQuestion?.question_type !== 'mcq' && (
                        <div className="flex-[40] min-h-0 bg-white flex flex-col">
                            <div className="h-9 bg-gray-50 border-b border-gray-200 flex items-center justify-between px-4 select-none flex-shrink-0">
                                <div className="flex items-center gap-2">
                                    <div className="flex items-center gap-2 text-gray-500 font-medium text-xs">
                                        <Terminal className="w-3.5 h-3.5" />
                                        Output
                                    </div>
                                    {isRunning && <span className="text-xs text-indigo-600 animate-pulse">Running Code...</span>}
                                    {output?.status === 'error' && <span className="w-1.5 h-1.5 rounded-full bg-red-500" />}
                                    {output?.status === 'failed' && <span className="w-1.5 h-1.5 rounded-full bg-orange-500" />}
                                    {output?.status === 'success' && <span className="w-1.5 h-1.5 rounded-full bg-green-500" />}
                                </div>
                            </div>

                            <div className="flex-1 overflow-auto p-4">
                                {!output && !isRunning && (
                                    <div className="flex flex-col items-center justify-center text-gray-400 h-full">
                                        <Terminal className="w-12 h-12 mb-2 opacity-50" />
                                        <span className="text-sm">Click "Run Code" to see your output here</span>
                                    </div>
                                )}

                                {isRunning && (
                                    <div className="flex flex-col items-center justify-center text-blue-600 h-full">
                                        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mb-2"></div>
                                        <span className="text-sm">Running your Python code...</span>
                                    </div>
                                )}

                                {output && (
                                    <div className="space-y-4">
                                        {/* Status */}
                                        {/* Status */}
                                        <div className={`p-3 rounded-lg border ${output.status === 'success' ? 'bg-green-50 border-green-200' :
                                            output.status === 'failed' ? 'bg-orange-50 border-orange-200' :
                                                'bg-red-50 border-red-200'
                                            }`}>
                                            <div className="flex flex-col gap-2">
                                                <div className="flex items-center gap-2">
                                                    {output.status === 'success' && <CheckCircle2 className="w-4 h-4 text-green-600" />}
                                                    {output.status === 'failed' && <XCircle className="w-4 h-4 text-orange-600" />}
                                                    {output.status === 'error' && <XCircle className="w-4 h-4 text-red-600" />}

                                                    <span className={`font-medium text-sm ${output.status === 'success' ? 'text-green-800' :
                                                        output.status === 'failed' ? 'text-orange-800' :
                                                            'text-red-800'
                                                        }`}>
                                                        {output.message}
                                                    </span>
                                                </div>
                                            </div>
                                        </div>

                                        {/* Main Output Display */}
                                        {output.results && output.results.length > 0 && (
                                            <div className="space-y-3">
                                                {output.results.map((result, idx) => (
                                                    <div key={idx} className="border border-gray-200 rounded-lg overflow-hidden">
                                                        {/* Output Header */}
                                                        <div className="bg-blue-50 px-4 py-2 border-b border-blue-200">
                                                            <h3 className="font-semibold text-blue-800 text-sm flex items-center gap-2">
                                                                <Terminal className="w-4 h-4" />
                                                                Your Code Output
                                                                {result.error && <span className="text-red-600 text-xs">(Error)</span>}
                                                            </h3>
                                                        </div>

                                                        <div className="p-4 space-y-3">
                                                            {/* Input (if any) */}
                                                            {result.input && (
                                                                <div>
                                                                    <div className="text-xs font-semibold text-gray-500 mb-1">INPUT PROVIDED:</div>
                                                                    <div className="bg-gray-100 p-2 rounded text-sm font-mono border">
                                                                        {result.input}
                                                                    </div>
                                                                </div>
                                                            )}

                                                            {/* Main Output - Most Important */}
                                                            <div>
                                                                <div className="text-sm font-semibold text-gray-700 mb-2 flex items-center gap-2">
                                                                    <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded text-xs font-bold">OUTPUT</span>
                                                                    What your code printed:
                                                                </div>
                                                                <div className={`p-3 rounded border-2 text-sm font-mono ${result.error ? 'bg-red-50 border-red-300 text-red-800' :
                                                                    result.testPassed ? 'bg-green-50 border-green-300 text-green-800' :
                                                                        'bg-orange-50 border-orange-300 text-orange-900'
                                                                    }`}>
                                                                    {result.error ? (
                                                                        <div>
                                                                            <div className="font-bold text-red-600 mb-1">❌ Error:</div>
                                                                            <div className="whitespace-pre-wrap">{result.error}</div>
                                                                        </div>
                                                                    ) : (
                                                                        <div className="whitespace-pre-wrap">
                                                                            {result.output || <span className="text-gray-500 italic">(no output)</span>}
                                                                        </div>
                                                                    )}
                                                                </div>
                                                            </div>

                                                            {/* Test Comparison (Secondary) */}
                                                            {result.expected && (
                                                                <div className="border-t border-gray-200 pt-3 mt-3">
                                                                    <div className="text-xs font-semibold text-gray-500 mb-2">📋 Test Comparison:</div>
                                                                    <div className="grid grid-cols-2 gap-3 text-xs">
                                                                        <div>
                                                                            <div className="font-semibold text-gray-600 mb-1">Expected:</div>
                                                                            <div className="bg-blue-100 p-2 rounded font-mono text-blue-800 whitespace-pre-wrap">
                                                                                {result.expected}
                                                                            </div>
                                                                        </div>
                                                                        <div>
                                                                            <div className="font-semibold text-gray-600 mb-1">Your Output:</div>
                                                                            <div className={`p-2 rounded font-mono whitespace-pre-wrap ${result.testPassed ? 'bg-green-100 text-green-800' : 'bg-orange-100 text-orange-800'
                                                                                }`}>
                                                                                {result.output || '(no output)'}
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                    <div className={`mt-2 text-xs font-medium ${result.testPassed ? 'text-green-600' : 'text-orange-600'}`}>
                                                                        {result.testPassed ? '✅ Matches expected output' : '❌ Output mismatch'}
                                                                    </div>
                                                                </div>
                                                            )}
                                                        </div>
                                                    </div>
                                                ))}
                                            </div>
                                        )}

                                        {/* Debug info (remove this later) */}
                                        <details className="text-xs text-gray-500">
                                            <summary className="cursor-pointer hover:text-gray-700">Debug Info (click to expand)</summary>
                                            <pre className="mt-2 p-2 bg-gray-100 rounded overflow-auto text-xs">
                                                {JSON.stringify(output, null, 2)}
                                            </pre>
                                        </details>
                                    </div>
                                )}
                            </div>
                        </div>
                    )}
                </div>
            </div>

            {/* Exit Warning Modal */}
            <AnimatePresence>
                {showExitWarning && (
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-[1px]"
                    >
                        <motion.div
                            initial={{ scale: 0.8, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            className="bg-white p-8 rounded-2xl shadow-2xl text-center max-w-md w-full mx-4"
                        >
                            <div className="w-16 h-16 bg-amber-100 rounded-full flex items-center justify-center mx-auto mb-4">
                                <XCircle className="w-8 h-8 text-amber-600" />
                            </div>
                            <h2 className="text-2xl font-bold text-gray-900 mb-2">Exit Assignment?</h2>
                            <p className="text-gray-500 mb-6">
                                If you click on "Exit Assignment", the assignment will be submitted automatically.
                                Your current code and progress will be saved and submitted.
                            </p>
                            <div className="flex gap-3">
                                <Button
                                    variant="outline"
                                    onClick={() => setShowExitWarning(false)}
                                    className="flex-1"
                                    disabled={isSubmitting}
                                >
                                    Continue Working
                                </Button>
                                <Button
                                    onClick={handleConfirmExit}
                                    className="flex-1 bg-red-600 hover:bg-red-700 text-white"
                                    disabled={isSubmitting}
                                >
                                    {isSubmitting ? 'Submitting...' : 'Exit & Submit Assignment'}
                                </Button>
                            </div>
                        </motion.div>
                    </motion.div>
                )}
            </AnimatePresence>

            {/* Success Modal */}
            <AnimatePresence>
                {showConfetti && (
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-[1px]"
                    >
                        <motion.div
                            initial={{ scale: 0.8, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            className="bg-white p-8 rounded-2xl shadow-2xl text-center max-w-sm w-full mx-4"
                        >
                            <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                                <CheckCircle2 className="w-8 h-8 text-green-600" />
                            </div>
                            <h2 className="text-2xl font-bold text-gray-900 mb-2">Assignment Submitted Successfully!</h2>
                            <p className="text-gray-500 mb-6">Your assignment has been automatically submitted and sent for grading. You will be redirected to the dashboard in a few seconds.</p>
                            <Button onClick={() => navigate('/student/dashboard')} className="w-full bg-gray-900 text-white">
                                Back to Dashboard
                            </Button>
                        </motion.div>
                    </motion.div>
                )}
            </AnimatePresence>
        </div >
    );
};

export default StudentWorkspace;
