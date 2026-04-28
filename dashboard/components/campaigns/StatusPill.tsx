import { clsx } from "clsx";

export default function StatusPill({ status }: { status: string }) {
  const active = status === "ACTIVE";
  return (
    <span
      className={clsx(
        "inline-flex items-center gap-1.5 px-2 py-0.5 rounded font-mono text-[10px] font-semibold tracking-wide border",
        active
          ? "bg-accent-wash text-accent border-accent-border"
          : "bg-surface-2 text-text-2 border-border-strong"
      )}
    >
      <span
        className={clsx(
          "w-1 h-1 rounded-full",
          active ? "bg-accent" : "bg-text-3"
        )}
      />
      {status}
    </span>
  );
}
