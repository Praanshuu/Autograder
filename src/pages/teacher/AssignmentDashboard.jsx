import { useState, useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import {
    MoveLeft,
    BarChart3,
    Users,
    CheckCircle2,
    ArrowUpDown,
    Search,
    Filter,
    ListChecks,
    ChevronRight,
    Target,
    XCircle,
    Loader2,
    AlertCircle
} from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

import TeacherLayout from "../../components/layout/TeacherLayout";
import { Button } from "../../components/ui/button";
import { Input } from "../../components/ui/input";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../../components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../../components/ui/tabs";
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "../../components/ui/table";

// Services
import { assignmentService } from "../../services/assignmentService";
import { submissionService } from "../../services/submissionService";

// Analytics Components (Mocked for now as we don't have endpoints yet)
import PerformanceMatrix from "../../components/features/analytics/PerformanceMatrix";
import ErrorHeatmap from "../../components/features/analytics/ErrorHeatmap";
import CodeSimilarityMap from "../../components/features/analytics/CodeSimilarityMap";

export default function AssignmentDashboard() {
    const { id } = useParams();
    const [searchTerm, setSearchTerm] = useState("");
    const [filterStatus, setFilterStatus] = useState("All");

    // Data State
    const [assignment, setAssignment] = useState(null);
    const [submissions, setSubmissions] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Analytics Navigation State
    const [selectedQuestion, setSelectedQuestion] = useState(null);
    const [selectedAnalyticsTag, setSelectedAnalyticsTag] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                setLoading(true);
                // 1. Fetch Assignment Details
                const assignResponse = await assignmentService.getAssignment(id);
                setAssignment(assignResponse.data);

                // 2. Fetch Submissions
                const subResponse = await submissionService.getAssignmentSubmissions(id);
                const subData = Array.isArray(subResponse.data) ? subResponse.data : (subResponse.data.results || []);
                setSubmissions(subData);
                setError(null);
            } catch (err) {
                console.error("Failed to load dashboard data:", err);
                setError("Failed to load assignment data. Please try again.");
            } finally {
                setLoading(false);
            }
        };

        if (id) fetchData();
    }, [id]);

    // Derived Stats
    const totalStudents = assignment?.class_obj?.student_count || 0; // Assuming API provides this or we fetch class details
    const submittedCount = submissions.length;
    const gradedCount = submissions.filter(s => s.is_graded).length;

    // Calculate Average Score
    const scores = submissions.filter(s => s.final_score !== null).map(s => s.final_score);
    const avgScore = scores.length > 0 ? (scores.reduce((a, b) => a + b, 0) / scores.length).toFixed(1) : 0;

    // Calculate Highest/Lowest
    const highestScore = scores.length > 0 ? Math.max(...scores) : 0;
    const lowestScore = scores.length > 0 ? Math.min(...scores) : 0;
    const completionRate = totalStudents > 0 ? Math.round((submittedCount / totalStudents) * 100) : 0;

    // Filter Logic
    const filteredSubmissions = submissions.filter(sub => {
        const studentName = sub.student?.first_name ? `${sub.student.first_name} ${sub.student.last_name}` : sub.student?.email || "Unknown";
        const matchesSearch = studentName.toLowerCase().includes(searchTerm.toLowerCase());

        let status = "To Grade";
        if (sub.is_graded) status = "Graded";
        // Simple mapping for now

        const matchesStatus = filterStatus === "All" || status === filterStatus;
        return matchesSearch && matchesStatus;
    });

    const currentQuestion = selectedQuestion && assignment?.questions
        ? assignment.questions.find(q => q.id === selectedQuestion)
        : null;

    if (loading) {
        return (
            <TeacherLayout>
                <div className="flex h-[80vh] items-center justify-center">
                    <Loader2 className="w-10 h-10 animate-spin text-indigo-600" />
                </div>
            </TeacherLayout>
        );
    }

    if (error || !assignment) {
        return (
            <TeacherLayout>
                <div className="flex flex-col h-[80vh] items-center justify-center text-red-500">
                    <AlertCircle className="w-12 h-12 mb-4" />
                    <h2 className="text-xl font-bold">Error</h2>
                    <p>{error || "Assignment not found"}</p>
                    <Button variant="outline" className="mt-4" asChild>
                        <Link to="/teacher/dashboard">Back to Dashboard</Link>
                    </Button>
                </div>
            </TeacherLayout>
        );
    }

    return (
        <TeacherLayout>
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="space-y-6"
            >
                {/* Header */}
                <div className="flex flex-col gap-4 md:flex-row md:items-center justify-between">
                    <div className="flex items-center gap-4">
                        <Button variant="ghost" size="icon" asChild>
                            <Link to="/teacher/dashboard">
                                <MoveLeft className="w-5 h-5" />
                            </Link>
                        </Button>
                        <div>
                            <div className="flex items-center gap-2">
                                <h1 className="text-2xl font-bold text-gray-900">{assignment.title}</h1>
                                <span className={`px-2 py-0.5 rounded-full text-xs font-medium border ${assignment.status === 'published' ? 'bg-green-100 text-green-700 border-green-200' : 'bg-gray-100 text-gray-700 border-gray-200'
                                    }`}>
                                    {assignment.status}
                                </span>
                            </div>
                            <p className="text-gray-500 text-sm mt-1">Due {new Date(assignment.due_date).toLocaleDateString()}</p>
                        </div>
                    </div>
                </div>

                {/* Main Content Tabs */}
                <Tabs defaultValue="submissions" className="space-y-6">
                    <TabsList className="bg-white border p-1 rounded-lg">
                        <TabsTrigger value="submissions" className="flex items-center gap-2">
                            <ListChecks className="w-4 h-4" />
                            Submissions
                        </TabsTrigger>
                        <TabsTrigger value="analytics" className="flex items-center gap-2">
                            <BarChart3 className="w-4 h-4" />
                            Analytics & Insights
                        </TabsTrigger>
                    </TabsList>

                    {/* --- TAB: SUBMISSIONS --- */}
                    <TabsContent value="submissions">
                        {/* Overall Stats Row */}
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
                            <Card>
                                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                    <CardTitle className="text-sm font-medium">Average Score</CardTitle>
                                    <BarChart3 className="h-4 w-4 text-muted-foreground" />
                                </CardHeader>
                                <CardContent>
                                    <div className="text-2xl font-bold">{avgScore}%</div>
                                    <p className="text-xs text-muted-foreground">Based on {gradedCount} graded</p>
                                </CardContent>
                            </Card>
                            <Card>
                                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                    <CardTitle className="text-sm font-medium">Submitted</CardTitle>
                                    <Users className="h-4 w-4 text-muted-foreground" />
                                </CardHeader>
                                <CardContent>
                                    <div className="text-2xl font-bold">{submittedCount}/{totalStudents || "?"}</div>
                                    <p className="text-xs text-muted-foreground">{completionRate}% completion rate</p>
                                </CardContent>
                            </Card>
                            <Card>
                                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                    <CardTitle className="text-sm font-medium">Graded</CardTitle>
                                    <CheckCircle2 className="h-4 w-4 text-muted-foreground" />
                                </CardHeader>
                                <CardContent>
                                    <div className="text-2xl font-bold">{gradedCount}</div>
                                    <p className="text-xs text-muted-foreground">To grade: {submittedCount - gradedCount}</p>
                                </CardContent>
                            </Card>
                            <Card>
                                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                    <CardTitle className="text-sm font-medium">Highest Score</CardTitle>
                                    <ArrowUpDown className="h-4 w-4 text-muted-foreground" />
                                </CardHeader>
                                <CardContent>
                                    <div className="text-2xl font-bold">{highestScore}</div>
                                    <p className="text-xs text-muted-foreground">Lowest: {lowestScore}</p>
                                </CardContent>
                            </Card>
                        </div>

                        {/* Submission Table */}
                        <Card>
                            <CardHeader>
                                <div className="flex items-center justify-between">
                                    <div>
                                        <CardTitle>All Submissions</CardTitle>
                                        <CardDescription>Manage individual student grades</CardDescription>
                                    </div>
                                    <div className="flex gap-2 items-center">
                                        <div className="relative w-64">
                                            <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-gray-400" />
                                            <Input
                                                placeholder="Search student..."
                                                className="pl-9"
                                                value={searchTerm}
                                                onChange={(e) => setSearchTerm(e.target.value)}
                                            />
                                        </div>
                                        <Button variant="outline"><Filter className="w-4 h-4 mr-2" /> Filter</Button>
                                    </div>
                                </div>
                            </CardHeader>
                            <CardContent>
                                <Table>
                                    <TableHeader>
                                        <TableRow>
                                            <TableHead>Student</TableHead>
                                            <TableHead>Status</TableHead>
                                            <TableHead>Sent At</TableHead>
                                            <TableHead className="text-right">Score</TableHead>
                                            <TableHead className="text-right">Action</TableHead>
                                        </TableRow>
                                    </TableHeader>
                                    <TableBody>
                                        {filteredSubmissions.length > 0 ? (
                                            filteredSubmissions.map((sub) => (
                                                <TableRow key={sub.id}>
                                                    <TableCell className="font-medium">
                                                        <div className="flex items-center gap-2">
                                                            <div className="w-8 h-8 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-700 text-xs font-bold uppercase">
                                                                {sub.student?.first_name?.[0] || sub.student?.email?.[0] || "?"}
                                                            </div>
                                                            <div>
                                                                <div className="text-sm font-medium">
                                                                    {sub.student?.first_name ? `${sub.student.first_name} ${sub.student.last_name}` : "Student"}
                                                                </div>
                                                                <div className="text-xs text-gray-500">{sub.student?.email}</div>
                                                            </div>
                                                        </div>
                                                    </TableCell>
                                                    <TableCell>
                                                        <span className={`px-2 py-1 rounded-full text-xs font-medium border ${sub.is_graded ? "bg-green-50 text-green-700 border-green-200" :
                                                                "bg-amber-50 text-amber-700 border-amber-200"
                                                            }`}>
                                                            {sub.is_graded ? "Graded" : "To Grade"}
                                                        </span>
                                                    </TableCell>
                                                    <TableCell className="text-xs text-gray-500">
                                                        {sub.created_at ? new Date(sub.created_at).toLocaleDateString() : "-"}
                                                    </TableCell>
                                                    <TableCell className="text-right font-bold">
                                                        {sub.final_score !== null ? `${sub.final_score}%` : "-"}
                                                    </TableCell>
                                                    <TableCell className="text-right">
                                                        <Button size="sm" variant="outline" asChild>
                                                            <Link to={`/teacher/grading/submission/${sub.id}`}>
                                                                View
                                                            </Link>
                                                        </Button>
                                                    </TableCell>
                                                </TableRow>
                                            ))
                                        ) : (
                                            <TableRow>
                                                <TableCell colSpan={5} className="text-center py-6 text-gray-500">
                                                    No submissions found {searchTerm && "matching your search"}
                                                </TableCell>
                                            </TableRow>
                                        )}
                                    </TableBody>
                                </Table>
                            </CardContent>
                        </Card>
                    </TabsContent>

                    {/* --- TAB: ANALYTICS --- */}
                    <TabsContent value="analytics" className="min-h-[500px]">
                        <div className="flex flex-col items-center justify-center py-16 text-center border-2 border-dashed border-gray-200 rounded-xl bg-gray-50/50">
                            <BarChart3 className="w-12 h-12 text-gray-300 mb-4" />
                            <h3 className="text-lg font-semibold text-gray-900">Analytics Coming Soon</h3>
                            <p className="text-gray-500 max-w-sm mt-2">
                                Detailed insights, code similarity checking, and error heatmaps will appear here once enough data is collected.
                            </p>
                        </div>
                    </TabsContent>
                </Tabs>
            </motion.div>
        </TeacherLayout>
    );
}


