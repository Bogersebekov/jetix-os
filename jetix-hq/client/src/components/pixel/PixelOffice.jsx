import { useRef, useEffect, useState, useMemo } from 'react';
import { ZoomIn, ZoomOut, Maximize2 } from 'lucide-react';
import { TILE_SIZE, TILE_SCALE, MAP_W, MAP_H, renderTileMap, roomPositions, roomLabels } from './tileMap';
import { SPRITE_W, SPRITE_H } from './spriteGenerator';
import PixelAgent from './PixelAgent';

const CANVAS_W = MAP_W * TILE_SIZE;
const CANVAS_H = MAP_H * TILE_SIZE;

export default function PixelOffice({ agents, rooms, onAgentClick }) {
  const canvasRef = useRef(null);
  const frameRef = useRef(0);
  const [zoom, setZoom] = useState(1);

  // Animate tile map (server LEDs, lamps)
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    let animId;
    function draw() {
      frameRef.current++;
      renderTileMap(ctx, frameRef.current);
      animId = requestAnimationFrame(draw);
    }
    draw();
    return () => cancelAnimationFrame(animId);
  }, []);

  // Place agents in their rooms
  const agentPositions = useMemo(() => {
    const positions = [];
    for (const room of rooms) {
      const bounds = roomPositions[room.id];
      if (!bounds) continue;

      const roomAgents = room.agents
        .map((id) => agents.find((a) => a.id === id))
        .filter(Boolean);

      roomAgents.forEach((agent, i) => {
        // Position within room, evenly spaced
        const cols = Math.min(roomAgents.length, bounds.w);
        const col = i % cols;
        const row = Math.floor(i / cols);
        const px = (bounds.x + col + 0.5) * TILE_SIZE - SPRITE_W / 2;
        const py = (bounds.y + row + 1) * TILE_SIZE - SPRITE_H + 4;
        positions.push({ agent, x: px, y: py });
      });
    }
    return positions;
  }, [agents, rooms]);

  const scaleStyle = {
    transform: `scale(${zoom * TILE_SCALE})`,
    transformOrigin: 'top left',
    width: CANVAS_W,
    height: CANVAS_H,
  };

  return (
    <div className="relative">
      {/* Zoom controls */}
      <div className="absolute top-2 right-2 z-20 flex gap-1">
        <button
          onClick={() => setZoom((z) => Math.min(z + 0.25, 2))}
          className="p-1.5 bg-ctp-surface0 border border-ctp-surface1 text-ctp-overlay1 hover:text-ctp-text"
        >
          <ZoomIn size={12} />
        </button>
        <button
          onClick={() => setZoom((z) => Math.max(z - 0.25, 0.5))}
          className="p-1.5 bg-ctp-surface0 border border-ctp-surface1 text-ctp-overlay1 hover:text-ctp-text"
        >
          <ZoomOut size={12} />
        </button>
        <button
          onClick={() => setZoom(1)}
          className="p-1.5 bg-ctp-surface0 border border-ctp-surface1 text-ctp-overlay1 hover:text-ctp-text"
        >
          <Maximize2 size={12} />
        </button>
      </div>

      {/* Scrollable container */}
      <div className="overflow-auto border-2 border-ctp-surface1 bg-ctp-crust" style={{ maxHeight: 520 }}>
        <div style={{ width: CANVAS_W * TILE_SCALE * zoom, height: CANVAS_H * TILE_SCALE * zoom }}>
          <div className="relative" style={scaleStyle}>
            {/* Tile map canvas */}
            <canvas
              ref={canvasRef}
              width={CANVAS_W}
              height={CANVAS_H}
              className="pixel-art absolute top-0 left-0"
              style={{ imageRendering: 'pixelated', width: CANVAS_W, height: CANVAS_H }}
            />

            {/* Room labels */}
            {roomLabels.map((room) => (
              <div
                key={room.id}
                className="absolute pointer-events-none"
                style={{
                  left: room.x * TILE_SIZE + 2,
                  top: room.y * TILE_SIZE - 1,
                }}
              >
                <span className="font-pixel text-[4px] text-ctp-overlay0 opacity-60 whitespace-nowrap">
                  {room.emoji} {room.name}
                </span>
              </div>
            ))}

            {/* Agent sprites (HTML overlay) */}
            {agentPositions.map(({ agent, x, y }) => (
              <PixelAgent
                key={agent.id}
                agent={agent}
                x={x}
                y={y}
                onClick={onAgentClick}
              />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
