import { useState } from "react";
import { Link, useParams } from "react-router-dom";
import {
    MoveLeft,
    BarChart3,
    Users,
    CheckCircle2,
    ArrowUpDown,
    Search,
    Filter,
    LineChart,
    Code2,
    ListChecks,
    ChevronRight,
    AlertTriangle,
    Target,
    XCircle // NEW
} from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

import TeacherLayout from "../../components/layout/TeacherLayout";
import { Button } from "../../components/ui/button";
import { Input } from "../../components/ui/input";
import { Card, CardContent, CardHeader, CardTitle, CardDescription, CardFooter } from "../../components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../../components/ui/tabs";
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "../../components/ui/table";

// Mock Data
import { MOCK_ASSIGNMENT, MOCK_SUBMISSIONS } from "../../mocks/assignments";

// Analytics Components
import PerformanceMatrix from "../../components/features/analytics/PerformanceMatrix";
import ErrorHeatmap from "../../components/features/analytics/ErrorHeatmap";
import CodeSimilarityMap from "../../components/features/analytics/CodeSimilarityMap";

import BoxPlotChart from "../../components/features/analytics/BoxPlotChart";
import ErrorWordCloud from "../../components/features/analytics/ErrorWordCloud";

// Mock Data for Box Plot
const MOCK_BOX_DATA = [
    { name: "Class", min: 45, q1: 68, median: 78, q3: 88, max: 98 }
];

export default function AssignmentDashboard() {
    const { id } = useParams();
    const [searchTerm, setSearchTerm] = useState("");
    const [filterStatus, setFilterStatus] = useState("All");

    // Analytics Navigation State
    const [selectedQuestion, setSelectedQuestion] = useState(null);
    const [selectedAnalyticsTag, setSelectedAnalyticsTag] = useState(null); // NEW: Filter from Word Cloud

    const filteredSubmissions = MOCK_SUBMISSIONS.filter(sub => {
        const matchesSearch = sub.studentName.toLowerCase().includes(searchTerm.toLowerCase());
        const matchesStatus = filterStatus === "All" || sub.status === filterStatus;
        const matchesTag = !selectedAnalyticsTag || (sub.feedbackTags && sub.feedbackTags.includes(selectedAnalyticsTag));
        return matchesSearch && matchesStatus && matchesTag;
    });

    // Filter submissions/data based on selected question (Mocking this logic)
    // In a real app, you'd fetch specific question analytics here
    const currentQuestion = selectedQuestion
        ? MOCK_ASSIGNMENT.questions.find(q => q.id === selectedQuestion)
        : null;

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
                                <h1 className="text-2xl font-bold text-gray-900">{MOCK_ASSIGNMENT.title}</h1>
                                <span className="px-2 py-0.5 rounded-full bg-green-100 text-green-700 text-xs font-medium border border-green-200">
                                    {MOCK_ASSIGNMENT.status}
                                </span>
                            </div>
                            <p className="text-gray-500 text-sm mt-1">Due {new Date(MOCK_ASSIGNMENT.dueDate).toLocaleDateString()}</p>
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
                                    <div className="text-2xl font-bold">{MOCK_ASSIGNMENT.stats.avgScore}%</div>
                                    <p className="text-xs text-muted-foreground">+2.5% from last assignment</p>
                                </CardContent>
                            </Card>
                            <Card>
                                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                    <CardTitle className="text-sm font-medium">Submitted</CardTitle>
                                    <Users className="h-4 w-4 text-muted-foreground" />
                                </CardHeader>
                                <CardContent>
                                    <div className="text-2xl font-bold">{MOCK_ASSIGNMENT.stats.submitted}/{MOCK_ASSIGNMENT.stats.totalStudents}</div>
                                    <p className="text-xs text-muted-foreground">84% completion rate</p>
                                </CardContent>
                            </Card>
                            <Card>
                                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                    <CardTitle className="text-sm font-medium">Graded</CardTitle>
                                    <CheckCircle2 className="h-4 w-4 text-muted-foreground" />
                                </CardHeader>
                                <CardContent>
                                    <div className="text-2xl font-bold">{MOCK_ASSIGNMENT.stats.graded}</div>
                                    <p className="text-xs text-muted-foreground">To grade: {MOCK_ASSIGNMENT.stats.submitted - MOCK_ASSIGNMENT.stats.graded}</p>
                                </CardContent>
                            </Card>
                            <Card>
                                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                    <CardTitle className="text-sm font-medium">Highest Score</CardTitle>
                                    <ArrowUpDown className="h-4 w-4 text-muted-foreground" />
                                </CardHeader>
                                <CardContent>
                                    <div className="text-2xl font-bold">{MOCK_ASSIGNMENT.stats.highestScore}</div>
                                    <p className="text-xs text-muted-foreground">Lowest: {MOCK_ASSIGNMENT.stats.lowestScore}</p>
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
                                        {selectedAnalyticsTag && (
                                            <Button
                                                variant="secondary"
                                                size="sm"
                                                onClick={() => setSelectedAnalyticsTag(null)}
                                                className="bg-orange-100 text-orange-700 hover:bg-orange-200 border border-orange-200"
                                            >
                                                Filtered by: {selectedAnalyticsTag} <XCircle className="w-4 h-4 ml-2" />
                                            </Button>
                                        )}
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
                                            <TableHead className="text-right">Auto-Grade</TableHead>
                                            <TableHead className="text-right">Action</TableHead>
                                        </TableRow>
                                    </TableHeader>
                                    <TableBody>
                                        {filteredSubmissions.map((sub) => (
                                            <TableRow key={sub.id}>
                                                <TableCell className="font-medium">
                                                    <div className="flex items-center gap-2">
                                                        <div className="w-8 h-8 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-700 text-xs font-bold">
                                                            {sub.avatar}
                                                        </div>
                                                        <div>
                                                            <div className="text-sm font-medium">{sub.studentName}</div>
                                                            <div className="text-xs text-gray-500">{sub.studentEmail}</div>
                                                        </div>
                                                    </div>
                                                </TableCell>
                                                <TableCell>
                                                    <span className={`px-2 py-1 rounded-full text-xs font-medium border ${sub.status === "Graded" ? "bg-green-50 text-green-700 border-green-200" :
                                                        sub.status === "To Grade" ? "bg-amber-50 text-amber-700 border-amber-200" :
                                                            "bg-gray-100 text-gray-700 border-gray-200"
                                                        }`}>
                                                        {sub.status}
                                                    </span>
                                                </TableCell>
                                                <TableCell className="text-xs text-gray-500">
                                                    {sub.submittedAt ? new Date(sub.submittedAt).toLocaleDateString() : "-"}
                                                </TableCell>
                                                <TableCell className="text-right font-bold">
                                                    {sub.autoGradeScore !== null ? `${sub.autoGradeScore}%` : "-"}
                                                </TableCell>
                                                <TableCell className="text-right">
                                                    <Button size="sm" variant="outline" asChild>
                                                        <Link to={`/teacher/grading/submission/${sub.id}`}>
                                                            View
                                                        </Link>
                                                    </Button>
                                                </TableCell>
                                            </TableRow>
                                        ))}
                                    </TableBody>
                                </Table>
                            </CardContent>
                        </Card>
                    </TabsContent>

                    {/* --- TAB: ANALYTICS --- */}
                    <TabsContent value="analytics" className="min-h-[500px]">
                        <AnimatePresence mode="wait">
                            {!selectedQuestion ? (
                                /* VIEW 1: Question Selector Grid */
                                <motion.div
                                    key="list"
                                    initial={{ opacity: 0, x: -20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    exit={{ opacity: 0, x: -20 }}
                                    className="space-y-6"
                                >
                                    <div>
                                        <h2 className="text-xl font-bold text-gray-900">Question Analysis</h2>
                                        <p className="text-gray-500">Select a question to view detailed performance metrics, UMAP clusters, and error heatmaps.</p>
                                    </div>

                                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                                        {MOCK_ASSIGNMENT.questions.map((q) => (
                                            <Card
                                                key={q.id}
                                                className="cursor-pointer hover:border-indigo-500 hover:shadow-md transition-all group relative overflow-hidden"
                                                onClick={() => setSelectedQuestion(q.id)}
                                            >
                                                <div className="absolute top-0 left-0 w-1 h-full bg-indigo-500 opacity-0 group-hover:opacity-100 transition-opacity" />
                                                <CardHeader className="pb-3">
                                                    <CardTitle className="flex justify-between items-start">
                                                        <span className="text-lg">{q.title}</span>
                                                        <ChevronRight className="w-5 h-5 text-gray-400 group-hover:text-indigo-500 group-hover:translate-x-1 transition-all" />
                                                    </CardTitle>
                                                    <CardDescription>
                                                        {q.testCases.length} Test Cases • {q.avgScore < 75 ? <span className="text-red-600 font-medium">Needs Attention</span> : "Healthy"}
                                                    </CardDescription>
                                                </CardHeader>
                                                <CardContent>
                                                    <div className="flex items-center justify-between text-sm">
                                                        <div className="flex items-center gap-2 text-gray-600">
                                                            <Target className="w-4 h-4" />
                                                            <span>Avg Score</span>
                                                        </div>
                                                        <span className={`font-bold ${q.avgScore < 75 ? "text-red-600" : "text-green-600"}`}>
                                                            {q.avgScore}%
                                                        </span>
                                                    </div>

                                                    {/* Mini failure indicator */}
                                                    {q.testCases.some(tc => tc.passRate < 60) && (
                                                        <div className="mt-4 p-2 bg-red-50 text-red-700 text-xs rounded border border-red-100 flex items-center gap-2">
                                                            <AlertTriangle className="w-3 h-3" />
                                                            High failure rate in edge cases
                                                        </div>
                                                    )}
                                                </CardContent>
                                            </Card>
                                        ))}
                                    </div>
                                </motion.div>
                            ) : (
                                /* VIEW 2: Detailed Question Analytics */
                                <motion.div
                                    key="detail"
                                    initial={{ opacity: 0, x: 20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    exit={{ opacity: 0, x: 20 }}
                                    className="space-y-6"
                                >
                                    <div className="flex items-center gap-4">
                                        <Button variant="outline" onClick={() => setSelectedQuestion(null)} className="gap-2">
                                            <MoveLeft className="w-4 h-4" />
                                            Back to Questions
                                        </Button>
                                        <div className="h-6 w-px bg-gray-200" />
                                        <h2 className="text-xl font-bold text-gray-900">{currentQuestion?.title} - Insights</h2>
                                    </div>

                                    {/* Detailed Charts */}
                                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                                        {/* Row 1: Left = Matrix, Right = Heatmap */}
                                        <PerformanceMatrix submissions={MOCK_SUBMISSIONS} />
                                        {/* Pass only the specific question to heatmap */}
                                        <ErrorHeatmap questions={[currentQuestion]} />
                                    </div>

                                    {/* New Advanced Analytics Row */}
                                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                                        <BoxPlotChart data={MOCK_BOX_DATA} />
                                        <ErrorWordCloud
                                            selectedTag={selectedAnalyticsTag}
                                            onSelectTag={setSelectedAnalyticsTag}
                                        />
                                    </div>

                                    {/* Row 2: UMAP full width */}
                                    <CodeSimilarityMap submissions={MOCK_SUBMISSIONS} />
                                </motion.div>
                            )}
                        </AnimatePresence>
                    </TabsContent>
                </Tabs>
            </motion.div>
        </TeacherLayout>
    );
}


