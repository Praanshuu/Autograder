import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuthUser } from "../../hooks/useAuthUser";
import { Button } from "../../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../../components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../../components/ui/tabs";
import {
    BookOpen,
    Trophy,
    TrendingUp,
    Target,
    Star,
    Clock,
    CheckCircle2,
    Home,
    ArrowLeft
} from "lucide-react";

import PracticeQuestionsList from "../../components/features/student/PracticeQuestionsList";
import { PointsDisplay } from "../../components/features/gamification";

export default function StudentPractice() {
    const { user } = useAuthUser();
    const navigate = useNavigate();
    const [activeTab, setActiveTab] = useState("questions");

    return (
        <div className="min-h-screen bg-gray-50">
            {/* Header */}
            <div className="bg-white border-b border-gray-200 shadow-sm">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="py-4 sm:py-6">
                        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
                            <div className="flex items-center gap-4">
                                <Button
                                    onClick={() => navigate('/student/dashboard')}
                                    variant="ghost"
                                    size="sm"
                                    className="flex items-center gap-2 text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg px-3 py-2 transition-all"
                                >
                                    <ArrowLeft className="w-4 h-4" />
                                    <span className="hidden sm:inline">Back to Dashboard</span>
                                    <span className="sm:hidden">Back</span>
                                </Button>
                                <div className="h-6 w-px bg-gray-300 hidden sm:block"></div>
                                <div>
                                    <h1 className="text-2xl sm:text-3xl font-bold text-gray-900">Practice Center</h1>
                                    <p className="mt-1 sm:mt-2 text-sm sm:text-base text-gray-600">
                                        Sharpen your coding skills with unlimited practice questions
                                    </p>
                                </div>
                            </div>
                            <div className="flex items-center justify-between sm:justify-end space-x-4">
                                <Button
                                    onClick={() => navigate('/student/dashboard')}
                                    variant="outline"
                                    size="sm"
                                    className="flex items-center gap-2 border-indigo-200 text-indigo-700 hover:bg-indigo-50 hover:border-indigo-300 transition-all"
                                >
                                    <Home className="w-4 h-4" />
                                    <span className="hidden sm:inline">Dashboard</span>
                                </Button>
                                <div className="text-right">
                                    <p className="text-xs sm:text-sm text-gray-500">Welcome back,</p>
                                    <p className="font-semibold text-sm sm:text-base text-gray-900">{user?.first_name || user?.username}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            {/* Main Content */}
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8">
                <Tabs value={activeTab} onValueChange={setActiveTab} className="space-y-6">
                    <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
                        <TabsList className="grid w-full grid-cols-3 sm:w-[400px] bg-gray-100 p-1 rounded-xl">
                            <TabsTrigger
                                value="questions"
                                className="flex items-center gap-2 rounded-lg data-[state=active]:bg-white data-[state=active]:shadow-sm transition-all text-xs sm:text-sm"
                            >
                                <BookOpen className="w-4 h-4" />
                                <span className="hidden sm:inline">Questions</span>
                                <span className="sm:hidden">Q</span>
                            </TabsTrigger>
                            <TabsTrigger
                                value="progress"
                                className="flex items-center gap-2 rounded-lg data-[state=active]:bg-white data-[state=active]:shadow-sm transition-all text-xs sm:text-sm"
                            >
                                <TrendingUp className="w-4 h-4" />
                                <span className="hidden sm:inline">Progress</span>
                                <span className="sm:hidden">P</span>
                            </TabsTrigger>
                            <TabsTrigger
                                value="achievements"
                                className="flex items-center gap-2 rounded-lg data-[state=active]:bg-white data-[state=active]:shadow-sm transition-all text-xs sm:text-sm"
                            >
                                <Trophy className="w-4 h-4" />
                                <span className="hidden sm:inline">Achievements</span>
                                <span className="sm:hidden">A</span>
                            </TabsTrigger>
                        </TabsList>

                        {/* Quick Stats */}
                        <div className="flex sm:hidden items-center justify-center gap-4 text-xs text-gray-600 bg-white p-3 rounded-lg border">
                            <div className="flex items-center gap-1">
                                <CheckCircle2 className="w-3 h-3 text-green-500" />
                                <span>0 Done</span>
                            </div>
                            <div className="flex items-center gap-1">
                                <Star className="w-3 h-3 text-yellow-500" />
                                <span>0 Pts</span>
                            </div>
                            <div className="flex items-center gap-1">
                                <Target className="w-3 h-3 text-blue-500" />
                                <span>0 Streak</span>
                            </div>
                        </div>

                        <div className="hidden md:flex items-center gap-6 text-sm text-gray-600">
                            <div className="flex items-center gap-2">
                                <CheckCircle2 className="w-4 h-4 text-green-500" />
                                <span>0 Completed</span>
                            </div>
                            <div className="flex items-center gap-2">
                                <Star className="w-4 h-4 text-yellow-500" />
                                <span>0 Points</span>
                            </div>
                            <div className="flex items-center gap-2">
                                <Target className="w-4 h-4 text-blue-500" />
                                <span>0 Day Streak</span>
                            </div>
                        </div>
                    </div>

                    <TabsContent value="questions" className="space-y-6">
                        <PracticeQuestionsList />
                    </TabsContent>

                    <TabsContent value="progress" className="space-y-6">
                        {/* Progress Overview Card */}
                        <Card className="bg-gradient-to-br from-indigo-50 to-blue-50 border-indigo-200">
                            <CardHeader>
                                <CardTitle className="flex items-center gap-2 text-indigo-900">
                                    <TrendingUp className="w-5 h-5" />
                                    Your Progress Journey
                                </CardTitle>
                            </CardHeader>
                            <CardContent>
                                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                                    <div className="text-center">
                                        <div className="text-3xl font-bold text-indigo-700">0</div>
                                        <div className="text-sm text-indigo-600">Questions Solved</div>
                                    </div>
                                    <div className="text-center">
                                        <div className="text-3xl font-bold text-blue-700">0</div>
                                        <div className="text-sm text-blue-600">Current Streak</div>
                                    </div>
                                    <div className="text-center">
                                        <div className="text-3xl font-bold text-purple-700">0h</div>
                                        <div className="text-sm text-purple-600">Time Practiced</div>
                                    </div>
                                </div>
                            </CardContent>
                        </Card>

                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                            {/* Progress Stats Cards */}
                            <Card className="hover:shadow-lg transition-shadow">
                                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                    <CardTitle className="text-sm font-medium">Questions Completed</CardTitle>
                                    <CheckCircle2 className="h-4 w-4 text-green-600" />
                                </CardHeader>
                                <CardContent>
                                    <div className="text-2xl font-bold">0</div>
                                    <p className="text-xs text-muted-foreground">
                                        +0 from last week
                                    </p>
                                </CardContent>
                            </Card>

                            <Card className="hover:shadow-lg transition-shadow">
                                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                    <CardTitle className="text-sm font-medium">Current Streak</CardTitle>
                                    <Target className="h-4 w-4 text-orange-600" />
                                </CardHeader>
                                <CardContent>
                                    <div className="text-2xl font-bold">0</div>
                                    <p className="text-xs text-muted-foreground">
                                        days in a row
                                    </p>
                                </CardContent>
                            </Card>

                            <PointsDisplay
                                showHistory={false}
                                showBreakdown={false}
                                className="hover:shadow-lg transition-shadow"
                            />

                            <Card className="hover:shadow-lg transition-shadow">
                                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                    <CardTitle className="text-sm font-medium">Time Spent</CardTitle>
                                    <Clock className="h-4 w-4 text-blue-600" />
                                </CardHeader>
                                <CardContent>
                                    <div className="text-2xl font-bold">0h</div>
                                    <p className="text-xs text-muted-foreground">
                                        total practice time
                                    </p>
                                </CardContent>
                            </Card>
                        </div>

                        {/* Progress Charts Placeholder */}
                        <Card className="hover:shadow-lg transition-shadow">
                            <CardHeader>
                                <CardTitle>Progress Overview</CardTitle>
                            </CardHeader>
                            <CardContent>
                                <div className="h-64 flex items-center justify-center text-gray-500">
                                    <div className="text-center">
                                        <TrendingUp className="w-12 h-12 mx-auto mb-4 text-gray-400" />
                                        <p className="text-lg font-medium mb-2">Start Your Journey!</p>
                                        <p>Progress charts will appear here as you complete practice questions</p>
                                        <Button
                                            onClick={() => setActiveTab("questions")}
                                            className="mt-4 bg-indigo-600 hover:bg-indigo-700"
                                        >
                                            Browse Questions
                                        </Button>
                                    </div>
                                </div>
                            </CardContent>
                        </Card>
                    </TabsContent>

                    <TabsContent value="achievements" className="space-y-6">
                        <Card className="bg-gradient-to-br from-yellow-50 to-orange-50 border-yellow-200">
                            <CardHeader>
                                <CardTitle className="flex items-center gap-2 text-yellow-900">
                                    <Trophy className="w-5 h-5" />
                                    Achievement Gallery
                                </CardTitle>
                            </CardHeader>
                            <CardContent>
                                <div className="h-64 flex items-center justify-center text-gray-500">
                                    <div className="text-center">
                                        <Trophy className="w-16 h-16 mx-auto mb-4 text-yellow-400" />
                                        <p className="text-xl font-semibold mb-2 text-gray-700">Ready to Earn Your First Badge?</p>
                                        <p className="text-gray-600 mb-4">Your achievements will appear here as you progress</p>
                                        <p className="text-sm text-gray-500 mb-4">Complete practice questions to unlock badges!</p>
                                        <div className="flex gap-2 justify-center">
                                            <Button
                                                onClick={() => setActiveTab("questions")}
                                                className="bg-yellow-600 hover:bg-yellow-700 text-white"
                                            >
                                                Start Practicing
                                            </Button>
                                            <Button
                                                onClick={() => navigate('/student/dashboard')}
                                                variant="outline"
                                                className="border-yellow-300 text-yellow-700 hover:bg-yellow-50"
                                            >
                                                View Dashboard
                                            </Button>
                                        </div>
                                    </div>
                                </div>
                            </CardContent>
                        </Card>
                    </TabsContent>
                </Tabs>
            </div>
        </div>
    );
}