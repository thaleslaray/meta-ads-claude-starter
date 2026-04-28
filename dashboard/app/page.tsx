"use client";

import { Suspense } from "react";
import { useSearchParams } from "next/navigation";
import Shell from "@/components/shell/Shell";
import KpiCard from "@/components/kpis/KpiCard";
import SpendChart from "@/components/charts/SpendChart";
import { useInsights } from "@/lib/api";
import { useActiveAccountId } from "@/lib/use-account";
import { fmtBRL, fmtNum, fmtPct } from "@/lib/formatters";

function DashboardContent() {
  const sp = useSearchParams();
  const accountId = useActiveAccountId(sp.get("account_id"));
  const datePreset = sp.get("date_preset") ?? "last_year";

  const { data, isLoading } = useInsights(accountId, datePreset);
  const curr = data?.current;
  const delta = data?.delta_pct ?? {};
  const series = data?.time_series ?? [];
  const empty = curr?.empty ?? true;

  return (
    <>
      <div className="mb-6">
        <div className="text-[10px] uppercase tracking-[4px] text-accent font-bold mb-2">
          Dashboard
        </div>
        <h1 className="text-3xl font-black tracking-tight text-text">
          Performance Overview
        </h1>
        <div className="h-[3px] w-10 bg-accent mt-6" />
      </div>

      <div className="grid grid-cols-6 gap-3 mb-8">
        <KpiCard
          label="Total Spend"
          loading={isLoading}
          value={empty ? "—" : fmtBRL(curr?.spend ?? 0)}
          delta={delta.spend}
        />
        <KpiCard
          label="Impressions"
          loading={isLoading}
          value={empty ? "—" : fmtNum(curr?.impressions ?? 0)}
          delta={delta.impressions}
        />
        <KpiCard
          label="Clicks"
          loading={isLoading}
          value={empty ? "—" : fmtNum(curr?.clicks ?? 0)}
          delta={delta.clicks}
        />
        <KpiCard
          label="CTR"
          loading={isLoading}
          value={empty ? "—" : fmtPct(curr?.ctr ?? 0)}
          delta={delta.ctr}
        />
        <KpiCard
          label="CPC"
          loading={isLoading}
          value={empty ? "—" : fmtBRL(curr?.cpc ?? 0)}
          delta={delta.cpc}
        />
        <KpiCard
          label="Reach"
          loading={isLoading}
          value={empty ? "—" : fmtNum(curr?.reach ?? 0)}
          delta={delta.reach}
        />
      </div>

      <section className="bg-surface border border-border rounded-xl p-6">
        <div className="flex items-baseline justify-between mb-4">
          <h2 className="text-lg font-bold text-text">Spend over time</h2>
          <span className="text-xs text-text-3 font-mono">{datePreset}</span>
        </div>
        {series.length > 0 ? (
          <SpendChart data={series} />
        ) : (
          <div className="h-64 flex items-center justify-center text-text-3 text-sm">
            {isLoading ? "Loading…" : "No time-series data for this period."}
          </div>
        )}
      </section>
    </>
  );
}

export default function DashboardPage() {
  return (
    <Shell>
      <Suspense fallback={<div className="text-text-3 text-sm">Loading…</div>}>
        <DashboardContent />
      </Suspense>
    </Shell>
  );
}
