import { useState, useCallback } from 'react';
import {
  DndContext, closestCorners, PointerSensor, useSensor, useSensors,
  DragOverlay,
} from '@dnd-kit/core';
import {
  SortableContext, verticalListSortingStrategy,
} from '@dnd-kit/sortable';
import KanbanCard from './KanbanCard';
import AddCardForm from './AddCardForm';

export default function KanbanBoard({ columns, onMove, onAdd, onCardClick }) {
  const [activeCard, setActiveCard] = useState(null);
  const sensors = useSensors(
    useSensor(PointerSensor, { activationConstraint: { distance: 5 } })
  );

  const handleDragStart = useCallback((event) => {
    const card = findCard(columns, event.active.id);
    setActiveCard(card);
  }, [columns]);

  const handleDragEnd = useCallback((event) => {
    const { active, over } = event;
    setActiveCard(null);
    if (!over || active.id === over.id) return;

    // Find source column and card
    let srcCol = null, srcIdx = -1;
    for (const col of columns) {
      const idx = col.cards.findIndex((c) => c.id === active.id);
      if (idx !== -1) { srcCol = col; srcIdx = idx; break; }
    }
    if (!srcCol) return;

    // Determine destination column
    let destCol = columns.find((col) => col.id === over.id);
    let destIdx = -1;

    if (!destCol) {
      // Over is a card, find its column
      for (const col of columns) {
        const idx = col.cards.findIndex((c) => c.id === over.id);
        if (idx !== -1) { destCol = col; destIdx = idx; break; }
      }
    }

    if (!destCol) return;

    // If dropped on column header (no destIdx), append to end
    if (destIdx === -1) destIdx = destCol.cards.length;

    onMove(active.id, srcCol.id, destCol.id, destIdx);
  }, [columns, onMove]);

  return (
    <DndContext
      sensors={sensors}
      collisionDetection={closestCorners}
      onDragStart={handleDragStart}
      onDragEnd={handleDragEnd}
    >
      <div className="flex gap-4 h-full overflow-x-auto pb-2">
        {columns.map((col) => (
          <KanbanColumn
            key={col.id}
            column={col}
            onAdd={onAdd}
            onCardClick={onCardClick}
          />
        ))}
      </div>

      <DragOverlay>
        {activeCard && (
          <div className="w-60 opacity-90 rotate-2">
            <KanbanCard card={activeCard} />
          </div>
        )}
      </DragOverlay>
    </DndContext>
  );
}

function KanbanColumn({ column, onAdd, onCardClick }) {
  const { id, label, color, wipLimit, cards } = column;
  const count = cards.length;
  const overWip = wipLimit > 0 && count >= wipLimit;
  const cardIds = cards.map((c) => c.id);

  return (
    <div className="w-64 shrink-0 flex flex-col" id={id}>
      {/* Header */}
      <div className={`flex items-center gap-2 mb-2 px-1 py-1 ${overWip ? 'bg-ctp-red/10 border border-ctp-red/30' : ''}`}>
        <div className="w-2.5 h-2.5" style={{ backgroundColor: color }} />
        <span className="font-pixel text-[9px] text-ctp-subtext0">{label}</span>
        <span className={`text-[10px] font-mono ml-auto ${overWip ? 'text-ctp-red font-bold' : 'text-ctp-overlay0'}`}>
          {count}{wipLimit > 0 ? `/${wipLimit}` : ''}
        </span>
      </div>

      {/* Cards */}
      <SortableContext items={cardIds} strategy={verticalListSortingStrategy} id={id}>
        <div className="flex-1 bg-ctp-mantle/30 border-2 border-dashed border-ctp-surface0 rounded-sm p-1.5 space-y-1.5 overflow-y-auto min-h-[100px]">
          {cards.map((card) => (
            <KanbanCard key={card.id} card={card} onClick={onCardClick} />
          ))}
          <AddCardForm columnId={id} onAdd={onAdd} />
        </div>
      </SortableContext>
    </div>
  );
}

function findCard(columns, cardId) {
  for (const col of columns) {
    const card = col.cards.find((c) => c.id === cardId);
    if (card) return card;
  }
  return null;
}
