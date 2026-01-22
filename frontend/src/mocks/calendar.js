export const MOCK_EVENTS = [
    {
        id: 1,
        title: "Dynamic Programming",
        date: new Date(new Date().getFullYear(), new Date().getMonth(), 15), // 15th of current month
        type: "Assignment",
        classId: "1", // Matches Advanced Algorithms in MOCK_CLASSES (assuming ID 1)
        className: "Advanced Algorithms"
    },
    {
        id: 2,
        title: "Graph Theory Quiz",
        date: new Date(new Date().getFullYear(), new Date().getMonth(), 18), // 18th
        type: "Quiz",
        classId: "1",
        className: "Advanced Algorithms"
    },
    {
        id: 3,
        title: "System Design Project",
        date: new Date(new Date().getFullYear(), new Date().getMonth(), 25), // 25th
        type: "Project",
        classId: "1",
        className: "Advanced Algorithms"
    },
    {
        id: 4,
        title: "Midterm Exam",
        date: new Date(new Date().getFullYear(), new Date().getMonth() + 1, 5), // 5th of next month
        type: "Exam",
        classId: "1",
        className: "Advanced Algorithms"
    },
    {
        id: 5,
        title: "Database Schema Design",
        date: new Date(new Date().getFullYear(), new Date().getMonth(), 12), // 12th
        type: "Assignment",
        classId: "2",
        className: "Database Systems"
    },
    {
        id: 6,
        title: "SQL Injection Workshop",
        date: new Date(new Date().getFullYear(), new Date().getMonth(), 20), // 20th
        type: "Workshop",
        classId: "2",
        className: "Database Systems"
    }
];
