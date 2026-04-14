const variants = {
  primary: `
    bg-ctp-mauve text-ctp-crust
    shadow-[inset_0_-2px_0_0_rgba(0,0,0,0.3),inset_0_1px_0_0_rgba(255,255,255,0.2)]
    hover:brightness-110 active:shadow-[inset_0_2px_0_0_rgba(0,0,0,0.3)]
    active:translate-y-[1px]
  `,
  secondary: `
    bg-ctp-surface1 text-ctp-text
    shadow-[inset_0_-2px_0_0_rgba(0,0,0,0.3),inset_0_1px_0_0_rgba(255,255,255,0.05)]
    hover:bg-ctp-surface2 active:shadow-[inset_0_2px_0_0_rgba(0,0,0,0.3)]
    active:translate-y-[1px]
  `,
  danger: `
    bg-ctp-red text-ctp-crust
    shadow-[inset_0_-2px_0_0_rgba(0,0,0,0.3),inset_0_1px_0_0_rgba(255,255,255,0.2)]
    hover:brightness-110 active:shadow-[inset_0_2px_0_0_rgba(0,0,0,0.3)]
    active:translate-y-[1px]
  `,
  success: `
    bg-ctp-green text-ctp-crust
    shadow-[inset_0_-2px_0_0_rgba(0,0,0,0.3),inset_0_1px_0_0_rgba(255,255,255,0.2)]
    hover:brightness-110 active:shadow-[inset_0_2px_0_0_rgba(0,0,0,0.3)]
    active:translate-y-[1px]
  `,
};

const sizes = {
  sm: 'px-3 py-1 text-xs',
  md: 'px-4 py-2 text-sm',
  lg: 'px-6 py-3 text-base',
};

export default function Button({
  children,
  variant = 'primary',
  size = 'md',
  pixel = false,
  className = '',
  ...props
}) {
  return (
    <button
      className={`
        inline-flex items-center justify-center gap-2
        border-2 border-transparent rpg-clip
        transition-all duration-100 cursor-pointer
        disabled:opacity-50 disabled:cursor-not-allowed
        ${pixel ? 'font-pixel text-[10px]' : 'font-semibold'}
        ${variants[variant]}
        ${sizes[size]}
        ${className}
      `}
      {...props}
    >
      {children}
    </button>
  );
}
