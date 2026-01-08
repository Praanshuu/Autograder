import { useState } from "react";
import { Plus } from "lucide-react";
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

export default function CreateClassDialog() {
    const [open, setOpen] = useState(false);
    const [className, setClassName] = useState("");
    const [section, setSection] = useState("");
    const [subject, setSubject] = useState("");
    const [room, setRoom] = useState("");

    const handleCreate = () => {
        // Logic to create class would go here
        console.log("Creating class:", { className, section, subject, room });
        setOpen(false);
        // Reset form
        setClassName("");
        setSection("");
        setSubject("");
        setRoom("");
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
                        />
                    </div>
                    <div className="grid grid-cols-4 items-center gap-4">
                        <Label htmlFor="subject" className="text-right">
                            Subject
                        </Label>
                        <Input
                            id="subject"
                            value={subject}
                            onChange={(e) => setSubject(e.target.value)}
                            placeholder="e.g. Computer Science"
                            className="col-span-3"
                        />
                    </div>
                    <div className="grid grid-cols-4 items-center gap-4">
                        <Label htmlFor="room" className="text-right">
                            Room
                        </Label>
                        <Input
                            id="room"
                            value={room}
                            onChange={(e) => setRoom(e.target.value)}
                            placeholder="e.g. 304"
                            className="col-span-3"
                        />
                    </div>
                </div>
                <DialogFooter>
                    <Button onClick={handleCreate}>Create Class</Button>
                </DialogFooter>
            </DialogContent>
        </Dialog>
    );
}
