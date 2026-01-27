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
                                        className={`p-3 rounded-lg border flex flex-col gap-3 ${statusColor} transition-all hover:shadow-sm`}
                                    >
                                        <div className="flex justify-between items-start gap-2">
                                            <span
                                                className="text-sm font-medium leading-tight truncate"
                                                title={tc.name} // Show full name on hover
                                            >
                                                {tc.concept || tc.name}
                                            </span>
                                            {icon}
                                        </div>

                                        <div className="mt-auto">
                                            <div className="flex justify-between text-xs mb-1.5 opacity-90 font-medium">
                                                <span>Success Rate</span>
                                                <span>{tc.passRate}%</span>
                                            </div>
                                            {/* Progress Bar */}
                                            <div className="h-2 w-full bg-white/50 rounded-full overflow-hidden">
                                                <div
                                                    className={`h-full rounded-full ${barColor}`}
                                                    style={{ width: `${tc.passRate}%` }}
                                                />
                                            </div>
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
