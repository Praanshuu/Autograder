import React from 'react';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../../ui/card";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, ReferenceLine } from 'recharts';
import { TrendingUp, TrendingDown, Minus } from 'lucide-react';

const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
        return (
            <div className="bg-white p-3 border rounded-lg shadow-lg">
                <p className="font-bold text-gray-900">{label}</p>
                <div className="flex items-center gap-2 mt-1">
                    <span className="text-sm text-gray-600">Score:</span>
                    <span className="text-sm font-bold text-indigo-600">{payload[0].value}%</span>
                </div>
                {payload[0].payload.average && (
                    <div className="flex items-center gap-2">
                        <span className="text-xs text-gray-400">Class Avg:</span>
                        <span className="text-xs font-medium text-gray-500">{payload[0].payload.average}%</span>
                    </div>
                )}
            </div>
        );
    }
    return null;
};

export default function LearningTrajectory({ data, studentName }) {
    // Calculate trend
    const sortedData = [...data].sort((a, b) => new Date(a.date) - new Date(b.date));
    const firstScore = sortedData[0]?.score || 0;
    const lastScore = sortedData[sortedData.length - 1]?.score || 0;
    const diff = lastScore - firstScore;

    let TrendIcon = Minus;
    let trendColor = "text-gray-500";
    let trendText = "Stable";

    if (diff > 5) {
        TrendIcon = TrendingUp;
        trendColor = "text-green-600";
        trendText = "Improving";
    } else if (diff < -5) {
        TrendIcon = TrendingDown;
        trendColor = "text-red-600";
        trendText = "Declining";
    }

    return (
        <Card>
            <CardHeader className="pb-2">
                <div className="flex items-center justify-between">
                    <div>
                        <CardTitle className="text-base font-semibold">Learning Trajectory</CardTitle>
                        <CardDescription>Performance over last 5 assignments</CardDescription>
                    </div>
                    <div className={`flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-medium bg-gray-50 border ${trendColor.replace('text', 'border')}`}>
                        <TrendIcon className={`w-3 h-3 ${trendColor}`} />
                        <span className={trendColor}>{trendText}</span>
                    </div>
                </div>
            </CardHeader>
            <CardContent>
                <div className="h-[200px] w-full mt-2">
                    <ResponsiveContainer width="100%" height="100%">
                        <LineChart data={sortedData} margin={{ top: 5, right: 5, bottom: 5, left: -20 }}>
                            <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f0f0f0" />
                            <XAxis
                                dataKey="title"
                                fontSize={10}
                                tickLine={false}
                                axisLine={false}
                                tickFormatter={(val) => val.split(' ')[0]} // Show only first word on X axis to save space
                            />
                            <YAxis
                                domain={[0, 100]}
                                fontSize={10}
                                tickLine={false}
                                axisLine={false}
                            />
                            <Tooltip content={<CustomTooltip />} />
                            <ReferenceLine y={70} stroke="#e2e8f0" strokeDasharray="5 5" label={{ value: 'Passing', fontSize: 10, fill: '#94a3b8', position: 'insideBottomRight' }} />

                            {/* Class Average Line (Faint) */}
                            <Line
                                type="monotone"
                                dataKey="average"
                                stroke="#cbd5e1"
                                strokeWidth={2}
                                dot={false}
                                strokeDasharray="4 4"
                                activeDot={false}
                            />

                            {/* Student Score Line */}
                            <Line
                                type="monotone"
                                dataKey="score"
                                stroke="#4f46e5"
                                strokeWidth={3}
                                dot={{ fill: '#4f46e5', strokeWidth: 2, r: 4, stroke: '#fff' }}
                                activeDot={{ r: 6, strokeWidth: 0 }}
                            />
                        </LineChart>
                    </ResponsiveContainer>
                </div>
            </CardContent>
        </Card>
    );
}
