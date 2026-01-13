import React from 'react';
import {
    Clock,
    CheckCircle2,
    ArrowRight,
    TrendingUp,
    Target,
    Flame,
    FileCode,
    ArrowUpRight,
    TrendingDown
} from 'lucide-react';
import { motion } from 'framer-motion';

// --- Mock Data ---

const HERO_TASK = {
    id: 101,
    course: "CSL100: Introduction to Computer Science",
    title: "Assignment 2: Text Processing",
    timeLeft: "2 Days",
    progress: 15, // Just started
    questionsSolved: 1,
    totalQuestions: 4,
    testsPassed: 3,
    totalTests: 12
};

const UP_NEXT = [
    {
        id: 1,
        title: "Assignment 4: List Manipulation",
        due: "Tomorrow, 11:59 PM",
        status: "Not Started",
        difficulty: "Medium"
    },
    {
        id: 2,
        title: "Practice: Negative Indexing",
        due: "Optional",
        status: "Recommended",
        difficulty: "Easy"
    }
];

// Replaced Radar Chart with Skill Map
const SKILL_MAP = [
    { topic: 'Python Syntax', mastery: 92, trend: 'up' },
    { topic: 'Control Flow', mastery: 85, trend: 'stable' },
    { topic: 'String Manipulation', mastery: 65, trend: 'up' },
    { topic: 'Edge Cases', mastery: 30, trend: 'down' }, // Major weakness from Assign 1
];

const RECENT_FEEDBACK = [
    {
        id: 301,
        assignment: "Assignment 1: Data Types",
        feedback: "Your logic works for positive numbers, but fails for negative inputs. Check your conditions.",
        type: "constructive"
    },
    {
        id: 302,
        assignment: "Warmup: Hello World",
        feedback: "Perfect submission. Good use of print formatting.",
        type: "positive"
    }
];

const MOMENTUM_STATS = [
    { label: "Active Days", value: "12", icon: Flame, color: "text-orange-500" },
    { label: "Problems Solved", value: "45", icon: CheckCircle2, color: "text-green-500" },
    { label: "Tests Passed", value: "128", icon: FileCode, color: "text-blue-500" },
];

// --- Components ---

const ProgressBar = ({ progress, className = "" }) => (
    <div className={`h-2 bg-gray-100 rounded-full overflow-hidden ${className}`}>
        <div
            className="h-full bg-gray-900 rounded-full transition-all duration-500 ease-out"
            style={{ width: `${progress}%` }}
        />
    </div>
);

import StudentLayout from '../../components/layout/StudentLayout';
import { useNavigate } from 'react-router-dom';

const StudentDashboard = () => {
    const navigate = useNavigate();
    return (
        <StudentLayout>
            <div className="space-y-6">

                {/* 1. Header & Momentum Indicators */}
                <header className="flex flex-col md:flex-row justify-between items-start md:items-end mb-10 gap-6">
                    <div>
                        <h1 className="text-3xl font-bold tracking-tight text-gray-900">Workspace</h1>
                        <p className="text-gray-500 mt-1">Focus on progress, not perfection.</p>
                    </div>

                    <div className="flex gap-6">
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

                            <div className="flex justify-between items-start mb-6">
                                <div>
                                    <span className="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-2 block">Current Focus</span>
                                    <h2 className="text-2xl font-bold text-gray-900 mb-2">{HERO_TASK.title}</h2>
                                    <p className="text-gray-500">{HERO_TASK.course}</p>
                                </div>
                                <div className="flex flex-col items-end">
                                    <div className="flex items-center gap-2 text-red-500 font-medium bg-red-50 px-3 py-1 rounded-full">
                                        <Clock className="w-4 h-4" />
                                        {HERO_TASK.timeLeft} left
                                    </div>
                                </div>
                            </div>

                            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
                                <div>
                                    <div className="flex justify-between text-sm mb-2">
                                        <span className="text-gray-500">Progress</span>
                                        <span className="font-medium">{HERO_TASK.progress}%</span>
                                    </div>
                                    <ProgressBar progress={HERO_TASK.progress} />
                                </div>
                                <div className="flex gap-4 text-sm">
                                    <div>
                                        <span className="block text-gray-400 mb-1">Tasks</span>
                                        <span className="font-semibold text-lg">{HERO_TASK.questionsSolved}<span className="text-gray-300">/</span>{HERO_TASK.totalQuestions}</span>
                                    </div>
                                    <div>
                                        <span className="block text-gray-400 mb-1">Tests</span>
                                        <span className="font-semibold text-lg text-green-600">{HERO_TASK.testsPassed}<span className="text-gray-300">/</span>{HERO_TASK.totalTests}</span>
                                    </div>
                                </div>
                            </div>

                            <button
                                onClick={() => navigate('/student/workspace/a2')}
                                className="w-full md:w-auto px-8 py-3 bg-gray-900 text-white rounded-xl font-semibold hover:bg-gray-800 transition-all flex items-center justify-center gap-2 shadow-lg shadow-gray-200"
                            >
                                Continue Work <ArrowRight className="w-4 h-4" />
                            </button>
                        </motion.div>

                        {/* 3. Up Next Queue */}
                        <motion.section
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.5, delay: 0.1 }}
                        >
                            <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                                <Clock className="w-5 h-5 text-gray-400" /> Up Next
                            </h3>
                            <div className="space-y-3">
                                {UP_NEXT.map(task => (
                                    <div key={task.id} className="bg-white p-4 rounded-xl border border-gray-100 flex items-center justify-between hover:border-gray-200 transition-colors">
                                        <div>
                                            <h4 className="font-semibold text-gray-900">{task.title}</h4>
                                            <p className="text-sm text-gray-500 mt-1">Due {task.due} • <span className="font-medium text-gray-600">{task.difficulty}</span></p>
                                        </div>
                                        <button className="text-sm font-medium text-gray-900 hover:text-blue-600 px-4 py-2 bg-gray-50 hover:bg-gray-100 rounded-lg transition-colors">
                                            Start
                                        </button>
                                    </div>
                                ))}
                            </div>
                        </motion.section>

                        {/* 4. Recent Feedback */}
                        <motion.section
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.5, delay: 0.2 }}
                        >
                            <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                                <CheckCircle2 className="w-5 h-5 text-gray-400" /> Recent Feedback
                            </h3>
                            <div className="grid gap-4">
                                {RECENT_FEEDBACK.map(item => (
                                    <div key={item.id} className="bg-white p-5 rounded-xl border border-gray-100">
                                        <div className="flex justify-between items-center mb-2">
                                            <h4 className="font-medium text-gray-900">{item.assignment}</h4>
                                            {item.type === 'positive' ? (
                                                <span className="text-xs font-bold bg-green-50 text-green-700 px-2 py-1 rounded">Great Job</span>
                                            ) : (
                                                <span className="text-xs font-bold bg-yellow-50 text-yellow-700 px-2 py-1 rounded">Review</span>
                                            )}
                                        </div>
                                        <p className="text-gray-600 text-sm italic">"{item.feedback}"</p>
                                    </div>
                                ))}
                            </div>
                        </motion.section>

                    </div>

                    {/* RIGHT COLUMN: Skills & Coaching */}
                    <div className="space-y-8">

                        {/* 5. AI Coach / Next Skill */}
                        <motion.div
                            initial={{ opacity: 0, x: 20 }}
                            animate={{ opacity: 1, x: 0 }}
                            transition={{ duration: 0.5, delay: 0.3 }}
                            className="bg-indigo-50 p-6 rounded-2xl border border-indigo-100 relative overflow-hidden"
                        >
                            <Target className="w-8 h-8 text-indigo-600 mb-4" />
                            <h3 className="text-lg font-bold text-indigo-900 mb-2">Next Best Step</h3>
                            <p className="text-indigo-800 text-sm mb-4 leading-relaxed">
                                You're mastering basic syntax, but recent tests show you struggled with **Negative Edge Cases** in strings.
                            </p>
                            <button className="w-full py-2.5 bg-white text-indigo-700 text-sm font-semibold rounded-lg shadow-sm hover:bg-indigo-100 transition-colors flex items-center justify-center gap-2">
                                Practice Edge Cases <ArrowUpRight className="w-4 h-4" />
                            </button>
                        </motion.div>

                        {/* 6. Skill Map */}
                        <motion.section
                            initial={{ opacity: 0, x: 20 }}
                            animate={{ opacity: 1, x: 0 }}
                            transition={{ duration: 0.5, delay: 0.4 }}
                            className="bg-white p-6 rounded-2xl border border-gray-100"
                        >
                            <div className="flex items-center gap-2 mb-6">
                                <TrendingUp className="w-5 h-5 text-gray-900" />
                                <h2 className="text-lg font-bold text-gray-900">Skill Map</h2>
                            </div>

                            <div className="space-y-6">
                                {SKILL_MAP.map((skill, idx) => (
                                    <div key={idx}>
                                        <div className="flex justify-between items-center mb-2">
                                            <span className="text-sm font-medium text-gray-700">{skill.topic}</span>
                                            <div className="flex items-center gap-2">
                                                {skill.trend === 'up' && <TrendingUp className="w-3 h-3 text-green-500" />}
                                                {skill.trend === 'down' && <TrendingDown className="w-3 h-3 text-red-500" />}
                                                <span className="text-xs text-gray-400 font-mono">{skill.mastery}%</span>
                                            </div>
                                        </div>
                                        <div className="h-1.5 bg-gray-50 rounded-full overflow-hidden">
                                            <div
                                                className={`h-full rounded-full ${skill.mastery >= 80 ? 'bg-green-500' :
                                                    skill.mastery >= 60 ? 'bg-indigo-500' :
                                                        'bg-orange-500'
                                                    }`}
                                                style={{ width: `${skill.mastery}%` }}
                                            />
                                        </div>
                                    </div>
                                ))}
                            </div>

                            <button className="w-full mt-6 text-sm text-gray-500 hover:text-gray-900 font-medium">
                                View Detailed Analytics
                            </button>
                        </motion.section>

                    </div>
                </div>
            </div>
        </StudentLayout>
    );
};

export default StudentDashboard;
