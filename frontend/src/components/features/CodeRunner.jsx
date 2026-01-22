import React, { useState, useEffect } from 'react';
import { Play, Square, Clock, CheckCircle, XCircle, AlertCircle } from 'lucide-react';
import { Button } from '../ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../ui/card';
import { Badge } from '../ui/badge';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../ui/tabs';
import { submissionService } from '../../services/submissionService';

const CodeRunner = () => {
  const [code, setCode] = useState('');
  const [language, setLanguage] = useState('python');
  const [isRunning, setIsRunning] = useState(false);
  const [results, setResults] = useState(null);
  const [sampleQuestions, setSampleQuestions] = useState([]);
  const [selectedQuestion, setSelectedQuestion] = useState(null);
  const [executionTime, setExecutionTime] = useState(0);

  // Load sample questions on component mount
  useEffect(() => {
    loadSampleQuestions();
  }, []);

  const loadSampleQuestions = async () => {
    try {
      const response = await submissionService.getSampleQuestions();
      if (response.success) {
        setSampleQuestions(response.data);
        if (response.data.length > 0) {
          selectQuestion(response.data[0]);
        }
      }
    } catch (error) {
      console.error('Failed to load sample questions:', error);
    }
  };

  const selectQuestion = (question) => {
    setSelectedQuestion(question);
    setCode(question.starter_code || '');
    setResults(null);
  };

  const runCode = async () => {
    if (!code.trim()) {
      alert('Please enter some code to run');
      return;
    }

    setIsRunning(true);
    setResults(null);
    const startTime = Date.now();

    try {
      const testCases = selectedQuestion ? selectedQuestion.test_cases : [
        { input: '', expected_output: 'Hello, World!' }
      ];

      const response = await submissionService.runCode({
        code,
        language,
        test_cases: testCases,
        question_id: selectedQuestion?.id
      });

      const endTime = Date.now();
      setExecutionTime(endTime - startTime);

      if (response.success) {
        setResults(response.data);
      } else {
        setResults({
          error: response.message || 'Execution failed',
          summary: { total: 0, passed: 0, failed: 0, all_passed: false }
        });
      }
    } catch (error) {
      const endTime = Date.now();
      setExecutionTime(endTime - startTime);
      
      setResults({
        error: error.message || 'Network error occurred',
        summary: { total: 0, passed: 0, failed: 0, all_passed: false }
      });
    } finally {
      setIsRunning(false);
    }
  };

  const getStatusIcon = (passed) => {
    if (passed) return <CheckCircle className="w-4 h-4 text-green-500" />;
    return <XCircle className="w-4 h-4 text-red-500" />;
  };

  const getStatusBadge = (passed) => {
    return (
      <Badge variant={passed ? "success" : "destructive"}>
        {passed ? "PASS" : "FAIL"}
      </Badge>
    );
  };

  return (
    <div className="max-w-6xl mx-auto p-6 space-y-6">
      <div className="text-center">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">
          🧠 Code Runner - Test Your Solutions
        </h1>
        <p className="text-gray-600">
          Write, test, and debug your code with instant feedback
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Question Selection */}
        <Card className="lg:col-span-1">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <AlertCircle className="w-5 h-5" />
              Sample Questions
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-2">
              {sampleQuestions.map((question) => (
                <button
                  key={question.id}
                  onClick={() => selectQuestion(question)}
                  className={`w-full text-left p-3 rounded-lg border transition-colors ${
                    selectedQuestion?.id === question.id
                      ? 'border-blue-500 bg-blue-50'
                      : 'border-gray-200 hover:border-gray-300'
                  }`}
                >
                  <div className="font-medium">{question.title}</div>
                  <div className="text-sm text-gray-500 mt-1">
                    {question.difficulty} • {question.points} points
                  </div>
                </button>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Code Editor and Controls */}
        <Card className="lg:col-span-2">
          <CardHeader>
            <div className="flex items-center justify-between">
              <CardTitle>
                {selectedQuestion ? selectedQuestion.title : 'Code Editor'}
              </CardTitle>
              <div className="flex items-center gap-2">
                <select
                  value={language}
                  onChange={(e) => setLanguage(e.target.value)}
                  className="px-3 py-1 border border-gray-300 rounded-md text-sm"
                >
                  <option value="python">Python</option>
                  <option value="javascript">JavaScript</option>
                  <option value="java">Java</option>
                  <option value="cpp">C++</option>
                </select>
                <Button
                  onClick={runCode}
                  disabled={isRunning}
                  className="flex items-center gap-2"
                >
                  {isRunning ? (
                    <>
                      <Square className="w-4 h-4" />
                      Running...
                    </>
                  ) : (
                    <>
                      <Play className="w-4 h-4" />
                      Run Code
                    </>
                  )}
                </Button>
              </div>
            </div>
          </CardHeader>
          <CardContent>
            {selectedQuestion && (
              <div className="mb-4 p-3 bg-gray-50 rounded-lg">
                <h4 className="font-medium mb-2">Problem Description:</h4>
                <p className="text-sm text-gray-700">{selectedQuestion.description}</p>
              </div>
            )}
            
            <textarea
              value={code}
              onChange={(e) => setCode(e.target.value)}
              placeholder="Write your code here..."
              className="w-full h-64 p-3 font-mono text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              style={{ fontFamily: 'Monaco, Consolas, "Courier New", monospace' }}
            />
          </CardContent>
        </Card>
      </div>

      {/* Results */}
      {results && (
        <Card>
          <CardHeader>
            <div className="flex items-center justify-between">
              <CardTitle className="flex items-center gap-2">
                <Clock className="w-5 h-5" />
                Execution Results
              </CardTitle>
              <div className="flex items-center gap-4 text-sm text-gray-600">
                <span>Execution Time: {executionTime}ms</span>
                {results.summary && (
                  <span>
                    Score: {results.summary.passed}/{results.summary.total}
                  </span>
                )}
              </div>
            </div>
          </CardHeader>
          <CardContent>
            {results.error ? (
              <div className="p-4 bg-red-50 border border-red-200 rounded-lg">
                <h4 className="font-medium text-red-800 mb-2">Error:</h4>
                <pre className="text-sm text-red-700 whitespace-pre-wrap">
                  {results.error}
                </pre>
              </div>
            ) : (
              <Tabs defaultValue="summary" className="w-full">
                <TabsList>
                  <TabsTrigger value="summary">Summary</TabsTrigger>
                  <TabsTrigger value="details">Test Details</TabsTrigger>
                </TabsList>
                
                <TabsContent value="summary" className="space-y-4">
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <div className="text-center p-3 bg-blue-50 rounded-lg">
                      <div className="text-2xl font-bold text-blue-600">
                        {results.summary?.total || 0}
                      </div>
                      <div className="text-sm text-blue-800">Total Tests</div>
                    </div>
                    <div className="text-center p-3 bg-green-50 rounded-lg">
                      <div className="text-2xl font-bold text-green-600">
                        {results.summary?.passed || 0}
                      </div>
                      <div className="text-sm text-green-800">Passed</div>
                    </div>
                    <div className="text-center p-3 bg-red-50 rounded-lg">
                      <div className="text-2xl font-bold text-red-600">
                        {results.summary?.failed || 0}
                      </div>
                      <div className="text-sm text-red-800">Failed</div>
                    </div>
                    <div className="text-center p-3 bg-gray-50 rounded-lg">
                      <div className="text-2xl font-bold text-gray-600">
                        {results.summary?.all_passed ? '100%' : 
                         Math.round((results.summary?.passed || 0) / (results.summary?.total || 1) * 100) + '%'}
                      </div>
                      <div className="text-sm text-gray-800">Success Rate</div>
                    </div>
                  </div>
                  
                  {results.summary?.all_passed && (
                    <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
                      <div className="flex items-center gap-2 text-green-800">
                        <CheckCircle className="w-5 h-5" />
                        <span className="font-medium">All tests passed! Great job! 🎉</span>
                      </div>
                    </div>
                  )}
                </TabsContent>
                
                <TabsContent value="details" className="space-y-3">
                  {results.results?.map((result, index) => (
                    <div
                      key={index}
                      className={`p-4 border rounded-lg ${
                        result.passed ? 'border-green-200 bg-green-50' : 'border-red-200 bg-red-50'
                      }`}
                    >
                      <div className="flex items-center justify-between mb-2">
                        <div className="flex items-center gap-2">
                          {getStatusIcon(result.passed)}
                          <span className="font-medium">Test Case {result.test_case_id}</span>
                          {getStatusBadge(result.passed)}
                        </div>
                        <span className="text-sm text-gray-600">
                          {result.execution_time}ms
                        </span>
                      </div>
                      
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                        <div>
                          <h5 className="font-medium mb-1">Input:</h5>
                          <pre className="bg-white p-2 rounded border text-xs">
                            {result.test_case?.input || 'No input'}
                          </pre>
                        </div>
                        <div>
                          <h5 className="font-medium mb-1">Expected Output:</h5>
                          <pre className="bg-white p-2 rounded border text-xs">
                            {result.expected_output}
                          </pre>
                        </div>
                        <div>
                          <h5 className="font-medium mb-1">Your Output:</h5>
                          <pre className={`p-2 rounded border text-xs ${
                            result.passed ? 'bg-white' : 'bg-red-50 border-red-200'
                          }`}>
                            {result.actual_output}
                          </pre>
                        </div>
                        {result.error && (
                          <div>
                            <h5 className="font-medium mb-1 text-red-700">Error:</h5>
                            <pre className="bg-red-50 p-2 rounded border border-red-200 text-xs text-red-700">
                              {result.error}
                            </pre>
                          </div>
                        )}
                      </div>
                    </div>
                  ))}
                </TabsContent>
              </Tabs>
            )}
          </CardContent>
        </Card>
      )}
    </div>
  );
};

export default CodeRunner;