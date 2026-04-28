"use client";

import { Suspense } from "react";
import { useSearchParams } from "next/navigation";
import Shell from "@/components/shell/Shell";
import { useQuota, useAccounts } from "@/lib/api";
import { useActiveAccountId } from "@/lib/use-account";

function ConfigCard({
  label,
  value,
  highlight,
}: {
  label: string;
  value: string;
  highlight?: "good" | "warn" | "bad";
}) {
  const tone =
    highlight === "good"
      ? "text-accent"
      : highlight === "bad"
      ? "text-red-500"
      : "text-text";
  return (
    <div className="bg-surface border border-border rounded-xl p-4">
      <div className="text-[10px] uppercase tracking-wider text-text-3 font-semibold mb-2">
        {label}
      </div>
      <div className={`font-mono text-sm ${tone}`}>{value}</div>
    </div>
  );
}

function SettingsContent() {
  const sp = useSearchParams();
  const accountId = useActiveAccountId(sp.get("account_id"));
  const { data: quota } = useQuota(accountId);
  const { data: accounts } = useAccounts();

  return (
    <>
      <div className="mb-6">
        <div className="text-[10px] uppercase tracking-[4px] text-accent font-bold mb-2">
          Settings
        </div>
        <h1 className="text-3xl font-black tracking-tight text-text">
          App Configuration
        </h1>
        <div className="h-[3px] w-10 bg-accent mt-6" />
      </div>

      <section className="mb-8">
        <h2 className="text-xs font-bold mb-3 uppercase tracking-wider text-text-3">
          Meta App
        </h2>
        <div className="grid grid-cols-2 gap-3">
          <ConfigCard label="Business Manager" value={accounts?.bm_id ?? "—"} />
          <ConfigCard label="Organization" value={accounts?.org_name ?? "—"} />
          <ConfigCard
            label="Auth method"
            value="System User token + appsecret_proof"
          />
        </div>
      </section>

      <section className="mb-8">
        <h2 className="text-xs font-bold mb-3 uppercase tracking-wider text-text-3">
          API Access
        </h2>
        <div className="grid grid-cols-2 gap-3">
          <ConfigCard
            label="Access Tier"
            value={quota?.tier ?? "—"}
            highlight={quota?.tier === "standard_access" ? "good" : undefined}
          />
          <ConfigCard
            label="Max points / hour"
            value={quota?.max_points?.toLocaleString("pt-BR") ?? "—"}
          />
          <ConfigCard
            label="Used this window"
            value={`${quota?.used_pct?.toFixed(1) ?? "—"}%`}
          />
          <ConfigCard
            label="Circuit breaker"
            value={quota?.circuit_breaker ? "OPEN" : "CLOSED"}
            highlight={quota?.circuit_breaker ? "bad" : "good"}
          />
        </div>
      </section>

      <section>
        <h2 className="text-xs font-bold mb-3 uppercase tracking-wider text-text-3">
          Ad Accounts
        </h2>
        <div className="grid grid-cols-1 gap-3">
          {accounts?.accounts.map((a) => (
            <ConfigCard key={a.id} label={a.label} value={`${a.name} · ${a.id}`} />
          ))}
        </div>
      </section>
    </>
  );
}

export default function SettingsPage() {
  return (
    <Shell>
      <Suspense fallback={<div className="text-text-3 text-sm">Loading…</div>}>
        <SettingsContent />
      </Suspense>
    </Shell>
  );
}
