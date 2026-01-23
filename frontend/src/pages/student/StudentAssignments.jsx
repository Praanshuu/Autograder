import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import {
    Search,
    Filter,
    Calendar,
    CheckCircle2,
    Clock,
    AlertCircle,
    ArrowRight,
    Loader2,
    Timer
} from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

import StudentLayout from "../../components/layout/StudentLayout";
import { Button } from "../../components/ui/button";
import { Input } from "../../components/ui/input";
import { Card, CardContent } from "../../components/ui/card";
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "../../components/ui/select";
import { Badge } from "../../components/ui/badge";

import { assignmentService } from "../../services/assignmentService";
import { classService } from "../../services/classService";

export default function StudentAssignments() {
    const navigate = useNavigate();
    const [assignments, setAssignments] = useState([]);
    const [classes, setClasses] = useState([]);
    const [loading, setLoading] = useState(true);
    const [searchTerm, setSearchTerm] = useState("");
    const [statusFilter, setStatusFilter] = useState("all");
    const [classFilter, setClassFilter] = useState("all");
    const [showStartConfirmation, setShowStartConfirmation] = useState(false);
    const [selectedAssignment, setSelectedAssignment] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                setLoading(true);
                // Parallel fetch
                const [assignRes, classRes] = await Promise.all([
                    assignmentService.getAssignments(),
                    classService.getClasses()
                ]);

                const assignData = Array.isArray(assignRes.data) ? assignRes.data : (assignRes.data.results || []);
                const classData = Array.isArray(classRes.data) ? classRes.data : (classRes.data.results || []);

                setAssignments(assignData);
                setClasses(classData);
            } catch (err) {
                console.error("Failed to load data:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    const handleStartAssignment = (assignment, e) => {
        e.preventDefault(); // Prevent Link navigation
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

    // Filter Logic
    const filteredAssignments = assignments.filter(item => {
        // 1. Search
        const matchesSearch = item.title.toLowerCase().includes(searchTerm.toLowerCase());

        // 2. Class Filter
        const matchesClass = classFilter === "all" || item.class_id?.toString() === classFilter;

        // 3. Status Filter (Mock logic for now, needing 'is_submitted' flag from backend)
        // Ideally backend provides 'status' or we derive it from 'submissions' list if available
        // For now, let's assume 'status' field exists or we default to 'pending'
        let status = "pending";
        if (item.is_submitted) status = "submitted";
        if (item.is_graded) status = "graded";

        const matchesStatus = statusFilter === "all" || status === statusFilter;

        return matchesSearch && matchesClass && matchesStatus;
    });

    const getStatusBadge = (item) => {
        if (item.is_graded) return <Badge className="bg-green-100 text-green-700 hover:bg-green-200 border-green-200">Graded</Badge>;
        if (item.is_submitted) return <Badge className="bg-blue-100 text-blue-700 hover:bg-blue-200 border-blue-200">Submitted</Badge>;

        // Check if overdue
        const isOverdue = new Date(item.due_date) < new Date();
        if (isOverdue) return <Badge variant="destructive">Missing</Badge>;

        return <Badge variant="outline" className="text-amber-600 border-amber-200 bg-amber-50">To Do</Badge>;
    };

    return (
        <StudentLayout>
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="max-w-6xl mx-auto space-y-8"
            >
                {/* Header */}
                <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                    <div>
                        <h1 className="text-2xl font-bold text-gray-900">All Assignments</h1>
                        <p className="text-gray-500">Track and manage your coding tasks</p>
                    </div>
                </div>

                {/* Filters */}
                <Card>
                    <CardContent className="p-4">
                        <div className="flex flex-col md:flex-row gap-4">
                            <div className="relative flex-1">
                                <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-gray-400" />
                                <Input
                                    placeholder="Search assignments..."
                                    className="pl-9"
                                    value={searchTerm}
                                    onChange={(e) => setSearchTerm(e.target.value)}
                                />
                            </div>
                            <div className="w-full md:w-48">
                                <Select value={classFilter} onValueChange={setClassFilter}>
                                    <SelectTrigger>
                                        <SelectValue placeholder="All Classes" />
                                    </SelectTrigger>
                                    <SelectContent>
                                        <SelectItem value="all">All Classes</SelectItem>
                                        {classes.map(c => (
                                            <SelectItem key={c.id} value={c.id.toString()}>{c.name}</SelectItem>
                                        ))}
                                    </SelectContent>
                                </Select>
                            </div>
                            <div className="w-full md:w-48">
                                <Select value={statusFilter} onValueChange={setStatusFilter}>
                                    <SelectTrigger>
                                        <SelectValue placeholder="All Status" />
                                    </SelectTrigger>
                                    <SelectContent>
                                        <SelectItem value="all">All Status</SelectItem>
                                        <SelectItem value="pending">To Do</SelectItem>
                                        <SelectItem value="submitted">Submitted</SelectItem>
                                        <SelectItem value="graded">Graded</SelectItem>
                                    </SelectContent>
                                </Select>
                            </div>
                        </div>
                    </CardContent>
                </Card>

                {/* List */}
                {loading ? (
                    <div className="flex justify-center py-12">
                        <Loader2 className="w-8 h-8 animate-spin text-indigo-600" />
                    </div>
                ) : filteredAssignments.length === 0 ? (
                    <div className="text-center py-12 bg-gray-50 rounded-lg border-2 border-dashed border-gray-200">
                        <div className="p-3 bg-gray-100 rounded-full w-fit mx-auto mb-4">
                            <Filter className="w-6 h-6 text-gray-400" />
                        </div>
                        <h3 className="text-lg font-medium text-gray-900">No assignments found</h3>
                        <p className="text-gray-500 max-w-sm mx-auto mt-2">
                            Try adjusting your search or filters to see more results.
                        </p>
                        <Button
                            variant="link"
                            onClick={() => { setSearchTerm(""); setStatusFilter("all"); setClassFilter("all") }}
                            className="mt-2 text-indigo-600"
                        >
                            Clear Filters
                        </Button>
                    </div>
                ) : (
                    <div className="grid grid-cols-1 gap-4">
                        {filteredAssignments.map((assignment) => (
                            <motion.div
                                key={assignment.id}
                                layout
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 1 }}
                            >
                                <Card className="hover:shadow-md transition-shadow group cursor-pointer overflow-hidden border-l-4 border-l-transparent hover:border-l-indigo-600">
                                    <div onClick={(e) => handleStartAssignment(assignment, e)} className="block">
                                        <CardContent className="p-6 flex flex-col md:flex-row md:items-center gap-6">
                                            {/* Date Box */}
                                            <div className="flex flex-row md:flex-col items-center md:items-start gap-2 md:gap-0 min-w-[100px]">
                                                <span className="text-xs font-bold text-gray-500 uppercase tracking-wider">Due</span>
                                                <div className="font-medium text-gray-900">
                                                    {new Date(assignment.due_date).toLocaleDateString(undefined, { month: 'short', day: 'numeric' })}
                                                </div>
                                                <div className="text-xs text-gray-400">
                                                    {new Date(assignment.due_date).toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' })}
                                                </div>
                                            </div>

                                            {/* Divider */}
                                            <div className="hidden md:block w-px h-10 bg-gray-100" />

                                            {/* Details */}
                                            <div className="flex-1">
                                                <div className="flex items-center gap-2 mb-1">
                                                    <h3 className="font-bold text-lg text-gray-900 group-hover:text-indigo-600 transition-colors">
                                                        {assignment.title}
                                                    </h3>
                                                    {getStatusBadge(assignment)}
                                                </div>
                                                <div className="flex items-center gap-4 text-sm text-gray-500">
                                                    <span className="flex items-center gap-1">
                                                        <CheckCircle2 className="w-3.5 h-3.5" />
                                                        {assignment.class_name || "Class"}
                                                    </span>
                                                    <span className="flex items-center gap-1">
                                                        <AlertCircle className="w-3.5 h-3.5" />
                                                        {assignment.difficulty || "Medium"}
                                                    </span>
                                                    <span>• {assignment.points} pts</span>
                                                </div>
                                            </div>

                                            {/* Action */}
                                            <div className="flex items-center gap-4">
                                                <Button variant="ghost" size="icon" className="text-gray-400 group-hover:text-indigo-600 group-hover:bg-indigo-50">
                                                    <ArrowRight className="w-5 h-5" />
                                                </Button>
                                            </div>
                                        </CardContent>
                                    </div>
                                </Card>
                            </motion.div>
                        ))}
                    </div>
                )}
            </motion.div>

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
        </StudentLayout>
    );
}
