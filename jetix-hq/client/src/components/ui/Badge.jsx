const statusColors = {
  active: 'bg-ctp-green/20 text-ctp-green border-ctp-green/30',
  idle: 'bg-ctp-yellow/20 text-ctp-yellow border-ctp-yellow/30',
  error: 'bg-ctp-red/20 text-ctp-red border-ctp-red/30',
  offline: 'bg-ctp-surface2/20 text-ctp-overlay1 border-ctp-surface2/30',
};

export default function Badge({ status = 'offline', label, className = '' }) {
  return (
    <span
      className={`
        inline-flex items-center gap-1.5 px-2 py-0.5
        text-[10px] font-pixel border rounded-sm
        ${statusColors[status]}
        ${className}
      `}
    >
      <span
        className={`w-1.5 h-1.5 rounded-full ${
          status === 'active'
            ? 'bg-ctp-green animate-pulse'
            : status === 'error'
            ? 'bg-ctp-red animate-pulse'
            : status === 'idle'
            ? 'bg-ctp-yellow'
            : 'bg-ctp-overlay0'
        }`}
      />
      {label || status}
    </span>
  );
}
