import { useEffect, useState, useRef } from 'react';
import confetti from 'canvas-confetti';

export default function LevelUpOverlay({ level, levelName, levelIcon, onDone }) {
  const [visible, setVisible] = useState(true);
  const fired = useRef(false);

  useEffect(() => {
    if (!fired.current) {
      fired.current = true;
      // Confetti burst
      confetti({
        particleCount: 150,
        spread: 100,
        origin: { y: 0.5 },
        colors: ['#cba6f7', '#89b4fa', '#a6e3a1', '#f9e2af', '#f38ba8', '#fab387'],
      });
    }

    const timer = setTimeout(() => {
      setVisible(false);
      onDone?.();
    }, 3000);
    return () => clearTimeout(timer);
  }, [onDone]);

  if (!visible) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-ctp-crust/80 animate-[fadeIn_0.3s_ease-out]">
      <div className="text-center">
        <div className="text-6xl mb-4 animate-bounce">{levelIcon}</div>
        <h1
          className="font-pixel text-2xl text-ctp-mauve mb-2"
          style={{ textShadow: '0 0 20px #cba6f7, 0 0 40px #cba6f780' }}
        >
          LEVEL UP!
        </h1>
        <p className="font-pixel text-sm text-ctp-text mb-1">Level {level}</p>
        <p className="font-pixel text-[10px] text-ctp-subtext0">{levelName}</p>
      </div>
    </div>
  );
}
