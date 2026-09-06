
import React from "react";
import type { HiveContext, SeasonTheme, StatusEntry } from "../../types.js";
import { useHiveActivity } from "./useHiveActivity.js";
import "./HiveActivity.css";

export interface HiveActivityProps {
  context: HiveContext;
  statuses?: StatusEntry[];
  seasons?: SeasonTheme[];
  seed?: string | number;
  className?: string;
  label?: string;
  showGlyph?: boolean;
  onExposure?: Parameters<typeof useHiveActivity>[0]["onExposure"];
}

export function HiveActivity({
  context,
  statuses,
  seasons,
  seed,
  className = "",
  label = "The hive is working",
  showGlyph = true,
  onExposure,
}: HiveActivityProps) {
  const snapshot = useHiveActivity({ context, statuses, seasons, seed, onExposure });

  return (
    <div
      className={`hive-activity ${snapshot.seasonId ? `hive-season-${snapshot.seasonId}` : ""} ${className}`}
      data-phase={context.phase}
      data-motion-cue={snapshot.motionCue}
      aria-live="polite"
      aria-label={`${label}: ${snapshot.text}`}
    >
      {showGlyph && <span className="hive-glyph" aria-hidden="true">✦</span>}
      <span className="hive-shimmer-text">{snapshot.text}</span>
    </div>
  );
}
