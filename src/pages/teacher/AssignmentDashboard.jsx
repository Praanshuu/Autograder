import { useState } from "react";
import { Link, useParams } from "react-router-dom";
import {
    MoveLeft,
    BarChart3,
    Users,
    CheckCircle2,
    Clock,
    Search,
    Filter,
    ArrowUpDown
} from "lucide-react";
import { motion } from "framer-motion";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from 'recharts';

import TeacherLayout from "../../components/layout/TeacherLayout";
import { Button } from "../../components/ui/button";
import { Input } from "../../components/ui/input";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../../components/ui/card";
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "../../components/ui/table";
import { MOCK_ASSIGNMENT, MOCK_SUBMISSIONS } from "../../mocks/assignments";

// Simple chart data derived from mock
const CHART_DATA = [
    { range: '0-59', count: 2 },
    { range: '60-69', count: 3 },
    { range: '70-79', count: 8 },
    { range: '80-89', count: 12 },
    { range: '90-100', count: 13 },
];

export default function AssignmentDashboard() {
    const { id } = useParams();
    const [searchTerm, setSearchTerm] = useState("");

    // In a real app, filters would be state-driven
    const [filterStatus, setFilterStatus] = useState("All");

    const filteredSubmissions = MOCK_SUBMISSIONS.filter(sub =>
        sub.studentName.toLowerCase().includes(searchTerm.toLowerCase()) &&
        (filterStatus === "All" || sub.status === filterStatus)
    );

    return (
        <TeacherLayout>
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="space-y-8"
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

                {/* Analytics Section */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
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

                <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    {/* Grade Distribution Chart (Simple) */}
                    <Card className="lg:col-span-1">
                        <CardHeader>
                            <CardTitle>Grade Distribution</CardTitle>
                            <CardDescription>Overall performance overview</CardDescription>
                        </CardHeader>
                        <CardContent className="h-[250px] w-full">
                            <ResponsiveContainer width="100%" height="100%">
                                <BarChart data={CHART_DATA}>
                                    <XAxis dataKey="range" fontSize={12} tickLine={false} axisLine={false} />
                                    <YAxis fontSize={12} tickLine={false} axisLine={false} tickFormatter={(value) => `${value}`} />
                                    <Tooltip
                                        cursor={{ fill: 'transparent' }}
                                        contentStyle={{ borderRadius: '8px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)' }}
                                    />
                                    <Bar dataKey="count" radius={[4, 4, 0, 0]}>
                                        {CHART_DATA.map((entry, index) => (
                                            <Cell key={`cell-${index}`} fill={index > 2 ? '#4f46e5' : '#94a3b8'} />
                                        ))}
                                    </Bar>
                                </BarChart>
                            </ResponsiveContainer>
                        </CardContent>
                    </Card>

                    {/* Submissions Table */}
                    <Card className="lg:col-span-2">
                        <CardHeader>
                            <CardTitle>Submissions</CardTitle>
                            <CardDescription>Manage student submissions and grades</CardDescription>

                            <div className="flex items-center gap-2 mt-4">
                                <div className="relative flex-1">
                                    <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-gray-400" />
                                    <Input
                                        placeholder="Search student..."
                                        className="pl-9"
                                        value={searchTerm}
                                        onChange={(e) => setSearchTerm(e.target.value)}
                                    />
                                </div>
                                <Button variant="outline" className="gap-2">
                                    <Filter className="w-4 h-4" />
                                    Filter
                                </Button>
                            </div>
                        </CardHeader>
                        <CardContent>
                            <Table>
                                <TableHeader>
                                    <TableRow>
                                        <TableHead>Student</TableHead>
                                        <TableHead>Status</TableHead>
                                        <TableHead>Submitted</TableHead>
                                        <TableHead className="text-right">Auto-Grade</TableHead>
                                        <TableHead className="text-right">Final</TableHead>
                                        <TableHead className="text-right">Action</TableHead>
                                    </TableRow>
                                </TableHeader>
                                <TableBody>
                                    {filteredSubmissions.map((sub) => (
                                        <TableRow key={sub.id} className="group">
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
                                                            sub.status === "Late" ? "bg-orange-50 text-orange-700 border-orange-200" :
                                                                "bg-gray-100 text-gray-700 border-gray-200"
                                                    }`}>
                                                    {sub.status}
                                                </span>
                                            </TableCell>
                                            <TableCell className="text-gray-500 text-xs">
                                                {sub.submittedAt ? new Date(sub.submittedAt).toLocaleString() : "-"}
                                            </TableCell>
                                            <TableCell className="text-right font-mono text-gray-600">
                                                {sub.autoGradeScore !== null ? `${sub.autoGradeScore}%` : "-"}
                                            </TableCell>
                                            <TableCell className="text-right font-bold">
                                                {sub.finalScore !== null ? `${sub.finalScore}%` : "-"}
                                            </TableCell>
                                            <TableCell className="text-right">
                                                <Button size="sm" variant={sub.status === "To Grade" ? "default" : "outline"} asChild>
                                                    <Link to={`/teacher/grading/submission/${sub.id}`}>
                                                        {sub.status === "To Grade" ? "Grade" : "Review"}
                                                    </Link>
                                                </Button>
                                            </TableCell>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        </CardContent>
                    </Card>
                </div>
            </motion.div>
        </TeacherLayout>
    );
}
