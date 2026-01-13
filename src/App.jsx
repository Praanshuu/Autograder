import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import TeacherDashboard from "./pages/teacher/TeacherDashboard";
import ClassPage from "./pages/teacher/ClassPage";
import CreateAssignment from "./pages/teacher/CreateAssignment";
import ArchivedClasses from "./pages/teacher/ArchivedClasses";
import AssignmentDashboard from "./pages/teacher/AssignmentDashboard";
import GradingInterface from "./pages/teacher/GradingInterface";
import Settings from "./pages/teacher/Settings";
import AllAssignments from "./pages/teacher/AllAssignments";
import TeacherCalendar from "./pages/teacher/TeacherCalendar";
import StudentDashboard from "./pages/student/StudentDashboard";
import StudentWorkspace from "./pages/student/StudentWorkspace";

// Placeholder Components
const Landing = () => (
  <div className="flex flex-col items-center justify-center min-h-screen bg-white">
    <h1 className="text-4xl font-bold tracking-tight text-gray-900 mb-4">Autograder</h1>
    <p className="text-gray-500 mb-8 text-lg">Coding LMS for the modern age.</p>
    <div className="flex gap-4">
      <a href="/teacher/dashboard" className="px-6 py-3 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition">Teacher View</a>
      <a href="/student/dashboard" className="px-6 py-3 bg-gray-100 text-gray-900 rounded-lg hover:bg-gray-200 transition">Student View</a>
    </div>
  </div>
);


const Login = () => <div className="p-8"><h1>Login</h1></div>;

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/login" element={<Login />} />

        {/* Teacher Routes */}
        <Route path="/teacher/dashboard" element={<TeacherDashboard />} />
        <Route path="/teacher/archived" element={<ArchivedClasses />} />
        <Route path="/teacher/class/:classId" element={<ClassPage />} />
        <Route path="/teacher/assignment/create" element={<CreateAssignment />} />
        <Route path="/teacher/assignment/:id" element={<AssignmentDashboard />} />
        <Route path="/teacher/grading/submission/:id" element={<GradingInterface />} />
        <Route path="/teacher/settings" element={<Settings />} />
        <Route path="/teacher/assignments" element={<AllAssignments />} />
        <Route path="/teacher/calendar" element={<TeacherCalendar />} />

        {/* Student Routes */}
        <Route path="/student/dashboard" element={<StudentDashboard />} />
        <Route path="/student/workspace/:id" element={<StudentWorkspace />} />
      </Routes>
    </Router>
  );
}

export default App;
