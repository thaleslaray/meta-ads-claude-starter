"use client";

import { Moon, Sun } from "lucide-react";
import { useTheme } from "@/lib/theme";

export default function ThemeToggle() {
  const { theme, toggle } = useTheme();
  const label = theme === "dark" ? "Brand" : "Dark";
  const Icon = theme === "dark" ? Sun : Moon;
  return (
    <button
      onClick={toggle}
      className="flex items-center gap-2 px-3 py-1.5 rounded-lg border border-border-strong text-xs font-semibold text-text-2 hover:bg-surface-2 hover:text-text transition"
      aria-label={`Switch to ${label} theme`}
    >
      <Icon size={13} />
      <span>{label}</span>
    </button>
  );
}
