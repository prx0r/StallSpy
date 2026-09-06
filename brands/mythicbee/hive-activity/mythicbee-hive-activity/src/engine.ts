
import type {
  EngineOptions,
  HiveActivitySnapshot,
  HiveContext,
  SelectionMeta,
  StatusEntry,
} from "./types.js";
import { hashSeed, mulberry32 } from "./random.js";
import { resolveSeason } from "./seasonal.js";
import { applySeasonalTransform, fillSlots } from "./render.js";

function weightedPick<T>(
  items: Array<{ value: T; weight: number }>,
  random: () => number,
): { value: T; weight: number; total: number } | null {
  const total = items.reduce((sum, x) => sum + Math.max(0, x.weight), 0);
  if (!total) return null;
  let r = random() * total;
  for (const item of items) {
    r -= Math.max(0, item.weight);
    if (r <= 0) return { ...item, total };
  }
  return { ...items[items.length - 1], total };
}

export class HiveActivityEngine {
  private readonly options: Required<Pick<EngineOptions, "minSwapMs" | "maxSwapMs" | "recentWindow">> & EngineOptions;
  private readonly random: () => number;
  private recent: string[] = [];
  private lastShownAt = new Map<string, number>();

  constructor(options: EngineOptions) {
    this.options = {
      minSwapMs: 2100,
      maxSwapMs: 4800,
      recentWindow: 8,
      ...options,
    };
    this.random = options.random ?? mulberry32(hashSeed(options.seed ?? Date.now()));
  }

  nextDelay(entry?: StatusEntry): number {
    const min = entry?.minDurationMs ?? this.options.minSwapMs;
    const max = entry?.maxDurationMs ?? this.options.maxSwapMs;
    return Math.round(min + this.random() * Math.max(0, max - min));
  }

  select(context: HiveContext): HiveActivitySnapshot {
    const now = context.now ?? new Date();
    const timestamp = now.getTime();
    const season = resolveSeason(this.options.seasons ?? [], context.season, now);

    if (context.explicitStatus) {
      const meta: SelectionMeta = {
        entryId: "explicit",
        source: "explicit",
        phase: context.phase,
        seasonId: season?.id,
        beeId: context.bee?.id,
        renderedText: context.explicitStatus,
        weight: 1,
        probabilityApprox: 1,
        at: timestamp,
      };
      this.options.onExposure?.(meta);
      return {
        text: context.explicitStatus,
        motionCue: "idle",
        seasonId: season?.id,
        beeId: context.bee?.id,
        meta,
      };
    }

    const pool = [...this.options.statuses, ...(season?.additions ?? [])];
    const missionTags = new Set(context.missionTags ?? []);
    const bee = context.bee;

    const candidates: Array<{ value: { entry: StatusEntry; text: string; source: "contextual" | "bank" }; weight: number }> = [];

    for (const entry of pool) {
      if (!entry.phases.includes(context.phase) && !entry.phases.includes("generic")) continue;
      if (entry.seasons?.length && (!season || !entry.seasons.includes(season.id))) continue;
      if (entry.suppressIfTags?.some(t => missionTags.has(t))) continue;
      if (entry.beeArchetypes?.length && (!bee || !entry.beeArchetypes.includes(bee.archetype))) continue;

      const last = this.lastShownAt.get(entry.id) ?? 0;
      if (timestamp - last < (entry.cooldownMs ?? 0)) continue;

      let rendered = fillSlots(entry.text, context.hooks ?? {});
      if (!rendered) continue;

      let weight = entry.weight ?? 1;
      const tags = new Set(entry.tags ?? []);

      for (const tag of bee?.phraseBiasTags ?? []) if (tags.has(tag)) weight *= 1.8;
      for (const tag of bee?.phraseAvoidTags ?? []) if (tags.has(tag)) weight *= 0.25;
      for (const tag of missionTags) if (tags.has(tag)) weight *= 1.35;

      if (this.recent.includes(entry.id)) weight *= 0.05;

      const rarity = entry.rarity ?? "common";
      if (rarity === "uncommon") weight *= 0.55;
      if (rarity === "rare") weight *= 0.14;

      const source = entry.contextualSlots?.length ? "contextual" : "bank";
      if (source === "contextual") weight *= 1.45;

      rendered = applySeasonalTransform(rendered, entry, season, this.random);
      candidates.push({ value: { entry, text: rendered, source }, weight });
    }

    const picked = weightedPick(candidates, this.random);
    if (!picked) {
      return {
        text: "Consulting the hive…",
        motionCue: "hover",
        seasonId: season?.id,
        beeId: bee?.id,
      };
    }

    const { entry, text, source } = picked.value;
    this.recent.push(entry.id);
    if (this.recent.length > this.options.recentWindow) this.recent.shift();
    this.lastShownAt.set(entry.id, timestamp);

    const meta: SelectionMeta = {
      entryId: entry.id,
      source,
      phase: context.phase,
      seasonId: season?.id,
      beeId: bee?.id,
      renderedText: text,
      weight: picked.weight,
      probabilityApprox: picked.weight / picked.total,
      at: timestamp,
    };
    this.options.onExposure?.(meta);

    return {
      text,
      motionCue: entry.motionCue ?? "hover",
      seasonId: season?.id,
      beeId: bee?.id,
      meta,
    };
  }
}
