import { useState } from "react";
import { Link } from "react-router-dom";
import {
    Search,
    Download,
    Filter,
    ArrowUpDown,
    CheckCircle2,
    XCircle,
    AlertCircle,
    TrendingUp,
    Trophy,
    TrendingDown,
    Eye
} from "lucide-react";
import { Button } from "../../ui/button";
import { Input } from "../../ui/input";
import { Switch } from "../../ui/switch";
import { Label } from "../../ui/label";
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "../../ui/table";
import { Card, CardContent } from "../../ui/card";
import { GRADEBOOK_DATA } from "../../../mocks/gradebook";

export default function MarksTab() {
    const [heatmapMode, setHeatmapMode] = useState(false);

    // Calculate Class Averages per Assignment
    const assignmentAverages = GRADEBOOK_DATA.assignments.map(assign => {
        const scores = GRADEBOOK_DATA.students.map(student => {
            const grade = GRADEBOOK_DATA.grades[`${student.id}-${assign.id}`];
            return grade?.score || 0;
        }).filter(score => score !== null);

        if (scores.length === 0) return 0;
        return Math.round(scores.reduce((a, b) => a + b, 0) / scores.length);
    });

    // Calculate Overall Student Averages
    const studentAverages = GRADEBOOK_DATA.students.map(student => {
        const scores = GRADEBOOK_DATA.assignments.map(assign => {
            const grade = GRADEBOOK_DATA.grades[`${student.id}-${assign.id}`];
            return grade?.score || 0;
        });
        return Math.round(scores.reduce((a, b) => a + b, 0) / scores.length);
    });

    // Class Stats
    const overallClassAverage = Math.round(studentAverages.reduce((a, b) => a + b, 0) / studentAverages.length);
    const highestAverage = Math.max(...studentAverages);

    const getGradeColor = (score, status) => {
        if (heatmapMode && score !== null && typeof score === 'number') {
            // Heatmap intensity
            if (score >= 90) return "bg-green-200 text-green-900";
            if (score >= 80) return "bg-green-100 text-green-800";
            if (score >= 70) return "bg-yellow-100 text-yellow-800";
            if (score >= 60) return "bg-orange-100 text-orange-800";
            return "bg-red-100 text-red-900";
        }

        if (status === "Missing") return "bg-red-50 text-red-700";
        if (status === "Late") return "bg-amber-50 text-amber-700";
        if (status === "To Grade") return "bg-blue-50 text-blue-700";
        if (score >= 90) return "text-green-700 font-bold bg-green-50/50";
        if (score >= 70) return "text-gray-900";
        if (score < 60) return "text-red-600 font-bold bg-red-50/50";
        return "text-gray-700";
    };

    return (
        <div className="space-y-6">
            {/* Summary Stats Cards */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <Card className="shadow-sm border-l-4 border-indigo-500">
                    <CardContent className="p-4 flex items-center justify-between">
                        <div>
                            <p className="text-sm font-medium text-gray-500">Class Overall Avg</p>
                            <h3 className="text-2xl font-bold text-gray-900">{overallClassAverage}%</h3>
                        </div>
                        <div className="p-2 bg-indigo-50 rounded-full">
                            <TrendingUp className="w-5 h-5 text-indigo-600" />
                        </div>
                    </CardContent>
                </Card>
                <Card className="shadow-sm border-l-4 border-green-500">
                    <CardContent className="p-4 flex items-center justify-between">
                        <div>
                            <p className="text-sm font-medium text-gray-500">Highest Avg</p>
                            <h3 className="text-2xl font-bold text-gray-900">{highestAverage}%</h3>
                        </div>
                        <div className="p-2 bg-green-50 rounded-full">
                            <Trophy className="w-5 h-5 text-green-600" />
                        </div>
                    </CardContent>
                </Card>
                <Card className="shadow-sm border-l-4 border-amber-500">
                    <CardContent className="p-4 flex items-center justify-between">
                        <div>
                            <p className="text-sm font-medium text-gray-500">Submissions Needed</p>
                            <h3 className="text-2xl font-bold text-gray-900">12</h3>
                        </div>
                        <div className="p-2 bg-amber-50 rounded-full">
                            <AlertCircle className="w-5 h-5 text-amber-600" />
                        </div>
                    </CardContent>
                </Card>
            </div>

            {/* Toolbar */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div className="flex items-center gap-2 max-w-sm w-full">
                    <div className="relative flex-1">
                        <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-gray-400" />
                        <Input
                            placeholder="Search students..."
                            className="pl-9"
                        />
                    </div>
                    <Button variant="outline" size="icon">
                        <Filter className="w-4 h-4" />
                    </Button>
                </div>

                <div className="flex items-center gap-3">
                    <div className="flex items-center space-x-2 bg-white px-3 py-2 rounded-md border shadow-sm">
                        <Switch id="heatmap-mode" checked={heatmapMode} onCheckedChange={setHeatmapMode} />
                        <Label htmlFor="heatmap-mode" className="text-sm font-medium text-gray-700 cursor-pointer flex items-center gap-2">
                            <Eye className="w-4 h-4" /> Heatmap
                        </Label>
                    </div>
                    <Button variant="outline" className="gap-2">
                        <Download className="w-4 h-4" />
                        <span className="hidden sm:inline">Export CSV</span>
                    </Button>
                </div>
            </div>

            {/* Spreadsheet */}
            <div className="border rounded-xl overflow-hidden bg-white shadow-md">
                <div className="overflow-x-auto">
                    <Table>
                        <TableHeader>
                            <TableRow className="bg-gray-50/80 hover:bg-gray-50/80 border-b border-gray-200">
                                <TableHead className="w-[200px] font-bold text-gray-700 sticky left-0 bg-gray-50 z-20 shadow-[2px_0_5px_-2px_rgba(0,0,0,0.1)]">Student Name</TableHead>
                                <TableHead className="w-[100px] text-center font-bold text-gray-700 bg-gray-50/50">Overall</TableHead>
                                {GRADEBOOK_DATA.assignments.map(assign => (
                                    <TableHead key={assign.id} className="text-center min-w-[140px] p-0">
                                        <div className="flex flex-col items-center justify-center h-full py-3 hover:bg-gray-100 transition-colors cursor-pointer group">
                                            <span className="font-semibold text-gray-900 group-hover:text-indigo-600 transition-colors">{assign.title}</span>
                                            <span className="text-[10px] text-gray-400 font-medium uppercase tracking-wide">
                                                {assign.totalPoints} Points
                                            </span>
                                        </div>
                                    </TableHead>
                                ))}
                            </TableRow>
                        </TableHeader>
                        <TableBody>
                            {GRADEBOOK_DATA.students.map((student, idx) => (
                                <TableRow key={student.id} className="group hover:bg-muted/30 transition-colors">
                                    <TableCell className="font-medium sticky left-0 bg-white group-hover:bg-gray-50 transition-colors z-10 border-r shadow-[2px_0_5px_-2px_rgba(0,0,0,0.1)] py-3">
                                        <div className="flex items-center gap-3">
                                            <div className="w-9 h-9 rounded-full bg-gradient-to-br from-indigo-100 to-purple-100 flex items-center justify-center text-indigo-700 text-xs font-bold border border-indigo-200 shadow-sm">
                                                {student.avatar}
                                            </div>
                                            <div>
                                                <div className="text-sm font-semibold text-gray-900">{student.name}</div>
                                                <div className="text-xs text-gray-500">ID: {student.id.toUpperCase()}</div>
                                            </div>
                                        </div>
                                    </TableCell>
                                    <TableCell className="text-center bg-gray-50/30">
                                        <span className={`inline-flex items-center justify-center w-12 h-8 rounded-md font-bold text-sm border ${studentAverages[idx] >= 90 ? "bg-green-100 text-green-700 border-green-200" :
                                                studentAverages[idx] < 60 ? "bg-red-100 text-red-700 border-red-200" :
                                                    "bg-white text-gray-900 border-gray-200"
                                            }`}>
                                            {studentAverages[idx]}%
                                        </span>
                                    </TableCell>

                                    {GRADEBOOK_DATA.assignments.map(assign => {
                                        const grade = GRADEBOOK_DATA.grades[`${student.id}-${assign.id}`];
                                        if (!grade) {
                                            return <TableCell key={assign.id} className="text-center bg-gray-50/20 p-0" />;
                                        }

                                        return (
                                            <TableCell key={assign.id} className="p-0 text-center border-l border-gray-100 hover:border-indigo-300 relative">
                                                {grade.submissionId ? (
                                                    <Link
                                                        to={`/teacher/grading/submission/${grade.submissionId}`}
                                                        className={`flex items-center justify-center w-full h-16 hover:brightness-95 transition-all ${getGradeColor(grade.score, grade.status)}`}
                                                    >
                                                        {grade.status === "To Grade" ? (
                                                            <div className="flex items-center gap-1.5 px-3 py-1.5 bg-white border border-blue-200 rounded-full shadow-sm">
                                                                <div className="w-2 h-2 bg-blue-500 rounded-full animate-pulse" />
                                                                <span className="text-xs font-bold text-blue-700">Grade</span>
                                                            </div>
                                                        ) : grade.status === "Missing" ? (
                                                            <div className="flex flex-col items-center text-red-400 opacity-70">
                                                                <XCircle className="w-5 h-5" />
                                                            </div>
                                                        ) : (
                                                            <div className="flex flex-col items-center">
                                                                <span className="text-lg font-mono font-medium tracking-tight">{grade.score}</span>
                                                                {grade.status === "Late" && !heatmapMode && <span className="text-[10px] font-bold uppercase tracking-wider text-amber-600 mt-0.5">Late</span>}
                                                            </div>
                                                        )}
                                                    </Link>
                                                ) : (
                                                    <div className={`flex items-center justify-center w-full h-16 ${getGradeColor(0, grade.status)}`}>
                                                        <div className="flex flex-col items-center text-red-300">
                                                            <XCircle className="w-5 h-5" />
                                                        </div>
                                                    </div>
                                                )}
                                            </TableCell>
                                        );
                                    })}
                                </TableRow>
                            ))}

                            {/* Class Averages Row */}
                            <TableRow className="bg-gray-50 border-t-2 border-gray-200">
                                <TableCell className="font-bold text-gray-500 sticky left-0 bg-gray-50 z-20 border-r shadow-[2px_0_5px_-2px_rgba(0,0,0,0.1)]">
                                    <span className="px-2">Class Average</span>
                                </TableCell>
                                <TableCell className="text-center font-bold text-gray-500">-</TableCell>
                                {assignmentAverages.map((avg, i) => (
                                    <TableCell key={i} className="text-center py-4">
                                        <div className="flex flex-col items-center gap-1">
                                            <span className={`text-sm font-bold px-2 py-0.5 rounded ${avg >= 80 ? 'bg-green-100 text-green-800' : 'bg-gray-200 text-gray-700'}`}>
                                                {avg}%
                                            </span>
                                        </div>
                                    </TableCell>
                                ))}
                            </TableRow>
                        </TableBody>
                    </Table>
                </div>
            </div>
        </div>
    );
}
