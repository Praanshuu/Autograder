import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../../ui/card";
import { AlertCircle, Filter, X, MessageSquareWarning } from "lucide-react";
import { Button } from "../../ui/button";

export default function ErrorWordCloud({ data = [], selectedTag, onSelectTag }) {
    if (!data || data.length === 0) {
        return (
            <Card className="col-span-1 border-dashed border-gray-200 bg-gray-50 h-full flex flex-col items-center justify-center p-6 text-center text-gray-500">
                <MessageSquareWarning className="w-8 h-8 mb-2 opacity-20" />
                <p>No feedback tags found for this assignment yet.</p>
            </Card>
        );
    }

    // Simple sizing logic based on value range
    const maxValue = Math.max(...data.map(d => d.value), 1);

    const getFontSize = (value) => {
        // Map 0-max to 12px-36px
        const minSize = 12;
        const maxSize = 32;
        const scale = (value / maxValue);
        return minSize + (scale * (maxSize - minSize));
    };

    const getColor = (item) => {
        // Basic mapping based on keyword heuristics if type isn't explicit
        const text = item.text.toLowerCase();
        if (text.includes('error') || text.includes('failed') || text.includes('exception')) return "#ef4444"; // Red
        if (text.includes('optimization') || text.includes('clean') || text.includes('perfect')) return "#22c55e"; // Green
        if (text.includes('warning') || text.includes('redundant')) return "#eab308"; // Yellow
        return "#f97316"; // Orange default
    };

    return (
        <Card className="col-span-1 border-orange-100 bg-orange-50/10 h-full">
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
                    Frequency of automated feedback tags.
                </CardDescription>
            </CardHeader>
            <CardContent>
                <div className="flex flex-wrap items-center justify-center gap-x-4 gap-y-2 p-4">
                    {data.map((item, i) => (
                        <span
                            key={i}
                            onClick={() => onSelectTag(selectedTag === item.text ? null : item.text)}
                            className={`cursor-pointer transition-all hover:scale-105 hover:underline decoration-2 underline-offset-4 ${selectedTag && selectedTag !== item.text ? "opacity-30 blur-[1px]" : "opacity-100"
                                }`}
                            style={{
                                fontSize: `${getFontSize(item.value)}px`,
                                color: getColor(item),
                                fontWeight: item.value > (maxValue / 2) ? 700 : 500,
                            }}
                            title={`${item.value} students`}
                        >
                            {item.text}
                        </span>
                    ))}
                </div>
                {selectedTag && (() => {
                    const selectedItem = data.find(i => i.text === selectedTag);
                    return (
                        <div className="mt-4 p-3 bg-white border rounded-md text-sm text-gray-600 shadow-sm animate-in fade-in slide-in-from-top-2">
                            <span className="font-semibold text-gray-900">Insight:</span>
                            {` ${selectedItem ? selectedItem.value : 0} students received the feedback "${selectedTag}".`}
                        </div>
                    );
                })()}
            </CardContent>
        </Card>
    );
}
