import { useState, useCallback } from 'react';
import { BookOpen, FolderTree, GitBranch, FileText } from 'lucide-react';
import useFetch from '../hooks/useFetch';
import FileTree from '../components/knowledge/FileTree';
import NotePreview from '../components/knowledge/NotePreview';
import SearchBar from '../components/knowledge/SearchBar';
import KnowledgeGraph from '../components/knowledge/KnowledgeGraph';

const API = import.meta.env.VITE_API_URL || '';

const modes = [
  { id: 'files', label: 'Files', icon: FolderTree },
  { id: 'graph', label: 'Graph', icon: GitBranch },
];

export default function Knowledge() {
  const [mode, setMode] = useState('files');
  const [selectedPath, setSelectedPath] = useState(null);
  const [file, setFile] = useState(null);
  const [fileLoading, setFileLoading] = useState(false);

  const { data: treeData, loading: treeLoading } = useFetch('/api/v1/knowledge/tree');

  const loadFile = useCallback(async (path) => {
    setSelectedPath(path);
    setFileLoading(true);
    try {
      const res = await fetch(`${API}/api/v1/knowledge/file?path=${encodeURIComponent(path)}`);
      const data = await res.json();
      setFile(data);
    } catch {
      setFile(null);
    }
    setFileLoading(false);
  }, []);

  // Navigate from wikilink — search for file by name
  const handleWikiNavigate = useCallback(async (target) => {
    const res = await fetch(`${API}/api/v1/knowledge/search?q=${encodeURIComponent(target)}`);
    const data = await res.json();
    if (data.results?.length > 0) {
      loadFile(data.results[0].path);
    }
  }, [loadFile]);

  // Graph node click
  const handleGraphSelect = useCallback((path) => {
    setMode('files');
    loadFile(path);
  }, [loadFile]);

  return (
    <div className="flex flex-col h-[calc(100vh-5rem)] -m-6">
      {/* Header */}
      <div className="flex items-center justify-between px-6 py-3 border-b-2 border-ctp-surface0 shrink-0">
        <div className="flex items-center gap-3">
          <BookOpen size={24} className="text-ctp-teal" />
          <h2 className="font-pixel text-sm text-ctp-text">KNOWLEDGE BASE</h2>
          {treeLoading && (
            <span className="text-[10px] text-ctp-overlay0 font-mono animate-pulse">loading...</span>
          )}
        </div>

        <div className="flex items-center gap-3">
          {/* Search */}
          <div className="w-64">
            <SearchBar onSelect={loadFile} />
          </div>

          {/* Mode tabs */}
          <div className="flex border-2 border-ctp-surface1 overflow-hidden">
            {modes.map(({ id, label, icon: Icon }) => (
              <button
                key={id}
                onClick={() => setMode(id)}
                className={`flex items-center gap-1.5 px-3 py-1.5 text-xs font-mono transition-colors ${
                  mode === id
                    ? 'bg-ctp-mauve text-ctp-crust'
                    : 'bg-ctp-surface0 text-ctp-overlay1 hover:text-ctp-text hover:bg-ctp-surface1'
                }`}
              >
                <Icon size={12} />
                {label}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Content */}
      <div className="flex-1 flex overflow-hidden">
        {mode === 'files' && (
          <>
            {/* File tree sidebar */}
            <div className="w-72 shrink-0 border-r-2 border-ctp-surface0 bg-ctp-mantle/30 overflow-y-auto">
              <FileTree
                tree={treeData?.tree || []}
                selectedPath={selectedPath}
                onSelect={loadFile}
              />
            </div>

            {/* Note preview */}
            <div className="flex-1 overflow-hidden">
              <NotePreview
                file={file}
                loading={fileLoading}
                onNavigate={handleWikiNavigate}
              />
            </div>
          </>
        )}

        {mode === 'graph' && (
          <div className="flex-1">
            <KnowledgeGraph onSelectFile={handleGraphSelect} />
          </div>
        )}
      </div>
    </div>
  );
}
