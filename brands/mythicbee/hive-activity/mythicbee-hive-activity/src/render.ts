
import type { SeasonTheme, StatusEntry } from "./types.js";

const SLOT_RE = /\{([a-zA-Z0-9_.-]+)\}/g;

export function fillSlots(text: string, hooks: Record<string, string> = {}): string | null {
  let missing = false;
  const rendered = text.replace(SLOT_RE, (_, key: string) => {
    const value = hooks[key];
    if (!value) {
      missing = true;
      return "";
    }
    return value;
  });
  return missing ? null : rendered.replace(/\s+/g, " ").trim();
}

export function applySeasonalTransform(
  text: string,
  entry: StatusEntry,
  season: SeasonTheme | null,
  random: () => number,
): string {
  if (!season) return text;
  let result = text;

  for (const transform of season.transformations ?? []) {
    if (transform.matchTag && !entry.tags?.includes(transform.matchTag)) continue;
    if ((transform.probability ?? 1) < random()) continue;

    if (transform.from) result = result.replace(transform.from, transform.to);
    else result = transform.to.replace("{base}", result.replace(/…$/, ""));
  }

  const prefix = season.phrasePrefixes?.length && random() < 0.08
    ? season.phrasePrefixes[Math.floor(random() * season.phrasePrefixes.length)] + " "
    : "";
  const suffix = season.phraseSuffixes?.length && random() < 0.05
    ? " " + season.phraseSuffixes[Math.floor(random() * season.phraseSuffixes.length)]
    : "";

  return `${prefix}${result}${suffix}`.replace(/\s+/g, " ").trim();
}
