import { useState, useEffect } from "react";
import { Plus, X, Trash2, ChevronDown } from "lucide-react";
import { Button } from "../../ui/button";
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
} from "../../ui/dialog";
import { Input } from "../../ui/input";
import { Label } from "../../ui/label";
import { Textarea } from "../../ui/textarea";
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from "../../ui/dropdown-menu";

export default function QuestionEditorDialog({ open, onOpenChange, questionToEdit, onSave }) {
    const [title, setTitle] = useState("");
    const [difficulty, setDifficulty] = useState("Easy");
    const [description, setDescription] = useState("");
    const [testCases, setTestCases] = useState([{ input: "", output: "" }]);

    useEffect(() => {
        if (questionToEdit) {
            setTitle(questionToEdit.title || "");
            setDifficulty(questionToEdit.difficulty || "Easy");
            setDescription(questionToEdit.description || "");
            setTestCases(questionToEdit.testCases || [{ input: "", output: "" }]);
        } else {
            // Reset for new question
            setTitle("");
            setDifficulty("Easy");
            setDescription("");
            setTestCases([{ input: "", output: "" }]);
        }
    }, [questionToEdit, open]);

    const handleSave = () => {
        onSave({
            id: questionToEdit ? questionToEdit.id : Date.now().toString(),
            title,
            difficulty,
            description,
            testCases
        });
        onOpenChange(false);
    };

    const addTestCase = () => {
        setTestCases([...testCases, { input: "", output: "" }]);
    };

    const removeTestCase = (index) => {
        setTestCases(testCases.filter((_, i) => i !== index));
    };

    const updateTestCase = (index, field, value) => {
        const newTestCases = [...testCases];
        newTestCases[index][field] = value;
        setTestCases(newTestCases);
    };

    return (
        <Dialog open={open} onOpenChange={onOpenChange}>
            <DialogContent className="sm:max-w-[700px] max-h-[90vh] overflow-y-auto">
                <DialogHeader>
                    <DialogTitle>{questionToEdit ? "Edit Question" : "Add New Question"}</DialogTitle>
                    <DialogDescription>
                        Define the problem details and test cases.
                    </DialogDescription>
                </DialogHeader>
                <div className="grid gap-6 py-4">
                    <div className="grid gap-2">
                        <Label htmlFor="q-title">Question Title</Label>
                        <Input
                            id="q-title"
                            placeholder="e.g. Reverse Linked List"
                            value={title}
                            onChange={(e) => setTitle(e.target.value)}
                        />
                    </div>

                    <div className="grid gap-2">
                        <Label>Difficulty</Label>
                        <DropdownMenu>
                            <DropdownMenuTrigger asChild>
                                <Button variant="outline" className="w-[150px] justify-between">
                                    {difficulty}
                                    <ChevronDown className="ml-2 h-4 w-4 opacity-50" />
                                </Button>
                            </DropdownMenuTrigger>
                            <DropdownMenuContent>
                                <DropdownMenuItem onClick={() => setDifficulty("Easy")}>Easy</DropdownMenuItem>
                                <DropdownMenuItem onClick={() => setDifficulty("Medium")}>Medium</DropdownMenuItem>
                                <DropdownMenuItem onClick={() => setDifficulty("Hard")}>Hard</DropdownMenuItem>
                            </DropdownMenuContent>
                        </DropdownMenu>
                    </div>

                    <div className="grid gap-2">
                        <Label htmlFor="q-desc">Problem Description (Markdown)</Label>
                        <Textarea
                            id="q-desc"
                            placeholder="Describe the problem..."
                            className="min-h-[150px] font-mono text-sm"
                            value={description}
                            onChange={(e) => setDescription(e.target.value)}
                        />
                    </div>

                    <div className="space-y-4">
                        <div className="flex items-center justify-between">
                            <Label>Test Cases</Label>
                            <Button type="button" variant="outline" size="sm" onClick={addTestCase}>
                                <Plus className="w-3 h-3 mr-1" /> Add Case
                            </Button>
                        </div>

                        {testCases.map((tc, i) => (
                            <div key={i} className="flex gap-2 items-start">
                                <div className="grid gap-1 flex-1">
                                    <Label className="text-xs text-gray-500">Input</Label>
                                    <Textarea
                                        value={tc.input}
                                        onChange={(e) => updateTestCase(i, 'input', e.target.value)}
                                        className="h-20 font-mono text-xs"
                                        placeholder="Input data"
                                    />
                                </div>
                                <div className="grid gap-1 flex-1">
                                    <Label className="text-xs text-gray-500">Output</Label>
                                    <Textarea
                                        value={tc.output}
                                        onChange={(e) => updateTestCase(i, 'output', e.target.value)}
                                        className="h-20 font-mono text-xs"
                                        placeholder="Expected output"
                                    />
                                </div>
                                <Button
                                    variant="ghost"
                                    size="icon"
                                    className="mt-6 text-red-500 hover:text-red-700"
                                    onClick={() => removeTestCase(i)}
                                >
                                    <Trash2 className="w-4 h-4" />
                                </Button>
                            </div>
                        ))}
                    </div>
                </div>
                <DialogFooter>
                    <Button variant="outline" onClick={() => onOpenChange(false)}>Cancel</Button>
                    <Button onClick={handleSave}>Save Question</Button>
                </DialogFooter>
            </DialogContent>
        </Dialog>
    );
}
