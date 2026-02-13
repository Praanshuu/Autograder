import { AlertTriangle, CheckCircle2, Clock, Zap, Cpu } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../../ui/card";

export default function ErrorHeatmapV2({ questions }) {
    if (!questions) return null;

    return (
        <Card className="h-full border-indigo-100 shadow-sm">
            <CardHeader>
                <div className="flex items-center justify-between">
                    <div>
                        <CardTitle className="flex items-center gap-2">
                            Error & Performance Heatmap
                            <span className="px-2 py-0.5 rounded-full bg-indigo-100 text-indigo-700 text-xs font-medium border border-indigo-200">
                                V2
                            </span>
                        </CardTitle>
                        <CardDescription>Failure rates per test case</CardDescription>
                    </div>
                </div>
            </CardHeader>
            <CardContent className="space-y-8">
                {questions.map((q) => (
                    <div key={q.id} className="space-y-4">
                        <div className="flex items-center justify-between border-b pb-2">
                            <h4 className="font-semibold text-sm flex items-center gap-2">
                                {q.title}
                            </h4>
                            <div className="flex items-center gap-4 text-xs text-gray-500">
                                <span>Avg Score: {q.avgScore}%</span>
                            </div>
                        </div>

                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                            {q.testCases.map((tc) => {
                                // Status Logic
                                let statusColor = "text-green-600";
                                let barColor = "bg-green-500";
                                if (tc.passRate < 50) {
                                    statusColor = "text-red-600";
                                    barColor = "bg-red-500";
                                } else if (tc.passRate < 85) {
                                    statusColor = "text-amber-600";
                                    barColor = "bg-amber-500";
                                }

                                return (
                                    <div
                                        key={tc.id}
                                        className="p-4 rounded-xl border border-gray-100 bg-white hover:border-indigo-200 hover:shadow-md transition-all group relative overflow-hidden"
                                    >
                                        {/* Header */}
                                        <div className="flex justify-between items-start mb-3">
                                            <div className="flex flex-col">
                                                <span className="text-sm font-semibold text-gray-900 line-clamp-1" title={tc.name}>
                                                    {tc.concept || tc.name}
                                                </span>
                                                <span className="text-xs text-gray-500">
                                                    {tc.total} Attempts
                                                </span>
                                            </div>
                                            <div className={`font-bold text-lg ${statusColor}`}>
                                                {tc.passRate}%
                                            </div>
                                        </div>

                                        {/* Progress Bar */}
                                        <div className="h-2 w-full bg-gray-100 rounded-full overflow-hidden flex mb-3">
                                            <div
                                                className={`h-full ${barColor}`}
                                                style={{ width: `${tc.passRate}%` }}
                                            />
                                            {/* Error Segments */}
                                            {tc.errorStats && tc.errorStats.map((err, idx) => {
                                                const width = (err.count / tc.total) * 100;
                                                const colors = ["bg-red-500", "bg-orange-500", "bg-amber-500"];
                                                return (
                                                    <div
                                                        key={`err-${idx}`}
                                                        className={`h-full ${colors[idx % 3]} border-l border-white/50`}
                                                        style={{ width: `${width}%` }}
                                                    />
                                                );
                                            })}
                                        </div>

                                        {/* Performance Metric - REMOVED per user request */}
                                        <div className="flex items-center justify-between pt-2 border-t border-gray-50 mt-2">
                                            {/* Most Common Error Badge */}
                                            {tc.errorStats && tc.errorStats.length > 0 ? (
                                                <span className="text-[10px] px-1.5 py-0.5 bg-red-50 text-red-600 rounded-md border border-red-100 truncate max-w-[100px]">
                                                    {tc.errorStats[0].type}
                                                </span>
                                            ) : <span></span>}
                                        </div>

                                        {/* Tooltip */}
                                        <div className="absolute opacity-0 group-hover:opacity-100 bottom-full left-0 mb-2 w-full p-3 bg-gray-900 text-white text-xs rounded-lg shadow-xl z-20 pointer-events-none transition-opacity">
                                            <div className="font-bold mb-2 pb-1 border-b border-gray-700">{tc.name} Details</div>
                                            <div className="grid grid-cols-2 gap-x-4 gap-y-1">
                                                <span>Pass Rate:</span> <span className="text-right text-green-400">{tc.passRate}%</span>
                                                <span className="col-span-2 mt-1 font-semibold text-gray-400">Top Errors:</span>
                                                {tc.errorStats && tc.errorStats.slice(0, 3).map(err => (
                                                    <div key={err.type} className="contents">
                                                        <span className="truncate">{err.type}</span>
                                                        <span className="text-right text-red-300">{err.count}</span>
                                                    </div>
                                                ))}
                                            </div>
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                ))}
            </CardContent>
        </Card >
    );
}
