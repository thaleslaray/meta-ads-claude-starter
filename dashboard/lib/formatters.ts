export const fmtBRL = (n: number) =>
  n.toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL",
    maximumFractionDigits: 2,
  });

export const fmtBRLCompact = (n: number) => {
  if (n >= 1_000_000) return `R$ ${(n / 1_000_000).toFixed(1)}M`;
  if (n >= 1_000) return `R$ ${(n / 1_000).toFixed(1)}k`;
  return fmtBRL(n);
};

export const fmtNum = (n: number) => n.toLocaleString("pt-BR");

export const fmtNumCompact = (n: number) => {
  if (n >= 1_000_000) return `${(n / 1_000_000).toFixed(1)}M`;
  if (n >= 1_000) return `${(n / 1_000).toFixed(1)}k`;
  return fmtNum(n);
};

export const fmtPct = (n: number, decimals = 2) => `${n.toFixed(decimals)}%`;
