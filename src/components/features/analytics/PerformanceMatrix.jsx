import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, ReferenceLine, Label } from 'recharts';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../../ui/card";

export default function PerformanceMatrix({ submissions }) {
    // Filter out null scores for the chart
    const data = submissions
        .filter(s => s.final_score !== null && s.time_spent !== null)
        .map(s => ({
            x: s.time_spent,
            y: s.final_score,
            name: s.student?.first_name ? `${s.student.first_name} ${s.student.last_name || ''}` : `Student ${s.student_id}`,
            status: s.status
        }));

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
                                    <div className="bg-white p-3 border rounded shadow-lg text-sm">
                                        <p className="font-bold">{data.name}</p>
                                        <p>Score: <span className={data.y >= 70 ? "text-green-600" : "text-red-600"}>{data.y}%</span></p>
                                        <p>Time: {data.x} mins</p>
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
