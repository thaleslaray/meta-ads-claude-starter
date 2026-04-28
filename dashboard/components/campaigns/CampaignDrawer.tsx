"use client";

import { useEffect, useState } from "react";
import { X } from "lucide-react";
import type { Campaign } from "@/lib/types";
import { mutateStatus, mutateBudget } from "@/lib/api";
import { fmtBRL } from "@/lib/formatters";
import StatusPill from "./StatusPill";

interface CampaignDrawerProps {
  campaign: Campaign;
  onClose: () => void;
  onMutated: () => Promise<unknown>;
  onOptimisticUpdate: (patch: Partial<Campaign>) => void;
}

export default function CampaignDrawer({
  campaign,
  onClose,
  onMutated,
  onOptimisticUpdate,
}: CampaignDrawerProps) {
  const [confirmStatus, setConfirmStatus] = useState(false);
  const [confirmBudget, setConfirmBudget] = useState(false);
  const [newBudget, setNewBudget] = useState<string>(
    campaign.daily_budget?.toString() ?? ""
  );
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  const newStatus = campaign.status === "PAUSED" ? "ACTIVE" : "PAUSED";

  const doStatus = async () => {
    setBusy(true);
    setError(null);
    try {
      await mutateStatus(campaign.id, newStatus);
      // Optimistically patch the table cache so UI updates instantly
      onOptimisticUpdate({ status: newStatus });
      // Close drawer immediately; revalidation continues in background
      onClose();
      onMutated();
    } catch (e) {
      setError((e as Error).message);
      setBusy(false);
      setConfirmStatus(false);
    }
  };

  const doBudget = async () => {
    setBusy(true);
    setError(null);
    const newBudgetNum = parseFloat(newBudget);
    try {
      await mutateBudget(campaign.id, newBudgetNum);
      onOptimisticUpdate({ daily_budget: newBudgetNum });
      onClose();
      onMutated();
    } catch (e) {
      setError((e as Error).message);
      setBusy(false);
      setConfirmBudget(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex">
      <div className="flex-1 bg-black/40 backdrop-blur-sm" onClick={onClose} />
      <div className="w-[520px] bg-surface border-l border-border overflow-y-auto shadow-2xl">
        <div className="flex items-start justify-between p-6 border-b border-border">
          <div className="min-w-0 pr-4">
            <div className="text-[10px] uppercase tracking-wider text-accent font-bold mb-1">
              Campaign
            </div>
            <h2 className="font-bold text-lg text-text break-words">
              {campaign.name}
            </h2>
            <div className="font-mono text-xs text-text-3 mt-1">{campaign.id}</div>
          </div>
          <button
            onClick={onClose}
            className="p-2 hover:bg-surface-2 rounded-lg text-text-2 hover:text-text transition shrink-0"
            aria-label="Close"
          >
            <X size={18} />
          </button>
        </div>

        <div className="p-6 space-y-6">
          {error && (
            <div className="bg-red-500/10 border border-red-500/25 text-red-500 rounded-lg p-3 text-xs font-mono">
              {error}
            </div>
          )}

          <div className="grid grid-cols-2 gap-4">
            <div>
              <div className="text-[10px] uppercase tracking-wider text-text-3 font-semibold mb-2">
                Current status
              </div>
              <StatusPill status={campaign.status} />
            </div>
            <div>
              <div className="text-[10px] uppercase tracking-wider text-text-3 font-semibold mb-2">
                Daily budget
              </div>
              <div className="font-mono text-sm text-text">
                {campaign.daily_budget ? fmtBRL(campaign.daily_budget) : "—"}
              </div>
            </div>
            <div>
              <div className="text-[10px] uppercase tracking-wider text-text-3 font-semibold mb-2">
                Objective
              </div>
              <div className="font-mono text-xs text-text">{campaign.objective}</div>
            </div>
            <div>
              <div className="text-[10px] uppercase tracking-wider text-text-3 font-semibold mb-2">
                Spend
              </div>
              <div className="font-mono text-sm text-text">
                {campaign.spend ? fmtBRL(campaign.spend) : "—"}
              </div>
            </div>
          </div>

          {/* Action: Pause / Activate */}
          <section className="border border-border rounded-xl p-5">
            <h3 className="font-bold text-sm mb-1 text-text">Pause / Activate</h3>
            <p className="text-xs text-text-3 mb-4">
              Toggle campaign delivery state. Requires human approval.
            </p>
            {!confirmStatus ? (
              <button
                onClick={() => setConfirmStatus(true)}
                className="px-4 py-2 rounded-lg bg-text text-bg text-sm font-semibold hover:opacity-90 transition"
              >
                Propose change to {newStatus}
              </button>
            ) : (
              <div
                className="rounded-lg p-4 flex items-center justify-between gap-4"
                style={{
                  background: "var(--accent-wash)",
                  border: "1px solid var(--accent-border)",
                  animation: "slide-down 0.3s cubic-bezier(0.16, 1, 0.3, 1)",
                }}
              >
                <div className="text-sm text-text">
                  Confirm:{" "}
                  <strong className="text-accent font-mono">{campaign.status}</strong>
                  {" → "}
                  <strong className="text-accent font-mono">{newStatus}</strong>?
                </div>
                <div className="flex gap-2 shrink-0">
                  <button
                    onClick={() => setConfirmStatus(false)}
                    disabled={busy}
                    className="px-3 py-1.5 rounded-lg border border-border-strong text-xs font-semibold text-text-2 hover:text-text hover:bg-surface-2"
                  >
                    Cancel
                  </button>
                  <button
                    onClick={doStatus}
                    disabled={busy}
                    className="px-3 py-1.5 rounded-lg bg-accent text-white text-xs font-semibold hover:opacity-90"
                  >
                    {busy ? "Calling…" : "Approve & Execute"}
                  </button>
                </div>
              </div>
            )}
          </section>

          {/* Action: Update daily budget */}
          <section className="border border-border rounded-xl p-5">
            <h3 className="font-bold text-sm mb-1 text-text">Update daily budget</h3>
            <p className="text-xs text-text-3 mb-4">
              Change the campaign&apos;s daily spend cap. Requires human approval.
            </p>
            {!campaign.daily_budget && (
              <div className="mb-4 p-3 rounded-lg bg-[var(--accent-wash)] border border-accent-border text-xs text-text-2">
                This campaign uses <strong className="text-accent">Ad Set Budget Optimization</strong> —
                budget lives at the ad set level, not the campaign. Budget updates here are only
                supported for Campaign Budget Optimization (CBO) campaigns.
              </div>
            )}
            <div className="flex gap-2 mb-3">
              <span className="flex items-center px-3 bg-surface-2 border border-border-strong rounded-lg font-mono text-sm text-text-2">
                R$
              </span>
              <input
                type="number"
                min={1}
                step={1}
                value={newBudget}
                onChange={(e) => setNewBudget(e.target.value)}
                className="flex-1 bg-surface-2 border border-border-strong rounded-lg px-3 py-2 font-mono text-sm text-text"
                placeholder="e.g. 500"
              />
            </div>
            {!confirmBudget ? (
              <button
                onClick={() => setConfirmBudget(true)}
                disabled={!newBudget || parseFloat(newBudget) < 1}
                className="px-4 py-2 rounded-lg bg-text text-bg text-sm font-semibold hover:opacity-90 disabled:opacity-40 disabled:cursor-not-allowed transition"
              >
                Propose change
              </button>
            ) : (
              <div
                className="rounded-lg p-4 flex items-center justify-between gap-4"
                style={{
                  background: "var(--accent-wash)",
                  border: "1px solid var(--accent-border)",
                  animation: "slide-down 0.3s cubic-bezier(0.16, 1, 0.3, 1)",
                }}
              >
                <div className="text-sm text-text">
                  Confirm: daily budget →{" "}
                  <strong className="text-accent font-mono">
                    {fmtBRL(parseFloat(newBudget))}/day
                  </strong>
                </div>
                <div className="flex gap-2 shrink-0">
                  <button
                    onClick={() => setConfirmBudget(false)}
                    disabled={busy}
                    className="px-3 py-1.5 rounded-lg border border-border-strong text-xs font-semibold text-text-2 hover:text-text hover:bg-surface-2"
                  >
                    Cancel
                  </button>
                  <button
                    onClick={doBudget}
                    disabled={busy}
                    className="px-3 py-1.5 rounded-lg bg-accent text-white text-xs font-semibold hover:opacity-90"
                  >
                    {busy ? "Calling…" : "Approve & Execute"}
                  </button>
                </div>
              </div>
            )}
          </section>
        </div>
      </div>
    </div>
  );
}
