
import os

file_path = '/home/anshul/Projects/Autograder/frontend/src/pages/teacher/AssignmentDashboard.jsx'

with open(file_path, 'r') as f:
    lines = f.readlines()

nested_use_memo_line = -1

# Find the nested useMemo (indented deep)
for i, line in enumerate(lines):
    if 'useMemo' in line and len(line) - len(line.lstrip()) > 20:
        nested_use_memo_line = i
        break

if nested_use_memo_line != -1:
    print(f"Found nested useMemo at line {nested_use_memo_line+1}")
    
    # Search backwards for start of IIFE
    start_line = -1
    for i in range(nested_use_memo_line, -1, -1):
        if '(() => {' in lines[i]:
            start_line = i
            break
            
    # Search forwards for end of IIFE
    end_line = -1
    for i in range(nested_use_memo_line, len(lines)):
        if '})()' in lines[i]:
            end_line = i
            # We want to include this line in replacement
            break
            
    if start_line != -1 and end_line != -1:
        print(f"Replacing block from {start_line+1} to {end_line+1}")
        
        new_content = [
            '                                {validSubs.length === 0 ? (\n',
            '                                    <Card className="border-dashed bg-gray-50/50">\n',
            '                                        <CardContent className="flex flex-col items-center justify-center py-20 text-center">\n',
            '                                            <div className="bg-white p-4 rounded-full shadow-sm mb-4">\n',
            '                                                <Clock className="w-10 h-10 text-indigo-400" />\n',
            '                                            </div>\n',
            '                                            <h3 className="text-xl font-semibold text-gray-900 mb-2">\n',
            '                                                {new Date(assignment.due_date) > new Date() ? "Analytics In Progress" : "No Data Available"}\n',
            '                                            </h3>\n',
            '                                            <p className="text-gray-500 max-w-sm mx-auto mb-6">\n',
            '                                                {new Date(assignment.due_date) > new Date()\n',
            '                                                    ? "This assignment is currently active. Graphs and insights will populate automatically as students submit their work."\n',
            '                                                    : "No graded submissions were found for this question."}\n',
            '                                            </p>\n',
            '                                            {submissions.filter(s => (s.question_id || s.question?.id) === selectedQuestion).length > 0 && (\n',
            '                                                <p className="text-xs text-amber-600 font-medium bg-amber-50 px-3 py-1 rounded-full border border-amber-200">\n',
            '                                                     Pending submissions waiting to be graded\n',
            '                                                </p>\n',
            '                                            )}\n',
            '                                        </CardContent>\n',
            '                                    </Card>\n',
            '                                ) : (\n',
            '                                    <div className="space-y-6">\n',
            '                                        {/* Row 1: Key Performance Metrics */}\n',
            '                                        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 h-[400px]">\n',
            '                                            <div className="lg:col-span-2 h-full">\n',
            '                                                <PerformanceMatrix\n',
            '                                                    submissions={validSubs}\n',
            '                                                />\n',
            '                                            </div>\n',
            '                                            <div className="lg:col-span-1 h-full">\n',
            '                                                <BoxPlotChart\n',
            '                                                    data={boxPlotData}\n',
            '                                                />\n',
            '                                            </div>\n',
            '                                        </div>\n',
            '\n',
            '                                        {/* Row 2: Deep Dive (Heatmap + Word Cloud) */}\n',
            '                                        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 h-[400px]">\n',
            '                                            <div className="lg:col-span-2 h-full">\n',
            '                                                <ErrorHeatmap\n',
            '                                                    questions={heatmapQuestions}\n',
            '                                                />\n',
            '                                            </div>\n',
            '                                            <div className="lg:col-span-1 h-full">\n',
            '                                                <ErrorWordCloud\n',
            '                                                    data={wordCloudData}\n',
            '                                                    selectedTag={selectedAnalyticsTag}\n',
            '                                                    onSelectTag={setSelectedAnalyticsTag}\n',
            '                                                />\n',
            '                                            </div>\n',
            '                                        </div>\n',
            '\n',
            '                                        {/* Row 3: Advanced Analysis */}\n',
            '                                        <div className="h-[600px]">\n',
            '                                            <CodeSimilarityMap />\n',
            '                                        </div>\n',
            '                                    </div>\n',
            '                                )}\n'
        ]
        
        final_lines = lines[:start_line] + new_content + lines[end_line+1:]
        
        with open(file_path, 'w') as f:
            f.writelines(final_lines)
        print("Successfully patched AssignmentDashboard.jsx")
    else:
        print(f"Could not find start/end. Start: {start_line}, End: {end_line}")
else:
    print("Could not find nested useMemo.")
