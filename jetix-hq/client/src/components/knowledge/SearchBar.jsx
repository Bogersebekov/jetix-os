import { useState, useEffect, useRef } from 'react';
import { Search, FileText, X } from 'lucide-react';

const API = import.meta.env.VITE_API_URL || '';

export default function SearchBar({ onSelect }) {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [open, setOpen] = useState(false);
  const debounceRef = useRef(null);
  const containerRef = useRef(null);

  useEffect(() => {
    if (!query.trim()) { setResults([]); setOpen(false); return; }

    if (debounceRef.current) clearTimeout(debounceRef.current);
    debounceRef.current = setTimeout(async () => {
      try {
        const res = await fetch(`${API}/api/v1/knowledge/search?q=${encodeURIComponent(query)}`);
        const data = await res.json();
        setResults(data.results || []);
        setOpen(true);
      } catch { setResults([]); }
    }, 300);

    return () => { if (debounceRef.current) clearTimeout(debounceRef.current); };
  }, [query]);

  // Close on outside click
  useEffect(() => {
    function handleClick(e) {
      if (containerRef.current && !containerRef.current.contains(e.target)) setOpen(false);
    }
    document.addEventListener('mousedown', handleClick);
    return () => document.removeEventListener('mousedown', handleClick);
  }, []);

  return (
    <div ref={containerRef} className="relative">
      <div className="relative">
        <Search size={14} className="absolute left-2.5 top-1/2 -translate-y-1/2 text-ctp-overlay0" />
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search files..."
          className="w-full bg-ctp-surface0 text-ctp-text text-sm pl-8 pr-8 py-2 border border-ctp-surface1 focus:border-ctp-mauve focus:outline-none placeholder:text-ctp-overlay0"
        />
        {query && (
          <button onClick={() => { setQuery(''); setResults([]); setOpen(false); }}
            className="absolute right-2.5 top-1/2 -translate-y-1/2 text-ctp-overlay0 hover:text-ctp-text">
            <X size={14} />
          </button>
        )}
      </div>

      {open && results.length > 0 && (
        <div className="absolute top-full left-0 right-0 mt-1 bg-ctp-mantle border-2 border-ctp-surface1 shadow-lg z-20 max-h-64 overflow-y-auto">
          {results.map((r, i) => (
            <button
              key={i}
              onClick={() => { onSelect(r.path); setOpen(false); setQuery(''); }}
              className="w-full flex items-start gap-2 px-3 py-2 text-left hover:bg-ctp-surface0/50 transition-colors border-b border-ctp-surface0/50"
            >
              <FileText size={14} className="text-ctp-overlay1 shrink-0 mt-0.5" />
              <div className="min-w-0">
                <p className="text-xs text-ctp-text truncate">{r.name.replace('.md', '')}</p>
                {r.snippet && (
                  <p className="text-[10px] text-ctp-overlay0 line-clamp-2 mt-0.5">{r.snippet}</p>
                )}
                <p className="text-[9px] text-ctp-overlay0 font-mono mt-0.5">{r.path}</p>
              </div>
            </button>
          ))}
        </div>
      )}

      {open && query && results.length === 0 && (
        <div className="absolute top-full left-0 right-0 mt-1 bg-ctp-mantle border-2 border-ctp-surface1 p-3">
          <p className="text-xs text-ctp-overlay0 text-center">No results for "{query}"</p>
        </div>
      )}
    </div>
  );
}
