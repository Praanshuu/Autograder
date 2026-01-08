import { Plus, Users } from "lucide-react";
import { Button } from "../../ui/button";

export default function PeopleTab() {
    return (
        <div className="max-w-4xl mx-auto space-y-8">
            <div className="space-y-4">
                <div className="flex items-center justify-between border-b border-indigo-100 pb-2">
                    <h2 className="text-2xl font-medium text-indigo-600">Teachers</h2>
                    <Button variant="ghost" size="icon" className="text-indigo-600">
                        <Plus className="w-5 h-5" />
                    </Button>
                </div>
                <div className="flex items-center gap-4 py-2">
                    <div className="w-9 h-9 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-700 font-bold border border-indigo-200">
                        JD
                    </div>
                    <span className="font-medium text-gray-900">John Doe</span>
                </div>
            </div>

            <div className="space-y-4">
                <div className="flex items-center justify-between border-b border-indigo-100 pb-2">
                    <h2 className="text-2xl font-medium text-indigo-600">Students</h2>
                    <Button variant="ghost" size="icon" className="text-indigo-600">
                        <Plus className="w-5 h-5" />
                    </Button>
                </div>
                <div className="bg-gray-50 rounded-lg p-8 flex flex-col items-center justify-center text-center">
                    <Users className="w-12 h-12 text-gray-300 mb-2" />
                    <p className="text-gray-500 font-medium">Use the class code to invite students!</p>
                </div>
            </div>
        </div>
    );
}
