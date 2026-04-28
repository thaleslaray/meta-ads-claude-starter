import { clsx } from "clsx";

interface KpiCardProps {
  label: string;
  value: string;
  delta?: number;
  loading?: boolean;
}

export default function KpiCard({ label, value, delta, loading }: KpiCardProps) {
  return (
    <div className="relative bg-surface border border-border rounded-xl p-4 overflow-hidden">
      <div className="absolute top-0 inset-x-0 h-px bg-gradient-to-r from-transparent via-border-strong to-transparent" />
      <div className="text-[10px] uppercase tracking-wider text-text-3 font-semibold mb-2">
        {label}
      </div>
      <div className="flex items-end justify-between gap-3 min-h-[48px]">
        <div className="min-w-0 w-full">
          {loading ? (
            <div className="h-6 w-20 bg-surface-2 rounded animate-pulse" />
          ) : (
            <div className="font-mono text-xl font-semibold tabular-nums truncate">
              {value}
            </div>
          )}
          {!loading && delta !== undefined && (
            <div
              className={clsx(
                "text-xs font-mono tabular-nums mt-1",
                delta >= 0 ? "text-accent" : "text-text-3"
              )}
            >
              {delta >= 0 ? "↑" : "↓"} {Math.abs(delta).toFixed(1)}% vs prev
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
