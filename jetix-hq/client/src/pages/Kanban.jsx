import { useState, useCallback } from 'react';
import { Columns3 } from 'lucide-react';
import useFetch from '../hooks/useFetch';
import KanbanBoard from '../components/kanban/KanbanBoard';
import CardDetailModal from '../components/kanban/CardDetailModal';

const API = import.meta.env.VITE_API_URL || '';

const views = [
  { id: 'projects', label: 'Projects' },
  { id: 'agents', label: 'Agent Tasks' },
  { id: 'personal', label: 'Personal' },
];

export default function Kanban() {
  const [view, setView] = useState('projects');
  const [selectedCard, setSelectedCard] = useState(null);
  const [optimisticColumns, setOptimisticColumns] = useState(null);

  const { data, loading, refetch } = useFetch(`/api/v1/kanban?view=${view}`);
  const columns = optimisticColumns || data?.columns || [];

  // Reset optimistic state when data arrives
  const handleRefetch = useCallback(() => {
    setOptimisticColumns(null);
    refetch();
  }, [refetch]);

  // Apply optimistic update to columns
  function applyOptimistic(updater) {
    setOptimisticColumns((prev) => updater(prev || columns));
  }

  // --- Card move (drag-and-drop) ---
  const handleMove = useCallback(async (cardId, srcColId, destColId, destIdx) => {
    // Optimistic: move card in local state
    applyOptimistic((cols) => {
      const next = cols.map((col) => ({ ...col, cards: [...col.cards] }));
      const srcCol = next.find((c) => c.id === srcColId);
      const destCol = next.find((c) => c.id === destColId);
      if (!srcCol || !destCol) return cols;

      const cardIdx = srcCol.cards.findIndex((c) => c.id === cardId);
      if (cardIdx === -1) return cols;
      const [card] = srcCol.cards.splice(cardIdx, 1);
      card.column_id = destColId;
      destCol.cards.splice(destIdx, 0, card);
      return next;
    });

    // Persist: build position updates
    const currentCols = optimisticColumns || columns;
    const destCol = currentCols.find((c) => c.id === destColId);
    const srcCol = currentCols.find((c) => c.id === srcColId);

    // Build updates for all cards in affected columns
    const updates = [];
    const affectedCols = srcColId === destColId ? [destCol] : [srcCol, destCol];
    // Recompute from optimistic state after move
    const afterMove = (optimisticColumns || columns).map((col) => ({ ...col, cards: [...col.cards] }));
    const src = afterMove.find((c) => c.id === srcColId);
    const dst = afterMove.find((c) => c.id === destColId);
    if (src && srcColId !== destColId) {
      const ci = src.cards.findIndex((c) => c.id === cardId);
      if (ci !== -1) src.cards.splice(ci, 1);
    }
    if (dst) {
      const ci = dst.cards.findIndex((c) => c.id === cardId);
      if (ci === -1) {
        const card = currentCols.flatMap((c) => c.cards).find((c) => c.id === cardId);
        if (card) dst.cards.splice(destIdx, 0, { ...card, column_id: destColId });
      }
    }

    for (const col of [src, dst].filter(Boolean)) {
      col.cards.forEach((c, i) => {
        updates.push({ id: c.id, column_id: col.id, position: i * 1000 });
      });
    }

    try {
      await fetch(`${API}/api/v1/kanban/cards/reorder`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ updates }),
      });
    } catch { /* ignore — optimistic already applied */ }

    setTimeout(handleRefetch, 300);
  }, [columns, optimisticColumns, handleRefetch]);

  // --- Add card ---
  const handleAdd = useCallback(async (columnId, title) => {
    // Optimistic
    const tempId = `temp-${Date.now()}`;
    const tempCard = { id: tempId, title, column_id: columnId, priority: 'medium', tags: [], subtasks: [], comments: [] };
    applyOptimistic((cols) =>
      cols.map((col) =>
        col.id === columnId ? { ...col, cards: [...col.cards, tempCard] } : col
      )
    );

    try {
      await fetch(`${API}/api/v1/kanban/cards`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ view, column_id: columnId, title }),
      });
    } catch { /* ignore */ }

    setTimeout(handleRefetch, 200);
  }, [view, handleRefetch]);

  // --- Update card ---
  const handleUpdate = useCallback(async (card) => {
    // Optimistic
    applyOptimistic((cols) =>
      cols.map((col) => ({
        ...col,
        cards: col.cards.map((c) => c.id === card.id ? { ...c, ...card } : c),
      }))
    );
    setSelectedCard((prev) => prev ? { ...prev, ...card } : prev);

    try {
      await fetch(`${API}/api/v1/kanban/cards/${card.id}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(card),
      });
    } catch { /* ignore */ }
  }, []);

  // --- Delete card ---
  const handleDelete = useCallback(async (cardId) => {
    setSelectedCard(null);
    applyOptimistic((cols) =>
      cols.map((col) => ({
        ...col,
        cards: col.cards.filter((c) => c.id !== cardId),
      }))
    );

    try {
      await fetch(`${API}/api/v1/kanban/cards/${cardId}`, { method: 'DELETE' });
    } catch { /* ignore */ }

    setTimeout(handleRefetch, 200);
  }, [handleRefetch]);

  // --- View switch ---
  function switchView(newView) {
    setView(newView);
    setOptimisticColumns(null);
    setSelectedCard(null);
  }

  return (
    <div className="flex flex-col h-[calc(100vh-5rem)] -m-6 p-6">
      {/* Header */}
      <div className="flex items-center justify-between mb-4 shrink-0">
        <div className="flex items-center gap-3">
          <Columns3 size={24} className="text-ctp-peach" />
          <h2 className="font-pixel text-sm text-ctp-text">TASK BOARD</h2>
          {loading && !optimisticColumns && (
            <span className="text-[10px] text-ctp-overlay0 font-mono animate-pulse">loading...</span>
          )}
        </div>

        {/* View tabs */}
        <div className="flex border-2 border-ctp-surface1 overflow-hidden">
          {views.map(({ id, label }) => (
            <button
              key={id}
              onClick={() => switchView(id)}
              className={`px-4 py-1.5 text-xs font-mono transition-colors ${
                view === id
                  ? 'bg-ctp-mauve text-ctp-crust'
                  : 'bg-ctp-surface0 text-ctp-overlay1 hover:text-ctp-text hover:bg-ctp-surface1'
              }`}
            >
              {label}
            </button>
          ))}
        </div>
      </div>

      {/* Board */}
      <div className="flex-1 overflow-hidden">
        <KanbanBoard
          columns={columns}
          onMove={handleMove}
          onAdd={handleAdd}
          onCardClick={setSelectedCard}
        />
      </div>

      {/* Card detail modal */}
      <CardDetailModal
        card={selectedCard}
        open={!!selectedCard}
        onClose={() => setSelectedCard(null)}
        onUpdate={handleUpdate}
        onDelete={handleDelete}
      />
    </div>
  );
}
