import { useState } from "react";
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from "../../ui/dialog";
import { Button } from "../../ui/button";
import { Input } from "../../ui/input";
import { Label } from "../../ui/label";
import { Loader2 } from "lucide-react";
import { classService } from "../../../services/classService";

export default function JoinClassDialog({ open, onOpenChange, onJoinSuccess }) {
    const [joinCode, setJoinCode] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleJoin = async () => {
        if (!joinCode.trim()) {
            setError("Please enter a class code.");
            return;
        }

        setLoading(true);
        setError(null);

        try {
            const response = await classService.joinClassByCode(joinCode.trim());

            if (response.success) {
                // Success
                setJoinCode("");
                onOpenChange(false);
                if (onJoinSuccess) onJoinSuccess();
            } else {
                setError(response.message || "Failed to join class. Please check the code.");
            }

        } catch (err) {
            console.error("Unexpected error:", err);
            setError("An unexpected error occurred.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <Dialog open={open} onOpenChange={onOpenChange}>
            <DialogContent className="sm:max-w-[425px]">
                <DialogHeader>
                    <DialogTitle>Join a Class</DialogTitle>
                    <DialogDescription>
                        Ask your teacher for the class code, then enter it here.
                    </DialogDescription>
                </DialogHeader>
                <div className="grid gap-4 py-4">
                    <div className="grid gap-2">
                        <Label htmlFor="code" className="">
                            Class Code
                        </Label>
                        <Input
                            id="code"
                            value={joinCode}
                            onChange={(e) => setJoinCode(e.target.value.toUpperCase())}
                            placeholder="e.g. XY-1234"
                            className="col-span-3 font-mono uppercase"
                        />
                    </div>
                    {error && (
                        <p className="text-sm text-red-500 font-medium">{error}</p>
                    )}
                </div>
                <DialogFooter>
                    <Button variant="outline" onClick={() => onOpenChange(false)}>Cancel</Button>
                    <Button onClick={handleJoin} disabled={loading} className="gap-2">
                        {loading && <Loader2 className="w-4 h-4 animate-spin" />}
                        Join Class
                    </Button>
                </DialogFooter>
            </DialogContent>
        </Dialog>
    );
}
