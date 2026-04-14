/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        ctp: {
          base: '#1e1e2e',
          mantle: '#181825',
          crust: '#11111b',
          surface0: '#313244',
          surface1: '#45475a',
          surface2: '#585b70',
          text: '#cdd6f4',
          subtext0: '#a6adc8',
          subtext1: '#bac2de',
          blue: '#89b4fa',
          green: '#a6e3a1',
          red: '#f38ba8',
          mauve: '#cba6f7',
          peach: '#fab387',
          yellow: '#f9e2af',
          teal: '#94e2d5',
          pink: '#f5c2e7',
          lavender: '#b4befe',
          rosewater: '#f5e0dc',
          flamingo: '#f2cdcd',
          maroon: '#eba0ac',
          sky: '#89dcfe',
          sapphire: '#74c7ec',
          overlay0: '#6c7086',
          overlay1: '#7f849c',
          overlay2: '#9399b2',
        },
      },
      fontFamily: {
        pixel: ['"Press Start 2P"', 'monospace'],
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', '"Fira Code"', 'monospace'],
      },
      animation: {
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
    },
  },
  plugins: [],
};
