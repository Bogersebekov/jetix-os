// Programmatic pixel sprite generator — 16x24 canvas, scaled x4
// Each agent gets unique body color, hair, and accessory

const SPRITE_W = 16;
const SPRITE_H = 24;
const SCALE = 4;

// Agent visual definitions
const AGENT_LOOKS = {
  strategist:           { body: '#cba6f7', hair: '#585b70', skin: '#f5e0dc', acc: 'crown' },
  manager:              { body: '#89b4fa', hair: '#313244', skin: '#f5e0dc', acc: 'tie' },
  'sales-lead':         { body: '#a6e3a1', hair: '#fab387', skin: '#f2cdcd', acc: 'chart' },
  'sales-researcher':   { body: '#94e2d5', hair: '#cdd6f4', skin: '#f5e0dc', acc: 'glasses' },
  'sales-outreach':     { body: '#89dcfe', hair: '#f9e2af', skin: '#f2cdcd', acc: 'mic' },
  'inbox-processor':    { body: '#74c7ec', hair: '#585b70', skin: '#f5e0dc', acc: 'inbox' },
  'knowledge-synth':    { body: '#94e2d5', hair: '#cba6f7', skin: '#f5e0dc', acc: 'book' },
  'personal-assistant': { body: '#b4befe', hair: '#f38ba8', skin: '#f2cdcd', acc: 'star' },
  'system-admin':       { body: '#45475a', hair: '#a6e3a1', skin: '#f5e0dc', acc: 'wrench' },
  'life-coach':         { body: '#fab387', hair: '#313244', skin: '#f2cdcd', acc: 'heart' },
  'meta-agent':         { body: '#f5c2e7', hair: '#89b4fa', skin: '#f5e0dc', acc: 'eye' },
  'crazy-agent':        { body: '#eba0ac', hair: '#f9e2af', skin: '#f5e0dc', acc: 'bolt' },
};

function hexToRgb(hex) {
  const r = parseInt(hex.slice(1, 3), 16);
  const g = parseInt(hex.slice(3, 5), 16);
  const b = parseInt(hex.slice(5, 7), 16);
  return [r, g, b];
}

function drawPixel(ctx, x, y, color) {
  ctx.fillStyle = color;
  ctx.fillRect(x, y, 1, 1);
}

function drawSprite(ctx, look) {
  const { body, hair, skin, acc } = look;
  const outline = '#11111b';
  const shoe = '#313244';
  const pants = '#45475a';

  // Head outline (rows 0-8)
  // Row 0-1: hair top
  for (let x = 5; x <= 10; x++) drawPixel(ctx, x, 0, hair);
  for (let x = 4; x <= 11; x++) drawPixel(ctx, x, 1, hair);

  // Row 2: hair sides + forehead
  drawPixel(ctx, 3, 2, hair); drawPixel(ctx, 4, 2, hair);
  for (let x = 5; x <= 10; x++) drawPixel(ctx, x, 2, skin);
  drawPixel(ctx, 11, 2, hair); drawPixel(ctx, 12, 2, hair);

  // Row 3: face
  drawPixel(ctx, 3, 3, hair);
  for (let x = 4; x <= 11; x++) drawPixel(ctx, x, 3, skin);
  drawPixel(ctx, 12, 3, hair);

  // Row 4: eyes
  drawPixel(ctx, 3, 4, hair);
  drawPixel(ctx, 4, 4, skin);
  drawPixel(ctx, 5, 4, skin);
  drawPixel(ctx, 6, 4, outline); // left eye
  drawPixel(ctx, 7, 4, skin);
  drawPixel(ctx, 8, 4, skin);
  drawPixel(ctx, 9, 4, outline); // right eye
  drawPixel(ctx, 10, 4, skin);
  drawPixel(ctx, 11, 4, skin);
  drawPixel(ctx, 12, 4, hair);

  // Row 5: nose/mouth area
  drawPixel(ctx, 3, 5, outline);
  for (let x = 4; x <= 11; x++) drawPixel(ctx, x, 5, skin);
  drawPixel(ctx, 7, 5, '#f38ba8'); // mouth
  drawPixel(ctx, 8, 5, '#f38ba8');
  drawPixel(ctx, 12, 5, outline);

  // Row 6: chin
  drawPixel(ctx, 4, 6, outline);
  for (let x = 5; x <= 10; x++) drawPixel(ctx, x, 6, skin);
  drawPixel(ctx, 11, 6, outline);

  // Row 7: neck
  drawPixel(ctx, 6, 7, skin); drawPixel(ctx, 7, 7, skin);
  drawPixel(ctx, 8, 7, skin); drawPixel(ctx, 9, 7, skin);

  // Body (rows 8-17)
  for (let y = 8; y <= 15; y++) {
    const w = y < 10 ? 4 : 5;
    const startX = 8 - w;
    const endX = 7 + w;
    for (let x = startX; x <= endX; x++) {
      if (x === startX || x === endX) {
        drawPixel(ctx, x, y, outline);
      } else {
        drawPixel(ctx, x, y, y < 13 ? body : pants);
      }
    }
  }

  // Arms (rows 9-14)
  drawPixel(ctx, 2, 9, body); drawPixel(ctx, 2, 10, body);
  drawPixel(ctx, 2, 11, body); drawPixel(ctx, 2, 12, skin);
  drawPixel(ctx, 13, 9, body); drawPixel(ctx, 13, 10, body);
  drawPixel(ctx, 13, 11, body); drawPixel(ctx, 13, 12, skin);

  // Legs (rows 16-20)
  for (let y = 16; y <= 20; y++) {
    drawPixel(ctx, 5, y, y < 19 ? pants : shoe);
    drawPixel(ctx, 6, y, y < 19 ? pants : shoe);
    drawPixel(ctx, 9, y, y < 19 ? pants : shoe);
    drawPixel(ctx, 10, y, y < 19 ? pants : shoe);
  }

  // Shoes
  drawPixel(ctx, 4, 21, shoe); drawPixel(ctx, 5, 21, shoe);
  drawPixel(ctx, 6, 21, shoe); drawPixel(ctx, 7, 21, shoe);
  drawPixel(ctx, 9, 21, shoe); drawPixel(ctx, 10, 21, shoe);
  drawPixel(ctx, 11, 21, shoe);

  // Accessory marker (small colored pixel on body)
  const accColors = {
    crown: '#f9e2af', tie: '#f38ba8', chart: '#a6e3a1', glasses: '#89b4fa',
    mic: '#cba6f7', inbox: '#74c7ec', book: '#94e2d5', star: '#f9e2af',
    wrench: '#a6adc8', heart: '#f38ba8', eye: '#89b4fa', bolt: '#f9e2af',
  };
  const accColor = accColors[acc] || '#f9e2af';
  drawPixel(ctx, 7, 9, accColor);
  drawPixel(ctx, 8, 9, accColor);
  if (acc === 'crown') {
    drawPixel(ctx, 6, 0, accColor);
    drawPixel(ctx, 8, 0, accColor);
    drawPixel(ctx, 10, 0, accColor);
  }
}

// Cache generated sprites
const spriteCache = new Map();

export function generateSprite(agentId) {
  if (spriteCache.has(agentId)) return spriteCache.get(agentId);

  const canvas = document.createElement('canvas');
  canvas.width = SPRITE_W;
  canvas.height = SPRITE_H;
  const ctx = canvas.getContext('2d');

  const look = AGENT_LOOKS[agentId] || AGENT_LOOKS.manager;
  drawSprite(ctx, look);

  const dataUrl = canvas.toDataURL();
  spriteCache.set(agentId, dataUrl);
  return dataUrl;
}

export function generateErrorSprite(agentId) {
  const key = `${agentId}-error`;
  if (spriteCache.has(key)) return spriteCache.get(key);

  const canvas = document.createElement('canvas');
  canvas.width = SPRITE_W;
  canvas.height = SPRITE_H;
  const ctx = canvas.getContext('2d');

  const look = AGENT_LOOKS[agentId] || AGENT_LOOKS.manager;
  drawSprite(ctx, { ...look, body: '#f38ba8' });

  // Red tint overlay
  ctx.fillStyle = 'rgba(243, 139, 168, 0.2)';
  ctx.fillRect(0, 0, SPRITE_W, SPRITE_H);

  const dataUrl = canvas.toDataURL();
  spriteCache.set(key, dataUrl);
  return dataUrl;
}

export { SPRITE_W, SPRITE_H, SCALE, AGENT_LOOKS };
