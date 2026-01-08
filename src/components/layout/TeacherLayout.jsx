import { Link, useLocation } from "react-router-dom";
import {
    LayoutDashboard,
    Calendar,
    BookOpen,
    Archive,
    Settings,
    LogOut,
    GraduationCap,
    Bell,
    Search,
    ChevronDown,
    Menu
} from "lucide-react";
import { cn } from "../../lib/utils";
import { Button } from "../ui/button";
import { DropdownMenu, DropdownMenuTrigger, DropdownMenuContent, DropdownMenuItem, DropdownMenuLabel, DropdownMenuSeparator } from "../ui/dropdown-menu";

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

export default function TeacherLayout({ children }) {
    const location = useLocation();

    return (
        <div className="min-h-screen bg-gray-50 flex">
            {/* Sidebar */}
            <aside className="w-64 bg-white border-r border-gray-200 fixed h-full z-30 hidden md:flex flex-col">
                <div className="h-16 flex items-center px-6 border-b border-gray-100">
                    <GraduationCap className="w-7 h-7 text-indigo-600 mr-2" />
                    <span className="text-xl font-bold text-gray-900 tracking-tight">Autograder +</span>
                </div>

                <div className="flex-1 overflow-y-auto p-4">
                    <SidebarSection title="Main">
                        <SidebarItem
                            icon={LayoutDashboard}
                            label="Dashboard"
                            href="/teacher/dashboard"
                            active={location.pathname === "/teacher/dashboard"}
                        />
                        <SidebarItem
                            icon={Calendar}
                            label="Calendar"
                            href="/teacher/calendar"
                            active={location.pathname === "/teacher/calendar"}
                        />
                    </SidebarSection>

                    <SidebarSection title="Teaching">
                        <SidebarItem
                            icon={BookOpen} // Was Assignments or Classes, let's make it distinct if we had a global list
                            label="All Assignments"
                            href="/teacher/assignments" // Placeholder for a global assignment view
                            active={location.pathname === "/teacher/assignments"}
                        />
                        <SidebarItem
                            icon={Archive}
                            label="Archived Classes"
                            href="/teacher/archived"
                            active={location.pathname === "/teacher/archived"}
                        />
                    </SidebarSection>

                    <SidebarSection title="Preferences">
                        <SidebarItem
                            icon={Settings}
                            label="Settings"
                            href="/teacher/settings"
                            active={location.pathname === "/teacher/settings"}
                        />
                    </SidebarSection>
                </div>

                <div className="p-4 border-t border-gray-100">
                    <button className="flex items-center gap-3 px-3 py-2 w-full text-sm font-medium text-red-600 hover:bg-red-50 rounded-md transition-colors">
                        <LogOut className="w-5 h-5" />
                        Sign Out
                    </button>
                </div>
            </aside>

            {/* Main Content Wrapper */}
            <div className="flex-1 md:ml-64 flex flex-col min-h-screen">
                {/* Topbar */}
                <header className="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-4 sm:px-8 sticky top-0 z-20">
                    <div className="flex items-center gap-4">
                        {/* Mobile Overlay Toggle */}
                        <Button variant="ghost" size="icon" className="md:hidden">
                            <Menu className="w-5 h-5" />
                        </Button>

                        {/* Breadcrumbs Placeholder - Dynamic in real app */}
                        <nav className="hidden sm:flex items-center text-sm font-medium text-gray-500">
                            <span className="hover:text-gray-900 cursor-pointer">Classroom</span>
                            <span className="mx-2">/</span>
                            <span className="text-gray-900">Dashboard</span>
                        </nav>
                    </div>

                    <div className="flex items-center gap-4">
                        <Button variant="ghost" size="icon" className="text-gray-500 hover:text-gray-900">
                            <Search className="w-5 h-5" />
                        </Button>
                        <Button variant="ghost" size="icon" className="text-gray-500 hover:text-gray-900 relative">
                            <Bell className="w-5 h-5" />
                            <span className="absolute top-2 right-2 w-2 h-2 bg-red-500 rounded-full border-2 border-white" />
                        </Button>

                        <div className="h-6 w-px bg-gray-200 mx-1" />

                        <DropdownMenu>
                            <DropdownMenuTrigger asChild>
                                <Button variant="ghost" className="flex items-center gap-2 pl-2 pr-1 rounded-full hover:bg-gray-100">
                                    <div className="w-8 h-8 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-700 font-bold border border-indigo-200">
                                        JD
                                    </div>
                                    <span className="text-sm font-medium text-gray-700 hidden sm:block">John Doe</span>
                                    <ChevronDown className="w-4 h-4 text-gray-400" />
                                </Button>
                            </DropdownMenuTrigger>
                            <DropdownMenuContent align="end" className="w-56">
                                <DropdownMenuLabel>My Account</DropdownMenuLabel>
                                <DropdownMenuSeparator />
                                <DropdownMenuItem>Profile</DropdownMenuItem>
                                <DropdownMenuItem>Settings</DropdownMenuItem>
                                <DropdownMenuSeparator />
                                <DropdownMenuItem className="text-red-600 focus:text-red-700 focus:bg-red-50">
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
