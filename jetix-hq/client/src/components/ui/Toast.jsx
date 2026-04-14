import { useState, useEffect, useCallback, createContext, useContext } from 'react';
import { X, CheckCircle, AlertTriangle, Info, XCircle } from 'lucide-react';

const ToastContext = createContext(null);

const typeConfig = {
  success: { icon: CheckCircle, border: 'border-ctp-green', iconColor: 'text-ctp-green' },
  error: { icon: XCircle, border: 'border-ctp-red', iconColor: 'text-ctp-red' },
  warning: { icon: AlertTriangle, border: 'border-ctp-yellow', iconColor: 'text-ctp-yellow' },
  info: { icon: Info, border: 'border-ctp-blue', iconColor: 'text-ctp-blue' },
};

let toastId = 0;

export function ToastProvider({ children }) {
  const [toasts, setToasts] = useState([]);

  const addToast = useCallback((message, type = 'info', duration = 4000) => {
    const id = ++toastId;
    setToasts((prev) => [...prev.slice(-2), { id, message, type, duration }]);
  }, []);

  const removeToast = useCallback((id) => {
    setToasts((prev) => prev.filter((t) => t.id !== id));
  }, []);

  return (
    <ToastContext.Provider value={addToast}>
      {children}
      <div className="fixed bottom-4 right-4 z-50 flex flex-col gap-2 w-80">
        {toasts.map((toast) => (
          <ToastItem key={toast.id} toast={toast} onClose={() => removeToast(toast.id)} />
        ))}
      </div>
    </ToastContext.Provider>
  );
}

function ToastItem({ toast, onClose }) {
  const { icon: Icon, border, iconColor } = typeConfig[toast.type] || typeConfig.info;

  useEffect(() => {
    const timer = setTimeout(onClose, toast.duration);
    return () => clearTimeout(timer);
  }, [toast.duration, onClose]);

  return (
    <div
      className={`
        bg-ctp-mantle border-2 ${border} rpg-clip p-3
        flex items-start gap-3 shadow-lg
        animate-[slideIn_0.2s_ease-out]
      `}
    >
      <Icon size={18} className={iconColor} />
      <p className="text-sm text-ctp-text flex-1">{toast.message}</p>
      <button onClick={onClose} className="text-ctp-overlay1 hover:text-ctp-text">
        <X size={14} />
      </button>
    </div>
  );
}

export function useToast() {
  const ctx = useContext(ToastContext);
  if (!ctx) throw new Error('useToast must be used within ToastProvider');
  return ctx;
}
