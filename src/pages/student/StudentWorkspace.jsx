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
    
    // Timer state
    const [timeSpent, setTimeSpent] = useState(0); // in seconds
    const [isTimerRunning, setIsTimerRunning] = useState(false);
    const [showHint, setShowHint] = useState(false);
    const timerIntervalRef = useRef(null);
    const lastUpdateRef = useRef(Date.now());

    // Language configuration
    const languageConfig = {
        python: {
            name: "Python 3",
            extension: "py",
            defaultCode: "# Write your Python code here\nprint(\"Hello, World!\")",
            icon: "🐍",
            prismLang: languages.python
        },
        javascript: {
            name: "JavaScript",
            extension: "js", 
            defaultCode: "// Write your JavaScript code here\nconsole.log(\"Hello, World!\");",
            icon: "🟨",
            prismLang: languages.javascript
        },
        java: {
            name: "Java",
            extension: "java",
            defaultCode: "// Write your Java code here\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}",
            icon: "☕",
            prismLang: languages.java
        },
        cpp: {
            name: "C++",
            extension: "cpp",
            defaultCode: "// Write your C++ code here\n#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"Hello, World!\" << endl;\n    return 0;\n}",
            icon: "⚡",
            prismLang: languages.cpp
        },
        c: {
            name: "C",
            extension: "c", 
            defaultCode: "// Write your C code here\n#include <stdio.h>\n\nint main() {\n    printf(\"Hello, World!\\n\");\n    return 0;\n}",
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
                    console.log("First question:", data.questions[0]);
                    try {
                        const timerResponse = await submissionService.getTimer(assignmentId, questionId);
                        if (timerResponse.success && timerResponse.data) {
                            setTimeSpent(timerResponse.data.time_spent || 0);
                            setCode(timerResponse.data.code_content || data.questions[0].starter_code || "# Write your python code here\n");
                        } else {
                            setCode(data.questions[0].starter_code || "# Write your python code here\n");
                        }
                    } catch (err) {
                        console.error("Failed to load timer:", err);
                        setCode(data.questions[0].starter_code || "# Write your python code here\n");
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
            e.returnValue = 'Are you sure you want to leave? Your progress will be saved but the timer will stop.';
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
        if (isTimerRunning) {
            timerIntervalRef.current = setInterval(() => {
                setTimeSpent(prev => prev + 1);
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
    }, [isTimerRunning]);
    
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
        
        const questionId = assignment.questions[0].id;
        try {
            await submissionService.startTimer(assignmentId, questionId);
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
        
        const questionId = assignment.questions[0].id;
        try {
            await submissionService.updateTimer(assignmentId, questionId, timeSpent);
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

    // Handle back button with warning
    const handleBackClick = () => {
        setShowExitWarning(true);
    };

    const handleConfirmExit = () => {
        pauseTimer();
        navigate('/student/dashboard');
    };

    // Language change handler
    const handleLanguageChange = (newLanguage) => {
        setSelectedLanguage(newLanguage);
        setCode(languageConfig[newLanguage].defaultCode);
        setOutput(null); // Clear previous output
    };

    // Handler: Run Code (Sandbox)
    const handleRunCode = async () => {
        if (!assignment || !assignment.questions?.[0]) return;

        setIsRunning(true);
        setOutput({ status: 'running' }); // UI State for "Running..."

        try {
            const question = assignment.questions[0];
            const testCases = question.test_cases || [];

            console.log("🚀 Starting code execution...");
            console.log("Code:", code);
            console.log("Test cases:", testCases);

            // Call Backend Sandbox with correct format
            const response = await submissionService.runCode({
                code: code,
                language: selectedLanguage, // Use selected language instead of hardcoded "python"
                test_cases: testCases,
                question_id: question.id
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
            
            const question = assignment.questions[0];
            const response = await submissionService.submitCode({
                assignment: assignment.id,
                question: question.id,
                code_content: code,
                language: selectedLanguage, // Use selected language instead of hardcoded "python"
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

    const currentQuestion = assignment.questions?.[0] || {};
    const testCases = currentQuestion.test_cases || [];

    return (
        <div className="flex flex-col h-screen bg-gray-50 text-gray-900 font-sans overflow-hidden">
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
                    </h1>
                    <div className="h-4 w-px bg-gray-200" />
                    {/* Timer Display */}
                    <div className="flex items-center gap-2 bg-gray-50 px-3 py-1 rounded-md border border-gray-200">
                        <Clock className="w-4 h-4 text-gray-600" />
                        <span className="font-mono text-sm font-medium text-gray-900">{formatTime(timeSpent)}</span>
                        <div className={`w-2 h-2 rounded-full ${isTimerRunning ? 'bg-green-500 animate-pulse' : 'bg-gray-400'}`} />
                    </div>
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
                        disabled={isRunning || isSubmitting}
                        className="h-8 px-4 bg-gray-100 hover:bg-gray-200 text-gray-700 border-0 font-medium text-xs gap-2"
                    >
                        {isRunning ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <Play className="w-3.5 h-3.5 fill-current" />}
                        Run Code
                    </Button>
                    <Button
                        size="sm"
                        onClick={handleSubmit}
                        disabled={isRunning || isSubmitting}
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
                                onClick={() => setCode(currentQuestion.starter_code || "")}
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
                                Are you sure you want to exit? Your progress will be saved, but the timer will stop. 
                                You can only exit by submitting your solution.
                            </p>
                            <div className="flex gap-3">
                                <Button 
                                    variant="outline" 
                                    onClick={() => setShowExitWarning(false)}
                                    className="flex-1"
                                >
                                    Continue Working
                                </Button>
                                <Button 
                                    onClick={handleConfirmExit}
                                    className="flex-1 bg-red-600 hover:bg-red-700 text-white"
                                >
                                    Exit Assignment
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
                            <h2 className="text-2xl font-bold text-gray-900 mb-2">Submitted!</h2>
                            <p className="text-gray-500 mb-6">Your code has been sent for grading. You will be redirected to the dashboard in a few seconds.</p>
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
