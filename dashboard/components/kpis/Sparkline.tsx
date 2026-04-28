"use client";

import { AreaChart, Area, ResponsiveContainer } from "recharts";

export default function Sparkline({ data }: { data: number[] }) {
  const chartData = data.map((y, i) => ({ i, y }));
  return (
    <ResponsiveContainer width="100%" height="100%">
      <AreaChart data={chartData}>
        <defs>
          <linearGradient id="spark-fill" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="var(--accent)" stopOpacity={0.3} />
            <stop offset="100%" stopColor="var(--accent)" stopOpacity={0} />
          </linearGradient>
        </defs>
        <Area
          type="monotone"
          dataKey="y"
          stroke="var(--accent)"
          strokeWidth={1.5}
          fill="url(#spark-fill)"
        />
      </AreaChart>
    </ResponsiveContainer>
  );
}
