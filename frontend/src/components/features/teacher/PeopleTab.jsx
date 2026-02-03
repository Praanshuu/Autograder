import { useState, useEffect } from "react";
import { Plus, UserPlus, MoreVertical, Mail, Trash2 } from "lucide-react";
import { Button } from "../../ui/button";
import { Input } from "../../ui/input";
import { DropdownMenu, DropdownMenuTrigger, DropdownMenuContent, DropdownMenuItem } from "../../ui/dropdown-menu";
import { classService } from "../../../services/classService";
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "../../ui/dialog";

export default function PeopleTab({ classId }) {
    const [inviteEmail, setInviteEmail] = useState("");
    const [students, setStudents] = useState([]);
    const [teachers, setTeachers] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const loadClassMembers = async () => {
            if (!classId) return;
            
            try {
                setLoading(true);
                const response = await classService.getClassMembers(classId);
                
                if (response.success && response.data) {
                    // Separate students and teachers
                    const studentMembers = response.data.filter(member => member.role === 'student');
                    const teacherMembers = response.data.filter(member => member.role === 'teacher');
                    
                    setStudents(studentMembers);
                    setTeachers(teacherMembers);
                }
            } catch (error) {
                console.error('Failed to load class members:', error);
                setStudents([]);
                setTeachers([]);
            } finally {
                setLoading(false);
            }
        };

        loadClassMembers();
    }, [classId]);

    const handleInvite = () => {
        // In a real app, this would make an API call
        console.log("Inviting:", inviteEmail);
        setInviteEmail(""); // Reset field
    };

    return (
        <div className="max-w-4xl mx-auto space-y-12">

            {/* Teachers Section */}
            <div className="space-y-4">
                <div className="flex items-center justify-between border-b border-indigo-200 pb-4">
                    <h2 className="text-3xl font-medium text-indigo-700">Teachers</h2>
                    <Dialog>
                        <DialogTrigger asChild>
                            <Button variant="ghost" size="icon" className="text-indigo-600 hover:bg-indigo-50">
                                <UserPlus className="w-5 h-5" />
                            </Button>
                        </DialogTrigger>
                        <DialogContent className="sm:max-w-md">
                            <DialogHeader>
                                <DialogTitle>Invite Teachers</DialogTitle>
                                <DialogDescription>
                                    Enter the email address of the teacher you want to invite to this class.
                                </DialogDescription>
                            </DialogHeader>
                            <div className="grid gap-4 py-4">
                                <div className="grid gap-2">
                                    <Input
                                        id="email"
                                        placeholder="teacher@school.edu"
                                        value={inviteEmail}
                                        onChange={(e) => setInviteEmail(e.target.value)}
                                    />
                                    <Button onClick={handleInvite}>Invite</Button>
                                </div>
                            </div>
                        </DialogContent>
                    </Dialog>
                </div>
                <div className="flex items-center justify-between py-4 px-2 hover:bg-gray-50 rounded-lg transition-colors group">
                    <div className="flex items-center gap-4">
                        <div className="w-10 h-10 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-700 font-bold border border-indigo-200">
                            JD
                        </div>
                        <span className="font-medium text-gray-900 text-sm">John Doe (You)</span>
                    </div>
                </div>
            </div>

            {/* Students Section */}
            <div className="space-y-4">
                <div className="flex items-center justify-between border-b border-indigo-200 pb-4">
                    <div className="flex items-center gap-4">
                        <h2 className="text-3xl font-medium text-indigo-700">Students</h2>
                        <span className="bg-indigo-100 text-indigo-700 text-xs font-bold px-2 py-1 rounded-full">
                            {students.length} students
                        </span>
                    </div>
                    <Dialog>
                        <DialogTrigger asChild>
                            <Button variant="ghost" size="icon" className="text-indigo-600 hover:bg-indigo-50">
                                <UserPlus className="w-5 h-5" />
                            </Button>
                        </DialogTrigger>
                        <DialogContent className="sm:max-w-md">
                            <DialogHeader>
                                <DialogTitle>Invite Students</DialogTitle>
                                <DialogDescription>
                                    Enter the email address of the student you want to invite to this class.
                                </DialogDescription>
                            </DialogHeader>
                            <div className="grid gap-4 py-4">
                                <div className="grid gap-2">
                                    <Input
                                        id="student-email"
                                        placeholder="student@school.edu"
                                        value={inviteEmail}
                                        onChange={(e) => setInviteEmail(e.target.value)}
                                    />
                                    <Button onClick={handleInvite}>Invite</Button>
                                </div>
                            </div>
                        </DialogContent>
                    </Dialog>
                </div>

                <div className="space-y-1">
                    {loading ? (
                        <div className="text-center py-4">
                            <p className="text-gray-500">Loading students...</p>
                        </div>
                    ) : students.length === 0 ? (
                        <div className="text-center py-8">
                            <p className="text-gray-500">No students enrolled yet</p>
                        </div>
                    ) : (
                        students.map((student) => (
                            <div key={student.user.id} className="flex items-center justify-between py-3 px-2 hover:bg-gray-50 rounded-lg transition-colors border-b border-gray-50 last:border-0 group">
                                <div className="flex items-center gap-4">
                                    <div className="w-9 h-9 rounded-full bg-gray-100 flex items-center justify-center text-gray-600 font-bold border border-gray-200 text-xs">
                                        {student.user.first_name?.[0]}{student.user.last_name?.[0]}
                                    </div>
                                    <div>
                                        <span className="font-medium text-gray-900 text-sm">
                                            {student.user.first_name} {student.user.last_name}
                                        </span>
                                        <p className="text-xs text-gray-500">{student.user.email}</p>
                                    </div>
                                </div>
                                <div className="opacity-0 group-hover:opacity-100 transition-opacity flex items-center gap-1">
                                    <Button variant="ghost" size="icon" className="h-8 w-8 text-gray-400 hover:text-indigo-600">
                                        <Mail className="w-4 h-4" />
                                    </Button>
                                    <DropdownMenu>
                                        <DropdownMenuTrigger asChild>
                                            <Button variant="ghost" size="icon" className="h-8 w-8 text-gray-400 hover:text-red-600">
                                                <MoreVertical className="w-4 h-4" />
                                            </Button>
                                        </DropdownMenuTrigger>
                                        <DropdownMenuContent align="end">
                                            <DropdownMenuItem>Email student</DropdownMenuItem>
                                            <DropdownMenuItem className="text-red-600 gap-2">
                                                <Trash2 className="w-4 h-4" />
                                                Remove
                                            </DropdownMenuItem>
                                        </DropdownMenuContent>
                                    </DropdownMenu>
                                </div>
                            </div>
                        ))
                    )}
                </div>
            </div>
        </div>
    );
}
