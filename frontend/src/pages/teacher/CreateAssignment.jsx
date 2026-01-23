import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { MoveLeft, Plus, Save, Trash2, GripVertical, Pencil, Loader2, AlertCircle } from "lucide-react";
import { motion, Reorder } from "framer-motion";

import TeacherLayout from "../../components/layout/TeacherLayout";
import { Button } from "../../components/ui/button";
import { Input } from "../../components/ui/input";
import { Label } from "../../components/ui/label";
import { Textarea } from "../../components/ui/textarea";
import { Card, CardContent, CardHeader, CardTitle } from "../../components/ui/card";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "../../components/ui/select";
import QuestionEditorDialog from "../../components/features/teacher/QuestionEditorDialog";

import { assignmentService } from "../../services/assignmentService";
import { classService } from "../../services/classService";

export default function CreateAssignment() {
    const navigate = useNavigate();

    // Form State
    const [title, setTitle] = useState("");
    const [instructions, setInstructions] = useState("");
    const [selectedClassId, setSelectedClassId] = useState("");
    const [difficulty, setDifficulty] = useState("Medium");
    const [points, setPoints] = useState(100);
    const [dueDate, setDueDate] = useState("");

    // Data State
    const [classes, setClasses] = useState([]);
    const [questions, setQuestions] = useState([]);

    // UI State
    const [loading, setLoading] = useState(false);
    const [initialLoading, setInitialLoading] = useState(true);
    const [error, setError] = useState(null);
    const [isQuestionDialogOpen, setIsQuestionDialogOpen] = useState(false);
    const [editingQuestion, setEditingQuestion] = useState(null);

    // Load Classes on Mount
    useEffect(() => {
        const loadClasses = async () => {
            try {
                const response = await classService.getClasses();
                const data = Array.isArray(response.data) ? response.data : (response.data.results || []);
                setClasses(data);
                if (data.length > 0) {
                    setSelectedClassId(data[0].id.toString());
                }
            } catch (err) {
                console.error("Failed to load classes", err);
                setError("Could not load classes. Please ensure you have created a class first.");
            } finally {
                setInitialLoading(false);
            }
        };
        loadClasses();
    }, []);

    const handleSave = async () => {
        if (!selectedClassId || !title) {
            setError("Please select a class and enter a title.");
            return;
        }

        setLoading(true);
        setError(null);

        try {
            // 1. Create Questions
            const createdQuestionIds = [];

            for (const q of questions) {
                // Prepare Test Cases for this question (embedded)
                const testCases = (q.testCases || []).filter(tc => tc.input || tc.output).map(tc => ({
                    input: tc.input || "",
                    expected_output: tc.output || "",
                    is_hidden: false,
                    points: 10
                }));

                // Create Question with embedded test cases
                const qResponse = await assignmentService.createQuestion({
                    title: q.title,
                    description: q.description,
                    difficulty: q.difficulty,
                    test_cases: testCases, // Send JSON list directly
                    time_limit: 1.0,
                    memory_limit: 128,
                    allowed_languages: ["python"],
                    starter_code: q.starterCode || "", // If your UI supports it, else empty
                    // order: questions.indexOf(q) // Model doesn't have order on Question, it's on AssignmentQuestion
                });

                if (qResponse?.data?.id) {
                    createdQuestionIds.push(qResponse.data.id);
                } else {
                    throw new Error("Failed to create question: No ID returned.");
                }
            }

            // 2. Create Assignment with Class ID and Question IDs
            const payload = {
                class_obj_id: selectedClassId, // Backend expects 'class_obj_id'
                title: title,
                description: instructions,
                question_ids: createdQuestionIds,
                points: points, // Make sure points matches model type (int)
                due_date: dueDate ? new Date(dueDate).toISOString() : null,
                is_published: true // Correct field for visibility
            };

            await assignmentService.createAssignment(payload);

            // Redirect to the class page (Classwork tab usually default or accessible)
            navigate(`/teacher/class/${selectedClassId}`);
        } catch (err) {
            console.error("Failed to save assignment:", err);
            // Enhanced error logging
            const msg = err.response?.data
                ? JSON.stringify(err.response.data)
                : err.message;
            setError("Failed to create assignment. " + msg);
        } finally {
            setLoading(false);
        }
    };

    const handleAddQuestion = () => {
        setEditingQuestion(null);
        setIsQuestionDialogOpen(true);
    };

    const handleEditQuestion = (question) => {
        setEditingQuestion(question);
        setIsQuestionDialogOpen(true);
    };

    const handleSaveQuestion = (questionData) => {
        if (editingQuestion) {
            setQuestions(questions.map(q => q.id === questionData.id ? questionData : q));
        } else {
            // Generate a temp ID for frontend management if not present
            const newQuestion = { ...questionData, id: questionData.id || `temp-${Date.now()}` };
            setQuestions([...questions, newQuestion]);
        }
    };

    const handleDeleteQuestion = (id) => {
        setQuestions(questions.filter(q => q.id !== id));
    };

    if (initialLoading) {
        return (
            <TeacherLayout>
                <div className="flex items-center justify-center h-screen">
                    <Loader2 className="w-8 h-8 animate-spin text-indigo-600" />
                </div>
            </TeacherLayout>
        );
    }

    return (
        <TeacherLayout>
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="max-w-4xl mx-auto pb-20"
            >
                {/* Header */}
                <div className="flex items-center justify-between mb-8">
                    <div className="flex items-center gap-4">
                        <Button variant="ghost" size="icon" asChild>
                            <Link to="/teacher/dashboard">
                                <MoveLeft className="w-5 h-5" />
                            </Link>
                        </Button>
                        <div>
                            <h1 className="text-2xl font-bold text-gray-900">Create Assignment</h1>
                            <p className="text-gray-500 text-sm">Draft a new coding assignment for your class</p>
                        </div>
                    </div>
                    <div className="flex gap-2">
                        <Button onClick={handleSave} disabled={loading} className="gap-2 min-w-[120px]">
                            {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : <Save className="w-4 h-4" />}
                            Publish Assignment
                        </Button>
                    </div>
                </div>

                {error && (
                    <div className="bg-red-50 text-red-600 p-4 rounded-lg mb-6 flex items-center gap-3 border border-red-200">
                        <AlertCircle className="w-5 h-5" />
                        {error}
                    </div>
                )}

                <div className="space-y-8">
                    {/* Basic Info */}
                    <Card>
                        <CardHeader>
                            <CardTitle>Assignment Details</CardTitle>
                        </CardHeader>
                        <CardContent className="space-y-6">
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                                <div className="space-y-2">
                                    <Label>Select Class</Label>
                                    <Select value={selectedClassId} onValueChange={setSelectedClassId}>
                                        <SelectTrigger>
                                            <SelectValue placeholder="Select a class" />
                                        </SelectTrigger>
                                        <SelectContent>
                                            {classes.map(c => (
                                                <SelectItem key={c.id} value={c.id.toString()}>{c.name} ({c.section})</SelectItem>
                                            ))}
                                        </SelectContent>
                                    </Select>
                                </div>
                                <div className="space-y-2">
                                    <Label htmlFor="title">Assignment Title</Label>
                                    <Input
                                        id="title"
                                        placeholder="e.g. Dynamic Programming Basics"
                                        value={title}
                                        onChange={(e) => setTitle(e.target.value)}
                                    />
                                </div>
                            </div>

                            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                                <div className="space-y-2">
                                    <Label>Difficulty</Label>
                                    <Select value={difficulty} onValueChange={setDifficulty}>
                                        <SelectTrigger>
                                            <SelectValue />
                                        </SelectTrigger>
                                        <SelectContent>
                                            <SelectItem value="Easy">Easy</SelectItem>
                                            <SelectItem value="Medium">Medium</SelectItem>
                                            <SelectItem value="Hard">Hard</SelectItem>
                                        </SelectContent>
                                    </Select>
                                </div>
                                <div className="space-y-2">
                                    <Label>Total Points</Label>
                                    <Input
                                        type="number"
                                        value={points}
                                        onChange={(e) => setPoints(e.target.value)}
                                    />
                                </div>
                                <div className="space-y-2">
                                    <Label>Due Date</Label>
                                    <Input
                                        type="datetime-local"
                                        value={dueDate}
                                        onChange={(e) => setDueDate(e.target.value)}
                                    />
                                </div>
                            </div>

                            <div className="space-y-2">
                                <Label htmlFor="instructions">Instructions</Label>
                                <Textarea
                                    id="instructions"
                                    placeholder="Enter detailed instructions (Markdown supported)..."
                                    className="min-h-[150px] font-mono text-sm"
                                    value={instructions}
                                    onChange={(e) => setInstructions(e.target.value)}
                                />
                            </div>
                        </CardContent>
                    </Card>

                    {/* Questions Section */}
                    <div className="space-y-4">
                        <div className="flex items-center justify-between">
                            <div>
                                <h2 className="text-lg font-semibold text-gray-900">Coding Problems</h2>
                                <p className="text-sm text-gray-500">Add at least one problem to this assignment.</p>
                            </div>
                            <Button variant="secondary" size="sm" className="gap-2" onClick={handleAddQuestion}>
                                <Plus className="w-4 h-4" />
                                Add Question
                            </Button>
                        </div>

                        {questions.length === 0 ? (
                            <div className="text-center py-12 bg-gray-50 rounded-lg border-2 border-dashed border-gray-300 hover:border-indigo-300 transition-colors">
                                <p className="text-gray-500 mb-2">No questions added yet.</p>
                                <Button variant="link" onClick={handleAddQuestion} className="text-indigo-600">
                                    Add your first question
                                </Button>
                            </div>
                        ) : (
                            <Reorder.Group axis="y" values={questions} onReorder={setQuestions} className="space-y-3">
                                {questions.map((q) => (
                                    <Reorder.Item key={q.id} value={q}>
                                        <div className="bg-white border rounded-lg p-4 flex items-center gap-4 shadow-sm hover:shadow-md transition-shadow cursor-move group">
                                            <GripVertical className="w-5 h-5 text-gray-400 group-hover:text-gray-600" />
                                            <div className="flex-1">
                                                <h3 className="font-medium text-gray-900">{q.title}</h3>
                                                <div className="flex items-center gap-2 mt-1">
                                                    <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${q.difficulty === "Easy" ? "bg-green-100 text-green-700" :
                                                        q.difficulty === "Medium" ? "bg-yellow-100 text-yellow-700" :
                                                            "bg-red-100 text-red-700"
                                                        }`}>
                                                        {q.difficulty}
                                                    </span>
                                                    <span className="text-xs text-gray-400">• {q.testCases?.length || 0} Test Cases</span>
                                                </div>
                                            </div>
                                            <div className="flex items-center gap-2">
                                                <Button variant="ghost" size="sm" onClick={() => handleEditQuestion(q)}>
                                                    <Pencil className="w-4 h-4 mr-1" /> Edit
                                                </Button>
                                                <Button
                                                    variant="ghost"
                                                    size="icon"
                                                    className="text-gray-400 hover:text-red-600 hover:bg-red-50"
                                                    onClick={() => handleDeleteQuestion(q.id)}
                                                >
                                                    <Trash2 className="w-4 h-4" />
                                                </Button>
                                            </div>
                                        </div>
                                    </Reorder.Item>
                                ))}
                            </Reorder.Group>
                        )}
                    </div>
                </div>
            </motion.div>

            <QuestionEditorDialog
                open={isQuestionDialogOpen}
                onOpenChange={setIsQuestionDialogOpen}
                questionToEdit={editingQuestion}
                onSave={handleSaveQuestion}
            />
        </TeacherLayout>
    );
}
