export interface Account {
  id: string;
  name: string;
  label: string;
}

export interface AccountsResponse {
  accounts: Account[];
  bm_id: string;
  org_name: string;
}

export interface Quota {
  tier: "development_access" | "standard_access";
  used_pct: number;
  max_points: number;
  remaining_points: number;
  circuit_breaker: boolean;
  points_used: number;
}

export interface InsightsCurrent {
  empty: boolean;
  date_preset: string;
  spend?: number;
  impressions?: number;
  clicks?: number;
  ctr?: number;
  cpc?: number;
  reach?: number;
  frequency?: number;
  error?: string;
}

type DeltaField = "spend" | "impressions" | "clicks" | "ctr" | "cpc" | "reach";

export interface InsightsWithDelta {
  current: InsightsCurrent;
  previous: InsightsCurrent;
  delta_pct: Partial<Record<DeltaField, number>>;
  time_series: Array<{ date: string; spend: number }>;
}

export interface Campaign {
  id: string;
  name: string;
  status: "ACTIVE" | "PAUSED" | "DELETED" | "ARCHIVED";
  effective_status?: string;
  objective: string;
  daily_budget: number | null;
  lifetime_budget: number | null;
  spend: number;
  impressions: number;
  clicks: number;
  ctr: number;
  cpc: number;
}

export interface CampaignsResponse {
  campaigns: Campaign[];
}

export interface AuditEntry {
  timestamp: string;
  epoch: number;
  operation: string;
  endpoint: string;
  resource_id: string;
  kind?: "read" | "write";
  response_code: number;
  user_confirmed?: boolean;
  before_state?: Record<string, unknown>;
  after_state?: Record<string, unknown>;
}
