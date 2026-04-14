const dotColors = {
  active: 'bg-ctp-green',
  error: 'bg-ctp-red',
  idle: 'bg-ctp-yellow',
  offline: 'bg-ctp-overlay0',
};

export default function StatusDot({ status = 'offline', size = 8, className = '' }) {
  const pulseClass = status === 'active' || status === 'error' ? 'animate-pulse' : '';

  return (
    <span
      className={`inline-block rounded-full ${dotColors[status]} ${pulseClass} ${className}`}
      style={{ width: size, height: size }}
      title={status}
    />
  );
}
