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
    Clock
} from "lucide-react";
import { Button } from "../../components/ui/button";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "../../components/ui/tabs";
import { motion, AnimatePresence } from "framer-motion";

// --- PRO DEPENDENCIES ---
import Editor from 'react-simple-code-editor';
import { highlight, languages } from 'prismjs/components/prism-core';
import 'prismjs/components/prism-clike';
import 'prismjs/components/prism-python';
import 'prismjs/components/prism-javascript';
import 'prismjs/components/prism-java';
import 'prismjs/components/prism-c';
import 'prismjs/components/prism-cpp';
import 'prismjs/themes/prism-tomorrow.css'; // Dark theme for code
import { Separator } from "../../components/ui/separator";
// import { Panel, Group } from "react-resizable-panels"; // Pro feature disabled for now

// Services
import { assignmentService } from "../../services/assignmentService";
import { submissionService } from "../../services/submissionService";
import QuestionPalette from "../../components/workspace/QuestionPalette";

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

    // Timer state
    const [timeSpent, setTimeSpent] = useState(0); // in seconds (for backend tracking)
    const [timeRemaining, setTimeRemaining] = useState(0); // countdown timer in seconds
    const [totalTimeAllowed, setTotalTimeAllowed] = useState(0); // total time for this difficulty
    const [isTimerRunning, setIsTimerRunning] = useState(false);
    const [showHint, setShowHint] = useState(false);
    const timerIntervalRef = useRef(null);
    const lastUpdateRef = useRef(Date.now());

    // Language configuration
    const languageConfig = {
        python: {
            name: "Python 3",
            extension: "py",
            defaultCode: "",
            icon: "🐍",
            prismLang: languages.python
        },
        javascript: {
            name: "JavaScript",
            extension: "js",
            defaultCode: "",
            icon: "🟨",
            prismLang: languages.javascript
        },
        java: {
            name: "Java",
            extension: "java",
            defaultCode: "",
            icon: "☕",
            prismLang: languages.java
        },
        cpp: {
            name: "C++",
            extension: "cpp",
            defaultCode: "",
            icon: "⚡",
            prismLang: languages.cpp
        },
        c: {
            name: "C",
            extension: "c",
            defaultCode: "",
            icon: "🔧",
            prismLang: languages.c
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
        if (assignment && assignment.questions && assignment.questions.length > 0) {
            startTimer();
        }

        // Cleanup on unmount - pause timer and save
        return () => {
            pauseTimer();
        };
    }, [assignment]);

    // Prevent browser back button
    useEffect(() => {
        const handleBeforeUnload = (e) => {
            e.preventDefault();
            e.returnValue = 'If you leave this page, your assignment will be submitted automatically. Are you sure?';
            return e.returnValue;
        };

        const handlePopState = (e) => {
            e.preventDefault();
            setShowExitWarning(true);
            // Push the current state back to prevent navigation
            window.history.pushState(null, '', window.location.pathname);
        };

        // Add event listeners
        window.addEventListener('beforeunload', handleBeforeUnload);
        window.addEventListener('popstate', handlePopState);

        // Push initial state to prevent back navigation
        window.history.pushState(null, '', window.location.pathname);

        return () => {
            window.removeEventListener('beforeunload', handleBeforeUnload);
            window.removeEventListener('popstate', handlePopState);
        };
    }, []);

    // Timer interval
    useEffect(() => {
        if (isTimerRunning && timeRemaining > 0) {
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
    }, [isTimerRunning, timeRemaining]);

    // Auto-save timer every 30 seconds
    useEffect(() => {
        const autoSaveInterval = setInterval(() => {
            if (assignment && assignment.questions && assignment.questions.length > 0 && timeSpent > 0) {
                updateTimerOnBackend();
            }
        }, 30000); // 30 seconds

        return () => clearInterval(autoSaveInterval);
    }, [assignment, timeSpent]);

    // Timer functions
    const startTimer = async () => {
        if (!assignment || !assignment.questions || assignment.questions.length === 0) return;

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
        setIsTimerRunning(false);
        await updateTimerOnBackend();
    };

    const updateTimerOnBackend = async () => {
        if (!assignment || !assignment.questions || assignment.questions.length === 0) return;

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
        setShowExitWarning(true);
    };

    const handleConfirmExit = async () => {
        try {
            setIsSubmitting(true);

            // Save timer before submitting
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
                setShowExitWarning(false);
                setShowConfetti(true);

                // Auto-close success modal and navigate after 3 seconds
                setTimeout(() => {
                    setShowConfetti(false);
                    pauseTimer();
                    navigate('/student/dashboard');
                }, 3000);
            } else {
                throw new Error(response.message || 'Submission failed');
            }
        } catch (err) {
            console.error("Failed to submit assignment:", err);
            alert("Failed to submit assignment. Please try again.");
            setShowExitWarning(false);
        } finally {
            setIsSubmitting(false);
        }
    };

    // Language change handler
    const handleLanguageChange = async (newLanguage) => {
        setSelectedLanguage(newLanguage);

        // Try to load existing submission for this language
        try {
            const timerResponse = await submissionService.getTimer(assignmentId, questionId, newLanguage);
            if (timerResponse.success && timerResponse.data && timerResponse.data.code_content) {
                // Use the existing code for this language
                setCode(timerResponse.data.code_content);
            } else {
                // No existing submission for this language, use starter code or default
                const questionStarterCode = assignment?.questions?.[currentQuestionIndex]?.starter_code;
                if (questionStarterCode && questionStarterCode.trim()) {
                    setCode(questionStarterCode);
                } else {
                    setCode(languageConfig[newLanguage].defaultCode);
                }
            }
        } catch (error) {
            console.error("Error loading language-specific code:", error);
            // Fallback to starter code or default
            const questionStarterCode = assignment?.questions?.[currentQuestionIndex]?.starter_code;
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

            const formattedOutput = {
                status: resultData.summary.execution_successful ? 'success' : 'error',
                message: resultData.summary.execution_successful ?
                    (resultData.summary.has_output ? 'Code executed successfully!' : 'Code ran but produced no output') :
                    'Code execution failed',
                results: resultData.results.map((r, index) => ({
                    id: index,
                    status: r.error ? 'error' : 'success', // Focus on execution, not test passing
                    output: r.actual_output || '',
                    expected: r.expected_output || '',
                    error: r.error || '',
                    input: r.test_case?.input || testCases[index]?.input || '',
                    showOutputOnly: r.show_output_only || false,
                    testPassed: r.passed // Keep test result but don't make it primary
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

    // Updated Submit Handler
    const handleSubmit = async () => {
        if (!currentAQ) return;

        setIsSubmitting(true);
        try {
            await updateTimerOnBackend();

            const response = await submissionService.submitCode({
                assignment_id: assignment.id,
                assignment_question_id: currentAQ.id,
                question_id: currentQuestion.id,
                code_content: code,
                language: selectedLanguage,
                time_spent: timeSpent
            });

            // Handle Response (Show Grade Results)
            // Backend returns the SubmissionAttempt object with test_results
            const attempt = response.data;
            processSubmissionResult(attempt);

        } catch (err) {
            console.error("Submission failed:", err);

            // Handle "Already Completed" (400)
            if (err.response?.status === 400 && err.response?.data?.message?.includes("already successfully completed")) {
                alert("You have already completed this question! Marking as complete.");
                setCompletedQuestions(prev => new Set(prev).add(currentQuestionIndex));
            } else {
                alert("Submission failed: " + (err.response?.data?.message || err.message));
            }
        } finally {
            setIsSubmitting(false);
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
            {/* Completed Banner */}
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
                    {/* Submit / Next Button Logic */}
                    {/* Submit / Next Button Logic */}
                    {completedQuestions.has(currentQuestionIndex) ? (
                        <div className="flex items-center gap-2">
                            {/* Allow Retry */}
                            <Button
                                size="sm"
                                variant="outline"
                                onClick={handleSubmit}
                                disabled={isRunning || isSubmitting || isReadOnly}
                                className="h-9 shadow-sm gap-2"
                            >
                                {isSubmitting ? <Loader2 className="w-4 h-4 animate-spin" /> : <RotateCcw className="w-4 h-4" />}
                                Retry
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
                            disabled={isRunning || isSubmitting || isReadOnly}
                            className="bg-green-600 hover:bg-green-700 text-white h-9 shadow-sm"
                        >
                            {isSubmitting ? <Loader2 className="w-4 h-4 animate-spin mr-2" /> : <Send className="w-4 h-4 mr-2" />}
                            Submit
                        </Button>
                    )}
                </div>
            </header>

            {/* 2. MAIN WORKSPACE */}
            <div className="flex-1 w-full overflow-hidden flex">
                {/* LEFT PANEL: Description */}
                <div className="w-[35%] min-w-[300px] max-w-[600px] bg-white border-r border-gray-200 flex flex-col h-full">
                    <div className="flex-1 overflow-y-auto p-6">
                        <div className="mb-6">
                            <h2 className="text-xl font-bold text-gray-900 mb-2">
                                {currentQuestionIndex + 1}. {currentQuestion.title}
                            </h2>
                            <Separator className="my-4" />
                            <div className="prose prose-sm max-w-none text-gray-700 leading-relaxed whitespace-pre-wrap">
                                {currentQuestion.description || assignment.description}
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
                    {/* EDITOR */}
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

                        <div className="flex-1 relative overflow-hidden bg-[#2d2d2d]">
                            <div className="h-full w-full overflow-auto">
                                <Editor
                                    value={code}
                                    onValueChange={code => setCode(code)}
                                    highlight={code => highlight(code, languageConfig[selectedLanguage].prismLang)}
                                    padding={20}
                                    disabled={isReadOnly}
                                    style={{
                                        fontFamily: '"Fira Code", "Fira Mono", monospace',
                                        fontSize: 14,
                                        backgroundColor: isReadOnly ? '#1e1e1e' : '#2d2d2d',
                                        color: isReadOnly ? '#aaa' : '#f8f8f2',
                                        minHeight: '100%'
                                    }}
                                    className="min-h-full"
                                />
                            </div>
                        </div>
                    </div>

                    {/* DIVIDER */}
                    <div className="h-1 bg-gray-800 flex-shrink-0" />

                    {/* CONSOLE - SIMPLIFIED VERSION */}
                    <div className="flex-[40] min-h-0 bg-white flex flex-col">
                        <div className="h-9 bg-gray-50 border-b border-gray-200 flex items-center justify-between px-4 select-none flex-shrink-0">
                            <div className="flex items-center gap-2">
                                <div className="flex items-center gap-2 text-gray-500 font-medium text-xs">
                                    <Terminal className="w-3.5 h-3.5" />
                                    Output
                                </div>
                                {isRunning && <span className="text-xs text-indigo-600 animate-pulse">Running Code...</span>}
                                {output?.status === 'error' && <span className="w-1.5 h-1.5 rounded-full bg-red-500" />}
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
                                    <div className={`p-3 rounded-lg border ${output.status === 'success' ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'}`}>
                                        <div className="flex flex-col gap-2">
                                            <div className="flex items-center gap-2">
                                                {output.status === 'success' ? (
                                                    <CheckCircle2 className="w-4 h-4 text-green-600" />
                                                ) : (
                                                    <XCircle className="w-4 h-4 text-red-600" />
                                                )}
                                                <span className={`font-medium text-sm ${output.status === 'success' ? 'text-green-800' : 'text-red-800'}`}>
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
                                                            <div className={`p-3 rounded border-2 text-sm font-mono ${result.error ? 'bg-red-50 border-red-300 text-red-800' : 'bg-green-50 border-green-300 text-green-800'}`}>
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
                                                                <div className="text-xs font-semibold text-gray-500 mb-2">📋 Test Case Comparison:</div>
                                                                <div className="grid grid-cols-2 gap-3 text-xs">
                                                                    <div>
                                                                        <div className="font-semibold text-gray-600 mb-1">Expected:</div>
                                                                        <div className="bg-blue-100 p-2 rounded font-mono text-blue-800">
                                                                            {result.expected}
                                                                        </div>
                                                                    </div>
                                                                    <div>
                                                                        <div className="font-semibold text-gray-600 mb-1">Your Output:</div>
                                                                        <div className={`p-2 rounded font-mono ${result.testPassed ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'}`}>
                                                                            {result.output || '(no output)'}
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div className={`mt-2 text-xs font-medium ${result.testPassed ? 'text-green-600' : 'text-yellow-600'}`}>
                                                                    {result.testPassed ? '✅ Matches expected output' : '⚠️ Different from expected output (but your code ran successfully!)'}
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
