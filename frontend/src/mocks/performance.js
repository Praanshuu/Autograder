// Mock performance data for student analytics
export const PERFORMANCE_DATA = {
  // Overall stats
  overview: {
    totalAssignments: 24,
    completedAssignments: 20,
    averageScore: 87.5,
    currentStreak: 5,
    totalTimeSpent: 4320, // minutes
    rank: 12,
    totalStudents: 156
  },

  // Grade distribution over time
  gradeHistory: [
    { assignment: "Hello World", score: 95, date: "2024-01-15", difficulty: "Easy" },
    { assignment: "Variables & Types", score: 88, date: "2024-01-18", difficulty: "Easy" },
    { assignment: "Control Flow", score: 92, date: "2024-01-22", difficulty: "Medium" },
    { assignment: "Functions", score: 85, date: "2024-01-25", difficulty: "Medium" },
    { assignment: "Arrays & Lists", score: 78, date: "2024-01-29", difficulty: "Medium" },
    { assignment: "String Manipulation", score: 91, date: "2024-02-01", difficulty: "Medium" },
    { assignment: "Loops & Iteration", score: 89, date: "2024-02-05", difficulty: "Medium" },
    { assignment: "Recursion Basics", score: 82, date: "2024-02-08", difficulty: "Hard" },
    { assignment: "Data Structures", score: 86, date: "2024-02-12", difficulty: "Hard" },
    { assignment: "Algorithm Analysis", score: 90, date: "2024-02-15", difficulty: "Hard" },
    { assignment: "Sorting Algorithms", score: 84, date: "2024-02-19", difficulty: "Hard" },
    { assignment: "Binary Search", score: 93, date: "2024-02-22", difficulty: "Medium" },
    { assignment: "Hash Tables", score: 87, date: "2024-02-26", difficulty: "Hard" },
    { assignment: "Graph Traversal", score: 81, date: "2024-03-01", difficulty: "Hard" },
    { assignment: "Dynamic Programming", score: 79, date: "2024-03-05", difficulty: "Hard" },
    { assignment: "Tree Algorithms", score: 88, date: "2024-03-08", difficulty: "Hard" },
    { assignment: "Greedy Algorithms", score: 92, date: "2024-03-12", difficulty: "Medium" },
    { assignment: "Backtracking", score: 85, date: "2024-03-15", difficulty: "Hard" },
    { assignment: "Graph Algorithms", score: 89, date: "2024-03-19", difficulty: "Hard" },
    { assignment: "Final Project", score: 94, date: "2024-03-22", difficulty: "Hard" }
  ],

  // Performance by difficulty
  difficultyStats: [
    { difficulty: "Easy", completed: 8, total: 8, avgScore: 91.5, avgTime: 25 },
    { difficulty: "Medium", completed: 7, total: 8, avgScore: 89.1, avgTime: 45 },
    { difficulty: "Hard", completed: 5, total: 8, avgScore: 84.2, avgTime: 78 }
  ],

  // Weekly activity (last 8 weeks)
  weeklyActivity: [
    { week: "Week 1", assignments: 3, timeSpent: 180, avgScore: 88 },
    { week: "Week 2", assignments: 2, timeSpent: 150, avgScore: 85 },
    { week: "Week 3", assignments: 4, timeSpent: 240, avgScore: 91 },
    { week: "Week 4", assignments: 3, timeSpent: 200, avgScore: 87 },
    { week: "Week 5", assignments: 2, timeSpent: 160, avgScore: 83 },
    { week: "Week 6", assignments: 3, timeSpent: 220, avgScore: 89 },
    { week: "Week 7", assignments: 2, timeSpent: 140, avgScore: 92 },
    { week: "Week 8", assignments: 1, timeSpent: 90, avgScore: 94 }
  ],

  // Language proficiency
  languageStats: [
    { language: "Python", assignments: 12, avgScore: 89, timeSpent: 1800 },
    { language: "JavaScript", assignments: 5, avgScore: 85, timeSpent: 900 },
    { language: "Java", assignments: 2, avgScore: 82, timeSpent: 480 },
    { language: "C++", assignments: 1, avgScore: 78, timeSpent: 120 }
  ],

  // Concept mastery
  conceptMastery: [
    { concept: "Variables & Data Types", mastery: 95, assignments: 3 },
    { concept: "Control Flow", mastery: 92, assignments: 4 },
    { concept: "Functions", mastery: 88, assignments: 3 },
    { concept: "Arrays & Lists", mastery: 85, assignments: 4 },
    { concept: "Loops", mastery: 90, assignments: 3 },
    { concept: "Recursion", mastery: 78, assignments: 2 },
    { concept: "Data Structures", mastery: 82, assignments: 3 },
    { concept: "Algorithms", mastery: 86, assignments: 4 },
    { concept: "Dynamic Programming", mastery: 75, assignments: 2 },
    { concept: "Graph Theory", mastery: 80, assignments: 2 }
  ],

  // Recent achievements
  achievements: [
    { 
      title: "Perfect Score", 
      description: "Scored 100% on an assignment", 
      date: "2024-03-22", 
      icon: "🏆",
      rarity: "rare"
    },
    { 
      title: "Speed Demon", 
      description: "Completed assignment in under 30 minutes", 
      date: "2024-03-19", 
      icon: "⚡",
      rarity: "common"
    },
    { 
      title: "Consistency King", 
      description: "5 assignments in a row above 85%", 
      date: "2024-03-15", 
      icon: "🎯",
      rarity: "uncommon"
    },
    { 
      title: "Algorithm Master", 
      description: "Mastered all sorting algorithms", 
      date: "2024-03-12", 
      icon: "🧠",
      rarity: "rare"
    }
  ],

  // Comparison with class average
  classComparison: [
    { metric: "Average Score", student: 87.5, classAvg: 82.3 },
    { metric: "Completion Rate", student: 83.3, classAvg: 78.1 },
    { metric: "Time Efficiency", student: 92, classAvg: 85 },
    { metric: "Code Quality", student: 88, classAvg: 81 }
  ]
};