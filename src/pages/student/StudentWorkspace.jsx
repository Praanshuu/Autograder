import React, { useState, useEffect } from "react";
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
    GripVertical
} from "lucide-react";
import { Button } from "../../components/ui/button";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "../../components/ui/tabs";
import { motion } from "framer-motion";

// --- PRO DEPENDENCIES ---
import Editor from 'react-simple-code-editor';
import { highlight, languages } from 'prismjs/components/prism-core';
import 'prismjs/components/prism-clike';
import 'prismjs/components/prism-python';
import 'prismjs/themes/prism-tomorrow.css'; // Dark theme for code
// ADAPTING TO INSTALLED VERSION: Using Group and Separator instead of PanelGroup/PanelResizeHandle
import { Panel, Group, Separator } from "react-resizable-panels";

// --- MOCK DATA FOR ASSIGNMENT 2 ---
const PROBLEM_DATA = {
    id: "a2",
    title: "Assignment 2: Text Processing",
    points: 100,
    difficulty: "Medium",
    description: `
    <h3>Palindrome Checker with Edge Cases</h3>
    <p>Write a function <code>isStrictModePalindrome(text)</code> that checks if a string is a palindrome.</p>
    
    <h4>Rules:</h4>
    <ul class="list-disc pl-5 space-y-1">
      <li>The check should be <strong>case-insensitive</strong>.</li>
      <li>You must <strong>ignore all non-alphanumeric characters</strong> (spaces, punctuation, symbols).</li>
      <li><strong>Important:</strong> If the input is a negative number (e.g., <code>-121</code>), it is <strong>NOT</strong> a palindrome.</li>
      <li>If the input is an empty string, return <code>true</code>.</li>
    </ul>

    <h4>Examples</h4>
    <pre class="bg-gray-100 p-3 rounded-md text-sm font-mono mt-2">
isStrictModePalindrome("A man, a plan, a canal: Panama") 
// Returns: True (reads "amanaplanacanalpanama")

isStrictModePalindrome("race a car") 
// Returns: False ("raceacar" != "racaecar")

isStrictModePalindrome("-121") 
// Returns: False (Negative numbers are strictly not palindromes)</pre>
  `,
    starterCode: `def isStrictModePalindrome(text):
    """
    Checks if the input text is a palindrome according to strict rules.
    """
    # TODO: Implement your logic here
    pass`,
    testCases: [
        { id: 1, label: "Case 1", input: 'text = "aba"', expected: "True", hidden: false },
        { id: 2, label: "Case 2", input: 'text = "RaceCar"', expected: "True", hidden: false },
        { id: 3, label: "Case 3", input: 'text = "hello"', expected: "False", hidden: false },
        { id: 4, label: "Case 4", input: 'text = "-121"', expected: "False", hidden: true } // The trap
    ]
};

const StudentWorkspace = () => {
    const { id } = useParams();
    const navigate = useNavigate();

    const [code, setCode] = useState(PROBLEM_DATA.starterCode);
    const [activeTab, setActiveTab] = useState("description");
    const [selectedTestCase, setSelectedTestCase] = useState(0);
    const [output, setOutput] = useState(null); // null, 'running', or result object
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [showConfetti, setShowConfetti] = useState(false);

    const [isConsoleOpen, setIsConsoleOpen] = useState(true);

    // Simulate Code Execution
    const handleRunCode = () => {
        setIsConsoleOpen(true); // Ensure console is visible
        setOutput('running');
        setTimeout(() => {
            // Mocking a result where they fail the Negative Number case
            setOutput({
                status: 'error',
                message: 'Runtime Error',
                results: [
                    { id: 1, status: 'pass', output: 'True' },
                    { id: 2, status: 'pass', output: 'True' },
                    { id: 3, status: 'pass', output: 'False' },
                    { id: 4, status: 'fail', output: 'True', expected: 'False', error: 'AssertionError: Expected False' },
                ]
            });
        }, 800);
    };

    const handleSubmit = () => {
        setIsSubmitting(true);
        setTimeout(() => {
            setIsSubmitting(false);
            setOutput({
                status: 'success',
                message: 'All Test Cases Passed!',
                results: [
                    { id: 1, status: 'pass' },
                    { id: 2, status: 'pass', output: 'True' },
                    { id: 3, status: 'pass', output: 'False' },
                    { id: 4, status: 'pass', output: 'False' },
                ]
            });
            setShowConfetti(true);
        }, 1500);
    };

    return (
        <div className="flex flex-col h-screen bg-gray-50 text-gray-900 font-sans overflow-hidden">

            {/* 1. COMPACT NAVBAR */}
            <header className="h-12 bg-white border-b border-gray-200 flex items-center justify-between px-4 z-20 shadow-sm flex-shrink-0">
                <div className="flex items-center gap-4">
                    <div className="flex items-center gap-2 cursor-pointer hover:bg-gray-50 py-1 pr-2 rounded transition-colors" onClick={() => navigate('/student/dashboard')}>
                        <div className="bg-gray-100 p-1 rounded">
                            <ChevronLeft className="w-4 h-4 text-gray-600" />
                        </div>
                        <span className="font-semibold text-sm text-gray-700">All Problems</span>
                    </div>
                    <div className="h-4 w-px bg-gray-200" />
                    <h1 className="font-bold text-sm text-gray-900 flex items-center gap-2">
                        {PROBLEM_DATA.title}
                        <span className="text-[10px] font-medium text-amber-600 bg-amber-50 border border-amber-100 px-1.5 py-0.5 rounded uppercase tracking-wider">{PROBLEM_DATA.difficulty}</span>
                    </h1>
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
                        disabled={isSubmitting || output === 'running'}
                        className="h-8 px-4 bg-gray-100 hover:bg-gray-200 text-gray-700 border-0 font-medium text-xs gap-2"
                    >
                        <Play className="w-3.5 h-3.5 fill-current" /> Run
                    </Button>
                    <Button
                        size="sm"
                        onClick={handleSubmit}
                        disabled={isSubmitting}
                        className="h-8 px-5 bg-green-600 hover:bg-green-700 text-white font-medium text-xs gap-2 shadow-sm"
                    >
                        {isSubmitting ? <div className="w-3.5 h-3.5 rounded-full border-2 border-white border-t-transparent animate-spin" /> : <Send className="w-3.5 h-3.5" />}
                        Submit
                    </Button>
                </div>
            </header>

            {/* 2. MAIN WORKSPACE (Resizable Split View) */}
            <div className="flex-1 flex overflow-hidden relative">
                <Group direction="horizontal">

                    {/* LEFT PANEL: Problem Description */}
                    <Panel defaultSize={40} minSize={20} className="bg-white flex flex-col">
                        <Tabs value={activeTab} onValueChange={setActiveTab} className="flex-1 flex flex-col h-full">
                            <div className="bg-gray-50 border-b border-gray-200 px-1 flex-shrink-0">
                                <TabsList className="bg-transparent h-9 p-0 w-full justify-start gap-1">
                                    <TabsTrigger value="description" className="data-[state=active]:bg-white data-[state=active]:shadow-sm data-[state=active]:text-indigo-600 text-xs font-medium px-4 h-7 rounded-t-md border-t border-x border-transparent data-[state=active]:border-gray-200 mb-[-1px]">
                                        <FileText className="w-3.5 h-3.5 mr-1.5" /> Description
                                    </TabsTrigger>
                                    <TabsTrigger value="hints" className="data-[state=active]:bg-white data-[state=active]:shadow-sm data-[state=active]:text-indigo-600 text-xs font-medium px-4 h-7 rounded-t-md border-t border-x border-transparent data-[state=active]:border-gray-200 mb-[-1px]">
                                        <Lightbulb className="w-3.5 h-3.5 mr-1.5" /> Hints
                                    </TabsTrigger>
                                </TabsList>
                            </div>

                            <div className="flex-1 overflow-y-auto p-5 scrollbar-thin scrollbar-thumb-gray-200 hover:scrollbar-thumb-gray-300">
                                <TabsContent value="description" className="mt-0 animate-in fade-in duration-300">
                                    <div className="prose prose-sm max-w-none prose-headings:text-gray-900 prose-p:text-gray-600 prose-code:text-indigo-600 prose-code:bg-indigo-50 prose-code:px-1 prose-code:rounded prose-pre:bg-gray-900 prose-pre:text-gray-50">
                                        <div dangerouslySetInnerHTML={{ __html: PROBLEM_DATA.description }} />
                                    </div>
                                </TabsContent>
                                <TabsContent value="hints" className="mt-0 space-y-3">
                                    <div className="p-3 bg-blue-50 border border-blue-100 rounded text-blue-800 text-sm">
                                        <strong>Hint 1:</strong> Negative signs are characters. <code>-121</code> reversed is <code>121-</code>.
                                    </div>
                                    <div className="p-3 bg-purple-50 border border-purple-100 rounded text-purple-800 text-sm">
                                        <strong>Hint 2:</strong> Python slicing <code>[::-1]</code> reverses strings efficiently.
                                    </div>
                                </TabsContent>
                            </div>
                        </Tabs>
                    </Panel>

                    <Separator className="w-1.5 bg-gray-100 hover:bg-indigo-400 transition-colors flex items-center justify-center group z-10">
                        <GripVertical className="h-4 w-4 text-gray-300 group-hover:text-white" />
                    </Separator>

                    {/* RIGHT PANEL: Editor & Output */}
                    <Panel minSize={30} className="flex flex-col min-w-0 bg-white md:w-[60%] relative">
                        <Group direction="vertical">

                            {/* Editor Area */}
                            <Panel defaultSize={60} minSize={20} className="flex flex-col relative bg-[#2d2d2d]">
                                <div className="bg-[#2d2d2d] border-b border-[#111] px-4 h-9 flex justify-between items-center text-xs text-gray-400 select-none flex-shrink-0">
                                    <div className="flex items-center gap-2">
                                        <span className="text-blue-400 font-medium">Python 3</span>
                                        <ChevronDown className="w-3 h-3" />
                                    </div>
                                    <div className="flex items-center gap-3">
                                        <span
                                            className="hover:text-white cursor-pointer transition-colors flex items-center gap-1"
                                            onClick={() => setCode(PROBLEM_DATA.starterCode)}
                                        >
                                            <RotateCcw className="w-3 h-3" /> Reset
                                        </span>
                                    </div>
                                </div>

                                <div className="flex-1 relative overflow-hidden bg-[#2d2d2d]">
                                    <div className="h-full w-full overflow-auto custom-scrollbar">
                                        <Editor
                                            value={code}
                                            onValueChange={code => setCode(code)}
                                            highlight={code => highlight(code, languages.python)}
                                            padding={20}
                                            style={{
                                                fontFamily: '"Fira Code", "Fira Mono", monospace',
                                                fontSize: 14,
                                                backgroundColor: '#2d2d2d', // Match Tomorrow Night background
                                                color: '#f8f8f2',
                                                minHeight: '100%'
                                            }}
                                            className="min-h-full"
                                        />
                                    </div>
                                </div>
                            </Panel>

                            <Separator className="h-1.5 bg-gray-800 hover:bg-indigo-500 transition-colors flex items-center justify-center group z-10 border-t border-b border-gray-900/50">
                                <div className="w-8 h-1 rounded-full bg-gray-600 group-hover:bg-white/50" />
                            </Separator>

                            {/* Console Area */}
                            <Panel defaultSize={40} minSize={10} className="bg-white flex flex-col">
                                <div className="h-9 min-h-[36px] bg-gray-50 border-b border-gray-200 flex items-center justify-between px-4 select-none flex-shrink-0">
                                    <div className="flex items-center gap-2">
                                        <div className="flex items-center gap-2 text-gray-500 font-medium text-xs">
                                            <Terminal className="w-3.5 h-3.5" />
                                            Test Results
                                        </div>
                                        {output === 'running' && <span className="text-xs text-indigo-600 animate-pulse">Running...</span>}
                                        {output && output.status === 'error' && output !== 'running' && <span className="w-1.5 h-1.5 rounded-full bg-red-500" />}
                                        {output && output.status === 'success' && <span className="w-1.5 h-1.5 rounded-full bg-green-500" />}
                                    </div>
                                </div>

                                {/* Console Content */}
                                <div className="flex-1 overflow-hidden flex flex-col relative w-full h-full">
                                    {/* Empty State */}
                                    {!output && (
                                        <div className="absolute inset-0 flex flex-col items-center justify-center text-gray-400 p-4">
                                            <span className="text-sm">Run your code to check test cases.</span>
                                        </div>
                                    )}

                                    {/* Results View */}
                                    {output && output !== 'running' && (
                                        <div className="flex h-full w-full">
                                            {/* Test Case Navigation */}
                                            <div className="w-36 bg-gray-50 border-r border-gray-200 overflow-y-auto py-2 flex-shrink-0">
                                                <div className="px-3 pb-2 text-[10px] font-bold text-gray-400 uppercase tracking-wider">Test Cases</div>
                                                {PROBLEM_DATA.testCases.map((tc, idx) => {
                                                    const result = output.results && output.results[idx];
                                                    const statusColor = !result ? 'gray' : result.status === 'pass' ? 'green' : 'red';
                                                    return (
                                                        <button
                                                            key={tc.id}
                                                            onClick={() => setSelectedTestCase(idx)}
                                                            className={`w-full text-left px-3 py-2 text-xs font-medium flex items-center gap-2 border-l-2 transition-all ${selectedTestCase === idx ? 'bg-white border-indigo-600 text-indigo-700 shadow-sm' : 'border-transparent text-gray-600 hover:bg-gray-100'
                                                                }`}
                                                        >
                                                            <span className={`w-1.5 h-1.5 rounded-full bg-${statusColor}-500 flex-shrink-0`} />
                                                            {tc.label}
                                                        </button>
                                                    )
                                                })}
                                            </div>

                                            {/* Test Case Details */}
                                            <div className="flex-1 p-4 overflow-y-auto min-w-0">
                                                {PROBLEM_DATA.testCases[selectedTestCase] && (
                                                    <div className="space-y-4 animate-in fade-in duration-200">
                                                        <div>
                                                            <h4 className="text-xs font-bold text-gray-500 uppercase mb-1">Input</h4>
                                                            <div className="bg-gray-50 p-3 rounded-md border border-gray-200 font-mono text-xs text-gray-800 break-all">
                                                                {PROBLEM_DATA.testCases[selectedTestCase].input}
                                                            </div>
                                                        </div>

                                                        <div className="grid grid-cols-2 gap-4">
                                                            <div className="min-w-0">
                                                                <h4 className="text-xs font-bold text-gray-500 uppercase mb-1">Expected Output</h4>
                                                                <div className="bg-gray-50 p-3 rounded-md border border-gray-200 font-mono text-xs text-gray-800 break-all">
                                                                    {PROBLEM_DATA.testCases[selectedTestCase].expected}
                                                                </div>
                                                            </div>
                                                            <div className="min-w-0">
                                                                <h4 className="text-xs font-bold text-gray-500 uppercase mb-1">Your Output</h4>
                                                                {output.results && output.results[selectedTestCase] ? (
                                                                    <div className={`p-3 rounded-md border font-mono text-xs break-all ${output.results[selectedTestCase].status === 'pass'
                                                                            ? 'bg-green-50 border-green-200 text-green-800'
                                                                            : 'bg-red-50 border-red-200 text-red-800'
                                                                        }`}>
                                                                        {output.results[selectedTestCase].output}
                                                                    </div>
                                                                ) : (
                                                                    <div className="text-gray-400 italic text-xs">Not run yet</div>
                                                                )}
                                                            </div>
                                                        </div>

                                                        {output.results && output.results[selectedTestCase]?.error && (
                                                            <div className="mt-2 text-red-600 bg-red-50 p-2 rounded text-xs font-mono border border-red-100 overflow-x-auto">
                                                                {output.results[selectedTestCase].error}
                                                            </div>
                                                        )}
                                                    </div>
                                                )}
                                            </div>
                                        </div>
                                    )}
                                </div>
                            </Panel>
                        </Group>
                    </Panel>
                </Group>
            </div>

            {showConfetti && (
                <div className="fixed inset-0 pointer-events-none z-50 flex items-center justify-center bg-black/50 backdrop-blur-[1px]">
                    <motion.div
                        initial={{ scale: 0.5, opacity: 0 }}
                        animate={{ scale: 1, opacity: 1 }}
                        className="bg-white p-8 rounded-2xl shadow-2xl text-center pointer-events-auto"
                    >
                        <div className="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                            <CheckCircle2 className="w-10 h-10 text-green-600" />
                        </div>
                        <h2 className="text-2xl font-bold text-gray-900 mb-2">Excellent Work!</h2>
                        <p className="text-gray-500 mb-6">You've mastered text processing edge cases.</p>
                        <Button onClick={() => navigate('/student/dashboard')} className="w-full bg-gray-900 text-white hover:bg-gray-800">
                            Back to Dashboard
                        </Button>
                    </motion.div>
                </div>
            )}
        </div>
    );
};

export default StudentWorkspace;
