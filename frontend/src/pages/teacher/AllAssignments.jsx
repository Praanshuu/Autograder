import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { CheckCircle2, Circle, Clock, MoreVertical, Filter, Loader2 } from "lucide-react";
import { Button } from "../../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../../components/ui/card";
import { Badge } from "../../components/ui/badge";
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from "../../components/ui/dropdown-menu";
import TeacherLayout from "../../components/layout/TeacherLayout";
import { assignmentService } from "../../services/assignmentService";

export default function AllAssignments() {
    const [activeTab, setActiveTab] = useState("all"); // 'all' | 'published' | 'draft'
    const [assignments, setAssignments] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchAssignments = async () => {
            try {
                const response = await assignmentService.getAssignments();
                const data = Array.isArray(response.data) ? response.data : (response.data.results || []);
                setAssignments(data);
            } catch (error) {
                console.error("Failed to fetch assignments:", error);
            } finally {
                setLoading(false);
            }
        };

        fetchAssignments();
    }, []);

    const filteredAssignments = assignments.filter(a => {
        if (activeTab === 'all') return true;
        return a.status === activeTab;
    });

    if (loading) {
        return (
            <TeacherLayout>
                <div className="flex justify-center items-center h-[50vh]">
                    <Loader2 className="w-8 h-8 animate-spin text-gray-400" />
                </div>
            </TeacherLayout>
        );
    }

    return (
        <TeacherLayout>
            <div className="max-w-5xl mx-auto space-y-8 pb-10">
                <div className="flex items-center justify-between">
                    <div className="space-y-1">
                        <h1 className="text-3xl font-bold tracking-tight text-gray-900">All Assignments</h1>
                        <p className="text-gray-500">Track and grade work across all your classes.</p>
                    </div>
                </div>

                {/* Custom Tabs */}
                <div className="flex items-center gap-1 bg-gray-100 p-1 rounded-lg w-fit">
                    <button
                        onClick={() => setActiveTab("all")}
                        className={`px-4 py-2 rounded-md text-sm font-medium transition-all ${activeTab === "all"
                            ? "bg-white text-indigo-600 shadow-sm"
                            : "text-gray-500 hover:text-gray-700 hover:bg-gray-200/50"
                            }`}
                    >
                        All
                    </button>
                    <button
                        onClick={() => setActiveTab("published")}
                        className={`px-4 py-2 rounded-md text-sm font-medium transition-all ${activeTab === "published"
                            ? "bg-white text-indigo-600 shadow-sm"
                            : "text-gray-500 hover:text-gray-700 hover:bg-gray-200/50"
                            }`}
                    >
                        Published
                    </button>
                    <button
                        onClick={() => setActiveTab("draft")}
                        className={`px-4 py-2 rounded-md text-sm font-medium transition-all ${activeTab === "draft"
                            ? "bg-white text-indigo-600 shadow-sm"
                            : "text-gray-500 hover:text-gray-700 hover:bg-gray-200/50"
                            }`}
                    >
                        Drafts
                    </button>
                </div>

                {/* Assignments List */}
                <div className="space-y-4">
                    {filteredAssignments.map((assignment) => (
                        <Link to={`/teacher/assignment/${assignment.id}`} key={assignment.id} className="block group">
                            <Card className="hover:shadow-md transition-shadow cursor-pointer border-l-4 border-l-transparent hover:border-l-indigo-500">
                                <CardContent className="p-6">
                                    <div className="flex items-start justify-between">
                                        <div className="space-y-1">
                                            <div className="flex items-center gap-2">
                                                <h3 className="text-lg font-semibold text-gray-900 group-hover:text-indigo-600 transition-colors">
                                                    {assignment.title}
                                                </h3>
                                                <Badge variant="outline" className="text-xs font-normal">
                                                    {assignment.status}
                                                </Badge>
                                            </div>
                                            <p className="text-sm text-gray-500 font-medium">
                                                {assignment.class_obj?.name || "Unknown Class"}
                                            </p>
                                            <div className="flex items-center gap-2 text-xs text-gray-400 mt-2">
                                                <Clock className="w-3.5 h-3.5" />
                                                <span>
                                                    {assignment.due_date
                                                        ? new Date(assignment.due_date).toLocaleDateString()
                                                        : "No due date"}
                                                </span>
                                            </div>
                                        </div>

                                        <div className="flex items-center gap-8">
                                            {/* Stats Placeholder - Backend needs to send these stats */}
                                            <div className="text-center">
                                                <p className="text-2xl font-light text-gray-900">--</p>
                                                <p className="text-xs text-gray-500 uppercase tracking-wide">To Grade</p>
                                            </div>
                                            <div className="text-center border-l pl-8">
                                                <p className="text-2xl font-light text-gray-900">--</p>
                                                <p className="text-xs text-gray-500 uppercase tracking-wide">Graded</p>
                                            </div>
                                            <div className="text-center border-l pl-8 pr-4">
                                                <p className="text-2xl font-light text-gray-900">{assignment.questions?.length || 0}</p>
                                                <p className="text-xs text-gray-500 uppercase tracking-wide">Questions</p>
                                            </div>
                                        </div>
                                    </div>
                                </CardContent>
                            </Card>
                        </Link>
                    ))}

                    {filteredAssignments.length === 0 && (
                        <div className="text-center py-12">
                            <div className="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-4 text-gray-400">
                                <CheckCircle2 className="w-8 h-8" />
                            </div>
                            <h3 className="text-lg font-medium text-gray-900">All caught up!</h3>
                            <p className="text-gray-500">No work to review right now.</p>
                        </div>
                    )}
                </div>
            </div>
        </TeacherLayout>
    );
}
