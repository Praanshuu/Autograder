export const GRADEBOOK_DATA = {
    assignments: [
        { id: "bfb8916e-9080-4965-aa87-01308323a6d7", title: "Data Types", totalPoints: 100 },
        { id: "a2", title: "Loops", totalPoints: 100 },
        { id: "a3", title: "Arrays", totalPoints: 50 },
        { id: "a4", title: "Functions", totalPoints: 100 },
    ],
    students: [
        {
            id: "s1", name: "Alice Freeman", avatar: "AF",
            history: [
                { title: "Variables", score: 75, date: "2024-02-01", average: 70 },
                { title: "Loops", score: 82, date: "2024-02-08", average: 72 },
                { title: "Conditionals", score: 90, date: "2024-02-15", average: 75 },
                { title: "Functions", score: 95, date: "2024-02-22", average: 74 },
                { title: "Arrays", score: 92, date: "2024-03-01", average: 76 },
            ]
        },
        {
            id: "s2", name: "Bob Smith", avatar: "BS",
            history: [
                { title: "Variables", score: 65, date: "2024-02-01", average: 70 },
                { title: "Loops", score: 60, date: "2024-02-08", average: 72 },
                { title: "Conditionals", score: 55, date: "2024-02-15", average: 75 },
                { title: "Functions", score: 50, date: "2024-02-22", average: 74 },
                { title: "Arrays", score: 45, date: "2024-03-01", average: 76 },
            ]
        },
        {
            id: "s3", name: "Charlie Brown", avatar: "CB",
            history: [
                { title: "Variables", score: 85, date: "2024-02-01", average: 70 },
                { title: "Loops", score: 88, date: "2024-02-08", average: 72 },
                { title: "Conditionals", score: 85, date: "2024-02-15", average: 75 },
                { title: "Functions", score: 86, date: "2024-02-22", average: 74 },
                { title: "Arrays", score: 88, date: "2024-03-01", average: 76 },
            ]
        },
        { id: "s4", name: "Diana Prince", avatar: "DP" },
        { id: "s5", name: "Evan Wright", avatar: "EW" },
    ],
    grades: {
        // Alice: Consistent high performer
        "s1-bfb8916e-9080-4965-aa87-01308323a6d7": { score: 98, status: "Graded", submissionId: "sub1" },
        "s1-a2": { score: 100, status: "Graded", submissionId: "sub6" },
        "s1-a3": { score: 48, status: "Graded", submissionId: "sub11" },
        "s1-a4": { score: 95, status: "Graded", submissionId: "sub16" },

        // Bob: Good but struggling with Functions
        "s2-bfb8916e-9080-4965-aa87-01308323a6d7": { score: 92, status: "Graded", submissionId: "sub2" },
        "s2-a2": { score: 88, status: "Graded", submissionId: "sub7" },
        "s2-a3": { score: 45, status: "Graded", submissionId: "sub12" },
        "s2-a4": { score: null, status: "To Grade", submissionId: "sub17" },

        // Charlie: Late submissions
        "s3-bfb8916e-9080-4965-aa87-01308323a6d7": { score: 85, status: "Late", submissionId: "sub3" },
        "s3-a2": { score: 75, status: "Graded", submissionId: "sub8" },
        "s3-a3": { score: null, status: "Missing", submissionId: null },
        "s3-a4": { score: 60, status: "Graded", submissionId: "sub18" },

        // Diana: Missing work
        "s4-bfb8916e-9080-4965-aa87-01308323a6d7": { score: null, status: "Missing", submissionId: null },
        "s4-a2": { score: null, status: "Missing", submissionId: null },
        "s4-a3": { score: 40, status: "Graded", submissionId: "sub13" },
        "s4-a4": { score: null, status: "To Grade", submissionId: "sub19" },

        // Evan: Average
        "s5-bfb8916e-9080-4965-aa87-01308323a6d7": { score: 100, status: "Graded", submissionId: "sub5" },
        "s5-a2": { score: 90, status: "Graded", submissionId: "sub10" },
        "s5-a3": { score: 42, status: "Graded", submissionId: "sub15" },
        "s5-a4": { score: 85, status: "Graded", submissionId: "sub20" },
    }
};
