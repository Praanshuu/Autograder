import { useState, useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import {
    MoveLeft,
    CheckCircle2,
    XCircle,
    Play,
    Save,
    ChevronRight,
    ChevronLeft,
    TerminalSquare,
    History,
    Loader2
} from "lucide-react";
import { motion } from "framer-motion";

import TeacherLayout from "../../components/layout/TeacherLayout";
import { Button } from "../../components/ui/button";
import { Input } from "../../components/ui/input";
import { Label } from "../../components/ui/label";
import { Textarea } from "../../components/ui/textarea";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../../components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../../components/ui/tabs";
import { submissionService } from "../../services/submissionService";
import LearningTrajectory from "../../components/features/analytics/LearningTrajectory";

export default function GradingInterface() {
    const { id } = useParams();
    const [submission, setSubmission] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const [manualScore, setManualScore] = useState(0);
    const [feedback, setFeedback] = useState("");

    useEffect(() => {
        const fetchSubmission = async () => {
            try {
                setLoading(true);
                const response = await submissionService.getSubmission(id);
                const data = response.data;
                setSubmission(data);
                setManualScore(data.manual_score !== null ? data.manual_score : (data.final_score || 0));
                setFeedback(data.feedback_text || "");
            } catch (err) {
                console.error("Failed to load submission:", err);
                setError("Failed to load submission.");
            } finally {
                setLoading(false);
            }
        };
        fetchSubmission();
    }, [id]);

    const handleRunTests = () => {
        // Mock running tests
        alert("Running Autograder... (Mock)");
    };

    const handleSave = async () => {
        try {
            console.log("Saving Grade:", { id, manualScore, feedback });
            await submissionService.gradeSubmission(id, {
                manual_score: manualScore,
                feedback_text: feedback
            });
            alert("Grade saved successfully!");
        } catch (err) {
            console.error("Failed to save grade:", err);
            alert("Failed to save grade.");
        }
    };

    if (loading) {
        return <div className="flex h-screen items-center justify-center"><Loader2 className="animate-spin text-indigo-600" /></div>;
    }

    if (error || !submission) {
        return <div className="p-8 text-center text-red-500">{error || "Submission not found"}</div>;
    }

    return (
        <div className="h-screen flex flex-col bg-gray-50">
            {/* Top Bar - Simplified for Focus */}
            <header className="h-16 bg-white border-b px-4 flex items-center justify-between shrink-0 z-10">
                <div className="flex items-center gap-4">
                    <Button variant="ghost" size="icon" asChild>
                        <Link to={`/teacher/assignment/${submission.assignment_id}`}> {/* Back to Assignment */}
                            <MoveLeft className="w-5 h-5" />
                        </Link>
                    </Button>
                    <div>
                        <h1 className="text-lg font-bold text-gray-900">{submission.student?.username || "Student"}</h1>
                        <p className="text-xs text-gray-500">Submission Time: {new Date(submission.created_at).toLocaleString()}</p>
                    </div>
                </div>
                <div className="flex items-center gap-2">
                    <Button variant="outline" className="gap-2" onClick={handleRunTests}>
                        <Play className="w-4 h-4 text-green-600" />
                        Rerun Tests
                    </Button>
                    <Button onClick={handleSave} className="gap-2">
                        <Save className="w-4 h-4" />
                        Save Grade
                    </Button>
                </div>
            </header>

            {/* Main Content - Split Pane */}
            <div className="flex-1 flex overflow-hidden">
                {/* Left Pane: Code Viewer */}
                <div className="flex-1 bg-gray-900 text-gray-100 overflow-auto p-4 font-mono text-sm relative">
                    <div className="absolute top-4 right-4 text-xs bg-gray-800 px-2 py-1 rounded text-gray-400">
                        main.py
                    </div>
                    <pre className="counter-reset: line">
                        <code>
                            {/* Fetch actual code content if not in submission object, might need to fetch blob */}
                            {/* Assuming for now we rely on what we have, or mock it if missing */}
                            {"# Code viewer placeholder - need to fetch code blob"}
                        </code>
                    </pre>
                </div>

                {/* Right Pane: Grading Tools */}
                <div className="w-[400px] border-l bg-white flex flex-col shadow-xl z-20">
                    <Tabs defaultValue="autograder" className="flex-1 flex flex-col">
                        <div className="border-b px-4">
                            <TabsList className="w-full justify-start h-12 bg-transparent p-0 gap-4">
                                <TabsTrigger value="autograder" className="data-[state=active]:bg-transparent data-[state=active]:border-b-2 data-[state=active]:border-indigo-600 rounded-none h-12 px-0">
                                    Autograder
                                </TabsTrigger>
                                <TabsTrigger value="manual" className="data-[state=active]:bg-transparent data-[state=active]:border-b-2 data-[state=active]:border-indigo-600 rounded-none h-12 px-0">
                                    Rubric
                                </TabsTrigger>
                                <TabsTrigger value="history" className="data-[state=active]:bg-transparent data-[state=active]:border-b-2 data-[state=active]:border-indigo-600 rounded-none h-12 px-0 flex items-center gap-2">
                                    <History className="w-3.5 h-3.5" />
                                    History
                                </TabsTrigger>
                            </TabsList>
                        </div>

                        <div className="flex-1 overflow-auto p-4">
                            <TabsContent value="autograder" className="mt-0 space-y-4">
                                <Card>
                                    <CardHeader className="pb-3">
                                        <CardTitle className="text-sm font-medium flex justify-between">
                                            <span>Test Suite Results</span>
                                            <span className="text-green-600 font-bold">{submission.autoGradeScore}% Passed</span>
                                        </CardTitle>
                                    </CardHeader>
                                    <CardContent className="space-y-3">
                                        {/* Mock Test Cases */}
                                        <div className="flex items-start gap-3 p-3 bg-green-50 rounded-lg border border-green-100">
                                            <CheckCircle2 className="w-5 h-5 text-green-600 shrink-0 mt-0.5" />
                                            <div>
                                                <p className="text-sm font-medium text-green-900">Test Case 1: Basic Input</p>
                                                <p className="text-xs text-green-700 mt-1">Input: `1, 2` &rarr; Output: `3`</p>
                                            </div>
                                        </div>
                                        <div className="flex items-start gap-3 p-3 bg-green-50 rounded-lg border border-green-100">
                                            <CheckCircle2 className="w-5 h-5 text-green-600 shrink-0 mt-0.5" />
                                            <div>
                                                <p className="text-sm font-medium text-green-900">Test Case 2: Zeroes</p>
                                                <p className="text-xs text-green-700 mt-1">Input: `0, 0` &rarr; Output: `0`</p>
                                            </div>
                                        </div>
                                        {submission.autoGradeScore < 100 && (
                                            <div className="flex items-start gap-3 p-3 bg-red-50 rounded-lg border border-red-100">
                                                <XCircle className="w-5 h-5 text-red-600 shrink-0 mt-0.5" />
                                                <div>
                                                    <p className="text-sm font-medium text-red-900">Test Case 3: Large Numbers</p>
                                                    <p className="text-xs text-red-700 mt-1">Expected: `1000` &rarr; Got: `Error`</p>
                                                </div>
                                            </div>
                                        )}
                                    </CardContent>
                                </Card>

                                <Card>
                                    <CardHeader className="pb-3">
                                        <CardTitle className="text-sm font-medium flex items-center gap-2">
                                            <TerminalSquare className="w-4 h-4" />
                                            Execution Output
                                        </CardTitle>
                                    </CardHeader>
                                    <CardContent>
                                        <div className="bg-black text-green-400 font-mono text-xs p-3 rounded-lg overflow-x-auto">
                                            <span>&gt; Running tests...</span><br />
                                            <span>&gt; Test 1 passed (2ms)</span><br />
                                            <span>&gt; Test 2 passed (1ms)</span><br />
                                            {submission.autoGradeScore < 100 && <span>&gt; Test 3 FAILED (Timeout)<br /></span>}
                                            <span>&gt; Done.</span>
                                        </div>
                                    </CardContent>
                                </Card>
                            </TabsContent>

                            <TabsContent value="manual" className="mt-0 space-y-6">
                                <div className="space-y-4">
                                    <div className="space-y-2">
                                        <Label>Final Score Override</Label>
                                        <div className="flex items-center gap-4">
                                            <Input
                                                type="number"
                                                value={manualScore}
                                                onChange={(e) => setManualScore(e.target.value)}
                                                className="text-lg font-bold w-24"
                                            />
                                            <span className="text-gray-500 font-medium">/ 100</span>
                                        </div>
                                        <p className="text-xs text-gray-500">
                                            Autograder gave {submission.autoGradeScore}%. You can override this based on code review.
                                        </p>
                                    </div>

                                    <div className="space-y-2">
                                        <Label>Teacher Feedback</Label>
                                        <Textarea
                                            placeholder="Leave a comment for the student..."
                                            className="h-40"
                                            value={feedback}
                                            onChange={(e) => setFeedback(e.target.value)}
                                        />
                                    </div>
                                </div>
                            </TabsContent>

                            <TabsContent value="history" className="mt-0 space-y-4">
                                {submission.history ? (
                                    <LearningTrajectory
                                        data={submission.history}
                                        studentName={submission.studentName}
                                    />
                                ) : (
                                    <div className="p-8 text-center text-gray-500 bg-gray-50 rounded-lg border border-dashed">
                                        <History className="w-8 h-8 mx-auto mb-2 opacity-20" />
                                        <p>No history data available for this student.</p>
                                    </div>
                                )}

                                <Card>
                                    <CardHeader className="pb-3">
                                        <CardTitle className="text-sm font-medium">Teacher Notes</CardTitle>
                                    </CardHeader>
                                    <CardContent>
                                        <p className="text-sm text-gray-600 hidden">
                                            Private notes about this student's progress...
                                        </p>
                                        <Textarea
                                            placeholder="Private notes (only visible to teachers)..."
                                            className="min-h-[100px] text-sm"
                                        />
                                    </CardContent>
                                </Card>
                            </TabsContent>
                        </div>
                    </Tabs>
                </div>
            </div>
        </div>
    );
}
