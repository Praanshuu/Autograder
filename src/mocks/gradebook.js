export const GRADEBOOK_DATA = {
    assignments: [
        { id: "a1", title: "Data Types", totalPoints: 100 },
        { id: "a2", title: "Loops", totalPoints: 100 },
        { id: "a3", title: "Arrays", totalPoints: 50 },
        { id: "a4", title: "Functions", totalPoints: 100 },
    ],
    students: [
        { id: "s1", name: "Alice Freeman", avatar: "AF" },
        { id: "s2", name: "Bob Smith", avatar: "BS" },
        { id: "s3", name: "Charlie Brown", avatar: "CB" },
        { id: "s4", name: "Diana Prince", avatar: "DP" },
        { id: "s5", name: "Evan Wright", avatar: "EW" },
    ],
    grades: {
        // Alice: Consistent high performer
        "s1-a1": { score: 98, status: "Graded", submissionId: "sub1" },
        "s1-a2": { score: 100, status: "Graded", submissionId: "sub6" },
        "s1-a3": { score: 48, status: "Graded", submissionId: "sub11" },
        "s1-a4": { score: 95, status: "Graded", submissionId: "sub16" },

        // Bob: Good but struggling with Functions
        "s2-a1": { score: 92, status: "Graded", submissionId: "sub2" },
        "s2-a2": { score: 88, status: "Graded", submissionId: "sub7" },
        "s2-a3": { score: 45, status: "Graded", submissionId: "sub12" },
        "s2-a4": { score: null, status: "To Grade", submissionId: "sub17" },

        // Charlie: Late submissions
        "s3-a1": { score: 85, status: "Late", submissionId: "sub3" },
        "s3-a2": { score: 75, status: "Graded", submissionId: "sub8" },
        "s3-a3": { score: null, status: "Missing", submissionId: null },
        "s3-a4": { score: 60, status: "Graded", submissionId: "sub18" },

        // Diana: Missing work
        "s4-a1": { score: null, status: "Missing", submissionId: null },
        "s4-a2": { score: null, status: "Missing", submissionId: null },
        "s4-a3": { score: 40, status: "Graded", submissionId: "sub13" },
        "s4-a4": { score: null, status: "To Grade", submissionId: "sub19" },

        // Evan: Average
        "s5-a1": { score: 100, status: "Graded", submissionId: "sub5" },
        "s5-a2": { score: 90, status: "Graded", submissionId: "sub10" },
        "s5-a3": { score: 42, status: "Graded", submissionId: "sub15" },
        "s5-a4": { score: 85, status: "Graded", submissionId: "sub20" },
    }
};
