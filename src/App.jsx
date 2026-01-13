import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider } from "./contexts/AuthContext";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import LoginForm from "./components/auth/LoginForm";
import RegisterForm from "./components/auth/RegisterForm";
import ApiTest from "./components/debug/ApiTest";
import AuthStatus from "./components/debug/AuthStatus";

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

// Landing Page Component
const Landing = () => (
  <div className="flex flex-col items-center justify-center min-h-screen bg-white p-8">
    <h1 className="text-4xl font-bold tracking-tight text-gray-900 mb-4">Autograder</h1>
    <p className="text-gray-500 mb-8 text-lg">Coding LMS for the modern age.</p>
    <div className="flex gap-4 mb-8">
      <a href="/login" className="px-6 py-3 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition">Sign In</a>
      <a href="/register" className="px-6 py-3 bg-gray-100 text-gray-900 rounded-lg hover:bg-gray-200 transition">Sign Up</a>
      <a href="/auth-test" className="px-6 py-3 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition">Auth Test</a>
    </div>
    
    {/* Debug Components */}
    <div className="w-full max-w-6xl space-y-8">
      <ApiTest />
      <AuthStatus />
    </div>
  </div>
);

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/login" element={<LoginForm />} />
          <Route path="/register" element={<RegisterForm />} />
          <Route path="/auth-test" element={<AuthTestPage />} />

          {/* Teacher Routes - Protected */}
          <Route path="/teacher/dashboard" element={
            <ProtectedRoute requiredRole="teacher">
              <TeacherDashboard />
            </ProtectedRoute>
          } />
          <Route path="/teacher/archived" element={
            <ProtectedRoute requiredRole="teacher">
              <ArchivedClasses />
            </ProtectedRoute>
          } />
          <Route path="/teacher/class/:classId" element={
            <ProtectedRoute requiredRole="teacher">
              <ClassPage />
            </ProtectedRoute>
          } />
          <Route path="/teacher/assignment/create" element={
            <ProtectedRoute requiredRole="teacher">
              <CreateAssignment />
            </ProtectedRoute>
          } />
          <Route path="/teacher/assignment/:id" element={
            <ProtectedRoute requiredRole="teacher">
              <AssignmentDashboard />
            </ProtectedRoute>
          } />
          <Route path="/teacher/grading/submission/:id" element={
            <ProtectedRoute requiredRole="teacher">
              <GradingInterface />
            </ProtectedRoute>
          } />
          <Route path="/teacher/settings" element={
            <ProtectedRoute requiredRole="teacher">
              <Settings />
            </ProtectedRoute>
          } />
          <Route path="/teacher/assignments" element={
            <ProtectedRoute requiredRole="teacher">
              <AllAssignments />
            </ProtectedRoute>
          } />
          <Route path="/teacher/calendar" element={
            <ProtectedRoute requiredRole="teacher">
              <TeacherCalendar />
            </ProtectedRoute>
          } />

        {/* Student Routes */}
        <Route path="/student/dashboard" element={<StudentDashboard />} />
      </Routes>
    </Router>
  );
}

export default App;
