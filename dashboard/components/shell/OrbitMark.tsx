export default function OrbitMark({ size = 28 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 100 100" fill="none" style={{ flexShrink: 0 }}>
      <circle cx="50" cy="50" r="16" fill="var(--text)" />
      <g style={{ transformOrigin: "50% 50%", animation: "orbit 12s linear infinite" }}>
        <ellipse cx="50" cy="50" rx="40" ry="14" stroke="var(--text)" strokeOpacity="0.25" strokeWidth="1.5" />
        <circle cx="90" cy="50" r="4" fill="var(--accent)" />
      </g>
    </svg>
  );
}
