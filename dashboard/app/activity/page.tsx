"use client";

import { useState, Suspense } from "react";
import { useAudit } from "@/lib/api";
import { useSWRConfig } from "swr";
import { RefreshCw } from "lucide-react";
import Shell from "@/components/shell/Shell";
import type { AuditEntry } from "@/lib/types";

type Filter = "all" | "write" | "read";

function ActivityContent() {
  const { data, isLoading } = useAudit();
  const { mutate } = useSWRConfig();
  const [filter, setFilter] = useState<Filter>("all");

  const entries: AuditEntry[] = data?.entries ?? [];
  const filtered =
    filter === "all"
      ? entries
      : entries.filter((e) => (e.kind ?? "write") === filter);

  return (
    <>
      <div className="mb-6 flex items-start justify-between gap-4">
        <div>
          <div className="text-[10px] uppercase tracking-[4px] text-accent font-bold mb-2">
            Activity
          </div>
          <h1 className="text-3xl font-black tracking-tight text-text">
            Audit Trail
          </h1>
          <div className="h-[3px] w-10 bg-accent mt-6" />
        </div>
        <button
          onClick={() => mutate("/api/audit?limit=30")}
          className="flex items-center gap-2 px-3 py-1.5 rounded-lg border border-border-strong text-xs font-semibold text-text-2 hover:text-text hover:bg-surface-2 transition"
        >
          <RefreshCw size={12} />
          Refresh
        </button>
      </div>

      <div className="flex gap-2 mb-4">
        {(["all", "write", "read"] as const).map((f) => (
          <button
            key={f}
            onClick={() => setFilter(f)}
            className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition border ${
              filter === f
                ? "bg-text text-bg border-text"
                : "border-border-strong text-text-2 hover:bg-surface-2 hover:text-text"
            }`}
          >
            {f === "all" ? "All" : f === "write" ? "Writes only" : "Reads only"}
          </button>
        ))}
      </div>

      <div className="bg-surface border border-border rounded-xl overflow-hidden">
        {isLoading && (
          <div className="p-8 text-center text-text-3 text-sm">Loading…</div>
        )}
        {!isLoading && filtered.length === 0 && (
          <div className="p-8 text-center text-text-3 text-sm">
            No matching entries.
          </div>
        )}
        {filtered.map((e, i) => (
          <AuditRow key={i} entry={e} />
        ))}
      </div>
    </>
  );
}

function AuditRow({ entry: e }: { entry: AuditEntry }) {
  const isWrite = e.kind === "write";
  const ts = e.timestamp?.slice(11, 19) ?? "—";

  return (
    <div className="grid grid-cols-[14px_1fr_auto] gap-4 px-6 py-3 border-b border-border last:border-b-0 items-center">
      <div
        className="w-2 h-2 rounded-full"
        style={{
          background: isWrite ? "var(--accent)" : "var(--text-3)",
          boxShadow: isWrite ? "0 0 6px var(--accent)" : "none",
        }}
      />
      <div className="min-w-0">
        <div className="flex items-center gap-2 flex-wrap text-sm text-text">
          <span
            className={`font-mono text-[10px] font-bold px-1.5 py-0.5 rounded border ${
              isWrite
                ? "text-accent bg-accent-wash border-accent-border"
                : "text-text-2 bg-surface-2 border-border-strong"
            }`}
          >
            {isWrite ? "WRITE" : "READ"}
          </span>
          <span className="font-mono text-sm">{e.operation}</span>
          {isWrite &&
            e.before_state &&
            e.after_state &&
            Object.keys(e.after_state).map((f) => (
              <span key={f} className="text-xs text-text-3 font-mono">
                · {f}:{" "}
                <code className="bg-surface-2 px-1 py-0.5 rounded border border-border">
                  {String(e.before_state![f] ?? "—")}
                </code>
                {" → "}
                <code
                  className="px-1 py-0.5 rounded border"
                  style={{
                    color: "var(--accent)",
                    background: "var(--accent-wash)",
                    borderColor: "var(--accent-border)",
                  }}
                >
                  {String(e.after_state![f] ?? "—")}
                </code>
              </span>
            ))}
        </div>
        <div className="font-mono text-[10px] text-text-3 mt-1 flex gap-3 flex-wrap">
          <span>endpoint: {e.endpoint}</span>
          <span>·</span>
          <span>HTTP {e.response_code}</span>
          {isWrite && (
            <>
              <span>·</span>
              <span className={e.user_confirmed ? "text-accent" : "text-red-500"}>
                {e.user_confirmed ? "human approved ✓" : "NOT approved ✗"}
              </span>
            </>
          )}
        </div>
      </div>
      <div className="font-mono text-[10px] text-text-3">{ts}</div>
    </div>
  );
}

export default function ActivityPage() {
  return (
    <Shell>
      <Suspense fallback={<div className="text-text-3 text-sm">Loading…</div>}>
        <ActivityContent />
      </Suspense>
    </Shell>
  );
}
