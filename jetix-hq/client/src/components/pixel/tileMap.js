// Tile-based office map — 20x16 grid, each tile 16x16 px (rendered at 4x = 64x64 CSS)
export const TILE_SIZE = 16;
export const TILE_SCALE = 4;
export const MAP_W = 20;
export const MAP_H = 16;

// Tile types
export const TILES = {
  VOID:   0,
  WOOD:   1,
  STONE:  2,
  CARPET: 3,
  METAL:  4,
  WALL_H: 5,  // horizontal wall
  WALL_V: 6,  // vertical wall
  DOOR:   7,
  DESK:   8,
  CHAIR:  9,
  SERVER: 10,
  PLANT:  11,
  COUCH:  12,
  BOOK:   13,
  LAMP:   14,
};

// Colors for each tile
export const TILE_COLORS = {
  [TILES.VOID]:   '#11111b',
  [TILES.WOOD]:   '#3b3222',
  [TILES.STONE]:  '#2a2a3a',
  [TILES.CARPET]: '#2d2040',
  [TILES.METAL]:  '#252535',
  [TILES.WALL_H]: '#45475a',
  [TILES.WALL_V]: '#45475a',
  [TILES.DOOR]:   '#585b70',
  [TILES.DESK]:   '#5a4a32',
  [TILES.CHAIR]:  '#4a3a28',
  [TILES.SERVER]: '#313244',
  [TILES.PLANT]:  '#2d5a3a',
  [TILES.COUCH]:  '#4a2840',
  [TILES.BOOK]:   '#3a4a5a',
  [TILES.LAMP]:   '#f9e2af',
};

// Secondary detail colors
const TILE_DETAIL = {
  [TILES.WOOD]:   '#453a2a',
  [TILES.STONE]:  '#323244',
  [TILES.CARPET]: '#362848',
  [TILES.METAL]:  '#2d2d3d',
  [TILES.DESK]:   '#6a5a42',
  [TILES.SERVER]: '#a6e3a1', // LED blink
};

// 20x16 office layout
// T = tile enum values
const T = TILES;
export const officeMap = [
  // Row 0: top wall
  [T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H],
  // Row 1-3: Director(0-4) | Management(5-9) | Sales(10-14) | Brain(15-19)
  [T.WALL_V,T.CARPET,T.CARPET,T.DESK,T.WALL_V,T.WOOD,T.WOOD,T.DESK,T.WOOD,T.WALL_V,T.WOOD,T.WOOD,T.DESK,T.WOOD,T.WALL_V,T.STONE,T.STONE,T.DESK,T.STONE,T.WALL_V],
  [T.WALL_V,T.CARPET,T.LAMP, T.CARPET,T.DOOR,  T.WOOD,T.WOOD,T.WOOD,T.CHAIR,T.DOOR,  T.WOOD,T.DESK,T.WOOD,T.WOOD,T.DOOR,  T.STONE,T.BOOK,T.STONE,T.STONE,T.WALL_V],
  [T.WALL_V,T.CARPET,T.CARPET,T.CARPET,T.WALL_V,T.WOOD,T.CHAIR,T.WOOD,T.WOOD,T.WALL_V,T.WOOD,T.WOOD,T.CHAIR,T.DESK,T.WALL_V,T.STONE,T.STONE,T.STONE,T.BOOK,T.WALL_V],
  [T.WALL_V,T.CARPET,T.PLANT, T.CARPET,T.WALL_V,T.WOOD,T.WOOD,T.WOOD,T.WOOD,T.WALL_V,T.WOOD,T.WOOD,T.WOOD,T.WOOD,T.WALL_V,T.STONE,T.STONE,T.LAMP, T.STONE,T.WALL_V],
  // Row 5: mid wall/doors
  [T.WALL_H,T.WALL_H,T.WALL_H,T.DOOR, T.WALL_H,T.WALL_H,T.WALL_H,T.DOOR, T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.DOOR, T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.DOOR, T.WALL_H,T.WALL_H],
  // Row 6: Hallway
  [T.WALL_V,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.WALL_V],
  [T.WALL_V,T.STONE,T.PLANT,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.STONE,T.PLANT,T.STONE,T.WALL_V],
  // Row 8: mid wall/doors
  [T.WALL_H,T.WALL_H,T.WALL_H,T.DOOR, T.WALL_H,T.WALL_H,T.WALL_H,T.DOOR, T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.DOOR, T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.DOOR, T.WALL_H,T.WALL_H],
  // Row 9-12: Server(0-4) | Lounge(5-9) | Lab(10-14) | Attic(15-19)
  [T.WALL_V,T.METAL,T.SERVER,T.METAL,T.WALL_V,T.WOOD,T.WOOD,T.WOOD,T.WOOD,T.WALL_V,T.STONE,T.STONE,T.DESK,T.STONE,T.WALL_V,T.CARPET,T.CARPET,T.CARPET,T.CARPET,T.WALL_V],
  [T.WALL_V,T.METAL,T.METAL,T.SERVER,T.DOOR,  T.WOOD,T.COUCH,T.WOOD,T.WOOD,T.DOOR,  T.STONE,T.BOOK,T.STONE,T.LAMP, T.DOOR,  T.CARPET,T.LAMP, T.CARPET,T.CARPET,T.WALL_V],
  [T.WALL_V,T.METAL,T.SERVER,T.METAL,T.WALL_V,T.WOOD,T.WOOD,T.PLANT,T.WOOD,T.WALL_V,T.STONE,T.STONE,T.STONE,T.STONE,T.WALL_V,T.CARPET,T.CARPET,T.PLANT, T.CARPET,T.WALL_V],
  [T.WALL_V,T.METAL,T.METAL,T.METAL,T.WALL_V,T.WOOD,T.WOOD,T.WOOD,T.COUCH,T.WALL_V,T.STONE,T.STONE,T.DESK,T.STONE,T.WALL_V,T.CARPET,T.CARPET,T.CARPET,T.CARPET,T.WALL_V],
  // Row 13: bottom wall
  [T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H,T.WALL_H],
  // Row 14-15: void
  [T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID],
  [T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID,T.VOID],
];

// Room boundaries (tile coords) for placing agents
export const roomPositions = {
  director:   { x: 1, y: 1, w: 3, h: 4 },   // cols 1-3, rows 1-4
  management: { x: 5, y: 1, w: 4, h: 4 },
  sales:      { x: 10, y: 1, w: 4, h: 4 },
  brain:      { x: 15, y: 1, w: 4, h: 4 },
  server:     { x: 1, y: 9, w: 3, h: 4 },
  lounge:     { x: 5, y: 9, w: 4, h: 4 },
  lab:        { x: 10, y: 9, w: 4, h: 4 },
  attic:      { x: 15, y: 9, w: 4, h: 4 },
};

// Room labels for overlay
export const roomLabels = [
  { id: 'director', emoji: '🌟', name: "Director's", x: 1, y: 1 },
  { id: 'management', emoji: '📊', name: 'Management', x: 5, y: 1 },
  { id: 'sales', emoji: '💰', name: 'Sales', x: 10, y: 1 },
  { id: 'brain', emoji: '📝', name: 'Brain', x: 15, y: 1 },
  { id: 'server', emoji: '🤖', name: 'Server Room', x: 1, y: 9 },
  { id: 'lounge', emoji: '🏋️', name: 'Lounge', x: 5, y: 9 },
  { id: 'lab', emoji: '🎓', name: 'Lab', x: 10, y: 9 },
  { id: 'attic', emoji: '🤪', name: 'Attic', x: 15, y: 9 },
];

// Render the tile map to a canvas
export function renderTileMap(ctx, frameCount = 0) {
  for (let y = 0; y < MAP_H; y++) {
    for (let x = 0; x < MAP_W; x++) {
      const tile = officeMap[y]?.[x] ?? TILES.VOID;
      const color = TILE_COLORS[tile];

      ctx.fillStyle = color;
      ctx.fillRect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE);

      // Detail patterns
      const detail = TILE_DETAIL[tile];
      if (detail && tile === TILES.WOOD) {
        // Wood grain
        if ((x + y) % 3 === 0) {
          ctx.fillStyle = detail;
          ctx.fillRect(x * TILE_SIZE + 2, y * TILE_SIZE + 4, 12, 1);
          ctx.fillRect(x * TILE_SIZE + 4, y * TILE_SIZE + 10, 8, 1);
        }
      }
      if (tile === TILES.CARPET && (x + y) % 2 === 0) {
        ctx.fillStyle = TILE_DETAIL[TILES.CARPET];
        ctx.fillRect(x * TILE_SIZE + 1, y * TILE_SIZE + 1, 6, 6);
      }
      if (tile === TILES.METAL) {
        ctx.fillStyle = TILE_DETAIL[TILES.METAL];
        ctx.fillRect(x * TILE_SIZE, y * TILE_SIZE + 8, TILE_SIZE, 1);
      }

      // Server LED blink
      if (tile === TILES.SERVER) {
        const blinkOn = (frameCount + x * 7 + y * 3) % 60 < 30;
        ctx.fillStyle = blinkOn ? '#a6e3a1' : '#313244';
        ctx.fillRect(x * TILE_SIZE + 6, y * TILE_SIZE + 3, 2, 2);
        ctx.fillStyle = blinkOn ? '#f38ba8' : '#313244';
        ctx.fillRect(x * TILE_SIZE + 10, y * TILE_SIZE + 3, 2, 2);
        // Rack lines
        ctx.fillStyle = '#3a3a4a';
        ctx.fillRect(x * TILE_SIZE + 2, y * TILE_SIZE + 7, 12, 1);
        ctx.fillRect(x * TILE_SIZE + 2, y * TILE_SIZE + 11, 12, 1);
      }

      // Lamp glow
      if (tile === TILES.LAMP) {
        ctx.fillStyle = `rgba(249, 226, 175, ${0.3 + Math.sin(frameCount * 0.05) * 0.15})`;
        ctx.fillRect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE);
      }

      // Wall detail
      if (tile === TILES.WALL_H) {
        ctx.fillStyle = '#3a3a4a';
        ctx.fillRect(x * TILE_SIZE, y * TILE_SIZE + TILE_SIZE - 2, TILE_SIZE, 2);
      }
      if (tile === TILES.WALL_V) {
        ctx.fillStyle = '#3a3a4a';
        ctx.fillRect(x * TILE_SIZE + TILE_SIZE - 2, y * TILE_SIZE, 2, TILE_SIZE);
      }
      if (tile === TILES.DOOR) {
        ctx.fillStyle = '#6c7086';
        ctx.fillRect(x * TILE_SIZE + 4, y * TILE_SIZE + 2, 8, TILE_SIZE - 4);
        ctx.fillStyle = '#f9e2af';
        ctx.fillRect(x * TILE_SIZE + 10, y * TILE_SIZE + 7, 2, 2);
      }
    }
  }
}
