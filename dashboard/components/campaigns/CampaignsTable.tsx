"use client";

import { useState } from "react";
import {
  useCampaigns,
  useRefreshAfterWrite,
  useOptimisticCampaignUpdate,
} from "@/lib/api";
import type { Campaign } from "@/lib/types";
import StatusPill from "./StatusPill";
import CampaignDrawer from "./CampaignDrawer";
import { fmtBRL, fmtNum, fmtPct } from "@/lib/formatters";

interface CampaignsTableProps {
  accountId: string;
  datePreset: string;
}

export default function CampaignsTable({ accountId, datePreset }: CampaignsTableProps) {
  const { data, isLoading } = useCampaigns(accountId, datePreset);
  const [selected, setSelected] = useState<string | null>(null);
  const refresh = useRefreshAfterWrite();
  const optimistic = useOptimisticCampaignUpdate();

  if (isLoading) {
    return <div className="p-8 text-center text-text-3 text-sm">Loading campaigns…</div>;
  }

  const campaigns: Campaign[] = data?.campaigns ?? [];

  if (!campaigns.length) {
    return (
      <div className="p-12 text-center bg-surface border border-border rounded-xl">
        <div className="text-text-3 text-sm">No campaigns in this account.</div>
      </div>
    );
  }

  const headers = [
    "Campaign",
    "Status",
    "Objective",
    "Daily budget",
    "Spend",
    "Impressions",
    "Clicks",
    "CTR",
  ];

  return (
    <>
      <div className="bg-surface border border-border rounded-xl overflow-hidden">
        <table className="w-full">
          <thead>
            <tr>
              {headers.map((h, i) => (
                <th
                  key={h}
                  className={`text-[10px] uppercase tracking-wider text-text-3 font-semibold bg-surface-2 px-4 py-3 ${
                    i > 2 ? "text-right" : "text-left"
                  }`}
                >
                  {h}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {campaigns.map((c) => (
              <tr
                key={c.id}
                onClick={() => setSelected(c.id)}
                className="cursor-pointer border-b border-border last:border-b-0 hover:bg-surface-2 transition"
              >
                <td
                  className="px-4 py-3 font-medium text-text max-w-[280px] truncate"
                  title={c.name}
                >
                  {c.name}
                </td>
                <td className="px-4 py-3">
                  <StatusPill status={c.status} />
                </td>
                <td className="px-4 py-3 font-mono text-xs text-text-2">
                  {c.objective}
                </td>
                <td className="px-4 py-3 font-mono text-xs text-right tabular-nums text-text">
                  {c.daily_budget ? fmtBRL(c.daily_budget) : "—"}
                </td>
                <td className="px-4 py-3 font-mono text-xs text-right tabular-nums text-text">
                  {c.spend ? fmtBRL(c.spend) : "—"}
                </td>
                <td className="px-4 py-3 font-mono text-xs text-right tabular-nums text-text-2">
                  {c.impressions ? fmtNum(c.impressions) : "—"}
                </td>
                <td className="px-4 py-3 font-mono text-xs text-right tabular-nums text-text-2">
                  {c.clicks ? fmtNum(c.clicks) : "—"}
                </td>
                <td className="px-4 py-3 font-mono text-xs text-right tabular-nums text-text">
                  {c.ctr ? fmtPct(c.ctr) : "—"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {selected && (
        <CampaignDrawer
          campaign={campaigns.find((c) => c.id === selected)!}
          onClose={() => setSelected(null)}
          onOptimisticUpdate={(patch) =>
            optimistic(accountId, datePreset, selected, patch)
          }
          onMutated={async () => {
            await refresh(accountId, datePreset);
          }}
        />
      )}
    </>
  );
}
