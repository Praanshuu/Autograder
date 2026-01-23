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
import { Panel, Group, Separator } from "react-resizable-panels";

// Services
import { assignmentService } from "../../services/assignmentService";
import { submissionService } from "../../services/submissionService";

const StudentWorkspace = () => {
    const { assignmentId } = useParams();
    const navigate = useNavigate();

    // State
    const [assignment, setAssignment] = useState(null);
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

    // Fetch Assignment Data
    useEffect(() => {
        const fetchAssignment = async () => {
            if (!assignmentId) return;
            try {
                setLoading(true);
                const response = await assignmentService.getAssignment(assignmentId);
                const data = response.data;
                console.log("Assignment data loaded:", data);
                console.log("Questions:", data.questions);
                setAssignment(data);

                // Get timer state from backend
                if (data.questions && data.questions.length > 0) {
                    const questionId = data.questions[0].id;
                    const question = data.questions[0];

                    // Calculate time limits
                    const timeLimit = getTimeLimit(question.difficulty);
                    setTotalTimeAllowed(timeLimit);

                    console.log("First question:", question);
                    // Check for existing submissions
                    try {
                        const submissionsResponse = await submissionService.getAssignmentSubmissions(assignmentId);
                        if (submissionsResponse.data && submissionsResponse.data.length > 0) {
                            const passed = submissionsResponse.data.some(s => s.status === 'success');
                            if (passed) {
                                setIsCompleted(true);
                                // Optional: Load the successful code
                                // setCode(passedSubmission.code_content);
                            }
                        }
                    } catch (err) {
                        console.error("Failed to check submissions:", err);
                    }

                    try {
                        const timerResponse = await submissionService.getTimer(assignmentId, questionId, selectedLanguage);
                        if (timerResponse.success && timerResponse.data) {
                            const spentTime = timerResponse.data.time_spent || 0;
                            setTimeSpent(spentTime);

                            // Calculate remaining time
                            const remaining = Math.max(0, timeLimit - spentTime);
                            setTimeRemaining(remaining);

                            // Only set code if not completed/submitted or if we want to show draft
                            if (!isCompleted) {
                                setCode(timerResponse.data.code_content || data.questions[0].starter_code || languageConfig[selectedLanguage].defaultCode);
                            }
                        } else {
                            setTimeSpent(0);
                            setTimeRemaining(timeLimit);
                            if (!isCompleted) setCode(data.questions[0].starter_code || languageConfig[selectedLanguage].defaultCode);
                        }
                    } catch (err) {
                        console.error("Failed to load timer:", err);
                        setTimeSpent(0);
                        setTimeRemaining(timeLimit);
                        if (!isCompleted) setCode(data.questions[0].starter_code || languageConfig[selectedLanguage].defaultCode);
                    }
                } else {
                    console.error("No questions found in assignment!");
                }
            } catch (err) {
                console.error("Failed to load assignment:", err);
                setError("Could not load assignment. Please try again.");
            } finally {
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

        const aqId = assignment.questions[0].id; // This is the AssignmentQuestion ID
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

        const aqId = assignment.questions[0].id;
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

            const question = assignment.questions[0];
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

            const question = assignment.questions[0];
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
                const questionStarterCode = assignment?.questions?.[0]?.starter_code;
                if (questionStarterCode && questionStarterCode.trim()) {
                    setCode(questionStarterCode);
                } else {
                    setCode(languageConfig[newLanguage].defaultCode);
                }
            }
        } catch (error) {
            console.error("Error loading language-specific code:", error);
            // Fallback to starter code or default
            const questionStarterCode = assignment?.questions?.[0]?.starter_code;
            if (questionStarterCode && questionStarterCode.trim()) {
                setCode(questionStarterCode);
            } else {
                setCode(languageConfig[newLanguage].defaultCode);
            }
        }

        setOutput(null); // Clear previous output
    };

    // Handler: Run Code (Sandbox)
    const handleRunCode = async () => {
        if (!assignment || !assignment.questions?.[0]) return;

        setIsRunning(true);
        setOutput({ status: 'running' }); // UI State for "Running..."

        try {
            const aq = assignment.questions[0];
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

    // Handler: Submit Code (Final)
    const handleSubmit = async () => {
        if (!assignment || !assignment.questions?.[0]) return;

        setIsSubmitting(true);
        try {
            // Save timer before submitting
            await updateTimerOnBackend();

            const aq = assignment.questions[0];
            const response = await submissionService.submitCode({
                assignment_id: assignment.id,
                assignment_question_id: aq.id,
                question_id: aq.question?.id,
                code_content: code,
                language: selectedLanguage,
                time_spent: timeSpent
            });

            // Backend grades it immediately for now (or queues it)
            // Assuming immediate grading response similar to runCode
            setShowConfetti(true);
            pauseTimer();

            // Navigate back to dashboard after 3 seconds
            setTimeout(() => {
                navigate('/student/dashboard');
            }, 3000);

        } catch (err) {
            console.error("Submission failed:", err);
            alert("Submission failed: " + (err.response?.data?.message || err.message));
        } finally {
            setIsSubmitting(false);
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

    // Helper to get current AQ and Question
    const getCurrentAQ = () => assignment?.questions?.[0]; // For now only first question
    const getCurrentQuestion = () => getCurrentAQ()?.question || {};

    const currentQuestion = getCurrentQuestion();
    const testCases = currentQuestion.test_cases || [];

    return (
        <div className="flex flex-col h-screen bg-gray-50 text-gray-900 font-sans overflow-hidden">
            {/* Completed Banner */}
            {isCompleted && (
                <div className="bg-green-100 border-b border-green-200 px-4 py-2 text-green-800 text-sm font-medium flex items-center justify-center gap-2">
                    <CheckCircle className="w-4 h-4" />
                    Assignment Completed! You cannot submit changes anymore.
                </div>
            )}

            {/* 1. HEADER */}
            <header className="h-12 bg-white border-b border-gray-200 flex items-center justify-between px-4 z-20 shadow-sm flex-shrink-0">
                <div className="flex items-center gap-4">
                    <div className="flex items-center gap-2 cursor-pointer hover:bg-gray-50 py-1 pr-2 rounded transition-colors" onClick={handleBackClick}>
                        <div className="bg-gray-100 p-1 rounded">
                            <ChevronLeft className="w-4 h-4 text-gray-600" />
                        </div>
                        <span className="font-semibold text-sm text-gray-700">Back</span>
                    </div>
                    <div className="h-4 w-px bg-gray-200" />
                    <h1 className="font-bold text-sm text-gray-900 flex items-center gap-2">
                        {assignment.title}
                        <span className="text-[10px] font-medium text-amber-600 bg-amber-50 border border-amber-100 px-1.5 py-0.5 rounded uppercase tracking-wider">
                            {assignment.difficulty || "Medium"}
                        </span>
                        <span className="text-[10px] font-medium text-blue-600 bg-blue-50 border border-blue-100 px-1.5 py-0.5 rounded">
                            {Math.floor(totalTimeAllowed / 60)} min
                        </span>
                    </h1>
                    <div className="h-4 w-px bg-gray-200" />
                    {/* Timer Display */}
                    {!isCompleted && (
                        <div className="flex items-center gap-2 bg-gray-50 px-3 py-1 rounded-md border border-gray-200">
                            <Clock className="w-4 h-4 text-gray-600" />
                            <span className={`font-mono text-sm font-medium ${timeRemaining <= 300 ? 'text-red-600' : 'text-gray-900'}`}>
                                {formatTime(timeRemaining)} remaining
                            </span>
                            <div className={`w-2 h-2 rounded-full ${isTimerRunning ? 'bg-green-500 animate-pulse' : 'bg-gray-400'}`} />
                        </div>
                    )}
                </div>

                <div className="flex items-center gap-2">
                    <Button variant="ghost" size="sm" className="h-8 text-gray-500 hover:text-gray-900">
                        <Settings className="w-4 h-4" />
                    </Button>
                    <div className="h-4 w-px bg-gray-200 mx-1" />
                    <Button
                        variant="secondary"
                        size="sm"
                        onClick={handleRunCode}
                        disabled={isRunning || isSubmitting || isCompleted}
                        className="h-8 px-4 bg-gray-100 hover:bg-gray-200 text-gray-700 border-0 font-medium text-xs gap-2"
                    >
                        {isRunning ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <Play className="w-3.5 h-3.5 fill-current" />}
                        Run Code
                    </Button>
                    <Button
                        size="sm"
                        onClick={handleSubmit}
                        disabled={isRunning || isSubmitting || isCompleted}
                        className="h-8 px-5 bg-green-600 hover:bg-green-700 text-white font-medium text-xs gap-2 shadow-sm"
                    >
                        {isSubmitting ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <Send className="w-3.5 h-3.5" />}
                        Submit
                    </Button>
                </div>
            </header>

            {/* 2. MAIN WORKSPACE */}
            <div className="h-[calc(100vh-3rem)] w-full overflow-hidden flex">
                {/* LEFT PANEL: Description - FIXED WIDTH */}
                <div className="w-[30%] min-w-[300px] max-w-[500px] bg-white border-r border-gray-200 flex flex-col">
                    <div className="bg-gray-50 border-b border-gray-200 px-3 h-10 flex items-center flex-shrink-0">
                        <FileText className="w-4 h-4 mr-2 text-gray-600" />
                        <span className="text-sm font-medium text-gray-700">Description</span>
                    </div>
                    <div className="flex-1 overflow-y-auto p-5">
                        <h2 className="text-lg font-bold text-gray-900 mb-3">{currentQuestion.title}</h2>
                        <p className="text-sm text-gray-600 leading-relaxed whitespace-pre-wrap">
                            {currentQuestion.description || assignment.description}
                        </p>

                        {/* Hint Section */}
                        {currentQuestion.hint && (
                            <div className="mt-6 border-t border-gray-200 pt-4">
                                <button
                                    onClick={() => setShowHint(!showHint)}
                                    className="flex items-center gap-2 text-sm font-medium text-indigo-600 hover:text-indigo-700 transition-colors mb-3"
                                >
                                    <Lightbulb className="w-4 h-4" />
                                    {showHint ? 'Hide Hint' : 'Show Hint'}
                                </button>

                                {showHint && (
                                    <div className="bg-amber-50 border border-amber-200 rounded-lg p-4">
                                        <div className="flex items-start gap-3">
                                            <Lightbulb className="w-5 h-5 text-amber-600 flex-shrink-0 mt-0.5" />
                                            <div>
                                                <h4 className="font-semibold text-amber-900 mb-1">Hint</h4>
                                                <p className="text-sm text-amber-800">{currentQuestion.hint}</p>
                                            </div>
                                        </div>
                                    </div>
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
                                    style={{
                                        fontFamily: '"Fira Code", "Fira Mono", monospace',
                                        fontSize: 14,
                                        backgroundColor: '#2d2d2d',
                                        color: '#f8f8f2',
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
        </div>
    );
};

export default StudentWorkspace;
