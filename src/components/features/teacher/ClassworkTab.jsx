import { Plus, StickyNote } from "lucide-react";
import { Link } from "react-router-dom";
import { Button } from "../../ui/button";

export default function ClassworkTab() {
    return (
        <div className="space-y-6">
            <div className="flex justify-between items-center">
                <Button className="gap-2 shadow-sm" asChild>
                    <Link to="/teacher/assignment/create">
                        <Plus className="w-5 h-5" />
                        Create
                    </Link>
                </Button>
                <div className="text-sm text-gray-500 font-medium">
                    View your work
                </div>
            </div>

            <div className="p-12 text-center border-2 border-dashed border-gray-200 rounded-xl">
                <StickyNote className="w-12 h-12 text-gray-300 mx-auto mb-4" />
                <h3 className="text-lg font-medium text-gray-900">Assignments will appear here</h3>
                <p className="text-gray-500 mt-1">Create assignments and questions to get started.</p>
            </div>
        </div>
    );
}
