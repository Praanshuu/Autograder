import { useState, useEffect } from "react";
import { Loader2, X, AlertCircle } from "lucide-react";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "../../ui/dialog";
import { classService } from "../../../services/classService";
import { Card, CardContent, CardHeader, CardTitle } from "../../ui/card";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from 'recharts';

export default function StudentAnalysisDrawer({ student, classId, isOpen, onClose }) {
    const [loading, setLoading] = useState(false);
    const [topicData, setTopicData] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        if (isOpen && student && classId) {
            fetchAnalysis();
        }
    }, [isOpen, student, classId]);

    const fetchAnalysis = async () => {
        try {
            setLoading(true);
            setError(null);
            const response = await classService.getStudentTopicGrades(classId, student.id);
            setTopicData(response.data || []);
        } catch (err) {
            console.error("Failed to fetch student analysis:", err);
            setError("Failed to load analysis data.");
        } finally {
            setLoading(false);
        }
    };

    if (!student) return null;

    return (
        <Dialog open={isOpen} onOpenChange={(open) => !open && onClose()}>
            <DialogContent className="sm:max-w-[600px] h-[90vh] overflow-y-auto flex flex-col p-0 gap-0">
                <DialogHeader className="p-6 pb-2 border-b bg-gray-50/50 sticky top-0 z-10 backdrop-blur-sm">
                    <div className="flex items-start justify-between">
                        <div className="flex items-center gap-3">
                            <div className="w-12 h-12 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-white text-lg font-bold shadow-md">
                                {student.name.charAt(0)}
                            </div>
                            <div>
                                <DialogTitle className="text-xl">{student.name}</DialogTitle>
                                <DialogDescription className="text-gray-500">{student.email}</DialogDescription>
                            </div>
                        </div>
                        {/* Close button is handled by Dialog primitives usually, but custom header implies custom close if needed */}
                    </div>
                </DialogHeader>

                <div className="flex-1 p-6 space-y-6">
                    {loading ? (
                        <div className="flex items-center justify-center h-48">
                            <Loader2 className="w-8 h-8 animate-spin text-indigo-600" />
                        </div>
                    ) : error ? (
                        <div className="p-4 bg-red-50 text-red-600 rounded-lg flex items-center gap-2">
                            <AlertCircle className="w-5 h-5" />
                            {error}
                        </div>
                    ) : (
                        <>
                            {/* Topic Performance Chart */}
                            <Card className="border-none shadow-sm bg-gray-50/50">
                                <CardHeader className="pb-2 flex flex-row items-center justify-between">
                                    <CardTitle className="text-sm font-medium uppercase tracking-wider text-gray-500">Topic Mastery</CardTitle>
                                    <div className="text-xs text-gray-400">Sorted by Score</div>
                                </CardHeader>
                                <CardContent>
                                    {topicData.length > 0 ? (
                                        <div style={{ height: `${Math.max(300, topicData.length * 60)}px`, minHeight: '300px' }}>
                                            <ResponsiveContainer width="100%" height="100%">
                                                <BarChart
                                                    data={[...topicData].sort((a, b) => b.score - a.score)}
                                                    layout="vertical"
                                                    margin={{ top: 20, right: 30, left: 60, bottom: 20 }}
                                                >
                                                    <CartesianGrid strokeDasharray="3 3" horizontal={true} vertical={false} stroke="#E5E7EB" />
                                                    <XAxis type="number" hide domain={[0, 100]} />
                                                    <YAxis
                                                        dataKey="topic"
                                                        type="category"
                                                        tick={{ fill: '#4B5563', fontSize: 13, fontWeight: 500 }}
                                                        width={180}
                                                        tickLine={false}
                                                        axisLine={false}
                                                        interval={0}
                                                    />
                                                    <Tooltip
                                                        cursor={{ fill: 'rgba(99, 102, 241, 0.1)' }}
                                                        contentStyle={{ borderRadius: '8px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)' }}
                                                    />
                                                    <Bar dataKey="score" radius={[0, 4, 4, 0]} barSize={24}>
                                                        {topicData.sort((a, b) => b.score - a.score).map((entry, index) => (
                                                            <Cell key={`cell-${index}`} fill={entry.score >= 80 ? '#10B981' : entry.score >= 50 ? '#F59E0B' : '#EF4444'} />
                                                        ))}
                                                    </Bar>
                                                </BarChart>
                                            </ResponsiveContainer>
                                        </div>
                                    ) : (
                                        <div className="flex flex-col items-center justify-center h-[300px] text-gray-400 text-sm">
                                            <p>No topic data available yet.</p>
                                            <p className="text-xs mt-1">Ensure questions are tagged.</p>
                                        </div>
                                    )}
                                </CardContent>
                            </Card>

                            {/* Recent Activity Placeholder */}
                            <div>
                                <h4 className="text-sm font-medium uppercase tracking-wider text-gray-500 mb-3">Recent Performance</h4>
                                <div className="space-y-3">
                                    {/* We can fetch real recent activity later. For now, static placeholder or empty state */}
                                    <div className="text-center py-8 bg-gray-50 rounded-lg border border-dashed border-gray-200 text-gray-400 text-sm">
                                        Detailed submission history coming soon.
                                    </div>
                                </div>
                            </div>
                        </>
                    )}
                </div>
            </DialogContent>
        </Dialog>
    );
}
