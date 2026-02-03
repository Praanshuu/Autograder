import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import {
    Search,
    Filter,
    CheckCircle2,
    Clock,
    Trophy,
    Star,
    ArrowRight,
    Loader2,
    BookOpen,
    Target,
    Zap
} from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { Button } from "../../ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../../ui/card";
import { Badge } from "../../ui/badge";
import { Input } from "../../ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "../../ui/select";

import { practiceService } from "../../../services/practiceService";

const DIFFICULTY_COLORS = {
  easy: "bg-green-100 text-green-700 border-green-200",
  medium: "bg-yellow-100 text-yellow-700 border-yellow-200", 
  hard: "bg-red-100 text-red-700 border-red-200"
};

const DIFFICULTY_ICONS = {
  easy: <Target className="w-3 h-3" />,
  medium: <Zap className="w-3 h-3" />,
  hard: <Trophy className="w-3 h-3" />
};

export default function PracticeQuestionsList() {
    const navigate = useNavigate();
    const [questions, setQuestions] = useState([]);
    const [progress, setProgress] = useState({});
    const [loading, setLoading] = useState(true);
    const [searchTerm, setSearchTerm] = useState("");
    const [selectedDifficulty, setSelectedDifficulty] = useState("all");
    const [selectedCategory, setSelectedCategory] = useState("all");
    const [completionFilter, setCompletionFilter] = useState("all");
    const [sortBy, setSortBy] = useState("created_at");
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        fetchPracticeQuestions();
        fetchPracticeProgress();
    }, [selectedDifficulty, selectedCategory, completionFilter, sortBy]);

    const fetchPracticeQuestions = async () => {
        try {
            setLoading(true);
            const params = {
                ordering: sortBy === "created_at" ? "-created_at" : sortBy,
                search: searchTerm
            };
            
            if (selectedDifficulty !== "all") {
                params.difficulty = selectedDifficulty;
            }
            
            if (selectedCategory !== "all") {
                params.category = selectedCategory;
            }

            const response = await practiceService.getPracticeQuestions(params);
            const questionsData = Array.isArray(response.data) ? response.data : (response.data.results || []);
            setQuestions(questionsData);

            // Extract unique categories
            const uniqueCategories = [...new Set(questionsData.map(q => q.category).filter(Boolean))];
            setCategories(uniqueCategories);
        } catch (err) {
            console.error("Failed to load practice questions:", err);
        } finally {
            setLoading(false);
        }
    };

    const fetchPracticeProgress = async () => {
        try {
            const params = {};
            if (completionFilter === "completed") {
                params.completion_status = "completed";
            } else if (completionFilter === "in_progress") {
                params.completion_status = "in_progress";
            } else if (completionFilter === "not_started") {
                params.completion_status = "not_started";
            }

            const response = await practiceService.getPracticeProgress(params);
            const progressData = Array.isArray(response.data) ? response.data : (response.data.results || []);
            
            // Convert to lookup object
            const progressLookup = {};
            progressData.forEach(p => {
                progressLookup[p.practice_question] = p;
            });
            setProgress(progressLookup);
        } catch (err) {
            console.error("Failed to load practice progress:", err);
        }
    };

    const handleSearch = (e) => {
        setSearchTerm(e.target.value);
        // Debounce search
        clearTimeout(window.searchTimeout);
        window.searchTimeout = setTimeout(() => {
            fetchPracticeQuestions();
        }, 500);
    };

    const handleStartPractice = (question) => {
        navigate(`/student/practice/${question.id}`);
    };

    const getCompletionStatus = (question) => {
        const questionProgress = progress[question.id];
        if (!questionProgress) return "not_started";
        if (questionProgress.is_completed) return "completed";
        if (questionProgress.attempts_count > 0) return "in_progress";
        return "not_started";
    };

    const getStatusBadge = (question) => {
        const status = getCompletionStatus(question);
        const questionProgress = progress[question.id];
        
        switch (status) {
            case "completed":
                return (
                    <Badge className="bg-green-100 text-green-700 border-green-200">
                        <CheckCircle2 className="w-3 h-3 mr-1" />
                        Completed
                    </Badge>
                );
            case "in_progress":
                return (
                    <Badge className="bg-blue-100 text-blue-700 border-blue-200">
                        <Clock className="w-3 h-3 mr-1" />
                        In Progress ({questionProgress?.attempts_count || 0} attempts)
                    </Badge>
                );
            default:
                return (
                    <Badge variant="outline" className="text-gray-600 border-gray-200">
                        <BookOpen className="w-3 h-3 mr-1" />
                        Not Started
                    </Badge>
                );
        }
    };

    const filteredQuestions = questions.filter(question => {
        const status = getCompletionStatus(question);
        if (completionFilter !== "all" && status !== completionFilter) {
            return false;
        }
        return true;
    });

    if (loading) {
        return (
            <div className="py-12 flex justify-center">
                <Loader2 className="w-8 h-8 animate-spin text-indigo-600" />
            </div>
        );
    }

    return (
        <div className="space-y-6">
            {/* Header */}
            <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
                <div>
                    <h1 className="text-2xl font-bold text-gray-900">Practice Questions</h1>
                    <p className="text-gray-600">Improve your skills with unlimited practice</p>
                </div>
                <div className="text-sm text-gray-500">
                    {filteredQuestions.length} question{filteredQuestions.length !== 1 ? 's' : ''} available
                </div>
            </div>

            {/* Filters */}
            <Card>
                <CardContent className="p-4">
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
                        {/* Search */}
                        <div className="relative">
                            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
                            <Input
                                placeholder="Search questions..."
                                value={searchTerm}
                                onChange={handleSearch}
                                className="pl-10"
                            />
                        </div>

                        {/* Difficulty Filter */}
                        <Select value={selectedDifficulty} onValueChange={setSelectedDifficulty}>
                            <SelectTrigger>
                                <SelectValue placeholder="Difficulty" />
                            </SelectTrigger>
                            <SelectContent>
                                <SelectItem value="all">All Difficulties</SelectItem>
                                <SelectItem value="easy">Easy</SelectItem>
                                <SelectItem value="medium">Medium</SelectItem>
                                <SelectItem value="hard">Hard</SelectItem>
                            </SelectContent>
                        </Select>

                        {/* Category Filter */}
                        <Select value={selectedCategory} onValueChange={setSelectedCategory}>
                            <SelectTrigger>
                                <SelectValue placeholder="Category" />
                            </SelectTrigger>
                            <SelectContent>
                                <SelectItem value="all">All Categories</SelectItem>
                                {categories.map(category => (
                                    <SelectItem key={category} value={category}>
                                        {category.charAt(0).toUpperCase() + category.slice(1)}
                                    </SelectItem>
                                ))}
                            </SelectContent>
                        </Select>

                        {/* Completion Filter */}
                        <Select value={completionFilter} onValueChange={setCompletionFilter}>
                            <SelectTrigger>
                                <SelectValue placeholder="Status" />
                            </SelectTrigger>
                            <SelectContent>
                                <SelectItem value="all">All Status</SelectItem>
                                <SelectItem value="not_started">Not Started</SelectItem>
                                <SelectItem value="in_progress">In Progress</SelectItem>
                                <SelectItem value="completed">Completed</SelectItem>
                            </SelectContent>
                        </Select>

                        {/* Sort */}
                        <Select value={sortBy} onValueChange={setSortBy}>
                            <SelectTrigger>
                                <SelectValue placeholder="Sort by" />
                            </SelectTrigger>
                            <SelectContent>
                                <SelectItem value="created_at">Newest First</SelectItem>
                                <SelectItem value="title">Title A-Z</SelectItem>
                                <SelectItem value="difficulty">Difficulty</SelectItem>
                                <SelectItem value="point_value">Points</SelectItem>
                            </SelectContent>
                        </Select>
                    </div>
                </CardContent>
            </Card>

            {/* Questions List */}
            {filteredQuestions.length === 0 ? (
                <div className="text-center py-12 text-gray-500 bg-gray-50 rounded-lg border-2 border-dashed border-gray-200">
                    <BookOpen className="w-12 h-12 mx-auto mb-4 text-gray-400" />
                    <p className="text-lg font-medium mb-2">No practice questions found</p>
                    <p>Try adjusting your filters or search terms</p>
                </div>
            ) : (
                <div className="grid gap-4">
                    {filteredQuestions.map((question, idx) => (
                        <motion.div
                            key={question.id}
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: idx * 0.05 }}
                        >
                            <Card className="hover:shadow-md transition-all duration-200 group cursor-pointer border-l-4 border-l-transparent hover:border-l-indigo-600">
                                <div onClick={() => handleStartPractice(question)}>
                                    <CardContent className="p-6">
                                        <div className="flex items-start justify-between gap-4">
                                            <div className="flex-1 min-w-0">
                                                {/* Title and Status */}
                                                <div className="flex items-center gap-3 mb-2">
                                                    <h3 className="font-semibold text-gray-900 group-hover:text-indigo-600 transition-colors truncate">
                                                        {question.title}
                                                    </h3>
                                                    {getStatusBadge(question)}
                                                </div>

                                                {/* Description */}
                                                <p className="text-gray-600 text-sm mb-3 line-clamp-2">
                                                    {question.description}
                                                </p>

                                                {/* Metadata */}
                                                <div className="flex items-center gap-4 text-xs text-gray-500">
                                                    <div className="flex items-center gap-1">
                                                        <Badge className={DIFFICULTY_COLORS[question.difficulty] || DIFFICULTY_COLORS.medium}>
                                                            {DIFFICULTY_ICONS[question.difficulty]}
                                                            <span className="ml-1 capitalize">{question.difficulty}</span>
                                                        </Badge>
                                                    </div>
                                                    
                                                    {question.category && (
                                                        <span className="bg-gray-100 px-2 py-1 rounded text-gray-600">
                                                            {question.category.charAt(0).toUpperCase() + question.category.slice(1)}
                                                        </span>
                                                    )}
                                                    
                                                    <span className="flex items-center gap-1">
                                                        <Star className="w-3 h-3 text-yellow-500" />
                                                        {question.point_value} pts
                                                    </span>

                                                    {progress[question.id] && (
                                                        <span>
                                                            Best: {Math.round(progress[question.id].best_score)}%
                                                        </span>
                                                    )}
                                                </div>
                                            </div>

                                            {/* Action Button */}
                                            <Button 
                                                variant="ghost" 
                                                size="icon" 
                                                className="text-gray-300 group-hover:text-indigo-600 shrink-0"
                                            >
                                                <ArrowRight className="w-5 h-5" />
                                            </Button>
                                        </div>
                                    </CardContent>
                                </div>
                            </Card>
                        </motion.div>
                    ))}
                </div>
            )}
        </div>
    );
}