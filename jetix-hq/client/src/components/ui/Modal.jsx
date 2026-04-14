import { useEffect, useRef } from 'react';
import { X } from 'lucide-react';

export default function Modal({ open, onClose, title, children, className = '' }) {
  const overlayRef = useRef(null);

  useEffect(() => {
    if (!open) return;
    const handleEsc = (e) => e.key === 'Escape' && onClose();
    document.addEventListener('keydown', handleEsc);
    return () => document.removeEventListener('keydown', handleEsc);
  }, [open, onClose]);

  if (!open) return null;

  return (
    <div
      ref={overlayRef}
      className="fixed inset-0 z-50 flex items-center justify-center bg-ctp-crust/70"
      onClick={(e) => e.target === overlayRef.current && onClose()}
    >
      <div
        className={`
          bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip
          w-full max-w-lg mx-4 shadow-2xl
          ${className}
        `}
      >
        {/* Title bar — double border RPG style */}
        <div className="flex items-center justify-between px-4 py-3 border-b-2 border-ctp-surface1 bg-ctp-surface0/30">
          <h2 className="font-pixel text-[11px] text-ctp-mauve">{title}</h2>
          <button
            onClick={onClose}
            className="p-1 text-ctp-overlay1 hover:text-ctp-red transition-colors"
          >
            <X size={16} />
          </button>
        </div>
        {/* Inner frame */}
        <div className="m-2 border border-ctp-surface0 p-4">{children}</div>
      </div>
    </div>
  );
}
