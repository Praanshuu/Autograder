import { AlertTriangle, CheckCircle2, XCircle } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../../ui/card";

export default function ErrorHeatmap({ questions }) {
    if (!questions) return null;

    return (
        <Card className="h-full">
            <CardHeader>
                <CardTitle>Error Heatmap</CardTitle>
                <CardDescription>Failure rates by specific test cases/concepts</CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
                {questions.map((q) => (
                    <div key={q.id}>
                        <h4 className="font-semibold text-sm mb-3 flex items-center justify-between">
                            {q.title}
                            <span className="text-gray-500 text-xs font-normal">Avg: {q.avgScore}%</span>
                        </h4>
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                            {q.testCases.map((tc) => {
                                // Logic: >85% Green, 50-85% Yellow, <50% Red
                                let statusColor = "bg-green-100 text-green-700 border-green-200";
                                let barColor = "bg-green-500";
                                let icon = <CheckCircle2 className="w-4 h-4 text-green-600" />;

                                if (tc.passRate < 50) {
                                    statusColor = "bg-red-50 text-red-700 border-red-200";
                                    barColor = "bg-red-500";
                                    icon = <AlertTriangle className="w-4 h-4 text-red-600" />;
                                } else if (tc.passRate < 85) {
                                    statusColor = "bg-amber-50 text-amber-700 border-amber-200";
                                    barColor = "bg-amber-500";
                                    icon = <AlertTriangle className="w-4 h-4 text-amber-600" />;
                                }

                                return (
                                    <div
                                        key={tc.id}
                                        className="p-3 rounded-lg border flex flex-col gap-3 bg-white hover:shadow-md transition-all relative group"
                                    >
                                        <div className="flex justify-between items-start gap-2">
                                            <span
                                                className="text-sm font-medium leading-tight truncate"
                                                title={tc.name}
                                            >
                                                {tc.concept || tc.name}
                                            </span>
                                            {tc.passRate >= 85 ? (
                                                <CheckCircle2 className="w-4 h-4 text-green-600" />
                                            ) : (
                                                <AlertTriangle className={`w-4 h-4 ${tc.passRate < 50 ? "text-red-500" : "text-amber-500"}`} />
                                            )}
                                        </div>

                                        <div className="mt-auto">
                                            <div className="flex justify-between text-xs mb-1.5 opacity-90 font-medium text-gray-600">
                                                <span>{tc.total} Attempts</span>
                                                <span>{tc.passRate}% Pass</span>
                                            </div>

                                            {/* Segmented Progress Bar */}
                                            <div className="h-3 w-full bg-gray-100 rounded-full overflow-hidden flex">
                                                {/* Pass Segment */}
                                                <div
                                                    className="h-full bg-green-500"
                                                    style={{ width: `${tc.passRate}%` }}
                                                />

                                                {/* Error Segments (Top 3) */}
                                                {tc.errorStats && tc.errorStats.slice(0, 3).map((err, idx) => {
                                                    const width = (err.count / tc.total) * 100;
                                                    // Assign colors based on index or type
                                                    const colors = ["bg-red-500", "bg-orange-500", "bg-amber-500"];
                                                    const color = colors[idx] || "bg-gray-400";

                                                    return (
                                                        <div
                                                            key={err.type}
                                                            className={`h-full ${color} border-l border-white/50`}
                                                            style={{ width: `${width}%` }}
                                                        />
                                                    );
                                                })}

                                                {/* Remainder (Other Errors) */}
                                                {/* Calculated implicitly by remaining space if any, or we can explicit add if needed. 
                                                    For now, let's assume coverage is 100% of attempts (pass + errors). 
                                                */}
                                            </div>

                                            {/* Error Breakdown Mini-Badges */}
                                            {tc.errorStats && tc.errorStats.length > 0 && (
                                                <div className="mt-2 flex flex-wrap gap-1">
                                                    {tc.errorStats.slice(0, 2).map(err => (
                                                        <span key={err.type} className="text-[10px] px-1.5 py-0.5 bg-red-50 text-red-700 rounded border border-red-100 truncate max-w-[100px]">
                                                            {err.type} ({Math.round((err.count / tc.total) * 100)}%)
                                                        </span>
                                                    ))}
                                                    {tc.errorStats.length > 2 && (
                                                        <span className="text-[10px] px-1.5 py-0.5 bg-gray-50 text-gray-600 rounded border border-gray-200">
                                                            +{tc.errorStats.length - 2} more
                                                        </span>
                                                    )}
                                                </div>
                                            )}
                                        </div>

                                        {/* Tooltip for detailed breakdown */}
                                        <div className="absolute opacity-0 group-hover:opacity-100 bottom-full left-0 mb-2 w-full p-2 bg-gray-900 text-white text-xs rounded shadow-lg z-10 pointer-events-none transition-opacity">
                                            <div className="font-bold mb-1">{tc.name} Breakdown:</div>
                                            <div>Pass: {tc.passRate}%</div>
                                            {tc.errorStats && tc.errorStats.map(err => (
                                                <div key={err.type} className="flex justify-between">
                                                    <span>{err.type}:</span>
                                                    <span>{err.count} ({Math.round((err.count / tc.total) * 100)}%)</span>
                                                </div>
                                            ))}
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                ))}
            </CardContent>
        </Card>
    );
}
