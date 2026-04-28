"use client";

import { useAccounts } from "./api";

/**
 * Resolves the active account ID from URL or falls back to the first
 * account returned by /api/accounts. This avoids hardcoding any specific
 * ad account ID in the frontend — the backend defines the list via the
 * META_AD_ACCOUNTS env var, and the UI just picks the first as default.
 *
 * Returns undefined while loading; pages should handle that case.
 */
export function useActiveAccountId(urlAccountId: string | null): string | undefined {
  const { data } = useAccounts();
  if (urlAccountId) return urlAccountId;
  return data?.accounts[0]?.id;
}
