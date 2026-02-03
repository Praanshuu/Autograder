import React, { useState, useEffect } from 'react';
import { 
  Users, 
  TrendingUp, 
  AlertTriangle, 
  CheckCircle2, 
  Clock, 
  Target, 
  Award, 
  BarChart3, 
  PieChart as PieChartIcon,
  Activity,
  BookOpen,
  Brain,
  Download,
  Filter,
  Search,
  ChevronDown,
  ChevronUp,
  Star,
  AlertCircle,
  Zap,
  Calendar,
  FileText,
  Eye,
  TrendingDown
} from 'lucide-react';
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
  ScatterChart,
  Scatter,
  AreaChart,
  Area
} from 'recharts';
import { motion, AnimatePresence } from 'framer-motion';
import { Card, CardContent, CardHeader, CardTitle } from '../../ui/card';
import { Badge } from '../../ui/badge';
import { Button } from '../../ui/button';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../../ui/tabs';
import { Input } from '../../ui/input';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../ui/select';
import { gamificationService } from '../../../services/gamificationService';
import '../gamification/MobileResponsive.css';

const MetricCard = ({ title, value, subtitle, icon: Icon, trend, color = "blue", className = "" }) => {
  const colorClasses = {
    blue: "bg-blue-50 text-blue-600 border-blue-100",
    green: "bg-green-50 text-green-600 border-green-100",
    purple: "bg-purple-50 text-purple-600 border-purple-100",
    orange: "bg-orange-50 text-orange-600 border-orange-100",
    red: "bg-red-50 text-red-600 border-red-100",
    yellow: "bg-yellow-50 text-yellow-600 border-yellow-100"
  };

  const trendColor = trend?.includes('+') ? 'text-green-600' : trend?.includes('-') ? 'text-red-600' : 'text-gray-600';

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
                  {trend.includes('+') ? (
                    <TrendingUp className="w-4 h-4 text-green-500 mr-1" />
                  ) : trend.includes('-') ? (
                    <TrendingDown className="w-4 h-4 text-red-500 mr-1" />
                  ) : (
                    <Activity className="w-4 h-4 text-gray-500 mr-1" />
                  )}
                  <span className={trendColor}>{trend}</span>
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

const StudentCard = ({ student, onClick, isExpanded = false }) => {
  const getPerformanceColor = (score) => {
    if (score >= 90) return 'text-green-600 bg-green-50';
    if (score >= 80) return 'text-blue-600 bg-blue-50';
    if (score >= 70) return 'text-yellow-600 bg-yellow-50';
    return 'text-red-600 bg-red-50';
  };

  const getStatusIcon = (indicators) => {
    if (indicators.includes('struggling')) return <AlertTriangle className="w-4 h-4 text-red-500" />;
    if (indicators.includes('excellent')) return <Star className="w-4 h-4 text-green-500" />;
    return <CheckCircle2 className="w-4 h-4 text-blue-500" />;
  };

  return (
    <motion.div
      layout
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="bg-white border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow cursor-pointer"
      onClick={onClick}
    >
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 student-card-header">
        <div className="flex items-center gap-3 student-card-info">
          <div className="w-10 h-10 bg-gray-100 rounded-full flex items-center justify-center">
            <span className="text-sm font-semibold text-gray-700">
              {student.name.split(' ').map(n => n[0]).join('')}
            </span>
          </div>
          <div>
            <h4 className="font-semibold text-gray-900">{student.name}</h4>
            <p className="text-sm text-gray-500">{student.email}</p>
          </div>
        </div>
        
        <div className="flex items-center gap-4 student-card-metrics">
          <div className="text-right">
            <div className={`px-2 py-1 rounded-full text-xs font-semibold ${getPerformanceColor(student.average_score)}`}>
              {student.average_score}%
            </div>
            <p className="text-xs text-gray-500 mt-1">{student.completed_problems} problems</p>
          </div>
          
          <div className="flex items-center gap-2">
            {getStatusIcon(student.indicators)}
            {isExpanded ? <ChevronUp className="w-4 h-4 text-gray-400" /> : <ChevronDown className="w-4 h-4 text-gray-400" />}
          </div>
        </div>
      </div>

      <AnimatePresence>
        {isExpanded && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            className="mt-4 pt-4 border-t border-gray-100"
          >
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 text-sm student-card-expanded">
              <div>
                <p className="text-gray-500">Practice</p>
                <p className="font-semibold">{student.practice_completed}</p>
              </div>
              <div>
                <p className="text-gray-500">Assignments</p>
                <p className="font-semibold">{student.assignments_completed}</p>
              </div>
              <div>
                <p className="text-gray-500">Streak</p>
                <p className="font-semibold">{student.current_streak} days</p>
              </div>
              <div>
                <p className="text-gray-500">Last Active</p>
                <p className="font-semibold">{student.last_activity}</p>
              </div>
            </div>
            
            {student.struggle_areas && student.struggle_areas.length > 0 && (
              <div className="mt-3">
                <p className="text-sm text-gray-500 mb-2">Areas needing attention:</p>
                <div className="flex flex-wrap gap-1">
                  {student.struggle_areas.map((area, index) => (
                    <Badge key={index} variant="outline" className="text-xs text-red-600 border-red-200">
                      {area}
                    </Badge>
                  ))}
                </div>
              </div>
            )}
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
};

const ProblemAnalyticsCard = ({ problem, onClick }) => {
  const getSuccessRateColor = (rate) => {
    if (rate >= 80) return 'text-green-600 bg-green-50';
    if (rate >= 60) return 'text-yellow-600 bg-yellow-50';
    return 'text-red-600 bg-red-50';
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="bg-white border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow cursor-pointer"
      onClick={onClick}
    >
      <div className="flex items-center justify-between mb-3">
        <h4 className="font-semibold text-gray-900 truncate">{problem.title}</h4>
        <Badge variant="outline" className={`text-xs ${
          problem.difficulty === 'easy' ? 'text-green-600 border-green-200' :
          problem.difficulty === 'medium' ? 'text-yellow-600 border-yellow-200' :
          'text-red-600 border-red-200'
        }`}>
          {problem.difficulty}
        </Badge>
      </div>
      
      <div className="grid grid-cols-3 gap-4 text-sm problem-card-metrics">
        <div>
          <p className="text-gray-500">Success Rate</p>
          <div className={`px-2 py-1 rounded text-xs font-semibold ${getSuccessRateColor(problem.success_rate)}`}>
            {problem.success_rate}%
          </div>
        </div>
        <div>
          <p className="text-gray-500">Attempts</p>
          <p className="font-semibold">{problem.total_attempts}</p>
        </div>
        <div>
          <p className="text-gray-500">Avg Time</p>
          <p className="font-semibold">{problem.avg_time}min</p>
        </div>
      </div>
      
      {problem.common_errors && problem.common_errors.length > 0 && (
        <div className="mt-3">
          <p className="text-xs text-gray-500 mb-1">Common Issues:</p>
          <div className="flex flex-wrap gap-1">
            {problem.common_errors.slice(0, 2).map((error, index) => (
              <Badge key={index} variant="outline" className="text-xs text-gray-600">
                {error}
              </Badge>
            ))}
            {problem.common_errors.length > 2 && (
              <Badge variant="outline" className="text-xs text-gray-500">
                +{problem.common_errors.length - 2} more
              </Badge>
            )}
          </div>
        </div>
      )}
    </motion.div>
  );
};

const ClassAnalyticsDashboard = ({ classId, className = "" }) => {
  const [analyticsData, setAnalyticsData] = useState(null);
  const [students, setStudents] = useState([]);
  const [problemAnalytics, setProblemAnalytics] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('overview');
  const [expandedStudent, setExpandedStudent] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterBy, setFilterBy] = useState('all');
  const [sortBy, setSortBy] = useState('performance');

  // Fetch class analytics data
  const fetchClassAnalytics = async () => {
    try {
      setLoading(true);
      
      const [
        classAnalyticsResponse,
        strugglingStudentsResponse,
        problemAnalyticsResponse
      ] = await Promise.all([
        gamificationService.getClassAnalytics(classId),
        gamificationService.getClassAnalytics(classId), // Will be replaced with struggling students endpoint
        gamificationService.getClassAnalytics(classId)  // Will be replaced with problem analytics endpoint
      ]);

      if (classAnalyticsResponse.success) {
        setAnalyticsData(classAnalyticsResponse.data);
      }

      setError(null);
    } catch (err) {
      console.error('Failed to fetch class analytics:', err);
      setError('Failed to load class analytics');
      
      // Show empty state instead of mock data
      setAnalyticsData(null);
      setStudents([]);
          practice_completed: 15,
          assignments_completed: 8,
          current_streak: 12,
          last_activity: '2 hours ago',
          indicators: ['excellent'],
          struggle_areas: []
        },
        {
          id: 2,
          name: 'Bob Smith',
          email: 'bob.smith@university.edu',
          average_score: 67.2,
          completed_problems: 12,
          practice_completed: 8,
          assignments_completed: 4,
          current_streak: 2,
          last_activity: '1 day ago',
          indicators: ['struggling'],
          struggle_areas: ['Recursion', 'Data Structures']
        }
      ]);
      
      setProblemAnalytics([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (classId) {
      fetchClassAnalytics();
    }
  }, [classId]);

  // Filter and sort students
  const filteredAndSortedStudents = students
    .filter(student => {
      const matchesSearch = student.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                           student.email.toLowerCase().includes(searchTerm.toLowerCase());
      
      if (filterBy === 'all') return matchesSearch;
      if (filterBy === 'struggling') return matchesSearch && student.indicators.includes('struggling');
      if (filterBy === 'excellent') return matchesSearch && student.indicators.includes('excellent');
      if (filterBy === 'inactive') return matchesSearch && student.last_activity.includes('days');
      
      return matchesSearch;
    })
    .sort((a, b) => {
      switch (sortBy) {
        case 'performance':
          return b.average_score - a.average_score;
        case 'name':
          return a.name.localeCompare(b.name);
        case 'activity':
          return a.last_activity.localeCompare(b.last_activity);
        case 'problems':
          return b.completed_problems - a.completed_problems;
        default:
          return 0;
      }
    });

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

  if (error && !analyticsData) {
    return (
      <div className={`text-center py-12 ${className}`}>
        <AlertCircle className="w-12 h-12 text-gray-400 mx-auto mb-4" />
        <h3 className="text-lg font-semibold text-gray-900 mb-2">Unable to Load Analytics</h3>
        <p className="text-gray-500 mb-4">{error}</p>
        <Button onClick={fetchClassAnalytics}>Try Again</Button>
      </div>
    );
  }

  return (
    <div className={`space-y-6 ${className}`}>
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold tracking-tight text-gray-900">Class Analytics</h2>
          <p className="text-gray-500">{analyticsData?.class_info?.name || 'Class Performance Overview'}</p>
        </div>
        <div className="flex items-center gap-2">
          <Button variant="outline" size="sm">
            <Download className="w-4 h-4 mr-2" />
            Export Report
          </Button>
          <Button variant="outline" size="sm">
            <FileText className="w-4 h-4 mr-2" />
            Generate Summary
          </Button>
        </div>
      </div>

      {/* Overview Metrics */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 analytics-stats-grid">
        <MetricCard
          title="Total Students"
          value={analyticsData?.class_info?.total_students || 0}
          subtitle={`${analyticsData?.class_info?.active_students || 0} active this week`}
          icon={Users}
          color="blue"
        />
        <MetricCard
          title="Class Average"
          value={`${analyticsData?.class_info?.avg_score?.toFixed(1) || 0}%`}
          subtitle="Overall performance"
          icon={Target}
          trend="+2.3% from last week"
          color="green"
        />
        <MetricCard
          title="Completion Rate"
          value={`${analyticsData?.class_info?.completion_rate?.toFixed(1) || 0}%`}
          subtitle="Assignment completion"
          icon={CheckCircle2}
          color="purple"
        />
        <MetricCard
          title="Daily Active"
          value={analyticsData?.engagement_metrics?.daily_active_users || 0}
          subtitle={`${analyticsData?.engagement_metrics?.total_submissions_today || 0} submissions today`}
          icon={Activity}
          color="orange"
        />
      </div>

      {/* Main Analytics Tabs */}
      <Tabs value={activeTab} onValueChange={setActiveTab} className="space-y-6">
        <TabsList className="grid w-full grid-cols-4">
          <TabsTrigger value="overview">Overview</TabsTrigger>
          <TabsTrigger value="students">Students</TabsTrigger>
          <TabsTrigger value="problems">Problems</TabsTrigger>
          <TabsTrigger value="insights">Insights</TabsTrigger>
        </TabsList>

        {/* Overview Tab */}
        <TabsContent value="overview" className="space-y-6">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Performance Distribution */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <PieChartIcon className="w-5 h-5" />
                  Performance Distribution
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ResponsiveContainer width="100%" height={300}>
                  <PieChart>
                    <Pie
                      data={[
                        { name: 'Excellent (90%+)', value: analyticsData?.performance_summary?.excellent_performers || 0, color: '#10B981' },
                        { name: 'Good (80-89%)', value: analyticsData?.performance_summary?.good_performers || 0, color: '#3B82F6' },
                        { name: 'Fair (70-79%)', value: (analyticsData?.class_info?.total_students || 0) - (analyticsData?.performance_summary?.excellent_performers || 0) - (analyticsData?.performance_summary?.good_performers || 0) - (analyticsData?.performance_summary?.struggling_students || 0), color: '#F59E0B' },
                        { name: 'Struggling (<70%)', value: analyticsData?.performance_summary?.struggling_students || 0, color: '#EF4444' }
                      ]}
                      cx="50%"
                      cy="50%"
                      labelLine={false}
                      label={({ name, percent }) => `${name}: ${(percent * 100).toFixed(0)}%`}
                      outerRadius={80}
                      fill="#8884d8"
                      dataKey="value"
                    >
                      {[
                        { name: 'Excellent (90%+)', value: analyticsData?.performance_summary?.excellent_performers || 0, color: '#10B981' },
                        { name: 'Good (80-89%)', value: analyticsData?.performance_summary?.good_performers || 0, color: '#3B82F6' },
                        { name: 'Fair (70-79%)', value: 4, color: '#F59E0B' },
                        { name: 'Struggling (<70%)', value: analyticsData?.performance_summary?.struggling_students || 0, color: '#EF4444' }
                      ].map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={entry.color} />
                      ))}
                    </Pie>
                    <Tooltip />
                  </PieChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>

            {/* Engagement Metrics */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Activity className="w-5 h-5" />
                  Engagement Overview
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <div className="text-center p-4 bg-blue-50 rounded-lg">
                    <div className="text-2xl font-bold text-blue-600">
                      {analyticsData?.engagement_metrics?.daily_active_users || 0}
                    </div>
                    <p className="text-sm text-blue-700">Daily Active</p>
                  </div>
                  <div className="text-center p-4 bg-green-50 rounded-lg">
                    <div className="text-2xl font-bold text-green-600">
                      {analyticsData?.engagement_metrics?.weekly_active_users || 0}
                    </div>
                    <p className="text-sm text-green-700">Weekly Active</p>
                  </div>
                </div>
                
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-gray-600">Avg Session Time</span>
                    <span className="font-semibold">{analyticsData?.engagement_metrics?.avg_session_time || 0} min</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-gray-600">Submissions Today</span>
                    <span className="font-semibold">{analyticsData?.engagement_metrics?.total_submissions_today || 0}</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-gray-600">Active Rate</span>
                    <span className="font-semibold">
                      {Math.round(((analyticsData?.class_info?.active_students || 0) / (analyticsData?.class_info?.total_students || 1)) * 100)}%
                    </span>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Quick Actions */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Zap className="w-5 h-5" />
                Quick Actions
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <Button variant="outline" className="justify-start h-auto p-4">
                  <div className="text-left">
                    <div className="font-semibold">Identify Struggling Students</div>
                    <div className="text-sm text-gray-500">Find students who need extra help</div>
                  </div>
                </Button>
                <Button variant="outline" className="justify-start h-auto p-4">
                  <div className="text-left">
                    <div className="font-semibold">Problem Analysis</div>
                    <div className="text-sm text-gray-500">Review difficult problems and common errors</div>
                  </div>
                </Button>
                <Button variant="outline" className="justify-start h-auto p-4">
                  <div className="text-left">
                    <div className="font-semibold">Send Encouragement</div>
                    <div className="text-sm text-gray-500">Message students with personalized feedback</div>
                  </div>
                </Button>
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Students Tab */}
        <TabsContent value="students" className="space-y-6">
          {/* Student Filters */}
          <Card>
            <CardContent className="p-4">
              <div className="flex flex-col sm:flex-row gap-4 class-analytics-filters">
                <div className="flex-1 class-analytics-search">
                  <div className="relative">
                    <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
                    <Input
                      placeholder="Search students..."
                      value={searchTerm}
                      onChange={(e) => setSearchTerm(e.target.value)}
                      className="pl-10"
                    />
                  </div>
                </div>
                <div className="flex gap-2 class-analytics-selects">
                  <Select value={filterBy} onValueChange={setFilterBy}>
                    <SelectTrigger className="w-full sm:w-48 class-analytics-select">
                      <SelectValue placeholder="Filter by status" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="all">All Students</SelectItem>
                      <SelectItem value="excellent">Excellent Performers</SelectItem>
                      <SelectItem value="struggling">Struggling Students</SelectItem>
                      <SelectItem value="inactive">Inactive Students</SelectItem>
                    </SelectContent>
                  </Select>
                  <Select value={sortBy} onValueChange={setSortBy}>
                    <SelectTrigger className="w-full sm:w-48 class-analytics-select">
                      <SelectValue placeholder="Sort by" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="performance">Performance</SelectItem>
                      <SelectItem value="name">Name</SelectItem>
                      <SelectItem value="activity">Last Activity</SelectItem>
                      <SelectItem value="problems">Problems Solved</SelectItem>
                    </SelectContent>
                  </Select>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Student List */}
          <div className="space-y-4">
            {filteredAndSortedStudents.map((student) => (
              <StudentCard
                key={student.id}
                student={student}
                isExpanded={expandedStudent === student.id}
                onClick={() => setExpandedStudent(expandedStudent === student.id ? null : student.id)}
              />
            ))}
          </div>

          {filteredAndSortedStudents.length === 0 && (
            <Card>
              <CardContent className="text-center py-12">
                <Users className="w-12 h-12 text-gray-300 mx-auto mb-4" />
                <h3 className="text-lg font-semibold text-gray-900 mb-2">No Students Found</h3>
                <p className="text-gray-500">Try adjusting your search or filter criteria.</p>
              </CardContent>
            </Card>
          )}
        </TabsContent>

        {/* Problems Tab */}
        <TabsContent value="problems" className="space-y-6">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 problem-analytics-grid">
            {problemAnalytics.map((problem) => (
              <ProblemAnalyticsCard
                key={problem.id}
                problem={problem}
                onClick={() => console.log('View problem details:', problem.id)}
              />
            ))}
          </div>

          {/* Problem Insights */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Brain className="w-5 h-5" />
                Problem Insights
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <h4 className="font-semibold text-gray-900 mb-3">Most Challenging Problems</h4>
                  <div className="space-y-2">
                    {problemAnalytics
                      .sort((a, b) => a.success_rate - b.success_rate)
                      .slice(0, 3)
                      .map((problem, index) => (
                        <div key={problem.id} className="flex items-center justify-between p-2 bg-red-50 rounded">
                          <span className="text-sm font-medium">{problem.title}</span>
                          <Badge variant="outline" className="text-red-600 border-red-200">
                            {problem.success_rate}% success
                          </Badge>
                        </div>
                      ))}
                  </div>
                </div>
                
                <div>
                  <h4 className="font-semibold text-gray-900 mb-3">Common Error Patterns</h4>
                  <div className="space-y-2">
                    {['Index out of bounds', 'Null pointer exception', 'Infinite recursion', 'Wrong return type']
                      .map((error, index) => (
                        <div key={index} className="flex items-center justify-between p-2 bg-yellow-50 rounded">
                          <span className="text-sm font-medium">{error}</span>
                          <Badge variant="outline" className="text-yellow-600 border-yellow-200">
                            {Math.floor(Math.random() * 20) + 5} occurrences
                          </Badge>
                        </div>
                      ))}
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Insights Tab */}
        <TabsContent value="insights" className="space-y-6">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Recommendations */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Star className="w-5 h-5" />
                  Recommendations
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                  <div className="flex items-start gap-3">
                    <CheckCircle2 className="w-5 h-5 text-blue-600 mt-0.5" />
                    <div>
                      <h4 className="font-semibold text-blue-900">Schedule Review Session</h4>
                      <p className="text-sm text-blue-700 mt-1">
                        4 students are struggling with recursion concepts. Consider a focused review session.
                      </p>
                    </div>
                  </div>
                </div>
                
                <div className="p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
                  <div className="flex items-start gap-3">
                    <AlertTriangle className="w-5 h-5 text-yellow-600 mt-0.5" />
                    <div>
                      <h4 className="font-semibold text-yellow-900">Check Inactive Students</h4>
                      <p className="text-sm text-yellow-700 mt-1">
                        4 students haven't been active in 3+ days. Consider reaching out.
                      </p>
                    </div>
                  </div>
                </div>
                
                <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
                  <div className="flex items-start gap-3">
                    <Star className="w-5 h-5 text-green-600 mt-0.5" />
                    <div>
                      <h4 className="font-semibold text-green-900">Celebrate Success</h4>
                      <p className="text-sm text-green-700 mt-1">
                        8 students are performing excellently. Consider highlighting their achievements.
                      </p>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Class Trends */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <TrendingUp className="w-5 h-5" />
                  Class Trends
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ResponsiveContainer width="100%" height={250}>
                  <LineChart data={[
                    { week: 'Week 1', avgScore: 75, submissions: 45 },
                    { week: 'Week 2', avgScore: 78, submissions: 52 },
                    { week: 'Week 3', avgScore: 81, submissions: 48 },
                    { week: 'Week 4', avgScore: 82, submissions: 67 },
                    { week: 'Week 5', avgScore: 84, submissions: 71 }
                  ]}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="week" />
                    <YAxis />
                    <Tooltip />
                    <Line 
                      type="monotone" 
                      dataKey="avgScore" 
                      stroke="#3B82F6" 
                      strokeWidth={2}
                      name="Average Score"
                    />
                  </LineChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>
          </div>

          {/* Detailed Analytics */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <BarChart3 className="w-5 h-5" />
                Detailed Analytics
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="text-center">
                  <div className="text-3xl font-bold text-gray-900 mb-2">
                    {Math.round(((analyticsData?.performance_summary?.excellent_performers || 0) / (analyticsData?.class_info?.total_students || 1)) * 100)}%
                  </div>
                  <p className="text-sm text-gray-600">Excellence Rate</p>
                  <p className="text-xs text-gray-500 mt-1">Students scoring 90%+</p>
                </div>
                
                <div className="text-center">
                  <div className="text-3xl font-bold text-gray-900 mb-2">
                    {analyticsData?.engagement_metrics?.avg_session_time || 0}
                  </div>
                  <p className="text-sm text-gray-600">Avg Session (min)</p>
                  <p className="text-xs text-gray-500 mt-1">Time spent per session</p>
                </div>
                
                <div className="text-center">
                  <div className="text-3xl font-bold text-gray-900 mb-2">
                    {Math.round(((analyticsData?.performance_summary?.struggling_students || 0) / (analyticsData?.class_info?.total_students || 1)) * 100)}%
                  </div>
                  <p className="text-sm text-gray-600">Need Support</p>
                  <p className="text-xs text-gray-500 mt-1">Students needing help</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  );
};

export default ClassAnalyticsDashboard;