import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";

// Auth
import { AuthProvider } from "./contexts/AuthContext";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import LoginForm from "./components/auth/LoginForm";
import RegisterForm from "./components/auth/RegisterForm";
import ForgotPassword from "./components/auth/ForgotPassword";
import ResetPassword from "./components/auth/ResetPassword";

// Test Components
import CodeRunnerTest from "./pages/CodeRunnerTest";

// Pages


// Teacher Pages
import TeacherDashboard from "./pages/teacher/TeacherDashboard";
import ClassPage from "./pages/teacher/ClassPage";
import CreateAssignment from "./pages/teacher/CreateAssignment";
import ArchivedClasses from "./pages/teacher/ArchivedClasses";
import AssignmentDashboard from "./pages/teacher/AssignmentDashboard";
import GradingInterface from "./pages/teacher/GradingInterface";
import Settings from "./pages/teacher/Settings";
import AllAssignments from "./pages/teacher/AllAssignments";
import TeacherCalendar from "./pages/teacher/TeacherCalendar";

// Student Pages
import StudentDashboard from "./pages/student/StudentDashboard";
import StudentWorkspace from "./pages/student/StudentWorkspace";
import StudentAssignments from "./pages/student/StudentAssignments";
import StudentClassPage from "./pages/student/StudentClassPage";
import StudentCalendar from "./pages/student/StudentCalendar";
import StudentPerformance from "./pages/student/StudentPerformance";

/* -----------------------------
   Landing Page
------------------------------*/
const Landing = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-white relative overflow-hidden">
      {/* Background decorations */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden z-0">
        <div className="absolute top-[-10%] right-[-5%] w-96 h-96 rounded-full bg-indigo-100 opacity-50 blur-3xl"></div>
        <div className="absolute bottom-[-10%] left-[-5%] w-[500px] h-[500px] rounded-full bg-blue-50 opacity-50 blur-3xl"></div>
      </div>

      <div className="z-10 flex flex-col items-center max-w-2xl mx-auto p-4 text-center">
        <div className="mb-8 p-3 bg-indigo-50 rounded-2xl">
          <svg className="w-12 h-12 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
          </svg>
        </div>

        <h1 className="text-5xl font-extrabold tracking-tight text-gray-900 mb-6 sm:text-6xl">
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-blue-500">
            Autograder
          </span>
        </h1>

        <p className="text-xl text-gray-600 mb-10 max-w-lg leading-relaxed">
          The modern Learning Management System for coding.
          Automated grading, instant feedback, and seamless class management.
        </p>

        <div className="flex flex-col sm:flex-row gap-4 w-full sm:w-auto">
          <a
            href="/login"
            className="px-8 py-4 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 hover:shadow-lg hover:-translate-y-0.5 transition-all duration-200 text-lg shadow-md"
          >
            Sign In
          </a>
          <a
            href="/register"
            className="px-8 py-4 bg-white text-indigo-900 border border-indigo-100 rounded-xl font-semibold hover:bg-gray-50 hover:border-indigo-200 transition-all duration-200 text-lg shadow-sm"
          >
            Create Account
          </a>
          <a
            href="/test-runner"
            className="px-8 py-4 bg-green-600 text-white rounded-xl font-semibold hover:bg-green-700 hover:shadow-lg hover:-translate-y-0.5 transition-all duration-200 text-lg shadow-md"
          >
            🧠 Test Code Runner
          </a>
        </div>
      </div>

      <div className="absolute bottom-8 text-sm text-gray-400">
        © 2024 Autograder Platform
      </div>
    </div>
  );
};

/* -----------------------------
   App Root
------------------------------*/
function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>

          {/* Public Routes */}
          <Route path="/" element={<Landing />} />
          <Route path="/login" element={<LoginForm />} />
          <Route path="/register" element={<RegisterForm />} />
          <Route path="/forgot-password" element={<ForgotPassword />} />
          <Route path="/reset-password/:uid/:token" element={<ResetPassword />} />

          {/* Test Route - Remove in production */}
          <Route path="/test-runner" element={<CodeRunnerTest />} />


          {/* Teacher Routes */}
          <Route
            path="/teacher/dashboard"
            element={
              <ProtectedRoute requiredRole="teacher">
                <TeacherDashboard />
              </ProtectedRoute>
            }
          />
          <Route
            path="/teacher/archived"
            element={
              <ProtectedRoute requiredRole="teacher">
                <ArchivedClasses />
              </ProtectedRoute>
            }
          />
          <Route
            path="/teacher/class/:classId"
            element={
              <ProtectedRoute requiredRole="teacher">
                <ClassPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/teacher/assignment/create"
            element={
              <ProtectedRoute requiredRole="teacher">
                <CreateAssignment />
              </ProtectedRoute>
            }
          />
          <Route
            path="/teacher/assignment/:id"
            element={
              <ProtectedRoute requiredRole="teacher">
                <AssignmentDashboard />
              </ProtectedRoute>
            }
          />
          <Route
            path="/teacher/grading/assignment/:assignmentId/student/:studentId"
            element={
              <ProtectedRoute requiredRole="teacher">
                <GradingInterface />
              </ProtectedRoute>
            }
          />
          <Route
            path="/teacher/assignments"
            element={
              <ProtectedRoute requiredRole="teacher">
                <AllAssignments />
              </ProtectedRoute>
            }
          />
          <Route
            path="/teacher/calendar"
            element={
              <ProtectedRoute requiredRole="teacher">
                <TeacherCalendar />
              </ProtectedRoute>
            }
          />
          <Route
            path="/teacher/settings"
            element={
              <ProtectedRoute requiredRole="teacher">
                <Settings />
              </ProtectedRoute>
            }
          />

          {/* Student Routes */}
          <Route
            path="/student/dashboard"
            element={
              <ProtectedRoute requiredRole="student">
                <StudentDashboard />
              </ProtectedRoute>
            }
          />
          <Route
            path="/student/workspace/:assignmentId"
            element={
              <ProtectedRoute requiredRole="student">
                <StudentWorkspace />
              </ProtectedRoute>
            }
          />
          <Route
            path="/student/assignments"
            element={
              <ProtectedRoute requiredRole="student">
                <StudentAssignments />
              </ProtectedRoute>
            }
          />
          <Route
            path="/student/class/:classId"
            element={
              <ProtectedRoute requiredRole="student">
                <StudentClassPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/student/calendar"
            element={
              <ProtectedRoute requiredRole="student">
                <StudentCalendar />
              </ProtectedRoute>
            }
          />
          <Route
            path="/student/performance"
            element={
              <ProtectedRoute requiredRole="student">
                <StudentPerformance />
              </ProtectedRoute>
            }
          />

          {/* Fallback */}
          <Route path="*" element={<Navigate to="/" replace />} />

        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
