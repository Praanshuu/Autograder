import { BarChart } from "lucide-react";

export default function MarksTab() {
    return (
        <div className="bg-white border rounded-lg overflow-hidden min-h-[400px] flex items-center justify-center">
            <div className="text-center">
                <BarChart className="w-12 h-12 text-gray-300 mx-auto mb-4" />
                <h3 className="text-lg font-medium text-gray-900">Gradebook is empty</h3>
                <p className="text-gray-500 mt-1">Add assignments and students to see grades.</p>
            </div>
        </div>
    );
}
