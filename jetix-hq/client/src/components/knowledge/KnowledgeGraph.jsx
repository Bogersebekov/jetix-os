import { useMemo, useCallback } from 'react';
import {
  ReactFlow, MiniMap, Controls, Background, useNodesState, useEdgesState,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';
import useFetch from '../../hooks/useFetch';

export default function KnowledgeGraph({ onSelectFile }) {
  const { data, loading } = useFetch('/api/v1/knowledge/graph');

  const { initialNodes, initialEdges } = useMemo(() => {
    if (!data?.nodes?.length) return { initialNodes: [], initialEdges: [] };

    const maxLinks = Math.max(1, ...data.nodes.map((n) => n.links));

    // Simple force-directed-like grid layout
    const cols = Math.ceil(Math.sqrt(data.nodes.length));
    const initialNodes = data.nodes.map((n, i) => {
      const row = Math.floor(i / cols);
      const col = i % cols;
      const size = 30 + (n.links / maxLinks) * 60;
      return {
        id: n.id,
        data: { label: n.label, links: n.links, path: n.id },
        position: { x: col * 180 + Math.random() * 40, y: row * 120 + Math.random() * 30 },
        style: {
          width: size,
          height: size,
          borderRadius: 0,
          background: n.links > 3 ? '#cba6f7' : n.links > 1 ? '#89b4fa' : '#313244',
          border: '2px solid #45475a',
          color: '#cdd6f4',
          fontSize: Math.max(8, Math.min(11, 8 + n.links)),
          fontFamily: '"Press Start 2P", monospace',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: 4,
          textAlign: 'center',
          lineHeight: 1.2,
          overflow: 'hidden',
          cursor: 'pointer',
        },
      };
    });

    const initialEdges = data.edges.map((e, i) => ({
      id: `e-${i}`,
      source: e.source,
      target: e.target,
      style: { stroke: '#45475a', strokeWidth: 1 },
      animated: false,
    }));

    return { initialNodes, initialEdges };
  }, [data]);

  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onNodeClick = useCallback((_, node) => {
    if (node.data.path) onSelectFile?.(node.data.path);
  }, [onSelectFile]);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-full">
        <p className="text-xs text-ctp-overlay0 animate-pulse">Building graph...</p>
      </div>
    );
  }

  if (!nodes.length) {
    return (
      <div className="flex items-center justify-center h-full">
        <p className="text-xs text-ctp-overlay0">No linked notes found</p>
      </div>
    );
  }

  return (
    <div className="h-full w-full">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onNodeClick={onNodeClick}
        fitView
        minZoom={0.2}
        maxZoom={2}
        proOptions={{ hideAttribution: true }}
      >
        <Background color="#313244" gap={20} />
        <Controls
          style={{ background: '#181825', border: '1px solid #45475a', borderRadius: 0 }}
        />
        <MiniMap
          nodeColor={(n) => n.style?.background || '#313244'}
          style={{ background: '#11111b', border: '1px solid #313244' }}
        />
      </ReactFlow>
    </div>
  );
}
