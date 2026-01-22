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
    Plus,
    AlertTriangle,
    Timer
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate } from 'react-router-dom';

import StudentLayout from '../../components/layout/StudentLayout';
import { assignmentService } from '../../services/assignmentService';
import { Button } from '../../components/ui/button';
import JoinClassDialog from '../../components/features/student/JoinClassDialog';
import RiveDashboardCharacter from '../../components/features/student/RiveDashboardCharacter';

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
    const [showStartConfirmation, setShowStartConfirmation] = useState(false);
    const [selectedAssignment, setSelectedAssignment] = useState(null);

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

    const handleStartAssignment = (assignment) => {
        setSelectedAssignment(assignment);
        setShowStartConfirmation(true);
    };

    const handleConfirmStart = () => {
        if (selectedAssignment) {
            navigate(`/student/workspace/${selectedAssignment.id}`);
        }
        setShowStartConfirmation(false);
        setSelectedAssignment(null);
    };

    useEffect(() => {
        fetchAssignments();
    }, []);

    // Derived State
    const activeAssignment = assignments.find(a => !a.completed) || assignments[0];
    const upNext = assignments.filter(a => a.id !== activeAssignment?.id).slice(0, 3);

    // Placeholder stats until we have a real submission history API
    const MOMENTUM_STATS = [
        { label: "Active Days", value: "1", icon: Flame, color: "text-orange-500", bg: "bg-orange-50" },
        { label: "Problems Solved", value: "0", icon: CheckCircle2, color: "text-green-500", bg: "bg-green-50" },
        { label: "Tests Passed", value: "0", icon: FileCode, color: "text-blue-500", bg: "bg-blue-50" },
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
            <div className="space-y-8 max-w-7xl mx-auto">

                {/* 1. Header & Momentum Indicators */}
                <header className="flex flex-col md:flex-row justify-between items-start md:items-end gap-6">
                    <div>
                        <h1 className="text-4xl font-extrabold tracking-tight text-gray-900">Workspace</h1>
                        <p className="text-gray-500 mt-2 text-lg">Good afternoon! Ready to ship some code?</p>
                    </div>

                    <div className="flex items-center gap-4 flex-wrap">
                        <Button
                            onClick={() => setIsJoinDialogOpen(true)}
                            variant="outline"
                            className="gap-2 rounded-xl border-gray-200 hover:bg-gray-50 hover:border-gray-300 transition-all font-medium"
                        >
                            <Plus className="w-4 h-4" />
                            Join Class
                        </Button>

                        <div className="flex gap-4">
                            {MOMENTUM_STATS.map((stat, idx) => (
                                <div key={idx} className="flex flex-col items-center bg-white border border-gray-100 shadow-sm rounded-xl px-4 py-2 hover:shadow-md transition-shadow">
                                    <div className="flex items-center gap-2 mb-1">
                                        <div className={`p-1.5 rounded-full ${stat.bg}`}>
                                            <stat.icon className={`w-3.5 h-3.5 ${stat.color}`} />
                                        </div>
                                        <span className="text-xl font-bold text-gray-900">{stat.value}</span>
                                    </div>
                                    <span className="text-[10px] font-bold text-gray-400 uppercase tracking-widest">{stat.label}</span>
                                </div>
                            ))}
                        </div>
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
                            className="bg-white rounded-3xl p-0 shadow-lg shadow-indigo-100/50 border border-gray-100 relative overflow-hidden group hover:shadow-xl hover:shadow-indigo-100/60 transition-all duration-500"
                        >
                            {/* Premium Gradient Background */}
                            <div className="absolute inset-0 bg-gradient-to-br from-white via-indigo-50/30 to-white opacity-80" />

                            <div className="relative z-10 p-8 md:p-10 flex flex-col md:flex-row gap-8 items-center">
                                {/* Left Content */}
                                <div className="flex-1 w-full">
                                    {activeAssignment ? (
                                        <>
                                            <div className="flex items-center gap-3 mb-4">
                                                <span className="text-xs font-bold text-indigo-600 bg-indigo-50 px-3 py-1 rounded-full uppercase tracking-wider border border-indigo-100">
                                                    Current Priority
                                                </span>
                                                {activeAssignment.due_date && (
                                                    <span className="text-xs font-semibold text-gray-400 flex items-center gap-1.5">
                                                        <Clock className="w-3.5 h-3.5" />
                                                        Due {new Date(activeAssignment.due_date).toLocaleDateString()}
                                                    </span>
                                                )}
                                            </div>

                                            <h2 className="text-3xl font-extrabold text-gray-900 mb-2 leading-tight">
                                                {activeAssignment.title}
                                            </h2>
                                            <p className="text-lg text-gray-500 mb-8 font-medium">
                                                {activeAssignment.class_name || "Assignments"}
                                            </p>

                                            <div className="grid grid-cols-2 gap-6 mb-8 bg-white/50 p-4 rounded-xl border border-gray-100">
                                                <div>
                                                    <span className="block text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">Points</span>
                                                    <span className="font-bold text-xl text-gray-900">{activeAssignment.points || 100}</span>
                                                </div>
                                                <div>
                                                    <span className="block text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">Difficulty</span>
                                                    <span className={`font-bold text-xl ${activeAssignment.difficulty === 'Easy' ? 'text-green-600' :
                                                        activeAssignment.difficulty === 'Medium' ? 'text-amber-600' :
                                                            'text-red-600'
                                                        }`}>{activeAssignment.difficulty || 'Medium'}</span>
                                                </div>
                                            </div>

                                            <button
                                                onClick={() => handleStartAssignment(activeAssignment)}
                                                className="w-full md:w-auto px-8 py-4 bg-gray-900 text-white rounded-xl font-bold hover:bg-black transition-all flex items-center justify-center gap-2 shadow-lg shadow-gray-200 hover:-translate-y-0.5"
                                            >
                                                Start Assignment <ArrowRight className="w-4 h-4 font-bold" />
                                            </button>
                                        </>
                                    ) : (
                                        <div className="py-10">
                                            <h3 className="text-2xl font-bold text-gray-900 mb-2">All Caught Up!</h3>
                                            <p className="text-gray-500">You have no pending assignments. Great job!</p>
                                        </div>
                                    )}
                                </div>

                                {/* Right Content - Rive Animation */}
                                <div className="w-full md:w-1/3 h-80 md:h-96 relative flex items-center justify-center">
                                    <div className="absolute inset-0 bg-indigo-100 rounded-full blur-3xl opacity-30 transform scale-75" />
                                    <RiveDashboardCharacter />
                                </div>
                            </div>
                        </motion.div>

                        {/* 3. Up Next Queue */}
                        {upNext.length > 0 && (
                            <motion.section
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ duration: 0.5, delay: 0.1 }}
                            >
                                <div className="flex items-center justify-between mb-4">
                                    <h3 className="text-lg font-bold text-gray-900 flex items-center gap-2">
                                        <Clock className="w-5 h-5 text-gray-400" /> Up Next
                                    </h3>
                                    <Button variant="link" className="text-indigo-600 font-semibold text-sm">View Calendar</Button>
                                </div>

                                <div className="space-y-3">
                                    {upNext.map((task, i) => (
                                        <div key={task.id} className="relative group">
                                            {/* Connector Line */}
                                            {i !== upNext.length - 1 && (
                                                <div className="absolute left-[26px] top-12 bottom-[-14px] w-0.5 bg-gray-100 z-0 group-hover:bg-indigo-50 transition-colors" />
                                            )}

                                            <div className="bg-white p-4 rounded-2xl border border-gray-100 flex items-center justify-between hover:border-indigo-100 hover:shadow-md transition-all relative z-10 group-hover:-translate-y-0.5 duration-300">
                                                <div className="flex items-center gap-4">
                                                    <div className="w-14 h-14 rounded-xl bg-gray-50 flex flex-col items-center justify-center border border-gray-100 group-hover:bg-indigo-50 group-hover:border-indigo-100 transition-colors">
                                                        <span className="text-xs font-semibold text-gray-400 uppercase group-hover:text-indigo-400">Due</span>
                                                        <span className="text-lg font-bold text-gray-900 group-hover:text-indigo-700">
                                                            {new Date(task.due_date).getDate()}
                                                        </span>
                                                    </div>
                                                    <div>
                                                        <div className="flex items-center gap-2 mb-1">
                                                            <h4 className="font-bold text-gray-900 group-hover:text-indigo-700 transition-colors">{task.title}</h4>
                                                            <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full border ${task.difficulty === 'Easy' ? 'bg-green-50 text-green-700 border-green-100' :
                                                                task.difficulty === 'Medium' ? 'bg-amber-50 text-amber-700 border-amber-100' :
                                                                    'bg-red-50 text-red-700 border-red-100'
                                                                }`}>{task.difficulty}</span>
                                                        </div>
                                                        <p className="text-sm text-gray-500 font-medium">
                                                            {task.class_name} • {task.points || 100} pts
                                                        </p>
                                                    </div>
                                                </div>
                                                <Button
                                                    onClick={() => handleStartAssignment(task)}
                                                    variant="ghost"
                                                    size="icon"
                                                    className="text-gray-400 hover:text-indigo-600 hover:bg-indigo-50"
                                                >
                                                    <ArrowRight className="w-5 h-5" />
                                                </Button>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </motion.section>
                        )}
                    </div>

                    {/* RIGHT COLUMN: Skills & Coaching */}
                    <div className="space-y-8">
                        {/* 5. AI Coach / Next Skill */}
                        <motion.div
                            initial={{ opacity: 0, x: 20 }}
                            animate={{ opacity: 1, x: 0 }}
                            transition={{ duration: 0.5, delay: 0.3 }}
                            className="bg-white p-6 rounded-3xl border border-gray-100 shadow-lg shadow-gray-100/50 relative overflow-hidden"
                        >
                            <div className="absolute top-0 right-0 w-32 h-32 bg-indigo-50 rounded-full blur-3xl opacity-50 -translate-y-1/2 translate-x-1/2" />

                            <div className="relative z-10">
                                <div className="w-10 h-10 bg-indigo-50 rounded-xl flex items-center justify-center mb-4">
                                    <Target className="w-5 h-5 text-indigo-600" />
                                </div>

                                <h3 className="text-lg font-bold text-gray-900 mb-2">Weekly Goal</h3>
                                <p className="text-gray-500 text-sm mb-6 leading-relaxed">
                                    Solve 3 medium difficulty problems to maintain your streak.
                                </p>

                                <div className="space-y-2 mb-2">
                                    <div className="flex justify-between text-xs font-bold text-gray-500 uppercase tracking-wider">
                                        <span>Progress</span>
                                        <span>1/3</span>
                                    </div>
                                    <ProgressBar progress={33} className="bg-gray-100" />
                                </div>
                            </div>
                        </motion.div>
                    </div>
                </div>

                {/* Start Assignment Confirmation Modal */}
                <AnimatePresence>
                    {showStartConfirmation && selectedAssignment && (
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-[1px]"
                        >
                            <motion.div
                                initial={{ scale: 0.8, opacity: 0 }}
                                animate={{ scale: 1, opacity: 1 }}
                                exit={{ scale: 0.8, opacity: 0 }}
                                className="bg-white p-8 rounded-2xl shadow-2xl text-center max-w-md w-full mx-4"
                            >
                                <div className="w-16 h-16 bg-indigo-100 rounded-full flex items-center justify-center mx-auto mb-4">
                                    <Timer className="w-8 h-8 text-indigo-600" />
                                </div>
                                <h2 className="text-2xl font-bold text-gray-900 mb-2">Start Assignment?</h2>
                                <p className="text-gray-500 mb-2">
                                    <strong>{selectedAssignment.title}</strong>
                                </p>
                                <p className="text-gray-500 mb-6">
                                    Once you start, the timer will begin and you can only exit by submitting your solution. 
                                    Are you ready to begin?
                                </p>
                                <div className="flex gap-3">
                                    <Button 
                                        variant="outline" 
                                        onClick={() => setShowStartConfirmation(false)}
                                        className="flex-1"
                                    >
                                        Cancel
                                    </Button>
                                    <Button 
                                        onClick={handleConfirmStart}
                                        className="flex-1 bg-indigo-600 hover:bg-indigo-700 text-white"
                                    >
                                        Start Assignment
                                    </Button>
                                </div>
                            </motion.div>
                        </motion.div>
                    )}
                </AnimatePresence>
            </div>
        </StudentLayout>
    );
};

export default StudentDashboard;
