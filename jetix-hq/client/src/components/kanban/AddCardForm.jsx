import { useState } from 'react';
import { Plus, X } from 'lucide-react';

export default function AddCardForm({ columnId, onAdd }) {
  const [open, setOpen] = useState(false);
  const [title, setTitle] = useState('');

  function handleSubmit(e) {
    e.preventDefault();
    if (!title.trim()) return;
    onAdd(columnId, title.trim());
    setTitle('');
    setOpen(false);
  }

  if (!open) {
    return (
      <button
        onClick={() => setOpen(true)}
        className="w-full flex items-center gap-1.5 px-2 py-1.5 text-[10px] text-ctp-overlay0 hover:text-ctp-text hover:bg-ctp-surface0/30 transition-colors"
      >
        <Plus size={12} /> Add card
      </button>
    );
  }

  return (
    <form onSubmit={handleSubmit} className="p-1.5">
      <textarea
        autoFocus
        rows={2}
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); handleSubmit(e); }
          if (e.key === 'Escape') setOpen(false);
        }}
        placeholder="Card title..."
        className="w-full bg-ctp-surface0 text-ctp-text text-xs p-2 border border-ctp-surface1 focus:border-ctp-mauve focus:outline-none resize-none placeholder:text-ctp-overlay0"
      />
      <div className="flex gap-1.5 mt-1.5">
        <button type="submit" className="px-2 py-1 text-[10px] bg-ctp-mauve text-ctp-crust hover:brightness-110">
          Add
        </button>
        <button type="button" onClick={() => setOpen(false)} className="p-1 text-ctp-overlay1 hover:text-ctp-text">
          <X size={12} />
        </button>
      </div>
    </form>
  );
}
