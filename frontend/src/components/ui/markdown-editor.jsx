import React, { useRef } from 'react';
import { Bold, Italic, List, ListOrdered, Code, Quote, Link as LinkIcon, Heading1, Heading2 } from 'lucide-react';
import { Button } from './button';
import { Textarea } from './textarea';
import { cn } from '../../lib/utils';

export function MarkdownEditor({ value, onChange, className, placeholder, id }) {
    const textareaRef = useRef(null);

    const insertFormat = (prefix, suffix = '') => {
        const textarea = textareaRef.current;
        if (!textarea) return;

        const start = textarea.selectionStart;
        const end = textarea.selectionEnd;
        const text = textarea.value;
        const before = text.substring(0, start);
        const selection = text.substring(start, end);
        const after = text.substring(end);

        const newText = before + prefix + selection + suffix + after;

        // Call parent onChange with event-like object or value
        // Standardizing on passing the value directly is usually easier for custom controls,
        // but to mimic event:
        const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
        nativeInputValueSetter.call(textarea, newText);

        const event = new Event('input', { bubbles: true });
        textarea.dispatchEvent(event);

        // If parent expects direct value update override:
        onChange({ target: { value: newText } });

        // Restore focus and selection
        setTimeout(() => {
            textarea.focus();
            textarea.setSelectionRange(start + prefix.length, end + prefix.length);
        }, 0);
    };

    const ToolbarButton = ({ icon: Icon, onClick, title }) => (
        <Button
            type="button"
            variant="ghost"
            size="sm"
            className="h-8 w-8 p-0"
            onClick={onClick}
            title={title}
        >
            <Icon className="h-4 w-4" />
        </Button>
    );

    return (
        <div className={cn("border rounded-md", className)}>
            <div className="flex items-center gap-1 p-1 border-b bg-muted/20">
                <ToolbarButton icon={Bold} title="Bold" onClick={() => insertFormat('**', '**')} />
                <ToolbarButton icon={Italic} title="Italic" onClick={() => insertFormat('*', '*')} />
                <div className="w-px h-4 bg-border mx-1" />
                <ToolbarButton icon={Heading1} title="Heading 1" onClick={() => insertFormat('# ')} />
                <ToolbarButton icon={Heading2} title="Heading 2" onClick={() => insertFormat('## ')} />
                <div className="w-px h-4 bg-border mx-1" />
                <ToolbarButton icon={List} title="Bullet List" onClick={() => insertFormat('- ')} />
                <ToolbarButton icon={ListOrdered} title="Numbered List" onClick={() => insertFormat('1. ')} />
                <div className="w-px h-4 bg-border mx-1" />
                <ToolbarButton icon={Code} title="Code Block" onClick={() => insertFormat('```\n', '\n```')} />
                <ToolbarButton icon={Quote} title="Quote" onClick={() => insertFormat('> ')} />
                <ToolbarButton icon={LinkIcon} title="Link" onClick={() => insertFormat('[', '](url)')} />
            </div>
            <Textarea
                ref={textareaRef}
                id={id}
                value={value}
                onChange={onChange}
                placeholder={placeholder}
                className="border-0 focus-visible:ring-0 min-h-[150px] rounded-t-none font-mono resize-y"
            />
        </div>
    );
}
