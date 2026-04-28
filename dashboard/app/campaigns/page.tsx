"use client";

import { Suspense } from "react";
import { useSearchParams } from "next/navigation";
import Shell from "@/components/shell/Shell";
import CampaignsTable from "@/components/campaigns/CampaignsTable";
import { useActiveAccountId } from "@/lib/use-account";

function CampaignsContent() {
  const sp = useSearchParams();
  const accountId = useActiveAccountId(sp.get("account_id"));
  const datePreset = sp.get("date_preset") ?? "last_year";

  return (
    <>
      <div className="mb-6">
        <div className="text-[10px] uppercase tracking-[4px] text-accent font-bold mb-2">
          Campaigns
        </div>
        <h1 className="text-3xl font-black tracking-tight text-text">All Campaigns</h1>
        <div className="h-[3px] w-10 bg-accent mt-6" />
      </div>

      <CampaignsTable accountId={accountId} datePreset={datePreset} />
    </>
  );
}

export default function CampaignsPage() {
  return (
    <Shell>
      <Suspense fallback={<div className="text-text-3 text-sm">Loading…</div>}>
        <CampaignsContent />
      </Suspense>
    </Shell>
  );
}
