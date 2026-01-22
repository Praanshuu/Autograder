import React from 'react';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../../ui/card";
import { Info } from "lucide-react";

/**
 * A specialized Box Plot component for Grade Distributions (0-100).
 * Implemented with pure SVG to avoid Recharts custom shape complexities.
 */
export default function BoxPlotChart({ data }) {
    // Expect data format: [{ name: "Class", min: 45, q1: 68, median: 78, q3: 88, max: 98 }]
    // We only take the first item since it's a single distribution summary for now.
    const stats = data[0];

    if (!stats) return null;

    // Canvas dimensions
    const width = 200;
    const height = 300;
    const padding = 20;
    const chartHeight = height - (padding * 2);

    // Y-Axis mapping: 0 (bottom) to 100 (top)
    // SVG Y: 0 is top, height is bottom.
    // Formula: y = height - (value / 100 * height) + padding
    const getY = (val) => {
        return (chartHeight - ((val / 100) * chartHeight)) + padding;
    };

    const yMin = getY(stats.min);
    const yQ1 = getY(stats.q1);
    const yMedian = getY(stats.median);
    const yQ3 = getY(stats.q3);
    const yMax = getY(stats.max);

    const centerX = width / 2;
    const boxWidth = 80;

    return (
        <Card className="col-span-1 border-indigo-100 shadow-sm">
            <CardHeader className="pb-2">
                <div className="flex items-center justify-between">
                    <div>
                        <CardTitle className="text-lg flex items-center gap-2">
                            Grade Distribution
                            <Info className="w-4 h-4 text-gray-400 cursor-help" title="Displays whiskers (Min/Max), Box (IQR), and Median line." />
                        </CardTitle>
                        <CardDescription>Class performance spread (0-100)</CardDescription>
                    </div>
                </div>
            </CardHeader>
            <CardContent className="flex justify-center pb-6">
                <div className="relative group">
                    <svg width={width} height={height} className="overflow-visible">
                        {/* Grid Lines (0, 25, 50, 75, 100) */}
                        {[0, 25, 50, 75, 100].map((tick) => (
                            <g key={tick}>
                                <line
                                    x1={0} y1={getY(tick)}
                                    x2={width} y2={getY(tick)}
                                    stroke="#e5e7eb"
                                    strokeDasharray="4 4"
                                />
                                <text x={0} y={getY(tick) + 4} fontSize="10" fill="#9ca3af" textAnchor="end" dx="-4">
                                    {tick}
                                </text>
                            </g>
                        ))}

                        {/* --- THE BOX PLOT --- */}

                        {/* Main Vertical Line (Whisker to Whisker) */}
                        <line x1={centerX} y1={yMin} x2={centerX} y2={yMax} stroke="#374151" strokeWidth={2} />

                        {/* Bottom Whisker (Min) */}
                        <line
                            x1={centerX - 20} y1={yMin}
                            x2={centerX + 20} y2={yMin}
                            stroke="#374151" strokeWidth={2}
                        />
                        <text x={centerX + 30} y={yMin + 4} fontSize="12" fill="#374151" fontWeight="bold">Min: {stats.min}</text>

                        {/* Top Whisker (Max) */}
                        <line
                            x1={centerX - 20} y1={yMax}
                            x2={centerX + 20} y2={yMax}
                            stroke="#374151" strokeWidth={2}
                        />
                        <text x={centerX + 30} y={yMax + 4} fontSize="12" fill="#374151" fontWeight="bold">Max: {stats.max}</text>

                        {/* The Box (Interquartile Range) */}
                        <rect
                            x={centerX - boxWidth / 2}
                            y={yQ3}
                            width={boxWidth}
                            height={yQ1 - yQ3}
                            fill="#818cf8"
                            stroke="#4f46e5"
                            strokeWidth={2}
                            rx={4}
                            className="transition-all hover:opacity-80 cursor-pointer"
                        />

                        {/* Median Line */}
                        <line
                            x1={centerX - boxWidth / 2} y1={yMedian}
                            x2={centerX + boxWidth / 2} y2={yMedian}
                            stroke="#111827"
                            strokeWidth={3}
                        />
                        <text x={centerX - boxWidth / 2 - 10} y={yMedian + 4} fontSize="12" fill="#111827" fontWeight="bold" textAnchor="end">
                            Median: {stats.median}
                        </text>

                    </svg>

                    {/* Hover Tooltip Overlay (Simple Implementation) */}
                    <div className="absolute inset-0 bg-transparent flex items-center justify-center opacity-0 group-hover:opacity-100 pointer-events-none transition-opacity">
                        <div className="bg-white/90 backdrop-blur px-3 py-2 rounded shadow-lg border text-sm transform translate-y-12">
                            <span className="font-bold text-indigo-600">IQR: {stats.q3 - stats.q1} pts</span>
                        </div>
                    </div>
                </div>
            </CardContent>
        </Card>
    );
}
