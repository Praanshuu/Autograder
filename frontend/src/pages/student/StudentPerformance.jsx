import { useState } from "react";
import StudentLayout from "../../components/layout/StudentLayout";
import { Card, CardContent, CardHeader, CardTitle } from "../../components/ui/card";
import { Button } from "../../components/ui/button";
import { 
    TrendingUp, 
    Clock, 
    Target, 
    Award, 
    BarChart3, 
    Calendar,
    Code2,
    Trophy,
    Zap,
    Brain,
    Star,
    ChevronRight,
    Filter
} from "lucide-react";
import { 
    LineChart, 
    Line, 
    XAxis, 
    YAxis, 
    CartesianGrid, 
    Tooltip, 
    ResponsiveContainer,
    BarChart,
    Bar,
    PieChart,
    Pie,
    Cell,
    RadarChart,
    PolarGrid,
    PolarAngleAxis,
    PolarRadiusAxis,
    Radar
} from "recharts";
import { PERFORMANCE_DATA } from "../../mocks/performance";

const StatCard = ({ title, value, subtitle, icon: Icon, trend, color = "blue" }) => {
    const colorClasses = {
        blue: "bg-blue-50 text-blue-600 border-blue-100",
        green: "bg-green-50 text-green-600 border-green-100",
        purple: "bg-purple-50 text-purple-600 border-purple-100",
        orange: "bg-orange-50 text-orange-600 border-orange-100"
    };

    return (
        <Card>
            <CardContent className="p-6">
                <div className="flex items-center justify-between">
                    <div>
                        <p className="text-sm font-medium text-gray-600">{title}</p>
                        <p className="text-2xl font-bold text-gray-900">{value}</p>
                        {subtitle && (
                            <p className="text-sm text-gray-500 mt-1">{subtitle}</p>
                        )}
                        {trend && (
                            <div className="flex items-center mt-2 text-sm">
                                <TrendingUp className="w-4 h-4 text-green-500 mr-1" />
                                <span className="text-green-600">{trend}</span>
                            </div>
                        )}
                    </div>
                    <div className={`p-3 rounded-lg ${colorClasses[color]}`}>
                        <Icon className="w-6 h-6" />
                    </div>
                </div>
            </CardContent>
        </Card>
    );
};

const AchievementBadge = ({ achievement }) => {
    const rarityColors = {
        common: "bg-gray-100 text-gray-700 border-gray-200",
        uncommon: "bg-green-100 text-green-700 border-green-200",
        rare: "bg-purple-100 text-purple-700 border-purple-200",
        legendary: "bg-yellow-100 text-yellow-700 border-yellow-200"
    };

    return (
        <div className={`p-4 rounded-lg border ${rarityColors[achievement.rarity]} hover:shadow-md transition-shadow`}>
            <div className="flex items-start gap-3">
                <span className="text-2xl">{achievement.icon}</span>
                <div className="flex-1">
                    <h4 className="font-semibold text-sm">{achievement.title}</h4>
                    <p className="text-xs opacity-80 mt-1">{achievement.description}</p>
                    <p className="text-xs opacity-60 mt-2">{new Date(achievement.date).toLocaleDateString()}</p>
                </div>
            </div>
        </div>
    );
};

export default function StudentPerformance() {
    const [selectedTimeframe, setSelectedTimeframe] = useState("all");
    const { overview, gradeHistory, difficultyStats, weeklyActivity, languageStats, conceptMastery, achievements, classComparison } = PERFORMANCE_DATA;

    // Colors for charts
    const COLORS = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6'];

    // Format time in minutes to hours/minutes
    const formatTime = (minutes) => {
        const hours = Math.floor(minutes / 60);
        const mins = minutes % 60;
        return hours > 0 ? `${hours}h ${mins}m` : `${mins}m`;
    };

    return (
        <StudentLayout>
            <div className="max-w-7xl mx-auto space-y-6 pb-10">
                {/* Header */}
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-3xl font-bold tracking-tight text-gray-900">My Performance</h1>
                        <p className="text-gray-500">Track your progress and analyze your coding journey.</p>
                    </div>
                    <div className="flex items-center gap-2">
                        <Button variant="outline" size="sm">
                            <Filter className="w-4 h-4 mr-2" />
                            Filter
                        </Button>
                        <Button variant="outline" size="sm">
                            Export Report
                        </Button>
                    </div>
                </div>

                {/* Overview Stats */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    <StatCard
                        title="Average Score"
                        value={`${overview.averageScore}%`}
                        subtitle={`${overview.completedAssignments}/${overview.totalAssignments} completed`}
                        icon={Target}
                        trend="+5.2% from last month"
                        color="blue"
                    />
                    <StatCard
                        title="Class Rank"
                        value={`#${overview.rank}`}
                        subtitle={`out of ${overview.totalStudents} students`}
                        icon={Trophy}
                        color="green"
                    />
                    <StatCard
                        title="Time Spent"
                        value={formatTime(overview.totalTimeSpent)}
                        subtitle="Total coding time"
                        icon={Clock}
                        color="purple"
                    />
                    <StatCard
                        title="Current Streak"
                        value={`${overview.currentStreak} days`}
                        subtitle="Daily coding streak"
                        icon={Zap}
                        trend="Personal best!"
                        color="orange"
                    />
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    {/* Grade Trend Chart */}
                    <Card className="lg:col-span-2">
                        <CardHeader>
                            <CardTitle className="flex items-center gap-2">
                                <TrendingUp className="w-5 h-5" />
                                Grade Progression
                            </CardTitle>
                        </CardHeader>
                        <CardContent>
                            <ResponsiveContainer width="100%" height={300}>
                                <LineChart data={gradeHistory.slice(-10)}>
                                    <CartesianGrid strokeDasharray="3 3" />
                                    <XAxis 
                                        dataKey="assignment" 
                                        tick={{ fontSize: 12 }}
                                        angle={-45}
                                        textAnchor="end"
                                        height={80}
                                    />
                                    <YAxis domain={[0, 100]} />
                                    <Tooltip 
                                        formatter={(value) => [`${value}%`, 'Score']}
                                        labelFormatter={(label) => `Assignment: ${label}`}
                                    />
                                    <Line 
                                        type="monotone" 
                                        dataKey="score" 
                                        stroke="#3B82F6" 
                                        strokeWidth={3}
                                        dot={{ fill: '#3B82F6', strokeWidth: 2, r: 4 }}
                                    />
                                </LineChart>
                            </ResponsiveContainer>
                        </CardContent>
                    </Card>

                    {/* Difficulty Breakdown */}
                    <Card>
                        <CardHeader>
                            <CardTitle className="flex items-center gap-2">
                                <BarChart3 className="w-5 h-5" />
                                By Difficulty
                            </CardTitle>
                        </CardHeader>
                        <CardContent>
                            <div className="space-y-4">
                                {difficultyStats.map((stat, index) => (
                                    <div key={stat.difficulty} className="space-y-2">
                                        <div className="flex justify-between items-center">
                                            <span className="text-sm font-medium">{stat.difficulty}</span>
                                            <span className="text-sm text-gray-500">{stat.avgScore.toFixed(1)}%</span>
                                        </div>
                                        <div className="w-full bg-gray-200 rounded-full h-2">
                                            <div 
                                                className={`h-2 rounded-full ${
                                                    stat.difficulty === 'Easy' ? 'bg-green-500' :
                                                    stat.difficulty === 'Medium' ? 'bg-yellow-500' : 'bg-red-500'
                                                }`}
                                                style={{ width: `${(stat.completed / stat.total) * 100}%` }}
                                            />
                                        </div>
                                        <div className="flex justify-between text-xs text-gray-500">
                                            <span>{stat.completed}/{stat.total} completed</span>
                                            <span>Avg: {formatTime(stat.avgTime)}</span>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </CardContent>
                    </Card>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                    {/* Weekly Activity */}
                    <Card>
                        <CardHeader>
                            <CardTitle className="flex items-center gap-2">
                                <Calendar className="w-5 h-5" />
                                Weekly Activity
                            </CardTitle>
                        </CardHeader>
                        <CardContent>
                            <ResponsiveContainer width="100%" height={250}>
                                <BarChart data={weeklyActivity}>
                                    <CartesianGrid strokeDasharray="3 3" />
                                    <XAxis dataKey="week" />
                                    <YAxis />
                                    <Tooltip />
                                    <Bar dataKey="assignments" fill="#3B82F6" name="Assignments" />
                                </BarChart>
                            </ResponsiveContainer>
                        </CardContent>
                    </Card>

                    {/* Language Proficiency */}
                    <Card>
                        <CardHeader>
                            <CardTitle className="flex items-center gap-2">
                                <Code2 className="w-5 h-5" />
                                Language Proficiency
                            </CardTitle>
                        </CardHeader>
                        <CardContent>
                            <ResponsiveContainer width="100%" height={250}>
                                <PieChart>
                                    <Pie
                                        data={languageStats}
                                        cx="50%"
                                        cy="50%"
                                        labelLine={false}
                                        label={({ language, assignments }) => `${language} (${assignments})`}
                                        outerRadius={80}
                                        fill="#8884d8"
                                        dataKey="assignments"
                                    >
                                        {languageStats.map((entry, index) => (
                                            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                                        ))}
                                    </Pie>
                                    <Tooltip />
                                </PieChart>
                            </ResponsiveContainer>
                        </CardContent>
                    </Card>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    {/* Concept Mastery Radar */}
                    <Card className="lg:col-span-2">
                        <CardHeader>
                            <CardTitle className="flex items-center gap-2">
                                <Brain className="w-5 h-5" />
                                Concept Mastery
                            </CardTitle>
                        </CardHeader>
                        <CardContent>
                            <ResponsiveContainer width="100%" height={300}>
                                <RadarChart data={conceptMastery}>
                                    <PolarGrid />
                                    <PolarAngleAxis dataKey="concept" tick={{ fontSize: 12 }} />
                                    <PolarRadiusAxis domain={[0, 100]} />
                                    <Radar
                                        name="Mastery"
                                        dataKey="mastery"
                                        stroke="#3B82F6"
                                        fill="#3B82F6"
                                        fillOpacity={0.3}
                                    />
                                    <Tooltip />
                                </RadarChart>
                            </ResponsiveContainer>
                        </CardContent>
                    </Card>

                    {/* Recent Achievements */}
                    <Card>
                        <CardHeader>
                            <CardTitle className="flex items-center gap-2">
                                <Award className="w-5 h-5" />
                                Recent Achievements
                            </CardTitle>
                        </CardHeader>
                        <CardContent>
                            <div className="space-y-3">
                                {achievements.slice(0, 4).map((achievement, index) => (
                                    <AchievementBadge key={index} achievement={achievement} />
                                ))}
                                <Button variant="ghost" className="w-full text-sm">
                                    View All Achievements
                                    <ChevronRight className="w-4 h-4 ml-1" />
                                </Button>
                            </div>
                        </CardContent>
                    </Card>
                </div>

                {/* Class Comparison */}
                <Card>
                    <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                            <Star className="w-5 h-5" />
                            Class Comparison
                        </CardTitle>
                    </CardHeader>
                    <CardContent>
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                            {classComparison.map((comparison, index) => (
                                <div key={index} className="text-center">
                                    <h4 className="text-sm font-medium text-gray-600 mb-2">{comparison.metric}</h4>
                                    <div className="space-y-2">
                                        <div className="flex justify-between items-center">
                                            <span className="text-xs text-gray-500">You</span>
                                            <span className="text-lg font-bold text-blue-600">{comparison.student}%</span>
                                        </div>
                                        <div className="flex justify-between items-center">
                                            <span className="text-xs text-gray-500">Class Avg</span>
                                            <span className="text-lg font-bold text-gray-400">{comparison.classAvg}%</span>
                                        </div>
                                        <div className="w-full bg-gray-200 rounded-full h-2">
                                            <div 
                                                className="h-2 bg-blue-500 rounded-full"
                                                style={{ width: `${(comparison.student / 100) * 100}%` }}
                                            />
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </CardContent>
                </Card>
            </div>
        </StudentLayout>
    );
}