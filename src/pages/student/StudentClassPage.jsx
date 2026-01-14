import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { Info, BookOpen, MessageSquare } from "lucide-react";
import { motion } from "framer-motion";

import StudentLayout from "../../components/layout/StudentLayout";
import { Button } from "../../components/ui/button";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../../components/ui/tabs";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../../components/ui/card";
import { Badge } from "../../components/ui/badge";

// Reusing teacher components (Read-Only mode where applicable)
// Ideally we should make separate student-specific components, but for speed:
import StreamTab from "../../components/features/teacher/StreamTab"; // Assuming we can make this readonly or it handles role check
import StudentClassworkTab from "../../components/features/student/StudentClassworkTab"; // We need to create this

import { classService } from "../../services/classService";

export default function StudentClassPage() {
    const { classId } = useParams();
    const [classData, setClassData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [activeTab, setActiveTab] = useState("stream");

    useEffect(() => {
        const fetchClass = async () => {
            try {
                const response = await classService.getClass(classId);
                setClassData(response.data);
            } catch (err) {
                console.error("Failed to load class:", err);
            } finally {
                setLoading(false);
            }
        };
        fetchClass();
    }, [classId]);

    if (loading) {
        return (
            <StudentLayout>
                <div className="flex justify-center py-20">Loading...</div>
            </StudentLayout>
        );
    }

    if (!classData) {
        return (
            <StudentLayout>
                <div className="text-center py-20 text-red-500">Class not found</div>
            </StudentLayout>
        );
    }

    return (
        <StudentLayout>
            <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                className="max-w-6xl mx-auto space-y-6"
            >
                {/* 1. Class Header (Student View) */}
                <div className="relative rounded-2xl overflow-hidden bg-gradient-to-br from-indigo-600 to-violet-700 text-white min-h-[200px] flex flex-col justify-end p-8 shadow-lg">
                    <div className="absolute top-0 right-0 p-32 bg-white/5 rounded-full blur-3xl" />
                    <div className="absolute bottom-0 left-0 p-24 bg-black/10 rounded-full blur-2xl" />

                    <div className="relative z-10">
                        <h1 className="text-4xl font-bold tracking-tight mb-2">{classData.name}</h1>
                        <div className="flex items-center gap-3 text-white/90">
                            <Badge variant="outline" className="text-white border-white/30 bg-white/10">{classData.section}</Badge>
                            <span className="text-sm font-medium opacity-80 flex items-center gap-1">
                                <Info className="w-4 h-4" />
                                {classData.class_code}
                            </span>
                        </div>
                    </div>
                </div>

                {/* 2. Tabs */}
                <Tabs defaultValue="stream" value={activeTab} onValueChange={setActiveTab} className="w-full">
                    <div className="flex items-center justify-between border-b border-gray-200 mb-6">
                        <TabsList className="bg-transparent p-0 -mb-[1px] gap-8">
                            <TabsTrigger
                                value="stream"
                                className="data-[state=active]:border-indigo-600 data-[state=active]:text-indigo-600 border-b-2 border-transparent px-1 pb-4 pt-2 rounded-none text-gray-500 font-medium"
                            >
                                Stream
                            </TabsTrigger>
                            <TabsTrigger
                                value="classwork"
                                className="data-[state=active]:border-indigo-600 data-[state=active]:text-indigo-600 border-b-2 border-transparent px-1 pb-4 pt-2 rounded-none text-gray-500 font-medium"
                            >
                                Classwork
                            </TabsTrigger>
                        </TabsList>
                    </div>

                    <TabsContent value="stream" className="mt-0">
                        {/* Reusing StreamTab but we might want to ensure it's student-friendly. 
                             For now, let's assume StreamTab renders posts. 
                             If StreamTab has "Create Post", we need to hide it for students if they aren't allowed.
                             Let's place a placeholder or reuse it if it handles permissions. 
                             Since I don't want to break existing code, I'll wrap it or use a simplified version.
                         */}
                        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                            {/* Left: Upcoming (Todo) */}
                            <div className="hidden lg:block space-y-4">
                                <Card>
                                    <CardHeader className="pb-3">
                                        <CardTitle className="text-sm font-medium text-gray-500 uppercase tracking-wider">Upcoming</CardTitle>
                                    </CardHeader>
                                    <CardContent>
                                        <p className="text-sm text-gray-400 italic">No work due soon</p>
                                    </CardContent>
                                </Card>
                            </div>

                            {/* Center: Stream Feed */}
                            <div className="lg:col-span-2 space-y-4">
                                {/* Announcement Placeholder */}
                                <Card className="bg-indigo-50 border-indigo-100">
                                    <CardContent className="p-4 flex items-center gap-4">
                                        <div className="w-10 h-10 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-600">
                                            <Info className="w-5 h-5" />
                                        </div>
                                        <div>
                                            <p className="text-indigo-900 font-medium">Welcome to {classData.name}!</p>
                                            <p className="text-indigo-700 text-sm">Check the Classwork tab for new assignments.</p>
                                        </div>
                                    </CardContent>
                                </Card>

                                {/* We can reuse StreamTab here if refined later */}
                            </div>
                        </div>
                    </TabsContent>

                    <TabsContent value="classwork">
                        <StudentClassworkTab classId={classId} />
                    </TabsContent>
                </Tabs>
            </motion.div>
        </StudentLayout>
    );
}
