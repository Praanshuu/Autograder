import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import {
    CheckCircle2,
    AlertCircle,
    ArrowRight,
    Loader2
} from "lucide-react";
import { motion } from "framer-motion";
import { Button } from "../../ui/button";
import { Card, CardContent } from "../../ui/card";
import { Badge } from "../../ui/badge";

import { assignmentService } from "../../../services/assignmentService";

export default function StudentClassworkTab({ classId }) {
    const [assignments, setAssignments] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchAssignments = async () => {
            try {
                setLoading(true);
                const response = await assignmentService.getClassAssignments(classId);
                const data = Array.isArray(response.data) ? response.data : (response.data.results || []);
                setAssignments(data);
            } catch (err) {
                console.error("Failed to load assignments:", err);
            } finally {
                setLoading(false);
            }
        };

        if (classId) fetchAssignments();
    }, [classId]);

    const getStatusBadge = (item) => {
        if (item.is_graded) return <Badge className="bg-green-100 text-green-700 hover:bg-green-200 border-green-200">Graded</Badge>;
        if (item.is_submitted) return <Badge className="bg-blue-100 text-blue-700 hover:bg-blue-200 border-blue-200">Submitted</Badge>;
        const isOverdue = new Date(item.due_date) < new Date();
        if (isOverdue) return <Badge variant="destructive">Missing</Badge>;
        return <Badge variant="outline" className="text-amber-600 border-amber-200 bg-amber-50">Assigned</Badge>;
    };

    if (loading) {
        return <div className="py-12 flex justify-center"><Loader2 className="w-8 h-8 animate-spin text-indigo-600" /></div>;
    }

    if (assignments.length === 0) {
        return (
            <div className="text-center py-12 text-gray-500 bg-gray-50 rounded-lg border-2 border-dashed border-gray-200">
                No assignments posted yet.
            </div>
        );
    }

    // Group by Topic? For now, simple list.
    return (
        <div className="space-y-4">
            {assignments.map((assignment, idx) => (
                <motion.div
                    key={assignment.id}
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: idx * 0.05 }}
                >
                    <Card className="hover:shadow-md transition-shadow group cursor-pointer border-l-4 border-l-transparent hover:border-l-indigo-600">
                        <Link to={`/student/workspace/${assignment.id}`} className="block">
                            <CardContent className="p-5 flex items-center gap-4">
                                <div className="w-10 h-10 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-600 font-bold shrink-0">
                                    {idx + 1}
                                </div>
                                <div className="flex-1">
                                    <div className="flex items-center gap-2 mb-1">
                                        <h3 className="font-semibold text-gray-900 group-hover:text-indigo-600 transition-colors">
                                            {assignment.title}
                                        </h3>
                                        {getStatusBadge(assignment)}
                                    </div>
                                    <div className="text-xs text-gray-500 flex gap-3">
                                        <span>Due: {new Date(assignment.due_date).toLocaleDateString()}</span>
                                        <span>• {assignment.points} pts</span>
                                    </div>
                                </div>
                                <Button variant="ghost" size="icon" className="text-gray-300 group-hover:text-indigo-600">
                                    <ArrowRight className="w-5 h-5" />
                                </Button>
                            </CardContent>
                        </Link>
                    </Card>
                </motion.div>
            ))}
        </div>
    );
}
