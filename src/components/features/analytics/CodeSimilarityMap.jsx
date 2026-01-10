import { ScatterChart, Scatter, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell, LabelList } from 'recharts';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../../ui/card";
import { MOCK_CLUSTERS } from "../../../mocks/assignments";

export default function CodeSimilarityMap({ submissions }) {
    // Merge submission data with cluster colors if possible, or just plot them directly
    const data = submissions.map(s => {
        const cluster = MOCK_CLUSTERS.find(c => c.name === s.approach) || {};
        return {
            x: s.umapX,
            y: s.umapY,
            name: s.studentName,
            approach: s.approach,
            color: cluster.color || "#94a3b8"
        };
    });

    return (
        <Card className="h-full">
            <CardHeader>
                <CardTitle>Approach Clusters (UMAP)</CardTitle>
                <CardDescription>Grouping students by solution strategy & logic.</CardDescription>
            </CardHeader>
            <CardContent className="h-[400px] relative">
                {/* Legend Overlay */}
                <div className="absolute top-0 right-6 bg-white/90 p-2 rounded border border-gray-100 z-10 text-xs space-y-1 shadow-sm">
                    {MOCK_CLUSTERS.map(c => (
                        <div key={c.name} className="flex items-center gap-2">
                            <div className="w-2 h-2 rounded-full" style={{ backgroundColor: c.color }} />
                            <span>{c.name}</span>
                        </div>
                    ))}
                </div>

                <ResponsiveContainer width="100%" height="100%">
                    <ScatterChart margin={{ top: 20, right: 20, bottom: 20, left: 20 }}>
                        <XAxis type="number" dataKey="x" hide domain={[0, 100]} />
                        <YAxis type="number" dataKey="y" hide domain={[0, 100]} />
                        <Tooltip cursor={false} content={({ active, payload }) => {
                            if (active && payload && payload.length) {
                                const data = payload[0].payload;
                                return (
                                    <div className="bg-white p-3 border rounded shadow-lg text-sm z-50">
                                        <p className="font-bold">{data.name}</p>
                                        <p className="text-gray-500 text-xs mb-1">{data.approach}</p>
                                        <div className="bg-gray-50 p-1 rounded font-mono text-[10px] text-gray-600 border border-gray-100">
                                            def solve(x)...
                                        </div>
                                    </div>
                                );
                            }
                            return null;
                        }} />
                        <Scatter name="Students" data={data}>
                            {data.map((entry, index) => (
                                <Cell key={`cell-${index}`} fill={entry.color} />
                            ))}
                        </Scatter>
                    </ScatterChart>
                </ResponsiveContainer>
            </CardContent>
        </Card>
    );
}
