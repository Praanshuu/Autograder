import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../../ui/card";
import { AlertCircle, Filter, X, MessageSquareWarning } from "lucide-react";
import { Button } from "../../ui/button";

// Mock Data representing aggregated strings from autograder logs
const MOCK_FEEDBACK_DATA = [
    { text: "Output Mismatch", value: 45, type: "error" },
    { text: "Infinite Loop", value: 38, type: "error" },
    { text: "Test Case 3 Failed", value: 30, type: "failure" },
    { text: "Memory Limit Exceeded", value: 25, type: "error" },
    { text: "Return Type Error", value: 20, type: "error" },
    { text: "Variable Not Initialized", value: 15, type: "warning" },
    { text: "Null Pointer", value: 12, type: "error" },
    { text: "Optimized Solution", value: 8, type: "success" },
    { text: "Syntax Error: missing ;", value: 18, type: "warning" },
    { text: "Index Out of Bounds", value: 22, type: "error" },
];

export default function ErrorWordCloud({ selectedTag, onSelectTag }) {
    // Controlled component: state moved to parent


    // Simple sizing logic based on value range (0 -> 50)
    const getFontSize = (value) => {
        // Map 0-50 to 12px-40px
        const minSize = 12;
        const maxSize = 36;
        const scale = (value / 50); // Normalized 0-1
        return minSize + (scale * (maxSize - minSize));
    };

    const getColor = (item) => {
        if (item.type === 'error') return "#ef4444"; // Red
        if (item.type === 'failure') return "#f97316"; // Orange
        if (item.type === 'warning') return "#eab308"; // Yellow
        return "#22c55e"; // Green/Success
    };

    return (
        <Card className="col-span-1 border-orange-100 bg-orange-50/10">
            <CardHeader>
                <CardTitle className="text-lg flex items-center justify-between">
                    <div className="flex items-center gap-2">
                        <MessageSquareWarning className="w-5 h-5 text-orange-500" />
                        <span>Feedback Analysis</span>
                    </div>
                    {selectedTag && (
                        <Button
                            variant="ghost"
                            size="sm"
                            className="h-6 px-2 text-xs text-orange-600 bg-orange-100 hover:bg-orange-200"
                            onClick={() => onSelectTag(null)}
                        >
                            {selectedTag} <X className="w-3 h-3 ml-1" />
                        </Button>
                    )}
                </CardTitle>
                <CardDescription>
                    Aggregated keywords from Autograder feedback logs.
                </CardDescription>
            </CardHeader>
            <CardContent>
                <div className="flex flex-wrap items-center justify-center gap-x-6 gap-y-3 p-4 min-h-[300px]">
                    {MOCK_FEEDBACK_DATA.map((item, i) => (
                        <span
                            key={i}
                            onClick={() => onSelectTag(selectedTag === item.text ? null : item.text)}
                            className={`cursor-pointer transition-all hover:scale-110 hover:underline decoration-2 underline-offset-4 ${selectedTag && selectedTag !== item.text ? "opacity-30 blur-[1px]" : "opacity-100"
                                }`}
                            style={{
                                fontSize: `${getFontSize(item.value)}px`,
                                color: getColor(item),
                                fontWeight: item.value > 25 ? 700 : 500,
                            }}
                        >
                            {item.text}
                        </span>
                    ))}
                </div>
                {selectedTag && (() => {
                    const selectedItem = MOCK_FEEDBACK_DATA.find(i => i.text === selectedTag);
                    return (
                        <div className="mt-4 p-3 bg-white border rounded-md text-sm text-gray-600 shadow-sm animate-in fade-in slide-in-from-top-2">
                            <span className="font-semibold text-gray-900">Drilldown:</span>
                            {selectedTag.includes("Test Case") ? " 30% of students failed this specific edge case. Check the test parameters." :
                                selectedTag.includes("Loop") ? " Suggests inefficient logic (O(n^2) or worse). Recommend reviewing time complexity." :
                                    ` ${selectedItem ? selectedItem.value : 0} students received this specific feedback string.`}
                        </div>
                    );
                })()}
            </CardContent>
        </Card>
    );
}
