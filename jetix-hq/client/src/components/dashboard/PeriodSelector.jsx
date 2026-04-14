const periods = [
  { id: 'today', label: 'Today' },
  { id: 'week', label: 'Week' },
  { id: 'month', label: 'Month' },
];

export default function PeriodSelector({ value, onChange }) {
  return (
    <div className="flex border-2 border-ctp-surface1 overflow-hidden">
      {periods.map(({ id, label }) => (
        <button
          key={id}
          onClick={() => onChange(id)}
          className={`px-4 py-1.5 text-xs font-mono transition-colors ${
            value === id
              ? 'bg-ctp-mauve text-ctp-crust'
              : 'bg-ctp-surface0 text-ctp-overlay1 hover:text-ctp-text hover:bg-ctp-surface1'
          }`}
        >
          {label}
        </button>
      ))}
    </div>
  );
}
