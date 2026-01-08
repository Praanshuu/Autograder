import { useState } from "react";
import { Info, StickyNote, Users, Send, MoreVertical, MessageSquare, Paperclip, X, Calendar } from "lucide-react";
import { Button } from "../../ui/button";
import { Card } from "../../ui/card";
import { Input } from "../../ui/input";
import { Textarea } from "../../ui/textarea";
import { Avatar, AvatarFallback, AvatarImage } from "../../ui/avatar";
import { DropdownMenu, DropdownMenuTrigger, DropdownMenuContent, DropdownMenuItem } from "../../ui/dropdown-menu";
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "../../ui/dialog";

export default function StreamTab() {
    const [isAnnouncing, setIsAnnouncing] = useState(false);
    const [announcementText, setAnnouncementText] = useState("");
    const [editingPostId, setEditingPostId] = useState(null);
    const [editText, setEditText] = useState("");

    // Mock Upcoming Data
    const upcomingWork = [
        { id: 1, title: "Dynamic Programming", due: "Friday at 11:59 PM", type: "Assignment" },
        { id: 2, title: "Graph Theory Quiz", due: "Monday at 10:00 AM", type: "Quiz" },
        { id: 3, title: "System Design Project", due: "Next Wednesday", type: "Project" },
        { id: 4, title: "Midterm Exam", due: "Oct 15", type: "Exam" }
    ];

    const [posts, setPosts] = useState([
        {
            id: 1,
            type: "assignment",
            author: "John Doe",
            title: "New Assignment: Dynamic Programming",
            date: "Jan 7",
            content: "Please review the attached material before starting the assignment. Due next Friday.",
            comments: [
                { id: 1, author: "Alice Freeman", text: "Is this pair programming?" },
                { id: 2, author: "John Doe", text: "Yes, you can work in pairs." }
            ],
            showComments: false
        },
        {
            id: 2,
            type: "announcement",
            author: "John Doe",
            date: "Jan 5",
            content: "Welcome to the Advanced Algorithms class! Please make sure to join the Discord server.",
            comments: [],
            showComments: false
        }
    ]);

    const handlePost = () => {
        if (!announcementText.trim()) return;
        const newPost = {
            id: Date.now(),
            type: "announcement",
            author: "John Doe",
            date: "Just now",
            content: announcementText,
            comments: [],
            showComments: false
        };
        setPosts([newPost, ...posts]);
        setAnnouncementText("");
        setIsAnnouncing(false);
    };

    const handleDelete = (id) => {
        setPosts(posts.filter(p => p.id !== id));
    };

    const startEdit = (post) => {
        setEditingPostId(post.id);
        setEditText(post.content);
    };

    const saveEdit = (id) => {
        setPosts(posts.map(p => p.id === id ? { ...p, content: editText } : p));
        setEditingPostId(null);
        setEditText("");
    };

    const toggleComments = (postId) => {
        setPosts(posts.map(post =>
            post.id === postId ? { ...post, showComments: !post.showComments } : post
        ));
    };

    return (
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
            {/* Left Sidebar */}
            <div className="space-y-6 hidden lg:block">
                <Card>
                    <div className="p-4 space-y-3">
                        <h3 className="font-semibold text-gray-600 text-sm">Class Code</h3>
                        <div className="text-2xl font-bold tracking-widest text-indigo-600">X7J2-9K</div>
                        <p className="text-xs text-gray-400">Share this code with students</p>
                    </div>
                </Card>
                <Card>
                    <div className="p-4 space-y-4">
                        <h3 className="font-semibold text-gray-600 text-sm">Upcoming</h3>
                        <div className="space-y-3">
                            {upcomingWork.slice(0, 2).map(work => (
                                <div key={work.id} className="text-sm">
                                    <p className="text-gray-900 font-medium">{work.title}</p>
                                    <p className="text-xs text-gray-500">Due {work.due}</p>
                                </div>
                            ))}
                        </div>

                        <Dialog>
                            <DialogTrigger asChild>
                                <Button variant="link" className="p-0 text-indigo-600 text-sm h-auto">View all</Button>
                            </DialogTrigger>
                            <DialogContent className="sm:max-w-md">
                                <DialogHeader>
                                    <DialogTitle>Upcoming Work</DialogTitle>
                                    <DialogDescription>
                                        All assignments and due dates for this class.
                                    </DialogDescription>
                                </DialogHeader>
                                <div className="space-y-4 py-4">
                                    {upcomingWork.map(work => (
                                        <div key={work.id} className="flex items-start gap-4 p-3 rounded-lg border bg-gray-50/50">
                                            <div className="w-10 h-10 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-600 shrink-0">
                                                <Calendar className="w-5 h-5" />
                                            </div>
                                            <div>
                                                <p className="font-semibold text-gray-900">{work.title}</p>
                                                <p className="text-sm text-gray-500">Due: {work.due}</p>
                                                <span className="inline-block mt-1 text-[10px] uppercase font-bold tracking-wider text-gray-400 border border-gray-200 px-1.5 rounded">
                                                    {work.type}
                                                </span>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </DialogContent>
                        </Dialog>
                    </div>
                </Card>
            </div>

            {/* Main Stream */}
            <div className="col-span-1 lg:col-span-3 space-y-6">
                {/* Announcement Input */}
                <Card className="shadow-sm transition-shadow">
                    {isAnnouncing ? (
                        <div className="p-4 space-y-4">
                            <Textarea
                                placeholder="Announce something to your class..."
                                className="min-h-[120px] resize-none border-0 focus-visible:ring-0 bg-gray-50 text-base"
                                value={announcementText}
                                onChange={(e) => setAnnouncementText(e.target.value)}
                                autoFocus
                            />
                            <div className="flex justify-between items-center">
                                <Button variant="ghost" size="icon" className="text-gray-400 hover:text-indigo-600">
                                    <Paperclip className="w-5 h-5" />
                                </Button>
                                <div className="flex gap-2">
                                    <Button variant="ghost" onClick={() => setIsAnnouncing(false)}>Cancel</Button>
                                    <Button onClick={handlePost} disabled={!announcementText.trim()}>Post</Button>
                                </div>
                            </div>
                        </div>
                    ) : (
                        <div
                            className="p-4 flex items-center gap-4 cursor-pointer hover:bg-gray-50/50 transition-colors rounded-lg"
                            onClick={() => setIsAnnouncing(true)}
                        >
                            <div className="w-10 h-10 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-700 font-bold">
                                JD
                            </div>
                            <div className="flex-1 text-gray-400 text-sm font-medium hover:text-gray-500">
                                Announce something to your class...
                            </div>
                        </div>
                    )}
                </Card>

                {/* Stream Items */}
                {posts.map((post) => (
                    <Card key={post.id} className="group">
                        <div className="p-6">
                            <div className="flex items-start justify-between mb-4">
                                <div className="flex items-center gap-3">
                                    <div className={`w-10 h-10 rounded-full flex items-center justify-center text-white ${post.type === 'assignment' ? 'bg-indigo-600' : 'bg-gray-500'
                                        }`}>
                                        {post.type === 'assignment' ? <StickyNote className="w-5 h-5" /> : "JD"}
                                    </div>
                                    <div>
                                        <h3 className="font-semibold text-gray-900">
                                            {post.type === 'assignment' ? post.title : post.author}
                                        </h3>
                                        <p className="text-xs text-gray-500">{post.date}</p>
                                    </div>
                                </div>
                                <DropdownMenu>
                                    <DropdownMenuTrigger asChild>
                                        <Button variant="ghost" size="icon" className="h-8 w-8 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <MoreVertical className="w-4 h-4" />
                                        </Button>
                                    </DropdownMenuTrigger>
                                    <DropdownMenuContent align="end">
                                        <DropdownMenuItem onClick={() => startEdit(post)}>Edit</DropdownMenuItem>
                                        <DropdownMenuItem className="text-red-600" onClick={() => handleDelete(post.id)}>Delete</DropdownMenuItem>
                                    </DropdownMenuContent>
                                </DropdownMenu>
                            </div>

                            {editingPostId === post.id ? (
                                <div className="space-y-3">
                                    <Textarea
                                        value={editText}
                                        onChange={(e) => setEditText(e.target.value)}
                                        className="min-h-[100px]"
                                    />
                                    <div className="flex justify-end gap-2">
                                        <Button variant="outline" size="sm" onClick={() => setEditingPostId(null)}>Cancel</Button>
                                        <Button size="sm" onClick={() => saveEdit(post.id)}>Save</Button>
                                    </div>
                                </div>
                            ) : (
                                <p className="text-gray-700 text-sm mb-4 whitespace-pre-wrap">
                                    {post.content}
                                </p>
                            )}

                            {post.type === 'assignment' && (
                                <div className="border border-gray-200 rounded-lg p-3 flex items-center gap-3 bg-gray-50 mb-4">
                                    <div className="w-10 h-10 bg-white rounded border flex items-center justify-center text-red-500 font-bold text-xs uppercase shadow-sm">
                                        PDF
                                    </div>
                                    <span className="text-sm font-medium text-indigo-600 hover:underline cursor-pointer">
                                        Assignment_Details.pdf
                                    </span>
                                </div>
                            )}
                        </div>

                        {/* Comments Section */}
                        <div className="bg-gray-50 border-t rounded-b-lg">
                            <div className="px-6 py-3 flex items-center gap-3 cursor-pointer hover:bg-gray-100 transition-colors" onClick={() => toggleComments(post.id)}>
                                <Users className="w-4 h-4 text-gray-400" />
                                <span className="text-xs font-medium text-gray-500">
                                    {post.comments.length} class comments
                                </span>
                            </div>

                            {post.showComments && (
                                <div className="px-6 pb-4 space-y-4 animate-in slide-in-from-top-2 duration-200">
                                    {post.comments.map(comment => (
                                        <div key={comment.id} className="flex gap-3">
                                            <div className="w-8 h-8 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-700 text-xs font-bold shrink-0">
                                                {comment.author.charAt(0)}
                                            </div>
                                            <div>
                                                <div className="flex items-center gap-2">
                                                    <span className="text-xs font-bold text-gray-900">{comment.author}</span>
                                                    <span className="text-[10px] text-gray-400">Jan 7</span>
                                                </div>
                                                <p className="text-sm text-gray-600 mt-0.5">{comment.text}</p>
                                            </div>
                                        </div>
                                    ))}
                                    <div className="flex gap-3 pt-2">
                                        <div className="w-8 h-8 rounded-full bg-gray-200 shrink-0" />
                                        <div className="relative flex-1">
                                            <Input placeholder="Add a class comment..." className="h-9 text-xs pr-8" />
                                            <Send className="w-3 h-3 text-gray-400 absolute right-3 top-3 cursor-pointer hover:text-indigo-600" />
                                        </div>
                                    </div>
                                </div>
                            )}
                        </div>
                    </Card>
                ))}

                <div className="text-center py-8">
                    <p className="text-gray-400 text-sm">You've reached the end of the stream.</p>
                </div>
            </div>
        </div>
    );
}
