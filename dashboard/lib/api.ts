"use client";

import useSWR, { useSWRConfig } from "swr";
import type {
  AccountsResponse,
  Quota,
  InsightsWithDelta,
  CampaignsResponse,
  AuditEntry,
} from "./types";

export const fetcher = async (url: string) => {
  // cache: 'no-store' defeats browser HTTP cache — dashboard data is
  // mutable and SWR handles its own in-memory caching.
  const r = await fetch(url, { cache: "no-store" });
  if (!r.ok) {
    const txt = await r.text();
    throw new Error(`${r.status}: ${txt}`);
  }
  return r.json();
};

export function useAccounts() {
  return useSWR<AccountsResponse>("/api/accounts", fetcher);
}

export function useQuota(accountId: string | undefined) {
  return useSWR<Quota>(
    accountId ? `/api/quota?account_id=${accountId}` : null,
    fetcher
  );
}

export function useInsights(accountId: string | undefined, datePreset: string) {
  return useSWR<InsightsWithDelta>(
    accountId
      ? `/api/account/${accountId}/insights-with-delta?date_preset=${datePreset}`
      : null,
    fetcher
  );
}

export function useCampaigns(accountId: string | undefined, datePreset: string) {
  return useSWR<CampaignsResponse>(
    accountId
      ? `/api/account/${accountId}/campaigns?date_preset=${datePreset}`
      : null,
    fetcher
  );
}

export function useAudit() {
  return useSWR<{ entries: AuditEntry[] }>("/api/audit?limit=30", fetcher);
}

/** Refresh all SWR caches affected by a write.
 *
 * `mutate(key, asyncFn, {...})` runs the fetcher again and replaces the cache
 * with its result. This is stronger than `mutate(key)` which can dedupe or
 * silently drop. Using the full fetcher ensures the in-memory cache is
 * actually replaced with a fresh response, which triggers a re-render.
 */
export function useRefreshAfterWrite() {
  const { mutate } = useSWRConfig();
  return (accountId: string, datePreset: string) => {
    const revalidate = (key: string) =>
      mutate(key, fetcher(key), { revalidate: true, populateCache: true, rollbackOnError: false });
    return Promise.all([
      revalidate("/api/audit?limit=30"),
      revalidate(`/api/quota?account_id=${accountId}`),
      revalidate(`/api/account/${accountId}/insights-with-delta?date_preset=${datePreset}`),
      revalidate(`/api/account/${accountId}/campaigns?date_preset=${datePreset}`),
    ]);
  };
}

/** Optimistic update of the campaigns list cache — replaces a single campaign
 * in-place without waiting for revalidation. Use alongside `useRefreshAfterWrite`
 * to get instant UI feedback plus eventual consistency.
 */
export function useOptimisticCampaignUpdate() {
  const { mutate } = useSWRConfig();
  return (
    accountId: string,
    datePreset: string,
    campaignId: string,
    patch: Partial<import("./types").Campaign>
  ) => {
    const key = `/api/account/${accountId}/campaigns?date_preset=${datePreset}`;
    return mutate(
      key,
      (current: import("./types").CampaignsResponse | undefined) => {
        if (!current) return current;
        return {
          ...current,
          campaigns: current.campaigns.map((c) =>
            c.id === campaignId ? { ...c, ...patch } : c
          ),
        };
      },
      { revalidate: false }
    );
  };
}

async function parseErrorDetail(r: Response, fallback: string): Promise<string> {
  try {
    const err = await r.json();
    if (err && typeof err.detail === "string") return err.detail;
  } catch {
    /* not JSON */
  }
  return fallback;
}

export async function mutateStatus(
  campaignId: string,
  newStatus: "ACTIVE" | "PAUSED"
) {
  const r = await fetch(`/api/campaign/${campaignId}/status`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ new_status: newStatus, user_confirmed: true }),
  });
  if (!r.ok) {
    const detail = await parseErrorDetail(r, `HTTP ${r.status}`);
    throw new Error(detail);
  }
  return r.json();
}

export async function mutateBudget(
  campaignId: string,
  dailyBudgetBrl: number
) {
  const r = await fetch(`/api/campaign/${campaignId}/budget`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      daily_budget_brl: dailyBudgetBrl,
      user_confirmed: true,
    }),
  });
  if (!r.ok) {
    const detail = await parseErrorDetail(r, `HTTP ${r.status}`);
    throw new Error(detail);
  }
  return r.json();
}
