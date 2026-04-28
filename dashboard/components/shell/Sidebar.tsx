"use client";

import Link from "next/link";
import { usePathname, useSearchParams } from "next/navigation";
import { LayoutDashboard, ListChecks, History, Settings } from "lucide-react";
import type { LucideIcon } from "lucide-react";

interface Item { href: string; icon: LucideIcon; label: string; num: string }

const ITEMS: Item[] = [
  { href: "/", icon: LayoutDashboard, label: "Dashboard", num: "01" },
  { href: "/campaigns", icon: ListChecks, label: "Campaigns", num: "02" },
  { href: "/activity", icon: History, label: "Activity", num: "03" },
  { href: "/settings", icon: Settings, label: "Settings", num: "04" },
];

export default function Sidebar() {
  const pathname = usePathname();
  const sp = useSearchParams();
  const qs = sp.toString();

  return (
    <aside className="sticky top-20 self-start flex flex-col gap-1">
      <div className="text-[10px] font-bold uppercase tracking-[3px] text-text-3 mb-2 px-2.5">
        Navigation
      </div>
      {ITEMS.map((it) => {
        const active = pathname === it.href;
        const href = qs ? `${it.href}?${qs}` : it.href;
        return (
          <Link
            key={it.href}
            href={href}
            className={`flex items-center gap-2.5 p-2.5 rounded-lg transition text-sm font-semibold ${
              active ? "bg-text text-bg" : "text-text-2 hover:bg-surface-2 hover:text-text"
            }`}
          >
            <span
              className={`w-7 h-7 rounded-full font-mono text-xs font-extrabold flex items-center justify-center shrink-0 ${
                active ? "bg-accent text-white" : "bg-surface-2 text-text"
              }`}
            >
              {it.num}
            </span>
            <span>{it.label}</span>
          </Link>
        );
      })}
    </aside>
  );
}
