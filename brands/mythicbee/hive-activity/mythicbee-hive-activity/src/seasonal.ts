
import type { SeasonTheme } from "./types.js";

function md(date: Date): string {
  return `${String(date.getMonth() + 1).padStart(2, "0")}-${String(date.getDate()).padStart(2, "0")}`;
}

function withinRange(value: string, start: string, end: string): boolean {
  if (start <= end) return value >= start && value <= end;
  return value >= start || value <= end;
}

export function inferSeason(themes: SeasonTheme[], now = new Date()): SeasonTheme | null {
  const value = md(now);
  for (const theme of themes) {
    if (theme.active?.explicitOnly) continue;
    for (const range of theme.active?.monthDayRanges ?? []) {
      if (withinRange(value, range.start, range.end)) return theme;
    }
  }
  return null;
}

export function resolveSeason(
  themes: SeasonTheme[],
  season: string | SeasonTheme | null | undefined,
  now = new Date(),
): SeasonTheme | null {
  if (typeof season === "object" && season) return season;
  if (typeof season === "string") {
    const key = season.toLowerCase();
    return themes.find(
      s => s.id.toLowerCase() === key || s.aliases?.some(a => a.toLowerCase() === key),
    ) ?? null;
  }
  return inferSeason(themes, now);
}
