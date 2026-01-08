import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { MoveLeft, Plus, Save, Trash2, GripVertical, Pencil } from "lucide-react";
import { motion, Reorder } from "framer-motion";

import TeacherLayout from "../../components/layout/TeacherLayout";
import { Button } from "../../components/ui/button";
import { Input } from "../../components/ui/input";
import { Label } from "../../components/ui/label";
import { Textarea } from "../../components/ui/textarea";
import { Card, CardContent, CardHeader, CardTitle } from "../../components/ui/card";
import QuestionEditorDialog from "../../components/features/teacher/QuestionEditorDialog";

export default function CreateAssignment() {
    const navigate = useNavigate();
    const [title, setTitle] = useState("");
    const [instructions, setInstructions] = useState("");

    // Question Management State
    const [questions, setQuestions] = useState([
        { id: "q1", title: "Two Sum", difficulty: "Easy", description: "Find two numbers that add up to target.", testCases: [] },
        { id: "q2", title: "Valid Palindrome", difficulty: "Medium", description: "Check if string is palindrome.", testCases: [] }
    ]);
    const [isQuestionDialogOpen, setIsQuestionDialogOpen] = useState(false);
    const [editingQuestion, setEditingQuestion] = useState(null);

    const handleSave = () => {
        // Mock save action
        console.log("Saving assignment:", { title, instructions, questions });
        navigate("/teacher/dashboard");
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
            setQuestions([...questions, questionData]);
        }
    };

    const handleDeleteQuestion = (id) => {
        setQuestions(questions.filter(q => q.id !== id));
    };

    return (
        <TeacherLayout>
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="max-w-4xl mx-auto"
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
                        <Button variant="outline">Save Draft</Button>
                        <Button onClick={handleSave} className="gap-2">
                            <Save className="w-4 h-4" />
                            Publish
                        </Button>
                    </div>
                </div>

                <div className="space-y-8">
                    {/* Basic Info */}
                    <Card>
                        <CardHeader>
                            <CardTitle>Assignment Details</CardTitle>
                        </CardHeader>
                        <CardContent className="space-y-4">
                            <div className="space-y-2">
                                <Label htmlFor="title">Assignment Title</Label>
                                <Input
                                    id="title"
                                    placeholder="e.g. Dynamic Programming Basics"
                                    value={title}
                                    onChange={(e) => setTitle(e.target.value)}
                                />
                            </div>
                            <div className="space-y-2">
                                <Label htmlFor="instructions">Instructions</Label>
                                <Textarea
                                    id="instructions"
                                    placeholder="Enter detailed instructions (Markdown supported)..."
                                    className="min-h-[150px]"
                                    value={instructions}
                                    onChange={(e) => setInstructions(e.target.value)}
                                />
                            </div>
                        </CardContent>
                    </Card>

                    {/* Questions Section */}
                    <div className="space-y-4">
                        <div className="flex items-center justify-between">
                            <h2 className="text-lg font-semibold text-gray-900">Coding Problems</h2>
                            <Button variant="secondary" size="sm" className="gap-2" onClick={handleAddQuestion}>
                                <Plus className="w-4 h-4" />
                                Add Question
                            </Button>
                        </div>

                        {questions.length === 0 ? (
                            <div className="text-center py-12 bg-gray-50 rounded-lg border border-dashed border-gray-300">
                                <p className="text-gray-500">No questions added yet.</p>
                                <Button variant="link" onClick={handleAddQuestion}>Add your first question</Button>
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
