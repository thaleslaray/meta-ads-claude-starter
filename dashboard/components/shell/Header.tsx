"use client";

import { useRouter, useSearchParams, usePathname } from "next/navigation";
import useSWR from "swr";
import { fetcher } from "@/lib/api";
import type { AccountsResponse } from "@/lib/types";
import OrbitMark from "./OrbitMark";
import ThemeToggle from "./ThemeToggle";

const DATE_OPTIONS = [
  { value: "today", label: "Today" },
  { value: "last_7d", label: "Last 7 days" },
  { value: "last_30d", label: "Last 30 days" },
  { value: "last_90d", label: "Last 90 days" },
  { value: "this_year", label: "This year" },
  { value: "last_year", label: "Last year" },
  { value: "maximum", label: "All time" },
];

export default function Header() {
  const router = useRouter();
  const pathname = usePathname();
  const sp = useSearchParams();

  const { data: accounts } = useSWR<AccountsResponse>("/api/accounts", fetcher);

  // Default to first account from /api/accounts (driven by META_AD_ACCOUNTS env var)
  const accountId = sp.get("account_id") ?? accounts?.accounts[0]?.id ?? "";
  const datePreset = sp.get("date_preset") ?? "last_year";

  const pushFilter = (key: string, value: string) => {
    const params = new URLSearchParams(sp);
    params.set(key, value);
    router.push(`${pathname}?${params.toString()}`);
  };

  return (
    <header className="sticky top-0 z-50 backdrop-blur-xl bg-bg/90 border-b border-border">
      <div className="max-w-[1280px] mx-auto px-8 h-16 flex items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          <OrbitMark />
          <div>
            <div className="text-sm font-extrabold tracking-tight text-text">
              Meta Ads — Operations
            </div>
            <div className="font-mono text-[11px] text-text-3">
              BM {accounts?.bm_id ?? "—"}
            </div>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <select
            value={accountId}
            onChange={(e) => pushFilter("account_id", e.target.value)}
            className="bg-surface border border-border-strong rounded-lg px-3 py-1.5 text-xs font-medium font-mono text-text max-w-[240px]"
          >
            {accounts?.accounts.map((a) => (
              <option key={a.id} value={a.id}>
                {a.label} — {a.name}
              </option>
            ))}
          </select>

          <select
            value={datePreset}
            onChange={(e) => pushFilter("date_preset", e.target.value)}
            className="bg-surface border border-border-strong rounded-lg px-3 py-1.5 text-xs font-medium text-text"
          >
            {DATE_OPTIONS.map((d) => (
              <option key={d.value} value={d.value}>
                {d.label}
              </option>
            ))}
          </select>

          <ThemeToggle />
        </div>
      </div>
    </header>
  );
}
