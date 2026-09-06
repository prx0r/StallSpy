
import { useEffect, useMemo, useRef, useState } from "react";
import { HiveActivityEngine } from "../../engine.js";
import { DEFAULT_SEASONS, DEFAULT_STATUSES } from "../../defaults.js";
import type { HiveActivitySnapshot, HiveContext, SelectionMeta, StatusEntry, SeasonTheme } from "../../types.js";

export interface UseHiveActivityOptions {
  context: HiveContext;
  statuses?: StatusEntry[];
  seasons?: SeasonTheme[];
  seed?: string | number;
  active?: boolean;
  onExposure?: (meta: SelectionMeta) => void;
}

export function useHiveActivity(options: UseHiveActivityOptions): HiveActivitySnapshot {
  const { context, active = true } = options;
  const onExposureRef = useRef(options.onExposure);
  onExposureRef.current = options.onExposure;

  const engine = useMemo(
    () => new HiveActivityEngine({
      statuses: options.statuses ?? DEFAULT_STATUSES,
      seasons: options.seasons ?? DEFAULT_SEASONS,
      seed: options.seed,
      onExposure: meta => onExposureRef.current?.(meta),
    }),
    [options.statuses, options.seasons, options.seed],
  );

  const [snapshot, setSnapshot] = useState(() => engine.select(context));

  useEffect(() => {
    if (!active) return;
    let cancelled = false;
    let timer: ReturnType<typeof setTimeout>;

    const tick = () => {
      const next = engine.select(context);
      if (!cancelled) setSnapshot(next);
      const delay = context.reducedMotion ? Math.max(3200, engine.nextDelay()) : engine.nextDelay();
      timer = setTimeout(tick, delay);
    };

    tick();
    return () => {
      cancelled = true;
      clearTimeout(timer);
    };
  }, [active, engine, context.phase, context.bee?.id, context.season, JSON.stringify(context.hooks), JSON.stringify(context.missionTags), context.explicitStatus, context.reducedMotion]);

  return snapshot;
}
