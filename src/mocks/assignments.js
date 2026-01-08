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
    }
};

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
        feedback: "Excellent work, just watch out for formatting.",
        code: "def add(a, b):\n    return a + b"
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
        code: "def add(a, b):\n    print(a + b)"
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
        feedback: "Good logic, but late submission penalty applied.",
        code: "def add(a, b):\n    return a + b # sum"
    },
    {
        id: "s4",
        studentName: "Diana Prince",
        studentEmail: "diana@university.edu",
        avatar: "DP",
        status: "Missing",
        submittedAt: null,
        autoGradeScore: 0,
        finalScore: 0,
        feedback: null,
        code: null
    },
    {
        id: "s5",
        studentName: "Evan Wright",
        studentEmail: "evan@university.edu",
        avatar: "EW",
        status: "Graded",
        submittedAt: "2024-03-18T16:45:00",
        autoGradeScore: 100,
        finalScore: 100,
        feedback: "Perfect.",
        code: "def add(a, b):\n    return a + b"
    },
];
