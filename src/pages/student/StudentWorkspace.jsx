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
    Pause,
    PlayCircle
} from "lucide-react";
import { Button } from "../../components/ui/button";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "../../components/ui/tabs";
import { motion, AnimatePresence } from "framer-motion";

// --- PRO DEPENDENCIES ---
import Editor from 'react-simple-code-editor';
import { highlight, languages } from 'prismjs/components/prism-core';
import 'prismjs/components/prism-clike';
import 'prismjs/components/prism-python';
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
    const [activeTab, setActiveTab] = useState("description");
    const [selectedTestCase, setSelectedTestCase] = useState(0);
    const [output, setOutput] = useState(null);
    const [isRunning, setIsRunning] = useState(false);
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [showConfetti, setShowConfetti] = useState(false);
    
    // Timer state
    const [timeSpent, setTimeSpent] = useState(0); // in seconds
    const [isTimerRunning, setIsTimerRunning] = useState(false);
    const [showHint, setShowHint] = useState(false);
    const timerIntervalRef = useRef(null);
    const lastUpdateRef = useRef(Date.now());

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

    // Handler: Run Code (Sandbox)
    const handleRunCode = async () => {
        if (!assignment || !assignment.questions?.[0]) return;

        setIsRunning(true);
        setOutput({ status: 'running' }); // UI State for "Running..."

        try {
            const question = assignment.questions[0];
            const testCases = question.test_cases || [];

            // Call Backend Sandbox
            const response = await submissionService.runCode(code, "python", testCases);

            // Format result for UI
            // Backend returns: { success: true, data: { results: [...], summary: ... } }
            const resultData = response.data.data;

            setOutput({
                status: resultData.summary.all_passed ? 'success' : 'error',
                message: resultData.summary.all_passed ? 'All Test Cases Passed!' : 'Some tests failed.',
                results: resultData.results.map((r, index) => ({
                    id: index,
                    status: r.passed ? 'pass' : 'fail',
                    output: r.actual_output,
                    expected: r.test_case.expected_output,
                    error: r.error,
                    input: r.test_case.input
                }))
            });

        } catch (err) {
            console.error("Run failed:", err);
            setOutput({
                status: 'error',
                message: 'Execution failed: ' + (err.response?.data?.message || err.message),
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
                language: "python",
                time_spent: timeSpent
            });

            // Backend grades it immediately for now (or queues it)
            // Assuming immediate grading response similar to runCode
            setShowConfetti(true);
            pauseTimer();

            // Optionally fetch the new "Submission" object to show history

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
                    <div className="flex items-center gap-2 cursor-pointer hover:bg-gray-50 py-1 pr-2 rounded transition-colors" onClick={() => navigate('/student/dashboard')}>
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
                        <button
                            onClick={() => isTimerRunning ? pauseTimer() : startTimer()}
                            className="ml-1 p-0.5 hover:bg-gray-200 rounded transition-colors"
                        >
                            {isTimerRunning ? (
                                <Pause className="w-3.5 h-3.5 text-gray-600" />
                            ) : (
                                <PlayCircle className="w-3.5 h-3.5 text-gray-600" />
                            )}
                        </button>
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
                                <span className="text-blue-400 font-medium">Python 3</span>
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
                                    highlight={code => highlight(code, languages.python)}
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

                    {/* CONSOLE */}
                    <div className="flex-[40] min-h-0 bg-white flex flex-col">
                        <div className="h-9 bg-gray-50 border-b border-gray-200 flex items-center justify-between px-4 select-none flex-shrink-0">
                            <div className="flex items-center gap-2">
                                <div className="flex items-center gap-2 text-gray-500 font-medium text-xs">
                                    <Terminal className="w-3.5 h-3.5" />
                                    Test Results
                                </div>
                                {isRunning && <span className="text-xs text-indigo-600 animate-pulse">Running Code...</span>}
                                {output?.status === 'error' && <span className="w-1.5 h-1.5 rounded-full bg-red-500" />}
                                {output?.status === 'success' && <span className="w-1.5 h-1.5 rounded-full bg-green-500" />}
                            </div>
                        </div>

                        <div className="flex-1 overflow-auto">
                            {!output && !isRunning && (
                                <div className="flex flex-col items-center justify-center text-gray-400 p-4 h-full">
                                    <span className="text-sm">Run your code to check test cases.</span>
                                </div>
                            )}

                            {output && (
                                <div className="flex h-full w-full">
                                    {/* Test Case List */}
                                    <div className="w-36 bg-gray-50 border-r border-gray-200 overflow-y-auto py-2 flex-shrink-0">
                                        <div className="px-3 pb-2 text-[10px] font-bold text-gray-400 uppercase tracking-wider">Cases</div>
                                        {output.results.map((result, idx) => (
                                            <button
                                                key={idx}
                                                onClick={() => setSelectedTestCase(idx)}
                                                className={`w-full text-left px-3 py-2 text-xs font-medium flex items-center gap-2 border-l-2 transition-all ${selectedTestCase === idx ? 'bg-white border-indigo-600 text-indigo-700' : 'border-transparent text-gray-600 hover:bg-gray-100'}`}
                                            >
                                                <span className={`w-1.5 h-1.5 rounded-full flex-shrink-0 ${result.status === 'pass' ? 'bg-green-500' : 'bg-red-500'}`} />
                                                Test Case {idx + 1}
                                            </button>
                                        ))}
                                    </div>

                                    {/* Result Details */}
                                    <div className="flex-1 p-4 overflow-y-auto min-w-0">
                                        {output.results[selectedTestCase] && (
                                            <div className="space-y-4">
                                                <div>
                                                    <h4 className="text-xs font-bold text-gray-500 uppercase mb-1">Input</h4>
                                                    <div className="bg-gray-50 p-2 rounded border border-gray-200 font-mono text-xs">{output.results[selectedTestCase].input}</div>
                                                </div>
                                                <div className="grid grid-cols-2 gap-4">
                                                    <div>
                                                        <h4 className="text-xs font-bold text-gray-500 uppercase mb-1">Expected</h4>
                                                        <div className="bg-gray-50 p-2 rounded border border-gray-200 font-mono text-xs">{output.results[selectedTestCase].expected}</div>
                                                    </div>
                                                    <div>
                                                        <h4 className="text-xs font-bold text-gray-500 uppercase mb-1">Your Output</h4>
                                                        <div className={`p-2 rounded border font-mono text-xs ${output.results[selectedTestCase].status === 'pass' ? 'bg-green-50 border-green-200 text-green-800' : 'bg-red-50 border-red-200 text-red-800'}`}>
                                                            {output.results[selectedTestCase].output}
                                                        </div>
                                                    </div>
                                                </div>
                                                {output.results[selectedTestCase].error && (
                                                    <div className="text-red-600 bg-red-50 p-2 rounded text-xs font-mono border border-red-100 mt-2">
                                                        {output.results[selectedTestCase].error}
                                                    </div>
                                                )}
                                            </div>
                                        )}
                                    </div>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </div>

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
                            <p className="text-gray-500 mb-6">Your code has been sent for grading.</p>
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
