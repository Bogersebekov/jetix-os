const colorMap = {
  mauve: 'bg-ctp-mauve',
  green: 'bg-ctp-green',
  blue: 'bg-ctp-blue',
  peach: 'bg-ctp-peach',
  red: 'bg-ctp-red',
  yellow: 'bg-ctp-yellow',
  teal: 'bg-ctp-teal',
};

export default function ProgressBar({
  value = 0,
  max = 100,
  color = 'mauve',
  label,
  showValue = false,
  size = 'md',
  className = '',
}) {
  const pct = Math.min(100, Math.max(0, (value / max) * 100));
  const heights = { sm: 'h-2', md: 'h-3', lg: 'h-4' };

  return (
    <div className={className}>
      {(label || showValue) && (
        <div className="flex justify-between items-center mb-1">
          {label && <span className="text-xs text-ctp-subtext0">{label}</span>}
          {showValue && (
            <span className="font-pixel text-[8px] text-ctp-subtext1">
              {value}/{max}
            </span>
          )}
        </div>
      )}
      <div className={`w-full ${heights[size]} bg-ctp-surface0 border border-ctp-surface1 overflow-hidden`}>
        <div
          className={`h-full ${colorMap[color]} transition-all duration-300`}
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  );
}
