import { useState, useEffect } from "react";
import { Plus, StickyNote, FileText, Calendar, Loader2 } from "lucide-react";
import { Link, useParams } from "react-router-dom";
import { Button } from "../../ui/button";
import { Card } from "../../ui/card";
import { assignmentService } from "../../../services/assignmentService";

export default function ClassworkTab() {
    const { classId } = useParams();
    const [assignments, setAssignments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchAssignments = async () => {
            if (!classId) return;
            try {
                setLoading(true);
                const response = await assignmentService.getClassAssignments(classId);
                const data = Array.isArray(response.data) ? response.data : (response.data.results || []);
                setAssignments(data);
            } catch (err) {
                console.error("Failed to load assignments", err);
                setError("Failed to load assignments.");
            } finally {
                setLoading(false);
            }
        };

        fetchAssignments();
    }, [classId]);

    if (loading) {
        return <div className="flex justify-center py-10"><Loader2 className="w-6 h-6 animate-spin text-gray-400" /></div>;
    }

    if (error) {
        return <div className="text-red-500 py-4 text-center">{error}</div>;
    }

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
                {assignments.map((assignment) => (
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
                                    <p className="text-sm text-gray-500 mt-1 line-clamp-1">{assignment.description || "No description provided."}</p>
                                    <div className="flex items-center gap-4 mt-3 text-xs text-gray-500">
                                        {assignment.due_date && (
                                            <div className="flex items-center gap-1">
                                                <Calendar className="w-3 h-3" />
                                                Due {new Date(assignment.due_date).toLocaleDateString()}
                                            </div>
                                        )}
                                        <span className={`px-2 py-0.5 rounded-full text-[10px] font-medium border ${assignment.status === "published" ? "bg-green-50 text-green-700 border-green-200" :
                                            "bg-gray-100 text-gray-700 border-gray-200"
                                            }`}>
                                            {assignment.status || "Draft"}
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

                {assignments.length === 0 && (
                    <div className="p-12 text-center border-2 border-dashed border-gray-200 rounded-xl">
                        <StickyNote className="w-12 h-12 text-gray-300 mx-auto mb-4" />
                        <h3 className="text-lg font-medium text-gray-900">Assignments will appear here</h3>
                        <p className="text-gray-500 mt-1">Create assignments to get started.</p>
                    </div>
                )}
            </div>
        </div>
    );
}
