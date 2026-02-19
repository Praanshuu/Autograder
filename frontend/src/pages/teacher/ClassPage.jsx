import { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import { MoveLeft, Settings, Loader2, AlertCircle, Archive } from "lucide-react";
import { motion } from "framer-motion";

import TeacherLayout from "../../components/layout/TeacherLayout";
import { Button } from "../../components/ui/button";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../../components/ui/tabs";
import StreamTab from "../../components/features/teacher/StreamTab";
import ClassworkTab from "../../components/features/teacher/ClassworkTab";
import PeopleTab from "../../components/features/teacher/PeopleTab";
import MarksTab from "../../components/features/teacher/MarksTab";
import MarksTabV2 from "../../components/features/teacher/MarksTabV2";
import { classService } from "../../services/classService";

export default function ClassPage() {
    const { classId } = useParams();
    const [activeTab, setActiveTab] = useState("stream");
    const [classData, setClassData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchClassDetails = async () => {
            try {
                setLoading(true);
                const response = await classService.getClass(classId);
                if (response.success) {
                    setClassData(response.data);
                } else {
                    setError(response.error?.message || "Failed to load class details.");
                }
            } catch (err) {
                console.error("Failed to fetch class details", err);
                setError("Failed to load class details.");
            } finally {
                setLoading(false);
            }
        };

        if (classId) {
            fetchClassDetails();
        }
    }, [classId]);

    if (loading) {
        return (
            <TeacherLayout>
                <div className="flex h-[80vh] items-center justify-center">
                    <Loader2 className="w-10 h-10 animate-spin text-indigo-600" />
                </div>
            </TeacherLayout>
        );
    }

    if (error || !classData) {
        return (
            <TeacherLayout>
                <div className="flex flex-col h-[80vh] items-center justify-center text-red-500">
                    <AlertCircle className="w-12 h-12 mb-4" />
                    <h2 className="text-xl font-bold">Error</h2>
                    <p>{error || "Class not found"}</p>
                    <Button variant="outline" className="mt-4" asChild>
                        <Link to="/teacher/dashboard">Back to Dashboard</Link>
                    </Button>
                </div>
            </TeacherLayout>
        );
    }

    return (
        <TeacherLayout>
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="space-y-6"
            >
                {/* Header */}
                <div className="flex flex-col gap-4">
                    {/* Archived Banner */}
                    {classData.is_archived && (
                        <div className="bg-amber-50 border border-amber-200 rounded-lg p-3 flex items-center gap-3 text-amber-800 mb-2">
                            <Archive className="w-5 h-5" />
                            <div className="flex-1">
                                <p className="font-medium text-sm">This class is archived</p>
                                <p className="text-xs text-amber-700 mt-0.5">
                                    You can restore it from the <Link to="/teacher/archived" className="underline hover:text-amber-900">Archived Classes</Link> page.
                                    Students can still view their work, but cannot make new submissions.
                                </p>
                            </div>
                        </div>
                    )}

                    <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                        <div className="flex items-center gap-4">
                            <Button variant="ghost" size="icon" asChild>
                                <Link to={classData.is_archived ? "/teacher/archived" : "/teacher/dashboard"}>
                                    <MoveLeft className="w-5 h-5" />
                                </Link>
                            </Button>
                            <div>
                                <div className="flex items-center gap-3">
                                    <h1 className="text-2xl font-bold text-gray-900">{classData.name}</h1>
                                    {classData.is_archived && (
                                        <span className="bg-amber-100 text-amber-800 text-xs font-bold px-2 py-0.5 rounded border border-amber-200 uppercase tracking-wide">
                                            Archived
                                        </span>
                                    )}
                                </div>
                                <p className="text-gray-500 text-sm mt-1">{classData.section || "No Section"} • {classData.term || "Current Term"}</p>
                            </div>
                        </div>
                        <Button variant="outline" size="sm" className="gap-2" asChild>
                            <Link to={`/teacher/class/${classId}/settings`}>
                                <Settings className="w-4 h-4" />
                                Class Settings
                            </Link>
                        </Button>
                    </div>
                </div>

                {/* Class Tabs */}
                <Tabs defaultValue="stream" className="w-full" onValueChange={setActiveTab}>
                    <TabsList className="bg-transparent p-0 border-b w-full justify-start h-auto rounded-none mb-6">
                        {["stream", "classwork", "people", "marks", "marks-v2"].map((tab) => (
                            <TabsTrigger
                                key={tab}
                                value={tab}
                                className="data-[state=active]:bg-transparent data-[state=active]:shadow-none data-[state=active]:border-b-2 data-[state=active]:border-indigo-600 rounded-none px-4 pb-3 pt-2 text-sm font-medium text-gray-500 data-[state=active]:text-indigo-600 transition-colors capitalize"
                            >
                                {tab === "marks-v2" ? "Marks (Beta)" : tab}
                            </TabsTrigger>
                        ))}
                    </TabsList>

                    <TabsContent value="stream" className="mt-0">
                        <StreamTab classId={classId} />
                    </TabsContent>

                    <TabsContent value="classwork">
                        <ClassworkTab classId={classId} />
                    </TabsContent>

                    <TabsContent value="people">
                        <PeopleTab classId={classId} />
                    </TabsContent>

                    <TabsContent value="marks">
                        <MarksTab classId={classId} />
                    </TabsContent>

                    <TabsContent value="marks-v2">
                        <MarksTabV2 classId={classId} />
                    </TabsContent>
                </Tabs>

            </motion.div>
        </TeacherLayout>
    );
}
