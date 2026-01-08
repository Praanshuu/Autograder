import { Info, StickyNote, Users } from "lucide-react";
import { Button } from "../../ui/button";
import { Card } from "../../ui/card";

export default function StreamTab() {
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
                        <p className="text-sm text-gray-500">Woohoo, no work due soon!</p>
                        <Button variant="link" className="p-0 text-indigo-600 text-sm h-auto">View all</Button>
                    </div>
                </Card>
            </div>

            {/* Main Stream */}
            <div className="col-span-1 lg:col-span-3 space-y-6">
                {/* Announcement Input */}
                <Card className="shadow-sm hover:shadow-md transition-shadow cursor-pointer">
                    <div className="p-4 flex items-center gap-4">
                        <div className="w-10 h-10 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-700 font-bold">
                            JD
                        </div>
                        <div className="flex-1 text-gray-400 hover:text-gray-600 text-sm font-medium">
                            Announce something to your class...
                        </div>
                    </div>
                </Card>

                {/* Stream Items */}
                <Card>
                    <div className="p-6">
                        <div className="flex items-start justify-between mb-4">
                            <div className="flex items-center gap-3">
                                <div className="w-10 h-10 rounded-full bg-indigo-600 flex items-center justify-center text-white">
                                    <StickyNote className="w-5 h-5" />
                                </div>
                                <div>
                                    <h3 className="font-semibold text-gray-900">New Assignment: Dynamic Programming</h3>
                                    <p className="text-xs text-gray-500">Posted Jan 7</p>
                                </div>
                            </div>
                            <Button variant="ghost" size="icon" className="h-8 w-8">
                                <Info className="w-4 h-4" />
                            </Button>
                        </div>
                        <p className="text-gray-600 text-sm mb-4">
                            Please review the attached material before starting the assignment. Due on Friday.
                        </p>
                        <div className="border border-gray-200 rounded-lg p-3 flex items-center gap-3 bg-gray-50">
                            <div className="w-10 h-10 bg-white rounded border flex items-center justify-center text-red-500 font-bold text-xs uppercase">
                                PDF
                            </div>
                            <span className="text-sm font-medium text-indigo-600 hover:underline cursor-pointer">
                                DP_Basics.pdf
                            </span>
                        </div>
                    </div>
                    <div className="px-6 py-3 border-t bg-gray-50 flex items-center gap-3">
                        <Users className="w-4 h-4 text-gray-400" />
                        <span className="text-xs font-medium text-gray-500">2 class comments</span>
                    </div>
                </Card>

                <div className="text-center py-8">
                    <p className="text-gray-400 text-sm">You've reached the end of the stream.</p>
                </div>
            </div>
        </div>
    );
}
