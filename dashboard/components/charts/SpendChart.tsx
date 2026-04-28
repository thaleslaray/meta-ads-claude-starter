"use client";

import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

interface SpendChartProps {
  data: Array<{ date: string; spend: number }>;
}

function shortDate(iso: string) {
  const d = new Date(iso);
  return d.toLocaleDateString("en-US", { month: "short", day: "numeric" });
}

export default function SpendChart({ data }: SpendChartProps) {
  return (
    <div className="h-64">
      <ResponsiveContainer width="100%" height="100%">
        <AreaChart data={data} margin={{ top: 10, right: 10, left: 0, bottom: 10 }}>
          <defs>
            <linearGradient id="chart-fill" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="var(--accent)" stopOpacity={0.25} />
              <stop offset="100%" stopColor="var(--accent)" stopOpacity={0} />
            </linearGradient>
          </defs>
          <CartesianGrid stroke="var(--border)" strokeDasharray="3 3" vertical={false} />
          <XAxis
            dataKey="date"
            stroke="var(--text-3)"
            fontSize={11}
            tickFormatter={shortDate}
            tick={{ fontFamily: "var(--font-mono-active)" }}
            minTickGap={24}
          />
          <YAxis
            stroke="var(--text-3)"
            fontSize={11}
            tick={{ fontFamily: "var(--font-mono-active)" }}
            tickFormatter={(v: number) => `R$${v}`}
            width={56}
          />
          <Tooltip
            contentStyle={{
              background: "var(--surface)",
              border: "1px solid var(--border-strong)",
              borderRadius: 8,
              fontFamily: "var(--font-mono-active)",
              fontSize: 12,
            }}
            labelFormatter={(label) => shortDate(String(label))}
            formatter={(v) => [`R$ ${Number(v).toFixed(2)}`, "Spend"]}
          />
          <Area
            type="monotone"
            dataKey="spend"
            stroke="var(--accent)"
            strokeWidth={2}
            fill="url(#chart-fill)"
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
}
