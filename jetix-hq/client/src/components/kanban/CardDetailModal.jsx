import { useState, useEffect, useRef, useCallback } from 'react';
import { X, Plus, Trash2, Check } from 'lucide-react';
import { Button, Badge } from '../ui';

const PRIORITIES = ['high', 'medium', 'low'];

export default function CardDetailModal({ card, open, onClose, onUpdate, onDelete }) {
  const [form, setForm] = useState(null);
  const debounceRef = useRef(null);

  useEffect(() => {
    if (card) setForm({ ...card });
  }, [card]);

  const scheduleUpdate = useCallback((updated) => {
    if (debounceRef.current) clearTimeout(debounceRef.current);
    debounceRef.current = setTimeout(() => {
      onUpdate(updated);
    }, 500);
  }, [onUpdate]);

  function updateField(field, value) {
    const next = { ...form, [field]: value };
    setForm(next);
    scheduleUpdate(next);
  }

  function toggleSubtask(index) {
    const subtasks = [...(form.subtasks || [])];
    subtasks[index] = { ...subtasks[index], done: !subtasks[index].done };
    updateField('subtasks', subtasks);
  }

  function addSubtask(text) {
    if (!text.trim()) return;
    const subtasks = [...(form.subtasks || []), { text: text.trim(), done: false }];
    updateField('subtasks', subtasks);
  }

  function removeSubtask(index) {
    const subtasks = (form.subtasks || []).filter((_, i) => i !== index);
    updateField('subtasks', subtasks);
  }

  function addComment(text) {
    if (!text.trim()) return;
    const comments = [...(form.comments || []), { text: text.trim(), author: 'Ruslan', date: new Date().toISOString() }];
    updateField('comments', comments);
  }

  if (!open || !form) return null;

  const overlayRef = useRef(null);

  return (
    <div
      ref={overlayRef}
      className="fixed inset-0 z-50 flex items-center justify-center bg-ctp-crust/70"
      onClick={(e) => e.target === overlayRef.current && onClose()}
    >
      <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip w-full max-w-2xl mx-4 shadow-2xl max-h-[85vh] flex flex-col">
        {/* Header */}
        <div className="flex items-center justify-between px-4 py-3 border-b-2 border-ctp-surface1 bg-ctp-surface0/30 shrink-0">
          <h2 className="font-pixel text-[11px] text-ctp-mauve">CARD DETAIL</h2>
          <div className="flex items-center gap-2">
            <button onClick={() => onDelete(form.id)} className="p-1 text-ctp-overlay1 hover:text-ctp-red">
              <Trash2 size={14} />
            </button>
            <button onClick={onClose} className="p-1 text-ctp-overlay1 hover:text-ctp-red">
              <X size={16} />
            </button>
          </div>
        </div>

        <div className="flex-1 overflow-y-auto m-2 border border-ctp-surface0 p-4 space-y-4">
          {/* Title */}
          <input
            value={form.title}
            onChange={(e) => updateField('title', e.target.value)}
            className="w-full bg-transparent text-ctp-text text-lg font-semibold border-b border-ctp-surface1 pb-1 focus:border-ctp-mauve focus:outline-none"
          />

          {/* Priority + Assignee + Due date row */}
          <div className="grid grid-cols-3 gap-3">
            <div>
              <label className="text-[10px] text-ctp-overlay0 block mb-1">Priority</label>
              <select
                value={form.priority}
                onChange={(e) => updateField('priority', e.target.value)}
                className="w-full bg-ctp-surface0 text-ctp-text text-xs p-1.5 border border-ctp-surface1 focus:outline-none"
              >
                {PRIORITIES.map((p) => <option key={p} value={p}>{p}</option>)}
              </select>
            </div>
            <div>
              <label className="text-[10px] text-ctp-overlay0 block mb-1">Assignee</label>
              <input
                value={form.assignee || ''}
                onChange={(e) => updateField('assignee', e.target.value || null)}
                placeholder="agent-name"
                className="w-full bg-ctp-surface0 text-ctp-text text-xs p-1.5 border border-ctp-surface1 focus:outline-none placeholder:text-ctp-overlay0"
              />
            </div>
            <div>
              <label className="text-[10px] text-ctp-overlay0 block mb-1">Due date</label>
              <input
                type="date"
                value={form.due_date || ''}
                onChange={(e) => updateField('due_date', e.target.value || null)}
                className="w-full bg-ctp-surface0 text-ctp-text text-xs p-1.5 border border-ctp-surface1 focus:outline-none"
              />
            </div>
          </div>

          {/* Tags */}
          <div>
            <label className="text-[10px] text-ctp-overlay0 block mb-1">Tags (comma-separated)</label>
            <input
              value={(form.tags || []).join(', ')}
              onChange={(e) => updateField('tags', e.target.value.split(',').map((t) => t.trim()).filter(Boolean))}
              className="w-full bg-ctp-surface0 text-ctp-text text-xs p-1.5 border border-ctp-surface1 focus:outline-none placeholder:text-ctp-overlay0"
              placeholder="tag1, tag2"
            />
          </div>

          {/* Description */}
          <div>
            <label className="text-[10px] text-ctp-overlay0 block mb-1">Description</label>
            <textarea
              rows={4}
              value={form.description || ''}
              onChange={(e) => updateField('description', e.target.value)}
              placeholder="Markdown description..."
              className="w-full bg-ctp-surface0 text-ctp-text text-xs p-2 border border-ctp-surface1 focus:outline-none resize-y font-mono placeholder:text-ctp-overlay0"
            />
          </div>

          {/* Subtasks */}
          <div>
            <label className="text-[10px] text-ctp-overlay0 block mb-1">Subtasks</label>
            <div className="space-y-1">
              {(form.subtasks || []).map((st, i) => (
                <div key={i} className="flex items-center gap-2">
                  <button onClick={() => toggleSubtask(i)} className={`w-4 h-4 border border-ctp-surface1 flex items-center justify-center ${st.done ? 'bg-ctp-green' : 'bg-ctp-surface0'}`}>
                    {st.done && <Check size={10} className="text-ctp-crust" />}
                  </button>
                  <span className={`text-xs flex-1 ${st.done ? 'text-ctp-overlay0 line-through' : 'text-ctp-text'}`}>{st.text}</span>
                  <button onClick={() => removeSubtask(i)} className="text-ctp-overlay0 hover:text-ctp-red"><Trash2 size={10} /></button>
                </div>
              ))}
            </div>
            <SubtaskInput onAdd={addSubtask} />
          </div>

          {/* Comments */}
          <div>
            <label className="text-[10px] text-ctp-overlay0 block mb-1">Comments</label>
            <div className="space-y-2 mb-2">
              {(form.comments || []).map((c, i) => (
                <div key={i} className="bg-ctp-surface0/50 border border-ctp-surface0 p-2">
                  <div className="flex items-center gap-2 mb-1">
                    <span className="text-[10px] font-semibold text-ctp-subtext1">{c.author}</span>
                    <span className="text-[9px] text-ctp-overlay0 font-mono">{c.date?.slice(0, 10)}</span>
                  </div>
                  <p className="text-xs text-ctp-subtext0">{c.text}</p>
                </div>
              ))}
            </div>
            <CommentInput onAdd={addComment} />
          </div>
        </div>
      </div>
    </div>
  );
}

function SubtaskInput({ onAdd }) {
  const [text, setText] = useState('');
  return (
    <div className="flex gap-1.5 mt-1.5">
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={(e) => { if (e.key === 'Enter') { onAdd(text); setText(''); } }}
        placeholder="Add subtask..."
        className="flex-1 bg-ctp-surface0 text-ctp-text text-[10px] px-2 py-1 border border-ctp-surface1 focus:outline-none placeholder:text-ctp-overlay0"
      />
      <button onClick={() => { onAdd(text); setText(''); }} className="px-2 py-1 text-[10px] bg-ctp-surface1 text-ctp-text hover:bg-ctp-surface2">
        <Plus size={10} />
      </button>
    </div>
  );
}

function CommentInput({ onAdd }) {
  const [text, setText] = useState('');
  return (
    <div className="flex gap-1.5">
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={(e) => { if (e.key === 'Enter') { onAdd(text); setText(''); } }}
        placeholder="Add comment..."
        className="flex-1 bg-ctp-surface0 text-ctp-text text-[10px] px-2 py-1 border border-ctp-surface1 focus:outline-none placeholder:text-ctp-overlay0"
      />
      <button onClick={() => { onAdd(text); setText(''); }} className="px-2 py-1 text-[10px] bg-ctp-surface1 text-ctp-text hover:bg-ctp-surface2">
        Send
      </button>
    </div>
  );
}
