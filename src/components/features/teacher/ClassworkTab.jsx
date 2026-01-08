import { Plus, StickyNote, FileText, Calendar } from "lucide-react";
import { Link } from "react-router-dom";
import { Button } from "../../ui/button";
import { Card, CardHeader, CardTitle, CardContent } from "../../ui/card";
import { MOCK_ASSIGNMENT } from "../../../mocks/assignments";

// Mock list derived from single mock for demo
const ASSIGNMENTS = [
    MOCK_ASSIGNMENT,
    { ...MOCK_ASSIGNMENT, id: "a2", title: "Loops & Conditions", status: "Draft", dueDate: "2024-03-25T23:59:00" }
];

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

            <div className="space-y-4">
                {ASSIGNMENTS.map((assignment) => (
                    <Card key={assignment.id} className="hover:shadow-md transition-shadow group">
                        <div className="flex items-center justify-between p-6">
                            <div className="flex items-start gap-4">
                                <div className="p-3 bg-indigo-50 text-indigo-600 rounded-lg group-hover:bg-indigo-100 transition-colors">
                                    <FileText className="w-6 h-6" />
                                </div>
                                <div>
                                    <Link to={`/teacher/assignment/${assignment.id}`} className="block">
                                        <h3 className="text-lg font-semibold text-gray-900 hover:text-indigo-600 transition-colors">
                                            {assignment.title}
                                        </h3>
                                    </Link>
                                    <p className="text-sm text-gray-500 mt-1 line-clamp-1">{assignment.description}</p>
                                    <div className="flex items-center gap-4 mt-3 text-xs text-gray-500">
                                        <div className="flex items-center gap-1">
                                            <Calendar className="w-3 h-3" />
                                            Due {new Date(assignment.dueDate).toLocaleDateString()}
                                        </div>
                                        <span className={`px-2 py-0.5 rounded-full text-[10px] font-medium border ${assignment.status === "Active" ? "bg-green-50 text-green-700 border-green-200" :
                                                "bg-gray-100 text-gray-700 border-gray-200"
                                            }`}>
                                            {assignment.status}
                                        </span>
                                    </div>
                                </div>
                            </div>
                            <Button variant="ghost" asChild>
                                <Link to={`/teacher/assignment/${assignment.id}`}>View</Link>
                            </Button>
                        </div>
                    </Card>
                ))}

                {ASSIGNMENTS.length === 0 && (
                    <div className="p-12 text-center border-2 border-dashed border-gray-200 rounded-xl">
                        <StickyNote className="w-12 h-12 text-gray-300 mx-auto mb-4" />
                        <h3 className="text-lg font-medium text-gray-900">Assignments will appear here</h3>
                        <p className="text-gray-500 mt-1">Create assignments and questions to get started.</p>
                    </div>
                )}
            </div>
        </div>
    );
}
