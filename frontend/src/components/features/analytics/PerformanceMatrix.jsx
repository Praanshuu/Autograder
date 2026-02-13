import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, ReferenceLine, Label } from 'recharts';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../../ui/card";

export default function PerformanceMatrix({ submissions }) {
    // 1. Group by student to find "best" submission per student
    const studentBestSub = {};

    submissions.forEach(sub => {
        if (sub.final_score === null || sub.time_spent === null) return;

        const studentId = sub.student_id || sub.student?.id;
        if (!studentId) return;

        const currentBest = studentBestSub[studentId];

        if (!currentBest) {
            studentBestSub[studentId] = sub;
            return;
        }

        // Priority Logic: Graded > Submitted > Others
        const statusPriority = { 'graded': 3, 'submitted': 2, 'in_progress': 1 };
        const newPriority = statusPriority[sub.status] || 0;
        const oldPriority = statusPriority[currentBest.status] || 0;

        if (newPriority > oldPriority) {
            studentBestSub[studentId] = sub;
        } else if (newPriority === oldPriority) {
            // Break tie with higher score
            if (sub.final_score > currentBest.final_score) {
                studentBestSub[studentId] = sub;
            }
        }
    });

    const data = Object.values(studentBestSub).map(s => {
        const student = s.student || {};
        const fullName = student.first_name
            ? `${student.first_name} ${student.last_name || ''}`.trim()
            : null;

        return {
            x: s.time_spent,
            y: Math.round(s.final_score),
            name: fullName || s.student_username || student.username || `Student`,
            email: student.email || '',
            studentId: s.student_id || student.id || student.username,
            status: s.status,
            original: s
        };
    });

    return (
        <Card className="h-full">
            <CardHeader>
                <CardTitle>Performance Matrix (Effort vs. Mastery)</CardTitle>
                <CardDescription>Identify students who are struggling (High Effort, Low Score)</CardDescription>
            </CardHeader>
            <CardContent className="h-[350px]">
                <ResponsiveContainer width="100%" height="100%">
                    <ScatterChart margin={{ top: 20, right: 20, bottom: 20, left: 20 }}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis type="number" dataKey="x" name="Time Spent" unit=" min">
                            <Label value="Time Spent (Minutes)" offset={-10} position="insideBottom" />
                        </XAxis>
                        <YAxis type="number" dataKey="y" name="Score" unit="%">
                            <Label value="Score" angle={-90} position="insideLeft" />
                        </YAxis>
                        <Tooltip cursor={{ strokeDasharray: '3 3' }} content={({ active, payload }) => {
                            if (active && payload && payload.length) {
                                const data = payload[0].payload;
                                return (
                                    <div className="bg-white p-3 border rounded shadow-lg text-sm z-50">
                                        <p className="font-bold text-gray-900">{data.name}</p>
                                        <p className="text-xs text-gray-500 mb-2">{data.email} {data.studentId && `(${data.studentId})`}</p>
                                        <div className="space-y-1">
                                            <p className="flex justify-between gap-4">
                                                <span className="text-gray-600">Score:</span>
                                                <span className={`font-semibold ${data.y >= 70 ? "text-green-600" : "text-red-600"}`}>{data.y}%</span>
                                            </p>
                                            <p className="flex justify-between gap-4">
                                                <span className="text-gray-600">Time:</span>
                                                <span className="font-medium">{data.x} mins</span>
                                            </p>
                                        </div>
                                    </div>
                                );
                            }
                            return null;
                        }} />

                        {/* Defined Quadrants */}
                        <ReferenceLine x={30} stroke="#9ca3af" strokeDasharray="5 5" />
                        <ReferenceLine y={70} stroke="#9ca3af" strokeDasharray="5 5" />

                        {/* Quadrant Labels (Simplified placement) */}
                        <ReferenceLine y={90} label="High Performers" stroke="none" />
                        <ReferenceLine y={20} label="Needs Intervention" stroke="none" />

                        <Scatter name="Students" data={data} fill="#4f46e5" />
                    </ScatterChart>
                </ResponsiveContainer>
            </CardContent>
        </Card>
    );
}
