import { useState, useEffect } from "react";
import { Link, useParams } from "react-router-dom";
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
    Eye,
    LineChart,
    Loader2
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
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription } from "../../ui/dialog";
import { classService } from "../../../services/classService";

export default function MarksTab() {
    const { classId } = useParams();
    const [heatmapMode, setHeatmapMode] = useState(false);
    const [selectedStudent, setSelectedStudent] = useState(null);
    const [loading, setLoading] = useState(true);

    // State for Real Data
    const [gradebook, setGradebook] = useState({ assignments: [], roster: [] });

    useEffect(() => {
        const fetchGrades = async () => {
            if (!classId) return;
            try {
                setLoading(true);
                const response = await classService.getClassGrades(classId);
                setGradebook({
                    assignments: response.data.assignments || [],
                    roster: response.data.roster || []
                });
            } catch (error) {
                console.error("Failed to fetch grades:", error);
            } finally {
                setLoading(false);
            }
        };

        fetchGrades();
    }, [classId]);

    if (loading) {
        return <div className="flex justify-center py-10"><Loader2 className="w-8 h-8 animate-spin text-indigo-600" /></div>;
    }

    const { assignments, roster } = gradebook;

    // Calculate Class Averages per Assignment
    const assignmentAverages = assignments.map(assign => {
        const scores = roster.map(student => {
            const grade = student.grades[assign.id];
            return grade !== undefined ? grade : null;
        }).filter(score => score !== null);

        if (scores.length === 0) return 0;
        return Math.round(scores.reduce((a, b) => a + b, 0) / scores.length);
    });

    // Calculate Overall Student Averages
    const studentAverages = roster.map(student => {
        const scores = assignments.map(assign => {
            const grade = student.grades[assign.id];
            return grade !== undefined ? grade : null;
        }).filter(score => score !== null);

        if (scores.length === 0) return 0;
        return Math.round(scores.reduce((a, b) => a + b, 0) / scores.length);
    });

    // Class Stats
    const overallClassAverage = studentAverages.length > 0
        ? Math.round(studentAverages.reduce((a, b) => a + b, 0) / studentAverages.length)
        : 0;
    const highestAverage = studentAverages.length > 0 ? Math.max(...studentAverages) : 0;
    const submissionsCount = roster.reduce((acc, student) => acc + Object.keys(student.grades).length, 0);

    const getGradeColor = (score) => {
        if (score === undefined || score === null) return "text-gray-400";
        if (heatmapMode) {
            // Heatmap intensity
            if (score >= 90) return "bg-green-200 text-green-900";
            if (score >= 80) return "bg-green-100 text-green-800";
            if (score >= 70) return "bg-yellow-100 text-yellow-800";
            if (score >= 60) return "bg-orange-100 text-orange-800";
            return "bg-red-100 text-red-900";
        }
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
                            <p className="text-sm font-medium text-gray-500">Total Submissions</p>
                            <h3 className="text-2xl font-bold text-gray-900">{submissionsCount}</h3>
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
                                {assignments.map(assign => (
                                    <TableHead key={assign.id} className="text-center min-w-[140px] p-0">
                                        <div className="flex flex-col items-center justify-center h-full py-3 hover:bg-gray-100 transition-colors cursor-pointer group">
                                            <span className="font-semibold text-gray-900 group-hover:text-indigo-600 transition-colors">{assign.title}</span>
                                            <span className="text-[10px] text-gray-400 font-medium uppercase tracking-wide">
                                                {assign.points} Points
                                            </span>
                                        </div>
                                    </TableHead>
                                ))}
                            </TableRow>
                        </TableHeader>
                        <TableBody>
                            {roster.map((student, idx) => (
                                <TableRow key={student.id} className="group hover:bg-muted/30 transition-colors">
                                    <TableCell className="font-medium sticky left-0 bg-white group-hover:bg-gray-50 transition-colors z-10 border-r shadow-[2px_0_5px_-2px_rgba(0,0,0,0.1)] py-3">
                                        <div className="flex items-center gap-3 cursor-pointer hover:opacity-80 transition-opacity">
                                            <div className="w-9 h-9 rounded-full bg-gradient-to-br from-indigo-100 to-purple-100 flex items-center justify-center text-indigo-700 text-xs font-bold border border-indigo-200 shadow-sm relative">
                                                {student.name.charAt(0)}
                                            </div>
                                            <div>
                                                <div className="text-sm font-semibold text-gray-900 group-hover:text-indigo-600 transition-colors">{student.name}</div>
                                                <div className="text-xs text-gray-500">{student.email}</div>
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

                                    {assignments.map(assign => {
                                        const grade = student.grades[assign.id];
                                        return (
                                            <TableCell key={assign.id} className="p-0 text-center border-l border-gray-100 hover:border-indigo-300 relative">
                                                <div className={`flex items-center justify-center w-full h-16 ${getGradeColor(grade)}`}>
                                                    {grade !== undefined ? (
                                                        <div className="flex flex-col">
                                                            <span className="text-lg font-mono font-medium tracking-tight">
                                                                {((grade / 100) * assign.points).toFixed(1)}
                                                            </span>
                                                            {!heatmapMode && (
                                                                <span className="text-[10px] text-gray-400 font-normal">
                                                                    /{assign.points}
                                                                </span>
                                                            )}
                                                        </div>
                                                    ) : (
                                                        <span className="text-gray-300">-</span>
                                                    )}
                                                </div>
                                            </TableCell>
                                        );
                                    })}
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </div>
            </div>
        </div>
    );
}

