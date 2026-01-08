import { useState } from "react";
import { useParams } from "react-router-dom";
import { Info, Pen } from "lucide-react";

import TeacherLayout from "../../components/layout/TeacherLayout";
import { Button } from "../../components/ui/button";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../../components/ui/tabs";
import StreamTab from "../../components/features/teacher/StreamTab";
import ClassworkTab from "../../components/features/teacher/ClassworkTab";
import PeopleTab from "../../components/features/teacher/PeopleTab";
import MarksTab from "../../components/features/teacher/MarksTab";

export default function ClassPage() {
    const { classId } = useParams();
    const [activeTab, setActiveTab] = useState("stream");

    return (
        <TeacherLayout>
            <div className="max-w-6xl mx-auto space-y-6">

                {/* 2.1 Class Header Section */}
                <div className="relative rounded-2xl overflow-hidden bg-gradient-to-r from-indigo-600 to-purple-700 text-white min-h-[240px] flex flex-col justify-end p-8 shadow-lg">
                    <div className="absolute top-4 right-4 flex gap-2">
                        <Button variant="ghost" size="icon" className="text-white hover:bg-white/20">
                            <Info className="w-5 h-5" />
                        </Button>
                        <Button variant="secondary" className="gap-2 bg-white/10 hover:bg-white/20 text-white border-0 backdrop-blur-sm">
                            <Pen className="w-4 h-4" />
                            Customize
                        </Button>
                    </div>

                    <div>
                        <h1 className="text-4xl font-bold tracking-tight mb-2">Autograder</h1>
                        <p className="text-xl opacity-90 font-medium">CSE (AI) • Section 2024</p>
                    </div>
                </div>

                {/* 2.2 Class Tabs */}
                <Tabs defaultValue="stream" className="w-full" onValueChange={setActiveTab}>
                    <div className="flex items-center justify-between border-b pb-1 mb-6">
                        <TabsList className="bg-transparent p-0 -mb-[1px] gap-6">
                            {["stream", "classwork", "people", "marks"].map((tab) => (
                                <TabsTrigger
                                    key={tab}
                                    value={tab}
                                    className="data-[state=active]:bg-transparent data-[state=active]:shadow-none data-[state=active]:border-b-2 data-[state=active]:border-indigo-600 rounded-none px-2 pb-3 pt-2 text-base font-medium text-gray-500 data-[state=active]:text-indigo-600 transition-colors uppercase tracking-wide"
                                >
                                    {tab}
                                </TabsTrigger>
                            ))}
                        </TabsList>
                    </div>

                    <TabsContent value="stream" className="mt-0">
                        <StreamTab />
                    </TabsContent>

                    <TabsContent value="classwork">
                        <ClassworkTab />
                    </TabsContent>

                    <TabsContent value="people">
                        <PeopleTab />
                    </TabsContent>

                    <TabsContent value="marks">
                        <MarksTab />
                    </TabsContent>
                </Tabs>

            </div>
        </TeacherLayout>
    );
}
