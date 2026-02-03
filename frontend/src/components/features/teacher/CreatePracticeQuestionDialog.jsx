import { useState, useEffect } from "react";
import { Plus, Trash2, Save, Loader2, AlertCircle } from "lucide-react";

import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "../../ui/dialog";
import { Button } from "../../ui/button";
import { Input } from "../../ui/input";
import { Label } from "../../ui/label";
import { Textarea } from "../../ui/textarea";
import { Card, CardContent, CardHeader, CardTitle } from "../../ui/card";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "../../ui/select";
import { Badge } from "../../ui/badge";

import { practiceService } from "../../../services/practiceService";

const TestCaseEditor = ({ testCase, index, onChange, onDelete }) => {
  const handleChange = (field, value) => {
    onChange(index, { ...testCase, [field]: value });
  };

  return (
    <Card className="border border-gray-200">
      <CardHeader className="pb-3">
        <div className="flex items-center justify-between">
          <CardTitle className="text-sm font-medium">
            Test Case {index + 1}
          </CardTitle>
          <Button
            variant="ghost"
            size="icon"
            onClick={() => onDelete(index)}
            className="h-8 w-8 text-gray-400 hover:text-red-600"
          >
            <Trash2 className="w-4 h-4" />
          </Button>
        </div>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="space-y-2">
            <Label className="text-xs font-medium text-gray-700">Input</Label>
            <Textarea
              placeholder="Enter test input..."
              value={testCase.input || ''}
              onChange={(e) => handleChange('input', e.target.value)}
              className="min-h-[80px] font-mono text-sm"
            />
          </div>
          <div className="space-y-2">
            <Label className="text-xs font-medium text-gray-700">Expected Output</Label>
            <Textarea
              placeholder="Enter expected output..."
              value={testCase.expected_output || ''}
              onChange={(e) => handleChange('expected_output', e.target.value)}
              className="min-h-[80px] font-mono text-sm"
            />
          </div>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="space-y-2">
            <Label className="text-xs font-medium text-gray-700">Explanation (Optional)</Label>
            <Input
              placeholder="Brief explanation of this test case..."
              value={testCase.explanation || ''}
              onChange={(e) => handleChange('explanation', e.target.value)}
              className="text-sm"
            />
          </div>
          <div className="space-y-2">
            <Label className="text-xs font-medium text-gray-700">Points</Label>
            <Input
              type="number"
              min="1"
              max="100"
              value={testCase.points || 10}
              onChange={(e) => handleChange('points', parseInt(e.target.value) || 10)}
              className="text-sm"
            />
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default function CreatePracticeQuestionDialog({ 
  open, 
  onOpenChange, 
  questionToEdit = null,
  onQuestionCreated,
  onQuestionUpdated 
}) {
  // Form State
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [difficulty, setDifficulty] = useState('medium');
  const [category, setCategory] = useState('');
  const [pointValue, setPointValue] = useState(100);
  const [starterCode, setStarterCode] = useState('');
  const [testCases, setTestCases] = useState([
    { input: '', expected_output: '', explanation: '', points: 10 }
  ]);

  // UI State
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const isEditMode = !!questionToEdit;

  // Load question data for editing
  useEffect(() => {
    if (questionToEdit) {
      setTitle(questionToEdit.title || '');
      setDescription(questionToEdit.description || '');
      setDifficulty(questionToEdit.difficulty || 'medium');
      setCategory(questionToEdit.category || '');
      setPointValue(questionToEdit.point_value || 100);
      setStarterCode(questionToEdit.starter_code || '');
      
      // Load test cases
      if (questionToEdit.test_cases && questionToEdit.test_cases.length > 0) {
        setTestCases(questionToEdit.test_cases.map(tc => ({
          input: tc.input || '',
          expected_output: tc.expected_output || '',
          explanation: tc.explanation || '',
          points: tc.points || 10
        })));
      } else {
        setTestCases([{ input: '', expected_output: '', explanation: '', points: 10 }]);
      }
    } else {
      // Reset form for new question
      setTitle('');
      setDescription('');
      setDifficulty('medium');
      setCategory('');
      setPointValue(100);
      setStarterCode('');
      setTestCases([{ input: '', expected_output: '', explanation: '', points: 10 }]);
    }
    setError(null);
  }, [questionToEdit, open]);

  const handleTestCaseChange = (index, updatedTestCase) => {
    setTestCases(prev => prev.map((tc, i) => i === index ? updatedTestCase : tc));
  };

  const handleAddTestCase = () => {
    setTestCases(prev => [...prev, { input: '', expected_output: '', explanation: '', points: 10 }]);
  };

  const handleDeleteTestCase = (index) => {
    if (testCases.length > 1) {
      setTestCases(prev => prev.filter((_, i) => i !== index));
    }
  };

  const validateForm = () => {
    if (!title.trim()) {
      setError('Question title is required');
      return false;
    }
    if (!description.trim()) {
      setError('Question description is required');
      return false;
    }
    if (!category.trim()) {
      setError('Category is required');
      return false;
    }
    if (testCases.length === 0) {
      setError('At least one test case is required');
      return false;
    }
    
    // Validate test cases
    for (let i = 0; i < testCases.length; i++) {
      const tc = testCases[i];
      if (!tc.input.trim() && !tc.expected_output.trim()) {
        setError(`Test case ${i + 1} must have either input or expected output`);
        return false;
      }
    }

    return true;
  };

  const handleSubmit = async () => {
    if (!validateForm()) {
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const questionData = {
        title: title.trim(),
        description: description.trim(),
        difficulty: difficulty,
        category: category.trim(),
        point_value: pointValue,
        starter_code: starterCode.trim(),
        test_cases: testCases.filter(tc => tc.input.trim() || tc.expected_output.trim()),
        is_active: true
      };

      if (isEditMode) {
        const response = await practiceService.updatePracticeQuestion(questionToEdit.id, questionData);
        onQuestionUpdated(response.data);
      } else {
        const response = await practiceService.createPracticeQuestion(questionData);
        onQuestionCreated(response.data);
      }

      onOpenChange(false);
    } catch (err) {
      console.error('Failed to save practice question:', err);
      const errorMessage = err.response?.data?.message || 
                          err.response?.data?.detail || 
                          `Failed to ${isEditMode ? 'update' : 'create'} practice question`;
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  const handleClose = () => {
    if (!loading) {
      onOpenChange(false);
    }
  };

  return (
    <Dialog open={open} onOpenChange={handleClose}>
      <DialogContent className="max-w-4xl max-h-[90vh] overflow-y-auto">
        <DialogHeader>
          <DialogTitle>
            {isEditMode ? 'Edit Practice Question' : 'Create Practice Question'}
          </DialogTitle>
        </DialogHeader>

        <div className="space-y-6">
          {error && (
            <div className="bg-red-50 text-red-600 p-4 rounded-lg flex items-center gap-3 border border-red-200">
              <AlertCircle className="w-5 h-5" />
              {error}
            </div>
          )}

          {/* Basic Information */}
          <Card>
            <CardHeader>
              <CardTitle className="text-lg">Question Details</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label htmlFor="title">Question Title *</Label>
                  <Input
                    id="title"
                    placeholder="e.g., Two Sum Problem"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="category">Category *</Label>
                  <Input
                    id="category"
                    placeholder="e.g., Arrays, Strings, Recursion"
                    value={category}
                    onChange={(e) => setCategory(e.target.value)}
                  />
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label>Difficulty *</Label>
                  <Select value={difficulty} onValueChange={setDifficulty}>
                    <SelectTrigger>
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="easy">Easy</SelectItem>
                      <SelectItem value="medium">Medium</SelectItem>
                      <SelectItem value="hard">Hard</SelectItem>
                    </SelectContent>
                  </Select>
                </div>
                <div className="space-y-2">
                  <Label htmlFor="pointValue">Point Value *</Label>
                  <Input
                    id="pointValue"
                    type="number"
                    min="1"
                    max="1000"
                    value={pointValue}
                    onChange={(e) => setPointValue(parseInt(e.target.value) || 100)}
                  />
                </div>
              </div>

              <div className="space-y-2">
                <Label htmlFor="description">Problem Description *</Label>
                <Textarea
                  id="description"
                  placeholder="Describe the problem clearly. Include examples, constraints, and any special requirements..."
                  className="min-h-[120px]"
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="starterCode">Starter Code (Optional)</Label>
                <Textarea
                  id="starterCode"
                  placeholder="def solution():\n    # Your code here\n    pass"
                  className="min-h-[100px] font-mono text-sm"
                  value={starterCode}
                  onChange={(e) => setStarterCode(e.target.value)}
                />
              </div>
            </CardContent>
          </Card>

          {/* Test Cases */}
          <Card>
            <CardHeader>
              <div className="flex items-center justify-between">
                <CardTitle className="text-lg">Test Cases</CardTitle>
                <Button
                  variant="outline"
                  size="sm"
                  onClick={handleAddTestCase}
                  className="gap-2"
                >
                  <Plus className="w-4 h-4" />
                  Add Test Case
                </Button>
              </div>
            </CardHeader>
            <CardContent className="space-y-4">
              {testCases.map((testCase, index) => (
                <TestCaseEditor
                  key={index}
                  testCase={testCase}
                  index={index}
                  onChange={handleTestCaseChange}
                  onDelete={handleDeleteTestCase}
                />
              ))}
              
              {testCases.length === 0 && (
                <div className="text-center py-8 text-gray-500">
                  <p>No test cases added yet.</p>
                  <Button
                    variant="outline"
                    onClick={handleAddTestCase}
                    className="mt-2 gap-2"
                  >
                    <Plus className="w-4 h-4" />
                    Add First Test Case
                  </Button>
                </div>
              )}
            </CardContent>
          </Card>

          {/* Actions */}
          <div className="flex justify-end gap-3 pt-4 border-t">
            <Button
              variant="outline"
              onClick={handleClose}
              disabled={loading}
            >
              Cancel
            </Button>
            <Button
              onClick={handleSubmit}
              disabled={loading}
              className="gap-2 min-w-[120px]"
            >
              {loading ? (
                <Loader2 className="w-4 h-4 animate-spin" />
              ) : (
                <Save className="w-4 h-4" />
              )}
              {isEditMode ? 'Update Question' : 'Create Question'}
            </Button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
}