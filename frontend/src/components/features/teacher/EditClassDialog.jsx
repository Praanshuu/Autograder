import { useState, useEffect } from "react";
import { Loader2 } from "lucide-react";
import { classService } from "../../../services/classService";
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

export default function EditClassDialog({ classData, open, onOpenChange, onClassUpdated }) {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const [className, setClassName] = useState("");
    const [section, setSection] = useState("");

    useEffect(() => {
        if (classData) {
            setClassName(classData.name || "");
            setSection(classData.section || "");
        }
    }, [classData]);

    const handleUpdate = async () => {
        if (!className || !classData) return;

        setLoading(true);
        setError(null);

        try {
            const updatedData = {
                name: className,
                section: section
            };

            const response = await classService.updateClass(classData.id, updatedData);

            if (onClassUpdated) {
                onClassUpdated(response.data);
            }

            onOpenChange(false);
        } catch (err) {
            console.error("Failed to update class:", err);
            setError("Failed to update class. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <Dialog open={open} onOpenChange={onOpenChange}>
            <DialogContent className="sm:max-w-[425px]">
                <DialogHeader>
                    <DialogTitle>Edit Class</DialogTitle>
                    <DialogDescription>
                        Update the details for your class. Click save when you're done.
                    </DialogDescription>
                </DialogHeader>

                {error && (
                    <div className="bg-red-50 text-red-600 p-3 rounded-md text-sm border border-red-200">
                        {error}
                    </div>
                )}

                <div className="grid gap-4 py-4">
                    <div className="grid grid-cols-4 items-center gap-4">
                        <Label htmlFor="edit-name" className="text-right">
                            Class Name
                        </Label>
                        <Input
                            id="edit-name"
                            value={className}
                            onChange={(e) => setClassName(e.target.value)}
                            placeholder="e.g. Intro to CS"
                            className="col-span-3"
                            disabled={loading}
                        />
                    </div>
                    <div className="grid grid-cols-4 items-center gap-4">
                        <Label htmlFor="edit-section" className="text-right">
                            Section
                        </Label>
                        <Input
                            id="edit-section"
                            value={section}
                            onChange={(e) => setSection(e.target.value)}
                            placeholder="e.g. 101-A"
                            className="col-span-3"
                            disabled={loading}
                        />
                    </div>
                </div>
                <DialogFooter>
                    <Button variant="outline" onClick={() => onOpenChange(false)} disabled={loading}>
                        Cancel
                    </Button>
                    <Button onClick={handleUpdate} disabled={loading || !className} className="min-w-[80px]">
                        {loading ? <Loader2 className="w-4 h-4 animate-spin mr-2" /> : null}
                        {loading ? "Saving..." : "Save"}
                    </Button>
                </DialogFooter>
            </DialogContent>
        </Dialog>
    );
}
