import React, { useEffect, useState } from 'react';
import {
    Clock,
    CheckCircle2,
    ArrowRight,
    TrendingUp,
    Target,
    Flame,
    FileCode,
    ArrowUpRight,
    TrendingDown,
    Loader2,
    Plus
} from 'lucide-react';
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';

import StudentLayout from '../../components/layout/StudentLayout';
import { assignmentService } from '../../services/assignmentService';
import { Button } from '../../components/ui/button';
import JoinClassDialog from '../../components/features/student/JoinClassDialog';

// --- Components ---

const ProgressBar = ({ progress, className = "" }) => (
    <div className={`h-2 bg-gray-100 rounded-full overflow-hidden ${className}`}>
        <div
            className="h-full bg-gray-900 rounded-full transition-all duration-500 ease-out"
            style={{ width: `${progress}%` }}
        />
    </div>
);

const StudentDashboard = () => {
    const navigate = useNavigate();
    const [assignments, setAssignments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [isJoinDialogOpen, setIsJoinDialogOpen] = useState(false);
    const [sidebarRefreshKey, setSidebarRefreshKey] = useState(0);

    const fetchAssignments = async () => {
        try {
            setLoading(true);
            const response = await assignmentService.getAssignments();
            const data = Array.isArray(response.data) ? response.data : (response.data.results || []);
            setAssignments(data);
        } catch (err) {
            console.error("Failed to load assignments", err);
            setError("Could not load your assignments.");
        } finally {
            setLoading(false);
        }
    };

    const handleJoinSuccess = () => {
        fetchAssignments();
        setSidebarRefreshKey(prev => prev + 1);
    };

    useEffect(() => {
        fetchAssignments();
    }, []);

    // Derived State
    const activeAssignment = assignments.find(a => !a.completed) || assignments[0];
    const upNext = assignments.filter(a => a.id !== activeAssignment?.id).slice(0, 3);

    // Placeholder stats until we have a real submission history API
    const MOMENTUM_STATS = [
        { label: "Active Days", value: "1", icon: Flame, color: "text-orange-500" },
        { label: "Problems Solved", value: "0", icon: CheckCircle2, color: "text-green-500" },
        { label: "Tests Passed", value: "0", icon: FileCode, color: "text-blue-500" },
    ];

    if (loading) {
        return (
            <StudentLayout>
                <div className="flex justify-center items-center h-[60vh]">
                    <Loader2 className="w-8 h-8 animate-spin text-gray-400" />
                </div>
            </StudentLayout>
        );
    }

    return (
        <StudentLayout refreshTrigger={sidebarRefreshKey}>
            <div className="space-y-6">

                {/* 1. Header & Momentum Indicators */}
                <header className="flex flex-col md:flex-row justify-between items-start md:items-end mb-10 gap-6">
                    <div>
                        <h1 className="text-3xl font-bold tracking-tight text-gray-900">Workspace</h1>
                        <p className="text-gray-500 mt-1">Focus on progress, not perfection.</p>
                    </div>

                    <div className="flex items-center gap-6">
                        <Button onClick={() => setIsJoinDialogOpen(true)} variant="outline" className="gap-2">
                            <Plus className="w-4 h-4" />
                            Join Class
                        </Button>

                        {MOMENTUM_STATS.map((stat, idx) => (
                            <div key={idx} className="flex flex-col items-center md:items-end">
                                <div className="flex items-center gap-1.5 mb-1">
                                    <stat.icon className={`w-4 h-4 ${stat.color}`} />
                                    <span className="text-xl font-bold text-gray-900">{stat.value}</span>
                                </div>
                                <span className="text-xs font-medium text-gray-400 uppercase tracking-wide">{stat.label}</span>
                            </div>
                        ))}
                    </div>
                </header>

                <JoinClassDialog
                    open={isJoinDialogOpen}
                    onOpenChange={setIsJoinDialogOpen}
                    onJoinSuccess={handleJoinSuccess}
                />

                <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">

                    {/* LEFT COLUMN: Focus & Tasks */}
                    <div className="lg:col-span-2 space-y-8">

                        {/* 2. Hero Focus Card */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.5 }}
                            className="bg-white rounded-2xl p-8 shadow-sm border border-gray-100 relative overflow-hidden"
                        >
                            {/* Subtle Gradient Accent */}
                            <div className="absolute top-0 left-0 w-1 bg-gray-900 h-full" />

                            {activeAssignment ? (
                                <>
                                    <div className="flex justify-between items-start mb-6">
                                        <div>
                                            <span className="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-2 block">Current Focus</span>
                                            <h2 className="text-2xl font-bold text-gray-900 mb-2">{activeAssignment.title}</h2>
                                            <p className="text-gray-500">{activeAssignment.class_name || "Assignments"}</p>
                                        </div>
                                        <div className="flex flex-col items-end">
                                            {activeAssignment.due_date && (
                                                <div className="flex items-center gap-2 text-red-500 font-medium bg-red-50 px-3 py-1 rounded-full">
                                                    <Clock className="w-4 h-4" />
                                                    {new Date(activeAssignment.due_date).toLocaleDateString()}
                                                </div>
                                            )}
                                        </div>
                                    </div>

                                    <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
                                        <div>
                                            <div className="flex justify-between text-sm mb-2">
                                                <span className="text-gray-500">Progress</span>
                                                <span className="font-medium">0%</span>
                                            </div>
                                            <ProgressBar progress={0} />
                                        </div>
                                        <div className="flex gap-4 text-sm">
                                            <div>
                                                <span className="block text-gray-400 mb-1">Points</span>
                                                <span className="font-semibold text-lg">{activeAssignment.points || 100}</span>
                                            </div>
                                            <div>
                                                <span className="block text-gray-400 mb-1">Difficulty</span>
                                                <span className={`font-semibold text-lg ${activeAssignment.difficulty === 'Easy' ? 'text-green-600' :
                                                    activeAssignment.difficulty === 'Medium' ? 'text-yellow-600' :
                                                        'text-red-600'
                                                    }`}>{activeAssignment.difficulty || 'Medium'}</span>
                                            </div>
                                        </div>
                                    </div>

                                    <button
                                        onClick={() => navigate(`/student/workspace/${activeAssignment.id}`)}
                                        className="w-full md:w-auto px-8 py-3 bg-gray-900 text-white rounded-xl font-semibold hover:bg-gray-800 transition-all flex items-center justify-center gap-2 shadow-lg shadow-gray-200"
                                    >
                                        Start Assignment <ArrowRight className="w-4 h-4" />
                                    </button>
                                </>
                            ) : (
                                <div className="text-center py-10">
                                    <h3 className="text-lg font-semibold text-gray-900">No Active Assignments</h3>
                                    <p className="text-gray-500 mt-2">You are all caught up! check back later.</p>
                                </div>
                            )}
                        </motion.div>

                        {/* 3. Up Next Queue */}
                        {upNext.length > 0 && (
                            <motion.section
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ duration: 0.5, delay: 0.1 }}
                            >
                                <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                                    <Clock className="w-5 h-5 text-gray-400" /> Up Next
                                </h3>
                                <div className="space-y-3">
                                    {upNext.map(task => (
                                        <div key={task.id} className="bg-white p-4 rounded-xl border border-gray-100 flex items-center justify-between hover:border-gray-200 transition-colors">
                                            <div>
                                                <h4 className="font-semibold text-gray-900">{task.title}</h4>
                                                <p className="text-sm text-gray-500 mt-1">
                                                    {task.due_date ? `Due ${new Date(task.due_date).toLocaleDateString()}` : "No due date"}
                                                    • <span className="font-medium text-gray-600">{task.difficulty}</span>
                                                </p>
                                            </div>
                                            <button
                                                onClick={() => navigate(`/student/workspace/${task.id}`)}
                                                className="text-sm font-medium text-gray-900 hover:text-blue-600 px-4 py-2 bg-gray-50 hover:bg-gray-100 rounded-lg transition-colors"
                                            >
                                                Start
                                            </button>
                                        </div>
                                    ))}
                                </div>
                            </motion.section>
                        )}
                    </div>

                    {/* RIGHT COLUMN: Skills & Coaching (Placeholder for now) */}
                    <div className="space-y-8">
                        {/* 5. AI Coach / Next Skill */}
                        <motion.div
                            initial={{ opacity: 0, x: 20 }}
                            animate={{ opacity: 1, x: 0 }}
                            transition={{ duration: 0.5, delay: 0.3 }}
                            className="bg-indigo-50 p-6 rounded-2xl border border-indigo-100 relative overflow-hidden"
                        >
                            <Target className="w-8 h-8 text-indigo-600 mb-4" />
                            <h3 className="text-lg font-bold text-indigo-900 mb-2">Welcome!</h3>
                            <p className="text-indigo-800 text-sm mb-4 leading-relaxed">
                                This is your personal dashboard. As you complete assignments, your skills and progress will appear here.
                            </p>
                        </motion.div>
                    </div>
                </div>
            </div>
        </StudentLayout>
    );
};

export default StudentDashboard;
