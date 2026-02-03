import { useState, useEffect } from "react";
import { Search, BookOpen, Plus, Loader2, AlertCircle, Filter } from "lucide-react";

import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "../../ui/dialog";
import { Button } from "../../ui/button";
import { Input } from "../../ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "../../ui/card";
import { Badge } from "../../ui/badge";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "../../ui/select";

import { practiceService } from "../../../services/practiceService";

const getDifficultyColor = (difficulty) => {
  switch (difficulty?.toLowerCase()) {
    case 'easy':
      return 'bg-green-100 text-green-700 border-green-200';
    case 'medium':
      return 'bg-yellow-100 text-yellow-700 border-yellow-200';
    case 'hard':
      return 'bg-red-100 text-red-700 border-red-200';
    default:
      return 'bg-gray-100 text-gray-700 border-gray-200';
  }
};

const LibraryQuestionCard = ({ libraryEntry, onAdd, isAdding }) => {
  const question = libraryEntry.question;

  return (
    <Card className="h-full hover:shadow-md transition-all duration-200 border border-gray-200 hover:border-gray-300">
      <CardHeader className="pb-3">
        <div className="flex items-start justify-between">
          <div className="flex-1 min-w-0">
            <CardTitle className="text-base font-semibold text-gray-900 truncate">
              {question.title}
            </CardTitle>
            <div className="flex items-center gap-2 mt-2">
              <Badge className={`text-xs font-medium ${getDifficultyColor(question.difficulty)}`}>
                {question.difficulty}
              </Badge>
              <Badge variant="outline" className="text-xs">
                {question.category}
              </Badge>
            </div>
          </div>
        </div>
      </CardHeader>
      <CardContent className="pt-0">
        <p className="text-sm text-gray-600 mb-4 line-clamp-3">
          {question.description}
        </p>
        
        <div className="flex items-center justify-between text-sm text-gray-500 mb-4">
          <span>{question.point_value} points</span>
          <span>{question.test_cases?.length || 0} test cases</span>
        </div>

        {libraryEntry.tags && libraryEntry.tags.length > 0 && (
          <div className="flex flex-wrap gap-1 mb-4">
            {libraryEntry.tags.slice(0, 3).map((tag, index) => (
              <Badge key={index} variant="secondary" className="text-xs">
                {tag}
              </Badge>
            ))}
            {libraryEntry.tags.length > 3 && (
              <Badge variant="secondary" className="text-xs">
                +{libraryEntry.tags.length - 3} more
              </Badge>
            )}
          </div>
        )}

        <div className="pt-3 border-t border-gray-100">
          <Button
            onClick={() => onAdd(libraryEntry)}
            disabled={isAdding}
            className="w-full gap-2"
            size="sm"
          >
            {isAdding ? (
              <Loader2 className="w-4 h-4 animate-spin" />
            ) : (
              <Plus className="w-4 h-4" />
            )}
            {isAdding ? 'Adding...' : 'Add to My Questions'}
          </Button>
        </div>
      </CardContent>
    </Card>
  );
};

export default function PracticeLibraryDialog({ open, onOpenChange, onQuestionAdded }) {
  // Data State
  const [libraryQuestions, setLibraryQuestions] = useState([]);
  const [filteredQuestions, setFilteredQuestions] = useState([]);
  
  // UI State
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [difficultyFilter, setDifficultyFilter] = useState('all');
  const [categoryFilter, setCategoryFilter] = useState('all');
  const [addingQuestions, setAddingQuestions] = useState(new Set());

  // Derived data
  const categories = [...new Set(libraryQuestions.map(lq => lq.question.category).filter(Boolean))];

  // Load library questions
  const fetchLibraryQuestions = async () => {
    try {
      setLoading(true);
      const response = await practiceService.getPracticeLibrary();
      const data = Array.isArray(response.data) ? response.data : (response.data.results || []);
      setLibraryQuestions(data);
      setError(null);
    } catch (err) {
      console.error('Failed to fetch practice library:', err);
      setError('Failed to load practice library. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (open) {
      fetchLibraryQuestions();
    }
  }, [open]);

  // Filter questions based on search and filters
  useEffect(() => {
    let filtered = libraryQuestions;

    // Search filter
    if (searchTerm) {
      filtered = filtered.filter(lq => {
        const q = lq.question;
        return (
          q.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
          q.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
          q.category.toLowerCase().includes(searchTerm.toLowerCase()) ||
          (lq.tags && lq.tags.some(tag => tag.toLowerCase().includes(searchTerm.toLowerCase())))
        );
      });
    }

    // Difficulty filter
    if (difficultyFilter !== 'all') {
      filtered = filtered.filter(lq => lq.question.difficulty.toLowerCase() === difficultyFilter);
    }

    // Category filter
    if (categoryFilter !== 'all') {
      filtered = filtered.filter(lq => lq.question.category === categoryFilter);
    }

    setFilteredQuestions(filtered);
  }, [libraryQuestions, searchTerm, difficultyFilter, categoryFilter]);

  const handleAddQuestion = async (libraryEntry) => {
    const questionId = libraryEntry.question.id;
    setAddingQuestions(prev => new Set([...prev, questionId]));

    try {
      // Create a copy of the library question as a new practice question
      const questionData = {
        title: libraryEntry.question.title,
        description: libraryEntry.question.description,
        difficulty: libraryEntry.question.difficulty,
        category: libraryEntry.question.category,
        point_value: libraryEntry.question.point_value,
        starter_code: libraryEntry.question.starter_code || '',
        test_cases: libraryEntry.question.test_cases || [],
        is_active: true
      };

      const response = await practiceService.createPracticeQuestion(questionData);
      onQuestionAdded({ ...libraryEntry, question: response.data });
      
      // Show success feedback (you could add a toast notification here)
      console.log('Question added successfully');
    } catch (err) {
      console.error('Failed to add question:', err);
      alert('Failed to add question. Please try again.');
    } finally {
      setAddingQuestions(prev => {
        const newSet = new Set(prev);
        newSet.delete(questionId);
        return newSet;
      });
    }
  };

  const clearFilters = () => {
    setSearchTerm('');
    setDifficultyFilter('all');
    setCategoryFilter('all');
  };

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="max-w-6xl max-h-[90vh] overflow-y-auto">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2">
            <BookOpen className="w-5 h-5" />
            Practice Question Library
          </DialogTitle>
        </DialogHeader>

        <div className="space-y-6">
          {/* Filters */}
          <Card>
            <CardContent className="p-4">
              <div className="flex flex-col md:flex-row gap-4">
                <div className="flex-1">
                  <div className="relative">
                    <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
                    <Input
                      placeholder="Search library questions..."
                      value={searchTerm}
                      onChange={(e) => setSearchTerm(e.target.value)}
                      className="pl-10"
                    />
                  </div>
                </div>
                <div className="flex gap-3">
                  <Select value={difficultyFilter} onValueChange={setDifficultyFilter}>
                    <SelectTrigger className="w-32">
                      <SelectValue placeholder="Difficulty" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="all">All Levels</SelectItem>
                      <SelectItem value="easy">Easy</SelectItem>
                      <SelectItem value="medium">Medium</SelectItem>
                      <SelectItem value="hard">Hard</SelectItem>
                    </SelectContent>
                  </Select>
                  <Select value={categoryFilter} onValueChange={setCategoryFilter}>
                    <SelectTrigger className="w-40">
                      <SelectValue placeholder="Category" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="all">All Categories</SelectItem>
                      {categories.map(category => (
                        <SelectItem key={category} value={category}>
                          {category}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                  {(searchTerm || difficultyFilter !== 'all' || categoryFilter !== 'all') && (
                    <Button variant="outline" onClick={clearFilters} size="sm">
                      Clear
                    </Button>
                  )}
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Content */}
          {loading ? (
            <div className="flex justify-center items-center h-64">
              <Loader2 className="w-8 h-8 animate-spin text-indigo-600" />
            </div>
          ) : error ? (
            <div className="flex flex-col items-center justify-center h-64 text-red-500">
              <AlertCircle className="w-10 h-10 mb-2" />
              <p>{error}</p>
              <Button variant="outline" onClick={fetchLibraryQuestions} className="mt-4">
                Retry
              </Button>
            </div>
          ) : filteredQuestions.length === 0 ? (
            <div className="text-center py-20">
              {libraryQuestions.length === 0 ? (
                <>
                  <BookOpen className="w-16 h-16 text-gray-400 mx-auto mb-4" />
                  <h3 className="text-xl font-semibold text-gray-700 mb-2">
                    No library questions available
                  </h3>
                  <p className="text-gray-500">
                    The practice question library is currently empty.
                  </p>
                </>
              ) : (
                <>
                  <h3 className="text-xl font-semibold text-gray-700 mb-2">
                    No questions match your filters
                  </h3>
                  <p className="text-gray-500 mb-4">
                    Try adjusting your search terms or filters
                  </p>
                  <Button variant="outline" onClick={clearFilters}>
                    Clear Filters
                  </Button>
                </>
              )}
            </div>
          ) : (
            <>
              {/* Results Summary */}
              <div className="flex items-center justify-between">
                <p className="text-sm text-gray-600">
                  Showing {filteredQuestions.length} of {libraryQuestions.length} questions
                </p>
              </div>

              {/* Questions Grid */}
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {filteredQuestions.map((libraryEntry) => (
                  <LibraryQuestionCard
                    key={libraryEntry.id}
                    libraryEntry={libraryEntry}
                    onAdd={handleAddQuestion}
                    isAdding={addingQuestions.has(libraryEntry.question.id)}
                  />
                ))}
              </div>
            </>
          )}
        </div>
      </DialogContent>
    </Dialog>
  );
}