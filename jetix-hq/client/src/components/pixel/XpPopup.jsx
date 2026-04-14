import { useState, useEffect } from 'react';

export default function XpPopup({ amount, x, y, onDone }) {
  const [offset, setOffset] = useState(0);
  const [opacity, setOpacity] = useState(1);

  useEffect(() => {
    let frame = 0;
    const id = setInterval(() => {
      frame++;
      setOffset(frame * 2);
      setOpacity(Math.max(0, 1 - frame * 0.04));
      if (frame > 25) {
        clearInterval(id);
        onDone?.();
      }
    }, 30);
    return () => clearInterval(id);
  }, [onDone]);

  return (
    <div
      className="fixed pointer-events-none z-50 font-pixel"
      style={{
        left: x,
        top: y - offset,
        opacity,
        color: '#cba6f7',
        fontSize: 14,
        textShadow: '0 0 4px #cba6f7, 2px 2px 0 #11111b',
      }}
    >
      +{amount} XP
    </div>
  );
}
