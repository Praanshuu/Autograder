import React from "react";
import { ChevronLeft, ChevronDown } from "lucide-react";
import { Button } from "../ui/button";

const QuestionPalette = ({
    currentQuestionIndex,
    totalQuestions,
    onSelectQuestion,
    onNext,
    onPrev
}) => {
    // Generate array of question indices [0, 1, 2...]
    const questions = Array.from({ length: totalQuestions }, (_, i) => i);

    return (
        <div className="flex items-center gap-1 bg-gray-100 p-1 rounded-lg">
            {/* Previous Button */}
            <Button
                variant="ghost"
                size="icon"
                className="h-7 w-7 rounded-md"
                onClick={onPrev}
                disabled={currentQuestionIndex === 0}
            >
                <ChevronLeft className="w-4 h-4" />
            </Button>

            {/* Question Numbers */}
            <div className="flex items-center gap-1 px-2">
                {questions.map((idx) => (
                    <button
                        key={idx}
                        onClick={() => onSelectQuestion(idx)}
                        className={`w-6 h-6 rounded flex items-center justify-center text-xs font-medium transition-all ${currentQuestionIndex === idx
                                ? 'bg-indigo-600 text-white shadow-md scale-110'
                                : 'hover:bg-gray-200 text-gray-600'
                            }`}
                        title={`Question ${idx + 1}`}
                    >
                        {idx + 1}
                    </button>
                ))}
            </div>

            {/* Next Button */}
            <Button
                variant="ghost"
                size="icon"
                className="h-7 w-7 rounded-md"
                onClick={onNext}
                disabled={currentQuestionIndex === totalQuestions - 1}
            >
                <ChevronDown className="w-4 h-4 -rotate-90" />
            </Button>
        </div>
    );
};

export default QuestionPalette;
