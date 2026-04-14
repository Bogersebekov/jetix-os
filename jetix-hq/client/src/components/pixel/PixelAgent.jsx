import { useState, useEffect, useRef, useMemo } from 'react';
import { generateSprite, generateErrorSprite, SPRITE_W, SPRITE_H, SCALE } from './spriteGenerator';
import { StatusDot } from '../ui';

const CLICK_ANIMS = ['jump', 'spin', 'pushup', 'wave'];

export default function PixelAgent({ agent, x, y, onClick }) {
  const [anim, setAnim] = useState(null);
  const [frame, setFrame] = useState(0);
  const animTimer = useRef(null);

  const spriteUrl = useMemo(() => {
    return agent.status === 'error' ? generateErrorSprite(agent.id) : generateSprite(agent.id);
  }, [agent.id, agent.status]);

  // Idle/working animation frame counter
  useEffect(() => {
    const id = setInterval(() => setFrame((f) => f + 1), 200);
    return () => clearInterval(id);
  }, []);

  function handleClick(e) {
    e.stopPropagation();
    // Random click animation
    const a = CLICK_ANIMS[Math.floor(Math.random() * CLICK_ANIMS.length)];
    setAnim(a);
    if (animTimer.current) clearTimeout(animTimer.current);
    animTimer.current = setTimeout(() => setAnim(null), 600);
    onClick?.(agent);
  }

  // Compute transform for current state
  let transform = '';
  const isWorking = agent.status === 'active';
  const isError = agent.status === 'error';

  if (anim === 'jump') {
    transform = `translateY(${frame % 3 === 0 ? -12 : 0}px)`;
  } else if (anim === 'spin') {
    transform = `rotate(${(frame % 4) * 90}deg)`;
  } else if (anim === 'pushup') {
    transform = `scaleY(${frame % 2 === 0 ? 0.8 : 1})`;
  } else if (anim === 'wave') {
    transform = `rotate(${Math.sin(frame * 0.5) * 10}deg)`;
  } else if (isWorking) {
    // Subtle bob
    transform = `translateY(${Math.sin(frame * 0.8) * 2}px)`;
  } else if (isError) {
    // Shake
    transform = `translateX(${(frame % 2 === 0 ? 2 : -2)}px)`;
  }

  const cssX = x * SCALE;
  const cssY = y * SCALE;

  return (
    <div
      className="absolute cursor-pointer group"
      style={{
        left: cssX,
        top: cssY,
        width: SPRITE_W * SCALE,
        height: SPRITE_H * SCALE,
        transform,
        transition: anim ? 'none' : 'transform 0.2s',
        zIndex: Math.floor(y),
      }}
      onClick={handleClick}
    >
      {/* Sprite image */}
      <img
        src={spriteUrl}
        alt={agent.name}
        className="pixel-art w-full h-full"
        style={{ imageRendering: 'pixelated' }}
        draggable={false}
      />

      {/* Status dot */}
      <StatusDot
        status={agent.status}
        size={8}
        className="absolute -bottom-1 left-1/2 -translate-x-1/2"
      />

      {/* Task bubble */}
      {agent.currentTask && (
        <div className="absolute bottom-full left-1/2 -translate-x-1/2 mb-1 px-1.5 py-0.5 bg-ctp-crust border border-ctp-surface1 whitespace-nowrap max-w-[120px] opacity-0 group-hover:opacity-100 transition-opacity">
          <p className="text-[7px] text-ctp-subtext0 truncate">{agent.currentTask}</p>
        </div>
      )}

      {/* Name on hover */}
      <div className="absolute top-full left-1/2 -translate-x-1/2 mt-0.5 opacity-0 group-hover:opacity-100 transition-opacity">
        <p className="font-pixel text-[6px] text-ctp-overlay1 whitespace-nowrap">{agent.name}</p>
      </div>
    </div>
  );
}
