import { useState } from 'react';
import { ChevronRight, ChevronDown, FileText, Folder, FolderOpen } from 'lucide-react';

export default function FileTree({ tree, selectedPath, onSelect }) {
  if (!tree?.length) {
    return <p className="p-4 text-xs text-ctp-overlay0">No files found</p>;
  }

  return (
    <div className="py-1">
      {tree.map((node) => (
        <TreeNode key={node.path} node={node} selectedPath={selectedPath} onSelect={onSelect} depth={0} />
      ))}
    </div>
  );
}

function TreeNode({ node, selectedPath, onSelect, depth }) {
  const [expanded, setExpanded] = useState(depth < 1);

  if (node.type === 'directory') {
    return (
      <div>
        <button
          onClick={() => setExpanded(!expanded)}
          className="w-full flex items-center gap-1.5 px-2 py-1 text-left hover:bg-ctp-surface0/30 transition-colors"
          style={{ paddingLeft: 8 + depth * 14 }}
        >
          {expanded ? (
            <ChevronDown size={12} className="text-ctp-overlay0 shrink-0" />
          ) : (
            <ChevronRight size={12} className="text-ctp-overlay0 shrink-0" />
          )}
          {expanded ? (
            <FolderOpen size={14} className="text-ctp-yellow shrink-0" />
          ) : (
            <Folder size={14} className="text-ctp-yellow shrink-0" />
          )}
          <span className="text-xs text-ctp-subtext0 truncate">{node.name}</span>
          <span className="text-[9px] text-ctp-overlay0 font-mono ml-auto shrink-0">
            {node.children?.length || 0}
          </span>
        </button>
        {expanded && node.children?.map((child) => (
          <TreeNode key={child.path} node={child} selectedPath={selectedPath} onSelect={onSelect} depth={depth + 1} />
        ))}
      </div>
    );
  }

  const isSelected = selectedPath === node.path;

  return (
    <button
      onClick={() => onSelect(node.path)}
      className={`w-full flex items-center gap-1.5 px-2 py-1 text-left transition-colors ${
        isSelected
          ? 'bg-ctp-surface0 text-ctp-blue border-l-2 border-ctp-blue'
          : 'hover:bg-ctp-surface0/30 text-ctp-subtext0 border-l-2 border-transparent'
      }`}
      style={{ paddingLeft: 8 + depth * 14 }}
    >
      <FileText size={14} className={isSelected ? 'text-ctp-blue shrink-0' : 'text-ctp-overlay1 shrink-0'} />
      <span className="text-xs truncate">{node.name.replace('.md', '')}</span>
    </button>
  );
}
