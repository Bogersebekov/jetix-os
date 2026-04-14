export default function Card({ children, className = '', pixel = false, title }) {
  return (
    <div
      className={`
        bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip
        ${pixel ? 'font-pixel' : ''}
        ${className}
      `}
    >
      {title && (
        <div className="px-4 py-2 border-b-2 border-ctp-surface1 bg-ctp-surface0/30">
          <h3 className={`text-sm text-ctp-subtext1 ${pixel ? 'font-pixel text-[10px]' : 'font-semibold'}`}>
            {title}
          </h3>
        </div>
      )}
      <div className="p-4">{children}</div>
    </div>
  );
}
