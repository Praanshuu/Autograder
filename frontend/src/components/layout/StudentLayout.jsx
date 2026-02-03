import { useState, useEffect } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import {
    LayoutDashboard,
    BookOpen,
    BarChart3,
    Settings,
    LogOut,
    Code2,
    Bell,
    Search,
    ChevronDown,
    Menu,
    Clock,
    CheckCircle2,
    MessageSquare,
    GraduationCap,
    Calendar
} from "lucide-react";
import { cn } from "../../lib/utils";
import { Button } from "../ui/button";
import { Input } from "../ui/input";
import { DropdownMenu, DropdownMenuTrigger, DropdownMenuContent, DropdownMenuItem, DropdownMenuLabel, DropdownMenuSeparator } from "../ui/dropdown-menu";
import { classService } from "../../services/classService";
import { useAuth } from "../../contexts/AuthContext";

const SidebarItem = ({ icon: Icon, label, href, active, count }) => (
    <Link
        to={href}
        className={cn(
            "flex items-center justify-between px-3 py-2 text-sm font-medium rounded-md transition-colors",
            active
                ? "bg-indigo-50 text-indigo-700"
                : "text-gray-600 hover:bg-gray-100 hover:text-gray-900"
        )}
    >
        <div className="flex items-center gap-3">
            <Icon className="w-5 h-5" />
            {label}
        </div>
        {count && (
            <span className="bg-indigo-100 text-indigo-700 text-xs px-2 py-0.5 rounded-full">
                {count}
            </span>
        )}
    </Link>
);

// Mock Notifications for Student
const NOTIFICATIONS = [
    {
        id: 1,
        title: "Feedback: Assignment 1",
        desc: "Teacher: 'Check your negative input handling.'",
        time: "2 hours ago",
        unread: true,
        type: "comment"
    },
    {
        id: 2,
        title: "New Assignment Posted",
        desc: "Assignment 4: List Manipulation is now live.",
        time: "5 hours ago",
        unread: true,
        type: "alert"
    }
];

const SidebarSection = ({ title, children }) => (
    <div className="mb-6">
        <h4 className="px-3 mb-2 text-xs font-semibold text-gray-500 uppercase tracking-wider">
            {title}
        </h4>
        <div className="space-y-1">
            {children}
        </div>
    </div>
);

export default function StudentLayout({ children, refreshTrigger = 0 }) {
    const location = useLocation();
    const navigate = useNavigate();
    const { logout, user } = useAuth();
    const [classes, setClasses] = useState([]);

    const handleLogout = () => {
        logout();
        navigate('/login');
    };

    useEffect(() => {
        const fetchClasses = async () => {
            try {
                const response = await classService.getClasses();
                const data = Array.isArray(response.data) ? response.data : (response.data.results || []);
                setClasses(data);
            } catch (error) {
                console.error("Failed to fetch classes for sidebar", error);
            }
        };
        fetchClasses();
    }, [refreshTrigger]);

    return (
        <div className="min-h-screen bg-gray-50 flex">
            {/* Sidebar */}
            <aside className="w-64 bg-white border-r border-gray-200 fixed h-full z-30 hidden md:flex flex-col">
                <div className="h-16 flex items-center px-6 border-b border-gray-100">
                    <Code2 className="w-7 h-7 text-indigo-600 mr-2" />
                    <span className="text-xl font-bold text-gray-900 tracking-tight">Autograder</span>
                </div>

                <div className="flex-1 overflow-y-auto p-4">
                    <SidebarSection title="Workspace">
                        <SidebarItem
                            icon={LayoutDashboard}
                            label="Dashboard"
                            href="/student/dashboard"
                            active={location.pathname === "/student/dashboard"}
                        />
                        <SidebarItem
                            icon={BookOpen}
                            label="Assignments"
                            href="/student/assignments"
                            active={location.pathname === "/student/assignments"}
                        />
                        <SidebarItem
                            icon={Code2}
                            label="Practice"
                            href="/student/practice"
                            active={location.pathname === "/student/practice"}
                        />
                        <SidebarItem
                            icon={Calendar}
                            label="Calendar"
                            href="/student/calendar"
                            active={location.pathname === "/student/calendar"}
                        />
                    </SidebarSection>

                    <SidebarSection title="My Classes">
                        {classes.length > 0 ? (
                            classes.map(cls => (
                                <SidebarItem
                                    key={cls.id}
                                    icon={GraduationCap}
                                    label={cls.name}
                                    href={`/student/class/${cls.id}`} // We can define this route later
                                    active={location.pathname === `/student/class/${cls.id}`}
                                />
                            ))
                        ) : (
                            <div className="px-3 py-2 text-xs text-gray-400 italic">No classes joined</div>
                        )}
                    </SidebarSection>

                    <SidebarSection title="Insights">
                        <SidebarItem
                            icon={BarChart3}
                            label="My Performance"
                            href="/student/performance"
                            active={location.pathname === "/student/performance"}
                        />
                    </SidebarSection>

                    <SidebarSection title="Account">
                        <SidebarItem
                            icon={Settings}
                            label="Settings"
                            href="/student/settings"
                            active={location.pathname === "/student/settings"}
                        />
                    </SidebarSection>
                </div>

                <div className="p-4 border-t border-gray-100">
                    <button 
                        onClick={handleLogout}
                        className="flex items-center gap-3 px-3 py-2 w-full text-sm font-medium text-red-600 hover:bg-red-50 rounded-md transition-colors"
                    >
                        <LogOut className="w-5 h-5" />
                        Sign Out
                    </button>
                </div>
            </aside>

            {/* Main Content Wrapper */}
            <div className="flex-1 md:ml-64 flex flex-col min-h-screen">
                {/* Topbar */}
                <header className="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-4 sm:px-8 sticky top-0 z-20">
                    <div className="flex items-center gap-4 flex-1">
                        {/* Mobile Overlay Toggle */}
                        <Button variant="ghost" size="icon" className="md:hidden">
                            <Menu className="w-5 h-5" />
                        </Button>

                        {/* Breadcrumbs Placeholder */}
                        <nav className="hidden sm:flex items-center text-sm font-medium text-gray-500">
                            <span className="text-gray-900 font-semibold">Student Workspace</span>
                        </nav>
                    </div>

                    <div className="flex items-center gap-4">
                        {/* Search Bar */}
                        <div className="hidden md:block relative w-64 transition-all focus-within:w-80">
                            <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-gray-400" />
                            <Input
                                placeholder="Search assignments or concepts..."
                                className="pl-9 bg-gray-50 border-gray-200 focus:bg-white transition-colors"
                            />
                        </div>

                        <div className="relative">
                            <DropdownMenu>
                                <DropdownMenuTrigger asChild>
                                    <Button variant="ghost" size="icon" className="text-gray-500 hover:text-gray-900 relative">
                                        <Bell className="w-5 h-5" />
                                        <span className="absolute top-2.5 right-2.5 w-2 h-2 bg-red-500 rounded-full border-2 border-white" />
                                    </Button>
                                </DropdownMenuTrigger>
                                <DropdownMenuContent align="end" className="w-80 p-0 bg-white">
                                    <div className="p-4 border-b border-gray-100 flex items-center justify-between">
                                        <h4 className="font-semibold text-gray-900">Notifications</h4>
                                        <span className="text-xs text-indigo-600 hover:text-indigo-700 cursor-pointer">Mark all read</span>
                                    </div>
                                    <div className="max-h-[350px] overflow-y-auto">
                                        {NOTIFICATIONS.map((notif) => (
                                            <DropdownMenuItem key={notif.id} className="p-4 cursor-pointer focus:bg-gray-50 border-b border-gray-50 last:border-0 items-start gap-3">
                                                <div className={`mt-1 p-1.5 rounded-full shrink-0 ${notif.type === 'comment' ? 'bg-blue-100 text-blue-600' :
                                                    'bg-orange-100 text-orange-600'
                                                    }`}>
                                                    {notif.type === 'comment' ? <MessageSquare className="w-3.5 h-3.5" /> :
                                                        <Clock className="w-3.5 h-3.5" />
                                                    }
                                                </div>
                                                <div className="space-y-1">
                                                    <div className="flex justify-between items-start gap-2">
                                                        <p className={`text-sm ${notif.unread ? 'font-semibold text-gray-900' : 'text-gray-700'}`}>
                                                            {notif.title}
                                                        </p>
                                                        {notif.unread && <span className="w-1.5 h-1.5 bg-indigo-600 rounded-full mt-1.5" />}
                                                    </div>
                                                    <p className="text-xs text-gray-500 line-clamp-2">{notif.desc}</p>
                                                    <p className="text-xs text-gray-400 pt-1">{notif.time}</p>
                                                </div>
                                            </DropdownMenuItem>
                                        ))}
                                    </div>
                                    <div className="p-3 border-t border-gray-100 bg-gray-50 text-center">
                                        <Button variant="link" className="text-xs h-auto p-0 text-gray-500">View all notifications</Button>
                                    </div>
                                </DropdownMenuContent>
                            </DropdownMenu>
                        </div>

                        <div className="h-6 w-px bg-gray-200 mx-1 hidden sm:block" />

                        <DropdownMenu>
                            <DropdownMenuTrigger asChild>
                                <Button variant="ghost" className="flex items-center gap-2 pl-2 pr-1 rounded-full hover:bg-gray-100 ring-offset-2 focus-visible:ring-2">
                                    <div className="w-8 h-8 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-700 font-bold border border-indigo-200">
                                        {user?.first_name?.[0]}{user?.last_name?.[0]}
                                    </div>
                                    <span className="text-sm font-medium text-gray-700 hidden sm:block">
                                        {user?.first_name} {user?.last_name?.[0]}.
                                    </span>
                                    <ChevronDown className="w-4 h-4 text-gray-400" />
                                </Button>
                            </DropdownMenuTrigger>
                            <DropdownMenuContent align="end" className="w-56">
                                <DropdownMenuLabel>My Account</DropdownMenuLabel>
                                <DropdownMenuSeparator />
                                <DropdownMenuItem className="cursor-pointer">
                                    Profile
                                </DropdownMenuItem>
                                <DropdownMenuItem asChild className="cursor-pointer">
                                    <Link to="/student/settings">Settings</Link>
                                </DropdownMenuItem>
                                <DropdownMenuSeparator />
                                <DropdownMenuItem className="text-red-600 focus:text-red-700 focus:bg-red-50 cursor-pointer">
                                    Logout
                                </DropdownMenuItem>
                            </DropdownMenuContent>
                        </DropdownMenu>
                    </div>
                </header>

                {/* Page Content */}
                <main className="p-4 sm:p-8 flex-1">
                    {children}
                </main>
            </div>
        </div>
    );
}
