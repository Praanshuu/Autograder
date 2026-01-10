export const MOCK_ASSIGNMENT = {
    id: "a1",
    title: "Data Type & Variables",
    status: "Active",
    dueDate: "2024-03-20T23:59:00",
    description: "Introduction to primitive data types and variable declarations in Python.",
    stats: {
        totalStudents: 45,
        submitted: 38,
        graded: 25,
        avgScore: 88.5,
        highestScore: 100,
        lowestScore: 65
    },
    // NEW: Question-level data for the Heatmap & UMAP
    questions: [
        {
            id: "q_palindrome",
            title: "Q1: Palindrome Check",
            avgScore: 65,
            testCases: [
                { id: "tc1", name: "Simple (121)", passRate: 95 },       // Green
                { id: "tc2", name: "Non-Palindrome (123)", passRate: 92 }, // Green
                { id: "tc3", name: "Negative Number (-121)", passRate: 28 }, // RED (Major Misconception)
                { id: "tc4", name: "Large Number Edge Case", passRate: 75 }  // Yellow (Confusion)
            ]
        },
        {
            id: "q2",
            title: "Q2: List Manipulation",
            avgScore: 76,
            testCases: [
                { id: "tc1", name: "Append Element", passRate: 95 },
                { id: "tc2", name: "Slicing Syntax", passRate: 72 },
                { id: "tc3", name: "Negative Indexing", passRate: 45 } // Major failing point
            ]
        }
    ]
};

// NEW: Clusters for UMAP Visualization
export const MOCK_CLUSTERS = [
    { name: "Standard Iterative", color: "#4f46e5", x: 10, y: 10 },
    { name: "Recursive Approach", color: "#0ea5e9", x: 60, y: 50 },
    { name: "One-Liner / Pythonic", color: "#10b981", x: 80, y: 20 },
    { name: "Incorrect Logic", color: "#ef4444", x: 30, y: 80 }
];

export const MOCK_SUBMISSIONS = [
    {
        id: "s1",
        studentName: "Alice Freeman",
        studentEmail: "alice@university.edu",
        avatar: "AF",
        status: "Graded",
        submittedAt: "2024-03-18T14:30:00",
        autoGradeScore: 100,
        finalScore: 98,
        feedback: "Excellent work.",
        code: "def solve(x):\n    return x * 2",
        // Analytics Data
        timeSpent: 45, // minutes
        attempts: 3,
        approach: "Standard Iterative", // UMAP Label
        umapX: 0.5,
        umapY: -1.2,
        history: [
            { title: "Variables", score: 65, date: "2024-02-01", average: 70 },
            { title: "Loops", score: 60, date: "2024-02-08", average: 72 },
            { title: "Conditionals", score: 55, date: "2024-02-15", average: 75 },
            { title: "Functions", score: 50, date: "2024-02-22", average: 74 },
            { title: "Arrays", score: 45, date: "2024-03-01", average: 76 },
        ]
    },
    {
        id: "s2",
        studentName: "Bob Smith",
        studentEmail: "bob@university.edu",
        avatar: "BS",
        status: "To Grade",
        submittedAt: "2024-03-19T09:15:00",
        autoGradeScore: 80,
        finalScore: null,
        feedback: null,
        code: "def solve(x):\n    # ...",
        timeSpent: 45, // minutes (High effort, lower score = Struggling)
        attempts: 5,
        approach: "Incorrect Logic",
        umapX: 28, umapY: 78
    },
    {
        id: "s3",
        studentName: "Charlie Brown",
        studentEmail: "charlie@university.edu",
        avatar: "CB",
        status: "Late",
        submittedAt: "2024-03-21T02:00:00",
        autoGradeScore: 90,
        finalScore: 85,
        feedback: "Good logic.",
        code: "def solve(x): return x*2",
        timeSpent: 5, // minutes (Super fast)
        attempts: 1,
        approach: "One-Liner / Pythonic",
        umapX: 82, umapY: 22,
        history: [
            { title: "Variables", score: 85, date: "2024-02-01", average: 70 },
            { title: "Loops", score: 88, date: "2024-02-08", average: 72 },
            { title: "Conditionals", score: 85, date: "2024-02-15", average: 75 },
            { title: "Functions", score: 86, date: "2024-02-22", average: 74 },
            { title: "Arrays", score: 88, date: "2024-03-01", average: 76 },
        ]
    },
    {
        id: "s4",
        studentName: "Diana Prince",
        studentEmail: "diana@university.edu",
        avatar: "DP",
        status: "Graded",
        submittedAt: "2024-03-18T10:00:00",
        autoGradeScore: 100,
        finalScore: 100,
        code: "def recursive_solve(x)...",
        timeSpent: 25,
        attempts: 2,
        approach: "Recursive Approach",
        umapX: 62, umapY: 48,
        history: [
            { title: "Variables", score: 95, date: "2024-02-01", average: 70 },
            { title: "Loops", score: 98, date: "2024-02-08", average: 72 },
            { title: "Conditionals", score: 100, date: "2024-02-15", average: 75 },
            { title: "Functions", score: 96, date: "2024-02-22", average: 74 },
            { title: "Arrays", score: 100, date: "2024-03-01", average: 76 },
        ]
    },
    {
        id: "s5",
        studentName: "Evan Wright",
        studentEmail: "evan@university.edu",
        avatar: "EW",
        status: "Graded",
        submittedAt: "2024-03-18T16:45:00",
        autoGradeScore: 40,
        finalScore: 40,
        code: "print('hello')",
        timeSpent: 5, // Low effort, low score = Disengaged
        attempts: 1,
        approach: "Incorrect Logic",
        umapX: 32, umapY: 82
    },
    // Generating more mock data points for charts
    ...Array.from({ length: 15 }).map((_, i) => ({
        id: `gen${i}`,
        studentName: `Student ${i + 1}`,
        studentEmail: `s${i}@uni.edu`,
        avatar: `S${i}`,
        status: i % 3 === 0 ? "Graded" : "To Grade",
        submittedAt: "2024-03-19T10:00:00",
        autoGradeScore: 60 + Math.floor(Math.random() * 40),
        finalScore: null,
        timeSpent: 10 + Math.floor(Math.random() * 50), // Random time 10-60m
        attempts: 1 + Math.floor(Math.random() * 5),
        approach: "Standard Iterative",
        umapX: 10 + Math.random() * 10,
        umapY: 10 + Math.random() * 10
    }))
];
