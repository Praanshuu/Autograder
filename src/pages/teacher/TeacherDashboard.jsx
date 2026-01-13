import { useEffect, useState } from "react";
import { MoreVertical, Users, Loader2, AlertCircle } from "lucide-react";
import { Link } from "react-router-dom";
import { motion } from "framer-motion";

import TeacherLayout from "../../components/layout/TeacherLayout";
import { classService } from "../../services/classService";
import { Button } from "../../components/ui/button";
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "../../components/ui/card";
import CreateClassDialog from "../../components/features/teacher/CreateClassDialog";

// Motion Variants
const containerVariants = {
    hidden: { opacity: 0 },
    show: {
        opacity: 1,
        transition: {
            staggerChildren: 0.1
        }
    }
};

const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    show: { opacity: 1, y: 0 }
};

const ClassCard = ({ cl }) => {
    // Determine gradient based on ID or name for consistent look
    // Fallback gradients if not provided by backend
    const gradients = [
        "bg-gradient-to-r from-blue-600 to-indigo-600",
        "bg-gradient-to-r from-emerald-600 to-teal-600",
        "bg-gradient-to-r from-orange-600 to-red-600",
        "bg-gradient-to-r from-purple-600 to-pink-600",
    ];
    // Simple hash to pick a color
    const colorIndex = (cl.id || 0) % gradients.length;
    const bgPattern = gradients[colorIndex];

    return (
        <motion.div variants={itemVariants}>
            <Card className="overflow-hidden hover:shadow-lg transition-shadow duration-300 h-full flex flex-col border-0 shadow-md">
                <div className={`h-24 ${bgPattern} relative p-4 flex flex-col justify-between`}>
                    <div className="flex justify-between items-start text-white">
                        <Link to={`/teacher/class/${cl.id}`} className="hover:underline">
                            <h3 className="text-xl font-bold leading-tight tracking-tight">{cl.name}</h3>
                        </Link>
                        <Button variant="ghost" size="icon" className="text-white hover:bg-black/20 hover:text-white h-8 w-8">
                            <MoreVertical className="w-5 h-5" />
                        </Button>
                    </div>
                    <p className="text-blue-50 text-sm font-medium opacity-90">{cl.section || "Term 1"}</p>
                </div>

                <CardContent className="p-4 flex-1 flex flex-col gap-4 mt-2">
                    <div className="flex items-center justify-between text-muted-foreground text-sm font-medium">
                        <div className="flex items-center gap-2">
                            <Users className="w-4 h-4 text-gray-400" />
                            <span>{cl.student_count || 0} Students</span>
                        </div>
                        <span>{cl.assignment_count || 0} Active Assignments</span>
                    </div>

                    {/* Pending grading indicator - TODO: Add verified logic */}
                    {cl.has_pending_grading && (
                        <div className="mt-auto pt-3 border-t">
                            <p className="text-amber-600 text-sm font-semibold flex items-center gap-2">
                                <span className="w-2 h-2 rounded-full bg-amber-500 animate-pulse shadow-[0_0_8px_rgba(245,158,11,0.5)]" />
                                Grading pending
                            </p>
                        </div>
                    )}
                </CardContent>

                <CardFooter className="px-4 py-3 bg-gray-50/50 border-t flex justify-end">
                    <Button variant="link" className="text-indigo-600 font-semibold p-0 h-auto" asChild>
                        <Link to={`/teacher/class/${cl.id}`}>
                            OPEN CLASS
                        </Link>
                    </Button>
                </CardFooter>
            </Card>
        </motion.div>
    );
};

export default function TeacherDashboard() {
    const [classes, setClasses] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchClasses = async () => {
        try {
            setLoading(true);
            const response = await classService.getClasses();
            // Backend returns array directly or { results: ... } depending on pagination
            // Assuming DRF default: it might be array if no pagination, or .results
            const data = Array.isArray(response.data) ? response.data : (response.data.results || []);
            setClasses(data);
            setError(null);
        } catch (err) {
            console.error("Failed to fetch classes:", err);
            setError("Failed to load classes. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchClasses();
    }, []);

    const handleClassCreated = (newClass) => {
        // Optimistic update or refetch
        setClasses(prev => [...prev, newClass]);
    };

    return (
        <TeacherLayout>
            <motion.div
                className="flex items-center justify-between mb-8"
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5 }}
            >
                <div>
                    <h1 className="text-3xl font-bold text-gray-900 tracking-tight">Dashboard</h1>
                    <p className="text-muted-foreground mt-1 text-lg">Overview of your active classes</p>
                </div>
                {/* Pass callback to update list after creation */}
                <CreateClassDialog onClassCreated={handleClassCreated} />
            </motion.div>

            {loading ? (
                <div className="flex justify-center items-center h-64">
                    <Loader2 className="w-8 h-8 animate-spin text-indigo-600" />
                </div>
            ) : error ? (
                <div className="flex flex-col items-center justify-center h-64 text-red-500">
                    <AlertCircle className="w-10 h-10 mb-2" />
                    <p>{error}</p>
                    <Button variant="outline" onClick={fetchClasses} className="mt-4">Retry</Button>
                </div>
            ) : classes.length === 0 ? (
                <div className="text-center py-20 bg-gray-50/50 border-2 border-dashed border-gray-200 rounded-xl">
                    <h3 className="text-xl font-semibold text-gray-700">No classes yet</h3>
                    <p className="text-gray-500 mt-2">Create your first class to get started</p>
                </div>
            ) : (
                <motion.div
                    className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
                    variants={containerVariants}
                    initial="hidden"
                    animate="show"
                >
                    {classes.map((cl) => (
                        <ClassCard key={cl.id} cl={cl} />
                    ))}
                </motion.div>
            )}
        </TeacherLayout>
    );
}
