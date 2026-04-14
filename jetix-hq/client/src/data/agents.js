// Department colors for avatars and accents
export const deptColors = {
  MGMT: { bg: 'bg-ctp-mauve', text: 'text-ctp-mauve', hex: '#cba6f7' },
  SALES: { bg: 'bg-ctp-green', text: 'text-ctp-green', hex: '#a6e3a1' },
  BRAIN: { bg: 'bg-ctp-teal', text: 'text-ctp-teal', hex: '#94e2d5' },
  OPS: { bg: 'bg-ctp-blue', text: 'text-ctp-blue', hex: '#89b4fa' },
  LIFE: { bg: 'bg-ctp-peach', text: 'text-ctp-peach', hex: '#fab387' },
  META: { bg: 'bg-ctp-pink', text: 'text-ctp-pink', hex: '#f5c2e7' },
};

export const departments = ['ALL', 'MGMT', 'SALES', 'BRAIN', 'OPS', 'LIFE', 'META'];

// Generates initials from agent name
export function getInitials(name) {
  return name
    .split(/[\s-]+/)
    .map((w) => w[0])
    .join('')
    .toUpperCase()
    .slice(0, 2);
}
