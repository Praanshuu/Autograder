import { useState, useEffect } from "react";
import { Plus, X, Trash2 } from "lucide-react";
import { Button } from "../../ui/button";
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
    DialogFooter
} from "../../ui/dialog";
import { Input } from "../../ui/input";
import { Label } from "../../ui/label";
import { MarkdownEditor } from "../../ui/markdown-editor";

export default function McqEditorDialog({ open, onOpenChange, questionToEdit, onSave }) {
    const [title, setTitle] = useState("");
    const [difficulty, setDifficulty] = useState("Easy");
    const [description, setDescription] = useState(""); // This serves as the actual MCQ prompt
    const [options, setOptions] = useState(["", "", "", ""]);
    const [correctOptionIndex, setCorrectOptionIndex] = useState(0);

    useEffect(() => {
        if (questionToEdit) {
            setTitle(questionToEdit.title || "");
            setDifficulty(questionToEdit.difficulty || "Easy");
            setDescription(questionToEdit.description || "");

            const configOpts = questionToEdit.config?.options || ["", "", "", ""];
            setOptions(configOpts);

            const testCases = questionToEdit.testCases || [];
            if (testCases.length > 0) {
                const expected = testCases[0]?.expected_output;
                const idx = configOpts.indexOf(expected);
                setCorrectOptionIndex(idx !== -1 ? idx : 0);
            }
        } else {
            // Reset for new item
            setTitle("");
            setDifficulty("Easy");
            setDescription("");
            setOptions(["", "", "", ""]);
            setCorrectOptionIndex(0);
        }
    }, [questionToEdit, open]);

    const handleSave = () => {
        // Validation
        if (!title.trim()) {
            alert("Please provide a title.");
            return;
        }
        if (!description.trim()) {
            alert("Please provide the question prompt.");
            return;
        }
        if (options.some(opt => !opt.trim())) {
            alert("Please fill in all options.");
            return;
        }

        const expected_output = options[correctOptionIndex];

        onSave({
            id: questionToEdit ? questionToEdit.id : Date.now().toString(),
            title,
            difficulty,
            description,
            question_type: "mcq",
            config: {
                options: options,
                correct_option: correctOptionIndex  // store the correct answer index here
            },
            testCases: []  // MCQ grading uses config.correct_option, not test_cases
        });

        onOpenChange(false);
    };

    const updateOption = (index, value) => {
        const newOptions = [...options];
        newOptions[index] = value;
        setOptions(newOptions);
    };

    return (
        <Dialog open={open} onOpenChange={onOpenChange}>
            <DialogContent className="sm:max-w-[700px] max-h-[90vh] overflow-y-auto">
                <DialogHeader>
                    <DialogTitle>{questionToEdit ? "Edit MCQ" : "Add New MCQ"}</DialogTitle>
                    <DialogDescription>
                        Define the prompt and multiple choice options.
                    </DialogDescription>
                </DialogHeader>

                <div className="grid gap-6 py-4">
                    <div className="grid gap-2">
                        <Label htmlFor="q-title">Question Title</Label>
                        <Input
                            id="q-title"
                            placeholder="e.g. Memory Management"
                            value={title}
                            onChange={(e) => setTitle(e.target.value)}
                        />
                    </div>

                    <div className="grid gap-2">
                        <Label>Difficulty</Label>
                        <select
                            className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                            value={difficulty}
                            onChange={(e) => setDifficulty(e.target.value)}
                        >
                            <option value="Easy">Easy</option>
                            <option value="Medium">Medium</option>
                            <option value="Hard">Hard</option>
                        </select>
                    </div>

                    <div className="grid gap-2">
                        <Label>Question Prompt</Label>
                        <MarkdownEditor
                            value={description}
                            onChange={(e) => setDescription(e.target ? e.target.value : e)}
                            placeholder="Write your question here..."
                        />
                    </div>

                    <div className="grid gap-4">
                        <Label>Options</Label>
                        {options.map((option, index) => (
                            <div key={index} className="flex items-center gap-3">
                                <input
                                    type="radio"
                                    name="correctOption"
                                    checked={correctOptionIndex === index}
                                    onChange={() => setCorrectOptionIndex(index)}
                                    className="w-5 h-5 text-indigo-600 focus:ring-indigo-500"
                                    title="Mark as correct answer"
                                />
                                <Input
                                    placeholder={`Option ${index + 1}`}
                                    value={option}
                                    onChange={(e) => updateOption(index, e.target.value)}
                                    className={correctOptionIndex === index ? "border-green-500 ring-1 ring-green-500" : ""}
                                />
                                {options.length > 2 && (
                                    <Button
                                        variant="ghost"
                                        size="icon"
                                        onClick={() => {
                                            const newOps = options.filter((_, i) => i !== index);
                                            setOptions(newOps);
                                            if (correctOptionIndex === index) setCorrectOptionIndex(0);
                                            else if (correctOptionIndex > index) setCorrectOptionIndex(correctOptionIndex - 1);
                                        }}
                                        className="text-red-500 hover:text-red-700"
                                    >
                                        <X className="w-4 h-4" />
                                    </Button>
                                )}
                            </div>
                        ))}
                        <Button
                            variant="outline"
                            size="sm"
                            onClick={() => setOptions([...options, ""])}
                            className="w-fit mt-2"
                        >
                            <Plus className="w-4 h-4 mr-2" />
                            Add Option
                        </Button>
                        <p className="text-xs text-muted-foreground mt-1">Select the radio button next to the correct option.</p>
                    </div>
                </div>

                <DialogFooter>
                    <Button variant="outline" onClick={() => onOpenChange(false)}>Cancel</Button>
                    <Button onClick={handleSave}>Save MCQ</Button>
                </DialogFooter>
            </DialogContent>
        </Dialog>
    );
}
