import { useState } from "react";
import { Plus, Loader2 } from "lucide-react";
import { classService } from "../../../services/classService";
import { Button } from "../../ui/button";
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "../../ui/dialog";
import { Input } from "../../ui/input";
import { Label } from "../../ui/label";

export default function CreateClassDialog({ onClassCreated }) {
    const [open, setOpen] = useState(false);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const [className, setClassName] = useState("");
    const [section, setSection] = useState("");

    const handleCreate = async () => {
        if (!className) return;

        setLoading(true);
        setError(null);

        try {
            const classData = {
                name: className,
                section: section
            };

            const response = await classService.createClass(classData);

            if (onClassCreated) {
                onClassCreated(response.data);
            }

            setOpen(false);
            // Reset form
            setClassName("");
            setSection("");
        } catch (err) {
            console.error("Failed to create class:", err);
            setError("Failed to create class. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <Dialog open={open} onOpenChange={setOpen}>
            <DialogTrigger asChild>
                <Button className="gap-2 shadow-lg hover:shadow-xl transition-all">
                    <Plus className="w-5 h-5" />
                    Create Class
                </Button>
            </DialogTrigger>
            <DialogContent className="sm:max-w-[425px]">
                <DialogHeader>
                    <DialogTitle>Create Class</DialogTitle>
                    <DialogDescription>
                        Enter the details for your new class. Click create when you're done.
                    </DialogDescription>
                </DialogHeader>

                {error && (
                    <div className="bg-red-50 text-red-600 p-3 rounded-md text-sm border border-red-200">
                        {error}
                    </div>
                )}

                <div className="grid gap-4 py-4">
                    <div className="grid grid-cols-4 items-center gap-4">
                        <Label htmlFor="name" className="text-right">
                            Class Name
                        </Label>
                        <Input
                            id="name"
                            value={className}
                            onChange={(e) => setClassName(e.target.value)}
                            placeholder="e.g. Intro to CS"
                            className="col-span-3"
                            disabled={loading}
                        />
                    </div>
                    <div className="grid grid-cols-4 items-center gap-4">
                        <Label htmlFor="section" className="text-right">
                            Section
                        </Label>
                        <Input
                            id="section"
                            value={section}
                            onChange={(e) => setSection(e.target.value)}
                            placeholder="e.g. 101-A"
                            className="col-span-3"
                            disabled={loading}
                        />
                    </div>
                </div>
                <DialogFooter>
                    <Button onClick={handleCreate} disabled={loading || !className} className="min-w-[120px]">
                        {loading ? <Loader2 className="w-4 h-4 animate-spin mr-2" /> : null}
                        {loading ? "Creating..." : "Create Class"}
                    </Button>
                </DialogFooter>
            </DialogContent>
        </Dialog>
    );
}
