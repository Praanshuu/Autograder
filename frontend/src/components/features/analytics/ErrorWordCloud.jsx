import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../../ui/card";
import { CheckCircle2, XCircle, Loader2, Sparkles, MessageSquareWarning } from "lucide-react";

const TABS = [
    {
        key: 'full',
        label: 'Full Score',
        icon: CheckCircle2,
        iconColor: 'text-emerald-500',
        activeRing: 'border-emerald-400 bg-emerald-50/60',
        inactiveRing: 'border-transparent text-gray-500 hover:text-gray-700',
        emptyTitle: 'No full-score submissions yet',
        emptyDesc: 'Word patterns from perfect submissions will appear here once students score full marks.',
    },
    {
        key: 'partial',
        label: 'Partial / Incorrect',
        icon: XCircle,
        iconColor: 'text-rose-500',
        activeRing: 'border-rose-400 bg-rose-50/60',
        inactiveRing: 'border-transparent text-gray-500 hover:text-gray-700',
        emptyTitle: 'No partial/incorrect data',
        emptyDesc: 'Error patterns and approach terms from incorrect submissions will appear here.',
    },
];

function SkeletonCloud() {
    return (
        <div className="animate-pulse flex items-center justify-center p-4 h-48 w-full">
            <div className="space-y-3 w-full">
                {[80, 55, 65, 45, 70].map((w, i) => (
                    <div
                        key={i}
                        className="h-3 rounded-full bg-gray-200 mx-auto"
                        style={{ width: `${w}%`, opacity: 1 - i * 0.12 }}
                    />
                ))}
            </div>
        </div>
    );
}

export default function ErrorWordCloud({ fullImage, partialImage, loading, hasAiData }) {
    const [activeTab, setActiveTab] = useState('full');

    const activeTabData = TABS.find(t => t.key === activeTab);
    const currentImage = activeTab === 'full' ? fullImage : partialImage;

    // Nothing to show — no AI data at all
    if (!hasAiData) {
        return (
            <Card className="col-span-1 border-dashed border-gray-200 bg-gray-50 h-full flex flex-col items-center justify-center p-6 text-center text-gray-400">
                <MessageSquareWarning className="w-8 h-8 mb-2 opacity-20" />
                <p className="text-sm font-medium">No AI analysis yet</p>
                <p className="text-xs mt-1">Run Autograder+ to generate feedback word clouds.</p>
            </Card>
        );
    }

    return (
        <Card className="col-span-1 h-full flex flex-col">
            <CardHeader className="pb-2">
                <CardTitle className="text-lg flex items-center gap-2">
                    <Sparkles className="w-5 h-5 text-indigo-500" />
                    Feedback Themes
                </CardTitle>
                <CardDescription className="text-xs">
                    Key terms extracted from Autograder+ analysis, segmented by score tier.
                </CardDescription>
            </CardHeader>

            {/* Tabs */}
            <div className="flex gap-1 px-5 border-b border-gray-100">
                {TABS.map(tab => {
                    const TabIcon = tab.icon;
                    const isActive = activeTab === tab.key;
                    return (
                        <button
                            key={tab.key}
                            onClick={() => setActiveTab(tab.key)}
                            className={`flex items-center gap-1.5 px-3 py-2 text-xs font-medium rounded-t-md border-b-2 transition-all ${
                                isActive ? tab.activeRing + ' text-gray-800' : tab.inactiveRing
                            }`}
                        >
                            <TabIcon className={`w-3.5 h-3.5 ${isActive ? tab.iconColor : 'text-gray-400'}`} />
                            {tab.label}
                        </button>
                    );
                })}
            </div>

            <CardContent className="flex-1 flex flex-col items-center justify-center p-4">
                {loading ? (
                    <SkeletonCloud />
                ) : currentImage ? (
                    <div className="w-full flex items-center justify-center">
                        <img
                            src={`data:image/png;base64,${currentImage}`}
                            alt={`${activeTabData.label} word cloud`}
                            className="max-w-full h-auto rounded-lg shadow-sm border border-gray-100"
                        />
                    </div>
                ) : (
                    <div className="flex flex-col items-center justify-center gap-2 py-10 text-center text-gray-400">
                        <activeTabData.icon className={`w-9 h-9 ${activeTabData.iconColor} opacity-25`} />
                        <p className="text-sm font-medium text-gray-500">{activeTabData.emptyTitle}</p>
                        <p className="text-xs max-w-[220px]">{activeTabData.emptyDesc}</p>
                    </div>
                )}
            </CardContent>
        </Card>
    );
}
