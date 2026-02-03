import React, { useState, useEffect } from 'react';
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
  Filter,
  Activity,
  Users,
  BookOpen,
  CheckCircle2,
  AlertCircle,
  Flame,
  Timer,
  LineChart
} from 'lucide-react';
import { 
  LineChart as RechartsLineChart, 
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
  Radar,
  AreaChart,
  Area
} from 'recharts';
import { motion, AnimatePresence } from 'framer-motion';
import { Card, CardContent, CardHeader, CardTitle } from '../../ui/card';
import { Badge } from '../../ui/badge';
import { Button } from '../../ui/button';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../../ui/tabs';
import { gamificationService } from '../../../services/gamificationService';
import '../gamification/MobileResponsive.css';

const StatCard = ({ title, value, subtitle, icon: Icon, trend, color = "blue", className = "" }) => {
  const colorClasses = {
    blue: "bg-blue-50 text-blue-600 border-blue-100",
    green: "bg-green-50 text-green-600 border-green-100",
    purple: "bg-purple-50 text-purple-600 border-purple-100",
    orange: "bg-orange-50 text-orange-600 border-orange-100",
    red: "bg-red-50 text-red-600 border-red-100",
    yellow: "bg-yellow-50 text-yellow-600 border-yellow-100"
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className={className}
    >
      <Card>
        <CardContent className="p-6">
          <div className="flex items-center justify-between">
            <div className="flex-1">
              <p className="text-sm font-medium text-gray-600">{title}</p>
              <p className="text-2xl font-bold text-gray-900 mt-1">{value}</p>
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
    </motion.div>
  );
};

const ProgressRing = ({ percentage, size = 120, strokeWidth = 8, color = "#3B82F6" }) => {
  const radius = (size - strokeWidth) / 2;
  const circumference = radius * 2 * Math.PI;
  const strokeDasharray = `${circumference} ${circumference}`;
  const strokeDashoffset = circumference - (percentage / 100) * circumference;

  return (
    <div className="relative inline-flex items-center justify-center">
      <svg
        className="transform -rotate-90"
        width={size}
        height={size}
      >
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          stroke="#E5E7EB"
          strokeWidth={strokeWidth}
          fill="transparent"
        />
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          stroke={color}
          strokeWidth={strokeWidth}
          fill="transparent"
          strokeDasharray={strokeDasharray}
          strokeDashoffset={strokeDashoffset}
          strokeLinecap="round"
          className="transition-all duration-1000 ease-out"
        />
      </svg>
      <div className="absolute inset-0 flex items-center justify-center">
        <span className="text-2xl font-bold text-gray-900">{Math.round(percentage)}%</span>
      </div>
    </div>
  );
};

const ConceptMasteryCard = ({ concept, mastery, color }) => (
  <motion.div
    initial={{ opacity: 0, scale: 0.9 }}
    animate={{ opacity: 1, scale: 1 }}
    className="bg-white p-4 rounded-lg border border-gray-200 hover:shadow-md transition-shadow"
  >
    <div className="flex items-center justify-between mb-3">
      <h4 className="font-semibold text-gray-900">{concept}</h4>
      <Badge variant={mastery >= 80 ? "default" : mastery >= 60 ? "secondary" : "destructive"}>
        {mastery}%
      </Badge>
    </div>
    <div className="w-full bg-gray-200 rounded-full h-2">
      <div 
        className={`h-2 rounded-full transition-all duration-1000 ${
          mastery >= 80 ? 'bg-green-500' : mastery >= 60 ? 'bg-yellow-500' : 'bg-red-500'
        }`}
        style={{ width: `${mastery}%` }}
      />
    </div>
    <p className="text-xs text-gray-500 mt-2">
      {mastery >= 80 ? 'Mastered' : mastery >= 60 ? 'Proficient' : 'Needs Practice'}
    </p>
  </motion.div>
);

const StudentAnalyticsDashboard = ({ className = "" }) => {
  const [analyticsData, setAnalyticsData] = useState(null);
  const [performanceTrends, setPerformanceTrends] = useState([]);
  const [conceptMastery, setConceptMastery] = useState({});
  const [comparisonData, setComparisonData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedTimeframe, setSelectedTimeframe] = useState('30');
  const [activeTab, setActiveTab] = useState('overview');

  // Fetch analytics data
  const fetchAnalyticsData = async () => {
    try {
      setLoading(true);
      
      const [
        analyticsResponse,
        trendsResponse,
        comparisonResponse
      ] = await Promise.all([
        gamificationService.getStudentAnalytics(),
        gamificationService.getPerformanceTrends(parseInt(selectedTimeframe)),
        gamificationService.getStudentAnalytics() // Will be replaced with comparison endpoint
      ]);

      if (analyticsResponse.success) {
        setAnalyticsData(analyticsResponse.data);
        
        // Extract concept mastery if available
        if (analyticsResponse.data.concept_mastery) {
          setConceptMastery(analyticsResponse.data.concept_mastery);
        }
      }

      if (trendsResponse.success) {
        setPerformanceTrends(trendsResponse.data.trends || []);
      }

      if (comparisonResponse.success) {
        setComparisonData(comparisonResponse.data);
      }

      setError(null);
    } catch (err) {
      console.error('Failed to fetch analytics data:', err);
      setError('Failed to load analytics data');
      
      // Show empty state instead of mock data
      setAnalyticsData(null);
      setPerformanceTrends([]);
      setConceptMastery({});
        'Loops': 78,
        'Functions': 85,
        'Recursion': 45,
        'Data Structures': 67,
        'Algorithms': 73
      });
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAnalyticsData();
  }, [selectedTimeframe]);

  // Format time in minutes to hours/minutes
  const formatTime = (minutes) => {
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;
    return hours > 0 ? `${hours}h ${mins}m` : `${mins}m`;
  };

  // Calculate completion rate
  const getCompletionRate = () => {
    if (!analyticsData) return 0;
    const total = analyticsData.total_practice_completed + analyticsData.total_assignments_completed;
    return total > 0 ? Math.round((analyticsData.total_practice_completed / total) * 100) : 0;
  };

  // Get performance status
  const getPerformanceStatus = () => {
    if (!analyticsData) return { status: 'unknown', color: 'gray' };
    
    const score = analyticsData.average_score;
    if (score >= 90) return { status: 'excellent', color: 'green' };
    if (score >= 80) return { status: 'good', color: 'blue' };
    if (score >= 70) return { status: 'fair', color: 'yellow' };
    return { status: 'needs improvement', color: 'red' };
  };

  // Colors for charts
  const COLORS = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#EC4899'];

  if (loading) {
    return (
      <div className={`space-y-6 ${className}`}>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {[...Array(4)].map((_, i) => (
            <Card key={i}>
              <CardContent className="p-6">
                <div className="animate-pulse">
                  <div className="h-4 bg-gray-200 rounded w-3/4 mb-2"></div>
                  <div className="h-8 bg-gray-200 rounded w-1/2 mb-2"></div>
                  <div className="h-3 bg-gray-200 rounded w-2/3"></div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    );
  }

  const performanceStatus = getPerformanceStatus();

  return (
    <div className={`space-y-6 ${className}`}>
      {/* Header */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 student-analytics-header">
        <div>
          <h2 className="text-2xl font-bold tracking-tight text-gray-900">Performance Analytics</h2>
          <p className="text-gray-500">Comprehensive insights into your coding journey and progress.</p>
        </div>
        <div className="flex items-center gap-2 student-analytics-controls">
          <select
            value={selectedTimeframe}
            onChange={(e) => setSelectedTimeframe(e.target.value)}
            className="px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 student-analytics-timeframe"
          >
            <option value="7">Last 7 days</option>
            <option value="30">Last 30 days</option>
            <option value="90">Last 90 days</option>
          </select>
          <Button variant="outline" size="sm" className="touch-target">
            <Filter className="w-4 h-4 mr-2" />
            <span className="hidden sm:inline">Export</span>
          </Button>
        </div>
      </div>

      {/* Overview Stats */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 analytics-stats-grid">
        <StatCard
          title="Average Score"
          value={`${analyticsData?.average_score?.toFixed(1) || 0}%`}
          subtitle={`${performanceStatus.status} performance`}
          icon={Target}
          trend={analyticsData?.average_score > 80 ? "+5.2% from last month" : null}
          color={performanceStatus.color}
        />
        <StatCard
          title="Problems Solved"
          value={`${(analyticsData?.total_practice_completed || 0) + (analyticsData?.total_assignments_completed || 0)}`}
          subtitle={`${analyticsData?.total_practice_completed || 0} practice, ${analyticsData?.total_assignments_completed || 0} assignments`}
          icon={CheckCircle2}
          color="green"
        />
        <StatCard
          title="Current Streak"
          value={`${analyticsData?.current_streak || 0} days`}
          subtitle={`Best: ${analyticsData?.longest_streak || 0} days`}
          icon={Flame}
          trend={analyticsData?.current_streak >= 7 ? "Great momentum!" : null}
          color="orange"
        />
        <StatCard
          title="Time Invested"
          value={formatTime(analyticsData?.total_time_spent || 0)}
          subtitle="Total coding time"
          icon={Clock}
          color="purple"
        />
      </div>

      {/* Main Analytics Tabs */}
      <Tabs value={activeTab} onValueChange={setActiveTab} className="space-y-6 analytics-tabs">
        <TabsList className="grid w-full grid-cols-4 analytics-tab-list">
          <TabsTrigger value="overview" className="analytics-tab-trigger">Overview</TabsTrigger>
          <TabsTrigger value="trends" className="analytics-tab-trigger">Trends</TabsTrigger>
          <TabsTrigger value="concepts" className="analytics-tab-trigger">Concepts</TabsTrigger>
          <TabsTrigger value="comparison" className="analytics-tab-trigger">Comparison</TabsTrigger>
        </TabsList>

        {/* Overview Tab */}
        <TabsContent value="overview" className="space-y-6">
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {/* Performance Overview */}
            <Card className="lg:col-span-2">
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Activity className="w-5 h-5" />
                  Performance Overview
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  <div className="text-center progress-ring-container">
                    <ProgressRing 
                      percentage={analyticsData?.average_score || 0} 
                      color="#3B82F6"
                    />
                    <p className="text-sm font-medium text-gray-600 mt-2">Average Score</p>
                  </div>
                  <div className="text-center progress-ring-container">
                    <ProgressRing 
                      percentage={getCompletionRate()} 
                      color="#10B981"
                    />
                    <p className="text-sm font-medium text-gray-600 mt-2">Completion Rate</p>
                  </div>
                  <div className="text-center progress-ring-container">
                    <ProgressRing 
                      percentage={Math.min(100, (analyticsData?.current_streak || 0) * 10)} 
                      color="#F59E0B"
                    />
                    <p className="text-sm font-medium text-gray-600 mt-2">Streak Progress</p>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Quick Stats */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <BarChart3 className="w-5 h-5" />
                  Quick Stats
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <BookOpen className="w-4 h-4 text-blue-500" />
                    <span className="text-sm text-gray-600">Practice Questions</span>
                  </div>
                  <span className="font-semibold">{analyticsData?.total_practice_completed || 0}</span>
                </div>
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <Award className="w-4 h-4 text-green-500" />
                    <span className="text-sm text-gray-600">Assignments</span>
                  </div>
                  <span className="font-semibold">{analyticsData?.total_assignments_completed || 0}</span>
                </div>
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <Timer className="w-4 h-4 text-purple-500" />
                    <span className="text-sm text-gray-600">Avg. Session</span>
                  </div>
                  <span className="font-semibold">
                    {formatTime(Math.round((analyticsData?.total_time_spent || 0) / Math.max(1, (analyticsData?.total_practice_completed || 0) + (analyticsData?.total_assignments_completed || 0))))}
                  </span>
                </div>
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <Calendar className="w-4 h-4 text-orange-500" />
                    <span className="text-sm text-gray-600">Last Activity</span>
                  </div>
                  <span className="font-semibold text-sm">
                    {analyticsData?.last_activity ? new Date(analyticsData.last_activity).toLocaleDateString() : 'Never'}
                  </span>
                </div>
              </CardContent>
            </Card>
          </div>
        </TabsContent>

        {/* Trends Tab */}
        <TabsContent value="trends" className="space-y-6">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Performance Trend Chart */}
            <Card className="lg:col-span-2">
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <LineChart className="w-5 h-5" />
                  Performance Trends
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ResponsiveContainer width="100%" height={300}>
                  <AreaChart data={performanceTrends}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis 
                      dataKey="date" 
                      tick={{ fontSize: 12 }}
                      tickFormatter={(value) => new Date(value).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
                    />
                    <YAxis domain={[0, 100]} />
                    <Tooltip 
                      formatter={(value, name) => [
                        name === 'score' ? `${value}%` : value,
                        name === 'score' ? 'Score' : name === 'activities' ? 'Activities' : 'Time (min)'
                      ]}
                      labelFormatter={(label) => new Date(label).toLocaleDateString()}
                    />
                    <Area 
                      type="monotone" 
                      dataKey="score" 
                      stroke="#3B82F6" 
                      fill="#3B82F6" 
                      fillOpacity={0.3}
                      strokeWidth={2}
                    />
                  </AreaChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>

            {/* Activity Pattern */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Activity className="w-5 h-5" />
                  Activity Pattern
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ResponsiveContainer width="100%" height={250}>
                  <BarChart data={performanceTrends}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis 
                      dataKey="date" 
                      tick={{ fontSize: 12 }}
                      tickFormatter={(value) => new Date(value).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
                    />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey="activities" fill="#10B981" name="Activities" />
                  </BarChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>

            {/* Time Investment */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Clock className="w-5 h-5" />
                  Time Investment
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ResponsiveContainer width="100%" height={250}>
                  <BarChart data={performanceTrends}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis 
                      dataKey="date" 
                      tick={{ fontSize: 12 }}
                      tickFormatter={(value) => new Date(value).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
                    />
                    <YAxis />
                    <Tooltip formatter={(value) => [`${value} min`, 'Time Spent']} />
                    <Bar dataKey="time_spent" fill="#8B5CF6" name="Time (min)" />
                  </BarChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>
          </div>
        </TabsContent>

        {/* Concepts Tab */}
        <TabsContent value="concepts" className="space-y-6">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Concept Mastery Radar */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Brain className="w-5 h-5" />
                  Concept Mastery Overview
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ResponsiveContainer width="100%" height={300}>
                  <RadarChart data={Object.entries(conceptMastery).map(([concept, mastery]) => ({ concept, mastery }))}>
                    <PolarGrid />
                    <PolarAngleAxis dataKey="concept" tick={{ fontSize: 12 }} />
                    <PolarRadiusAxis domain={[0, 100]} />
                    <Radar
                      name="Mastery"
                      dataKey="mastery"
                      stroke="#3B82F6"
                      fill="#3B82F6"
                      fillOpacity={0.3}
                      strokeWidth={2}
                    />
                    <Tooltip />
                  </RadarChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>

            {/* Detailed Concept Breakdown */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Target className="w-5 h-5" />
                  Detailed Breakdown
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  {Object.entries(conceptMastery).map(([concept, mastery], index) => (
                    <ConceptMasteryCard
                      key={concept}
                      concept={concept}
                      mastery={mastery}
                      color={COLORS[index % COLORS.length]}
                    />
                  ))}
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Recommendations */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Star className="w-5 h-5" />
                Recommendations
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {Object.entries(conceptMastery)
                  .filter(([_, mastery]) => mastery < 70)
                  .slice(0, 4)
                  .map(([concept, mastery]) => (
                    <div key={concept} className="p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
                      <div className="flex items-center gap-2 mb-2">
                        <AlertCircle className="w-4 h-4 text-yellow-600" />
                        <h4 className="font-semibold text-yellow-900">{concept}</h4>
                      </div>
                      <p className="text-sm text-yellow-700 mb-2">
                        Current mastery: {mastery}% - Needs improvement
                      </p>
                      <Button size="sm" variant="outline" className="text-yellow-700 border-yellow-300 hover:bg-yellow-100">
                        Practice {concept}
                        <ChevronRight className="w-3 h-3 ml-1" />
                      </Button>
                    </div>
                  ))}
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Comparison Tab */}
        <TabsContent value="comparison" className="space-y-6">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Class Comparison */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Users className="w-5 h-5" />
                  Class Comparison
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-6">
                  {[
                    { metric: 'Average Score', student: analyticsData?.average_score || 0, classAvg: 78.5 },
                    { metric: 'Problems Solved', student: (analyticsData?.total_practice_completed || 0) + (analyticsData?.total_assignments_completed || 0), classAvg: 18 },
                    { metric: 'Time Spent (hrs)', student: Math.round((analyticsData?.total_time_spent || 0) / 60 * 10) / 10, classAvg: 12.3 },
                    { metric: 'Current Streak', student: analyticsData?.current_streak || 0, classAvg: 3.2 }
                  ].map((comparison, index) => (
                    <div key={index} className="space-y-2">
                      <div className="flex justify-between items-center">
                        <span className="text-sm font-medium text-gray-700">{comparison.metric}</span>
                        <div className="flex items-center gap-4">
                          <span className="text-lg font-bold text-blue-600">{comparison.student}</span>
                          <span className="text-sm text-gray-500">vs</span>
                          <span className="text-lg font-bold text-gray-400">{comparison.classAvg}</span>
                        </div>
                      </div>
                      <div className="w-full bg-gray-200 rounded-full h-2">
                        <div 
                          className="h-2 bg-blue-500 rounded-full transition-all duration-1000"
                          style={{ width: `${Math.min(100, (comparison.student / Math.max(comparison.student, comparison.classAvg)) * 100)}%` }}
                        />
                      </div>
                      <div className="flex justify-between text-xs text-gray-500">
                        <span>You: {comparison.student}</span>
                        <span>Class Avg: {comparison.classAvg}</span>
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Performance Percentile */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Trophy className="w-5 h-5" />
                  Performance Percentile
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-center mb-6">
                  <div className="text-4xl font-bold text-blue-600 mb-2">
                    {Math.round(((analyticsData?.average_score || 0) / 100) * 85)}th
                  </div>
                  <p className="text-gray-600">Percentile</p>
                  <p className="text-sm text-gray-500 mt-1">
                    You're performing better than {Math.round(((analyticsData?.average_score || 0) / 100) * 85)}% of students
                  </p>
                </div>
                
                <div className="space-y-4">
                  <div className="flex items-center justify-between p-3 bg-green-50 rounded-lg">
                    <div className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-green-600" />
                      <span className="text-sm font-medium text-green-900">Strengths</span>
                    </div>
                    <span className="text-sm text-green-700">Problem Solving</span>
                  </div>
                  
                  <div className="flex items-center justify-between p-3 bg-yellow-50 rounded-lg">
                    <div className="flex items-center gap-2">
                      <AlertCircle className="w-4 h-4 text-yellow-600" />
                      <span className="text-sm font-medium text-yellow-900">Areas to Improve</span>
                    </div>
                    <span className="text-sm text-yellow-700">Consistency</span>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </TabsContent>
      </Tabs>
    </div>
  );
};

export default StudentAnalyticsDashboard;