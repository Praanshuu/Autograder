import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import {
    ChevronLeft,
    Play,
    Send,
    RotateCcw,
    CheckCircle2,
    XCircle,
    Lightbulb,
    Terminal,
    Loader2,
    Star,
    Trophy,
    Target,
    Zap,
    BookOpen,
    ArrowRight
} from "lucide-react";
import { Button } from "../../ui/button";
import { Badge } from "../../ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "../../ui/card";
import { Separator } from "../../ui/separator";
import { motion, AnimatePresence } from "framer-motion";

// Code Editor
import Editor from 'react-simple-code-editor';
import { highlight, languages } from 'prismjs/components/prism-core';
import 'prismjs/components/prism-clike';
import 'prismjs/components/prism-python';
import 'prismjs/components/prism-java';
import 'prismjs/components/prism-c';
import 'prismjs/themes/prism-tomorrow.css';

// Services
import { practiceService } from "../../../services/practiceService";

const DIFFICULTY_COLORS = {
  easy: "bg-green-100 text-green-700 border-green-200",
  medium: "bg-yellow-100 text-yellow-700 border-yellow-200", 
  hard: "bg-red-100 text-red-700 border-red-200"
};

const DIFFICULTY_ICONS = {
  easy: <Target className="w-3 h-3" />,
  medium: <Zap className="w-3 h-3" />,
  hard: <Trophy className="w-3 h-3" />
};

const PracticeWorkspace = () => {
    const { questionId } = useParams();
    const navigate = useNavigate();

    // State
    const [question, setQuestion] = useState(null);
    const [progress, setProgress] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const [code, setCode] = useState("");
    const [selectedLanguage, setSelectedLanguage] = useState("python");
    const [output, setOutput] = useState(null);
    const [isRunning, setIsRunning] = useState(false);
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [showHint, setShowHint] = useState(false);
    const [showSuccess, setShowSuccess] = useState(false);
    const [pointsEarned, setPointsEarned] = useState(0);

    // Language configuration - Limited to 3 languages supported by dynamic analyzer
    const languageConfig = {
        python: {
            name: "Python 3",
            extension: "py",
            defaultCode: "# Write your solution here\n",
            icon: "🐍",
            prismLang: languages.python
        },
        java: {
            name: "Java",
            extension: "java",
            defaultCode: "// Write your solution here\n",
            icon: "☕",
            prismLang: languages.java
        },
        c: {
            name: "C",
            extension: "c",
            defaultCode: "// Write your solution here\n",
            icon: "🔧",
            prismLang: languages.c
        }
    };

    // Load practice question and progress
    useEffect(() => {
        const fetchData = async () => {
            if (!questionId) return;
            
            try {
                setLoading(true);
                
                // Fetch question and progress in parallel
                const [questionRes, progressRes] = await Promise.all([
                    practiceService.getPracticeQuestion(questionId),
                    practiceService.getPracticeProgress({ practice_question: questionId })
                ]);

                setQuestion(questionRes.data);
                
                // Find progress for this specific question
                const progressData = Array.isArray(progressRes.data) ? progressRes.data : (progressRes.data.results || []);
                const questionProgress = progressData.find(p => p.practice_question == questionId);
                setProgress(questionProgress || null);

                // Set initial code
                if (questionRes.data.starter_code) {
                    setCode(questionRes.data.starter_code);
                } else {
                    setCode(languageConfig[selectedLanguage].defaultCode);
                }

            } catch (err) {
                console.error("Failed to load practice question:", err);
                setError("Failed to load practice question");
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, [questionId, selectedLanguage]);

    // Start practice session when component mounts
    useEffect(() => {
        if (question && !progress) {
            practiceService.startPracticeSession(questionId).catch(console.error);
        }
    }, [question, progress, questionId]);

    const handleLanguageChange = (newLanguage) => {
        setSelectedLanguage(newLanguage);
        
        // Reset to starter code or default for new language
        if (question?.starter_code) {
            setCode(question.starter_code);
        } else {
            setCode(languageConfig[newLanguage].defaultCode);
        }
        
        setOutput(null);
    };

    const handleRunCode = async () => {
        if (!question) return;

        setIsRunning(true);
        setOutput({ status: 'running' });

        try {
            const response = await practiceService.runPracticeCode(questionId, {
                code: code,
                language: selectedLanguage,
                test_cases: question.test_cases || []
            });

            // Format result for UI
            const resultData = response.data.data || response.data;
            
            const formattedOutput = {
                status: resultData.summary.execution_successful ? 'success' : 'error',
                message: resultData.summary.execution_successful ?
                    'Code executed successfully!' : 'Code execution failed',
                results: resultData.results.map((r, index) => ({
                    id: index,
                    status: r.error ? 'error' : 'success',
                    output: r.actual_output || '',
                    expected: r.expected_output || '',
                    error: r.error || '',
                    input: r.test_case?.input || question.test_cases[index]?.input || '',
                    testPassed: r.passed
                }))
            };

            setOutput(formattedOutput);

        } catch (err) {
            console.error("Run failed:", err);
            setOutput({
                status: 'error',
                message: 'Execution failed: ' + (err.message || 'Unknown error'),
                results: []
            });
        } finally {
            setIsRunning(false);
        }
    };

    const handleSubmit = async () => {
        if (!question) return;

        setIsSubmitting(true);
        
        try {
            const response = await practiceService.submitPracticeCode(questionId, {
                code: code,
                language: selectedLanguage
            });

            const submissionData = response.data;
            
            // Process submission result
            const formattedResults = submissionData.test_results.map((r, idx) => ({
                id: idx,
                status: r.status === 'pass' ? 'success' : 'error',
                output: r.actual_output || '',
                expected: question.test_cases[idx]?.expected_output || '',
                error: r.error_message || '',
                input: question.test_cases[idx]?.input || '',
                testPassed: r.status === 'pass'
            }));

            const allPassed = formattedResults.every(r => r.status === 'success');

            setOutput({
                status: allPassed ? 'success' : 'error',
                message: allPassed ? 
                    `🎉 Congratulations! All test cases passed! You earned ${submissionData.points_earned} points!` : 
                    'Some test cases failed. Keep trying - you can submit unlimited times!',
                results: formattedResults,
                isSubmission: true,
                pointsEarned: submissionData.points_earned || 0
            });

            if (allPassed) {
                setPointsEarned(submissionData.points_earned || 0);
                setShowSuccess(true);
                
                // Update progress
                setProgress(prev => ({
                    ...prev,
                    is_completed: true,
                    attempts_count: (prev?.attempts_count || 0) + 1,
                    best_score: 100
                }));
            } else {
                // Update attempt count
                setProgress(prev => ({
                    ...prev,
                    attempts_count: (prev?.attempts_count || 0) + 1
                }));
            }

        } catch (err) {
            console.error("Submission failed:", err);
            setOutput({
                status: 'error',
                message: 'Submission failed: ' + (err.response?.data?.message || err.message),
                results: []
            });
        } finally {
            setIsSubmitting(false);
        }
    };

    const handleBackClick = () => {
        navigate('/student/practice');
    };

    const handleTryAnother = () => {
        navigate('/student/practice');
    };

    if (loading) {
        return (
            <div className="flex h-screen items-center justify-center bg-gray-50">
                <div className="text-center">
                    <Loader2 className="w-10 h-10 animate-spin text-indigo-600 mx-auto mb-4" />
                    <p className="text-gray-500 font-medium">Loading practice question...</p>
                </div>
            </div>
        );
    }

    if (error || !question) {
        return (
            <div className="flex h-screen items-center justify-center bg-gray-50">
                <div className="text-center">
                    <XCircle className="w-12 h-12 text-red-500 mx-auto mb-4" />
                    <h2 className="text-xl font-bold text-gray-900 mb-2">Error Loading Question</h2>
                    <p className="text-gray-500 mb-6">{error || "Question not found."}</p>
                    <Button onClick={handleBackClick}>Back to Practice</Button>
                </div>
            </div>
        );
    }

    const testCases = question.test_cases || [];
    const isCompleted = progress?.is_completed || false;

    return (
        <div className="flex flex-col h-screen bg-gray-50 text-gray-900 font-sans overflow-hidden">
            {/* Completion Banner */}
            {isCompleted && (
                <div className="bg-green-100 border-b border-green-200 px-4 py-2 text-green-800 text-sm font-medium flex items-center justify-center gap-2">
                    <CheckCircle2 className="w-4 h-4" />
                    🎉 Completed! You earned {pointsEarned} points. Feel free to continue practicing or try another question.
                </div>
            )}

            {/* Header */}
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
                            {question.title}
                        </h1>
                        <div className="flex items-center gap-2 text-xs text-gray-500">
                            <Badge className={DIFFICULTY_COLORS[question.difficulty] || DIFFICULTY_COLORS.medium}>
                                {DIFFICULTY_ICONS[question.difficulty]}
                                <span className="ml-1 capitalize">{question.difficulty}</span>
                            </Badge>
                            <span>•</span>
                            <Star className="w-3 h-3 text-yellow-500" />
                            <span>{question.point_value} pts</span>
                            {progress?.attempts_count > 0 && (
                                <>
                                    <span>•</span>
                                    <span>{progress.attempts_count} attempt{progress.attempts_count !== 1 ? 's' : ''}</span>
                                </>
                            )}
                        </div>
                    </div>
                </div>

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

                    <Button
                        size="sm"
                        onClick={handleSubmit}
                        disabled={isRunning || isSubmitting}
                        className="bg-green-600 hover:bg-green-700 text-white h-9 shadow-sm"
                    >
                        {isSubmitting ? <Loader2 className="w-4 h-4 animate-spin mr-2" /> : <Send className="w-4 h-4 mr-2" />}
                        {isCompleted ? 'Submit Again' : 'Submit'}
                    </Button>
                </div>
            </header>

            {/* Main Workspace */}
            <div className="flex-1 w-full overflow-hidden flex">
                {/* Left Panel: Description */}
                <div className="w-[35%] min-w-[300px] max-w-[600px] bg-white border-r border-gray-200 flex flex-col h-full">
                    <div className="flex-1 overflow-y-auto p-6">
                        <div className="mb-6">
                            <div className="flex items-center gap-2 mb-4">
                                <BookOpen className="w-5 h-5 text-indigo-600" />
                                <h2 className="text-xl font-bold text-gray-900">
                                    {question.title}
                                </h2>
                            </div>
                            
                            {question.category && (
                                <div className="mb-4">
                                    <Badge variant="outline" className="text-gray-600 border-gray-200">
                                        {question.category.charAt(0).toUpperCase() + question.category.slice(1)}
                                    </Badge>
                                </div>
                            )}
                            
                            <Separator className="my-4" />
                            
                            <div className="prose prose-sm max-w-none text-gray-700 leading-relaxed whitespace-pre-wrap">
                                {question.description}
                            </div>
                        </div>

                        {/* Test Cases Preview */}
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

                        {/* Practice Info */}
                        <div className="mt-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                            <h4 className="text-sm font-semibold text-blue-900 mb-2 flex items-center gap-2">
                                <Target className="w-4 h-4" />
                                Practice Mode
                            </h4>
                            <ul className="text-xs text-blue-800 space-y-1">
                                <li>• Unlimited submissions until you get it right</li>
                                <li>• Immediate feedback on each attempt</li>
                                <li>• Earn full points when all test cases pass</li>
                                <li>• No time pressure - take your time to learn</li>
                            </ul>
                        </div>

                        {/* Hint */}
                        {question.hint && (
                            <div className="mt-6 border-t border-gray-100 pt-4">
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
                                        {question.hint}
                                    </motion.div>
                                )}
                            </div>
                        )}
                    </div>
                </div>

                {/* Right Panel: Editor & Output */}
                <div className="flex-1 bg-white flex flex-col h-full">
                    {/* Editor */}
                    <div className="flex-[60] min-h-0 flex flex-col bg-[#2d2d2d]">
                        <div className="bg-[#2d2d2d] border-b border-[#111] px-4 h-9 flex justify-between items-center text-xs text-gray-400 select-none flex-shrink-0">
                            <div className="flex items-center gap-2">
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
                            <span
                                className="hover:text-white cursor-pointer transition-colors flex items-center gap-1"
                                onClick={() => setCode(question.starter_code || languageConfig[selectedLanguage].defaultCode)}
                            >
                                <RotateCcw className="w-3 h-3" /> Reset
                            </span>
                        </div>

                        <div className="flex-1 relative overflow-hidden bg-[#2d2d2d]">
                            <div className="h-full w-full overflow-auto">
                                <Editor
                                    value={code}
                                    onValueChange={setCode}
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

                    {/* Divider */}
                    <div className="h-1 bg-gray-800 flex-shrink-0" />

                    {/* Output Console */}
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
                                    <span className="text-sm">Click "Run Code" to test your solution</span>
                                    <span className="text-xs mt-1">Or click "Submit" to check all test cases</span>
                                </div>
                            )}

                            {isRunning && (
                                <div className="flex flex-col items-center justify-center text-blue-600 h-full">
                                    <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mb-2"></div>
                                    <span className="text-sm">Running your code...</span>
                                </div>
                            )}

                            {output && (
                                <div className="space-y-4">
                                    {/* Status Message */}
                                    <div className={`p-3 rounded-lg border ${
                                        output.status === 'success' ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'
                                    }`}>
                                        <div className="flex items-center gap-2">
                                            {output.status === 'success' ? (
                                                <CheckCircle2 className="w-4 h-4 text-green-600" />
                                            ) : (
                                                <XCircle className="w-4 h-4 text-red-600" />
                                            )}
                                            <span className={`font-medium text-sm ${
                                                output.status === 'success' ? 'text-green-800' : 'text-red-800'
                                            }`}>
                                                {output.message}
                                            </span>
                                        </div>
                                        
                                        {output.isSubmission && output.pointsEarned > 0 && (
                                            <div className="mt-2 flex items-center gap-2 text-green-700">
                                                <Star className="w-4 h-4 text-yellow-500" />
                                                <span className="font-semibold">+{output.pointsEarned} points earned!</span>
                                            </div>
                                        )}
                                    </div>

                                    {/* Test Results */}
                                    {output.results && output.results.length > 0 && (
                                        <div className="space-y-3">
                                            {output.results.map((result, idx) => (
                                                <div key={idx} className="border border-gray-200 rounded-lg overflow-hidden">
                                                    <div className={`px-4 py-2 border-b ${
                                                        result.testPassed ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'
                                                    }`}>
                                                        <h3 className={`font-semibold text-sm flex items-center gap-2 ${
                                                            result.testPassed ? 'text-green-800' : 'text-red-800'
                                                        }`}>
                                                            {result.testPassed ? (
                                                                <CheckCircle2 className="w-4 h-4" />
                                                            ) : (
                                                                <XCircle className="w-4 h-4" />
                                                            )}
                                                            Test Case {idx + 1}
                                                            {result.testPassed ? ' - Passed ✓' : ' - Failed ✗'}
                                                        </h3>
                                                    </div>

                                                    <div className="p-4 space-y-3">
                                                        {result.input && (
                                                            <div>
                                                                <div className="text-xs font-semibold text-gray-500 mb-1">INPUT:</div>
                                                                <div className="bg-gray-100 p-2 rounded text-sm font-mono border">
                                                                    {result.input}
                                                                </div>
                                                            </div>
                                                        )}

                                                        <div className="grid grid-cols-2 gap-3">
                                                            <div>
                                                                <div className="text-xs font-semibold text-gray-500 mb-1">EXPECTED:</div>
                                                                <div className="bg-blue-100 p-2 rounded text-sm font-mono border text-blue-800">
                                                                    {result.expected || '(no output expected)'}
                                                                </div>
                                                            </div>
                                                            <div>
                                                                <div className="text-xs font-semibold text-gray-500 mb-1">YOUR OUTPUT:</div>
                                                                <div className={`p-2 rounded text-sm font-mono border ${
                                                                    result.testPassed ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
                                                                }`}>
                                                                    {result.error ? (
                                                                        <div className="text-red-600">
                                                                            <div className="font-bold">Error:</div>
                                                                            <div>{result.error}</div>
                                                                        </div>
                                                                    ) : (
                                                                        result.output || '(no output)'
                                                                    )}
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            ))}
                                        </div>
                                    )}

                                    {/* Encouragement for failed submissions */}
                                    {output.isSubmission && output.status === 'error' && (
                                        <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                                            <div className="flex items-center gap-2 text-blue-800 mb-2">
                                                <Target className="w-4 h-4" />
                                                <span className="font-semibold">Keep Going!</span>
                                            </div>
                                            <p className="text-sm text-blue-700">
                                                Don't worry - practice makes perfect! Review the failed test cases above, 
                                                adjust your code, and try again. You have unlimited attempts.
                                            </p>
                                        </div>
                                    )}
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </div>

            {/* Success Modal */}
            <AnimatePresence>
                {showSuccess && (
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
                            <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                                <Trophy className="w-8 h-8 text-green-600" />
                            </div>
                            <h2 className="text-2xl font-bold text-gray-900 mb-2">Congratulations! 🎉</h2>
                            <p className="text-gray-600 mb-4">
                                You've successfully completed this practice question and earned <strong>{pointsEarned} points</strong>!
                            </p>
                            <div className="flex gap-3">
                                <Button
                                    variant="outline"
                                    onClick={() => setShowSuccess(false)}
                                    className="flex-1"
                                >
                                    Continue Practicing
                                </Button>
                                <Button
                                    onClick={handleTryAnother}
                                    className="flex-1 bg-indigo-600 hover:bg-indigo-700 text-white"
                                >
                                    Try Another <ArrowRight className="w-4 h-4 ml-1" />
                                </Button>
                            </div>
                        </motion.div>
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    );
};

export default PracticeWorkspace;