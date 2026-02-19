import React from 'react';
import { useSortable } from '@dnd-kit/sortable';
import { CSS } from '@dnd-kit/utilities';
import { GripVertical, Pencil, Trash2 } from 'lucide-react';
import { Button } from '../../ui/button';

export function SortableQuestionItem({ question, onEdit, onDelete }) {
    const {
        attributes,
        listeners,
        setNodeRef,
        transform,
        transition,
        isDragging,
    } = useSortable({ id: question.id });

    const style = {
        transform: CSS.Transform.toString(transform),
        transition,
        opacity: isDragging ? 0.5 : 1,
    };

    return (
        <div
            ref={setNodeRef}
            style={style}
            className={`bg-white border rounded-lg p-4 flex items-center gap-4 shadow-sm hover:shadow-md transition-shadow ${isDragging ? 'border-indigo-500 ring-2 ring-indigo-200' : 'border-gray-200'
                }`}
        >
            <div {...attributes} {...listeners} className="cursor-move text-gray-400 hover:text-gray-600">
                <GripVertical className="w-5 h-5" />
            </div>

            <div className="flex-1 min-w-0">
                <h3 className="font-medium text-gray-900 truncate">{question.title}</h3>
                <div className="flex items-center gap-2 mt-1">
                    <span
                        className={`text-xs px-2 py-0.5 rounded-full font-medium ${question.difficulty === 'Easy'
                                ? 'bg-green-100 text-green-700'
                                : question.difficulty === 'Medium'
                                    ? 'bg-yellow-100 text-yellow-700'
                                    : 'bg-red-100 text-red-700'
                            }`}
                    >
                        {question.difficulty}
                    </span>
                    <span className="text-xs text-gray-400">
                        • {question.testCases?.length || 0} Test Cases
                    </span>
                </div>
            </div>

            <div className="flex items-center gap-2">
                <Button variant="ghost" size="sm" onClick={() => onEdit(question)}>
                    <Pencil className="w-4 h-4 mr-1" /> Edit
                </Button>
                <Button
                    variant="ghost"
                    size="icon"
                    className="text-gray-400 hover:text-red-600 hover:bg-red-50"
                    onClick={() => onDelete(question.id)}
                >
                    <Trash2 className="w-4 h-4" />
                </Button>
            </div>
        </div>
    );
}
