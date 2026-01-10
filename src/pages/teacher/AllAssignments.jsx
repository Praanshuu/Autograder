import { useState } from "react";
import { Link } from "react-router-dom";
import { CheckCircle2, Circle, Clock, MoreVertical, Filter } from "lucide-react";
import { Button } from "../../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../../components/ui/card";
import { Badge } from "../../components/ui/badge";
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from "../../components/ui/dropdown-menu";
import { MOCK_CLASSES } from "../../mocks/classes";
import TeacherLayout from "../../components/layout/TeacherLayout";

// Mock Aggregated Assignment Data
const ALL_ASSIGNMENTS = [
    { id: 1, title: "Dynamic Programming", class: "Advanced Algorithms", due: "Due Friday", turnedIn: 25, graded: 5, total: 30, status: "active" },
    { id: 2, title: "Graph Theory Quiz", class: "Advanced Algorithms", due: "Due Mon", turnedIn: 28, graded: 0, total: 30, status: "active" },
    { id: 3, title: "Database Schema Design", class: "Database Systems", due: "No due date", turnedIn: 15, graded: 12, total: 28, status: "active" },
    { id: 4, title: "Midterm Exam", class: "Advanced Algorithms", due: "Oct 15", turnedIn: 30, graded: 30, total: 30, status: "reviewed" },
    { id: 5, title: "Intro to SQL", class: "Database Systems", due: "Sep 20", turnedIn: 28, graded: 28, total: 28, status: "reviewed" },
];

export default function AllAssignments() {
    const [activeTab, setActiveTab] = useState("toreview"); // 'toreview' | 'reviewed'

    const filteredAssignments = ALL_ASSIGNMENTS.filter(a =>
        activeTab === "toreview" ? a.status === "active" : a.status === "reviewed"
    );

    return (
        <TeacherLayout>
            <div className="max-w-5xl mx-auto space-y-8 pb-10">
                <div className="flex items-center justify-between">
                    <div className="space-y-1">
                        <h1 className="text-3xl font-bold tracking-tight text-gray-900">All Assignments</h1>
                        <p className="text-gray-500">Track and grade work across all your classes.</p>
                    </div>
                    <Button variant="outline" className="gap-2">
                        <Filter className="w-4 h-4" />
                        All Classes
                    </Button>
                </div>

                {/* Custom Tabs */}
                <div className="flex items-center gap-1 bg-gray-100 p-1 rounded-lg w-fit">
                    <button
                        onClick={() => setActiveTab("toreview")}
                        className={`px-4 py-2 rounded-md text-sm font-medium transition-all ${activeTab === "toreview"
                            ? "bg-white text-indigo-600 shadow-sm"
                            : "text-gray-500 hover:text-gray-700 hover:bg-gray-200/50"
                            }`}
                    >
                        To Review
                        <Badge className={`ml-2 h-5 px-1.5 rounded-full ${activeTab === "toreview" ? "bg-indigo-100 text-indigo-700 hover:bg-indigo-100" : "bg-gray-200 text-gray-600"
                            }`}>
                            3
                        </Badge>
                    </button>
                    <button
                        onClick={() => setActiveTab("reviewed")}
                        className={`px-4 py-2 rounded-md text-sm font-medium transition-all ${activeTab === "reviewed"
                            ? "bg-white text-indigo-600 shadow-sm"
                            : "text-gray-500 hover:text-gray-700 hover:bg-gray-200/50"
                            }`}
                    >
                        Reviewed
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
                                            </div>
                                            <p className="text-sm text-gray-500 font-medium">{assignment.class}</p>
                                            <div className="flex items-center gap-2 text-xs text-gray-400 mt-2">
                                                <Clock className="w-3.5 h-3.5" />
                                                <span>{assignment.due}</span>
                                            </div>
                                        </div>

                                        <div className="flex items-center gap-8">
                                            {/* Stats for Teacher */}
                                            <div className="text-center">
                                                <p className="text-2xl font-light text-gray-900">{assignment.turnedIn - assignment.graded}</p>
                                                <p className="text-xs text-gray-500 uppercase tracking-wide">To Grade</p>
                                            </div>
                                            <div className="text-center border-l pl-8">
                                                <p className="text-2xl font-light text-gray-900">{assignment.graded}</p>
                                                <p className="text-xs text-gray-500 uppercase tracking-wide">Graded</p>
                                            </div>
                                            <div className="text-center border-l pl-8 pr-4">
                                                <p className="text-2xl font-light text-gray-900">{assignment.turnedIn}</p>
                                                <p className="text-xs text-gray-500 uppercase tracking-wide">Turned In</p>
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
