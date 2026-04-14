export default function Skeleton({ width, height = 16, rounded = false, className = '' }) {
  return (
    <div
      className={`bg-ctp-surface0 animate-pulse ${rounded ? 'rounded-full' : ''} ${className}`}
      style={{
        width: width || '100%',
        height,
      }}
    />
  );
}
