
export type HivePhase =
  | "listen"
  | "understand"
  | "ideate"
  | "council"
  | "generate-image"
  | "generate-video"
  | "generate-world"
  | "package"
  | "quote"
  | "checkout"
  | "fulfil"
  | "recover"
  | "generic";

export type Rarity = "common" | "uncommon" | "rare";
export type MotionCue =
  | "hover"
  | "fly-out"
  | "fly-in"
  | "peek"
  | "scribble"
  | "argue"
  | "pack"
  | "inspect"
  | "celebrate"
  | "shiver"
  | "idle";

export interface StatusEntry {
  id: string;
  text: string;
  phases: HivePhase[];
  weight?: number;
  rarity?: Rarity;
  beeArchetypes?: string[];
  seasons?: string[];
  tags?: string[];
  minDurationMs?: number;
  maxDurationMs?: number;
  cooldownMs?: number;
  motionCue?: MotionCue;
  contextualSlots?: string[];
  suppressIfTags?: string[];
}

export interface SeasonTheme {
  id: string;
  name: string;
  aliases?: string[];
  active?: {
    monthDayRanges?: Array<{ start: string; end: string }>;
    explicitOnly?: boolean;
  };
  visual: {
    label: string;
    accentClass: string;
    ambientClass?: string;
    icon?: string;
  };
  phrasePrefixes?: string[];
  phraseSuffixes?: string[];
  additions: StatusEntry[];
  transformations?: Array<{
    matchTag?: string;
    from?: string;
    to: string;
    probability?: number;
  }>;
}

export interface BeeProfile {
  id: string;
  name: string;
  archetype: string;
  toneTags: string[];
  phraseBiasTags?: string[];
  phraseAvoidTags?: string[];
  verbosity?: "terse" | "balanced" | "verbose";
}

export interface HiveContext {
  phase: HivePhase;
  bee?: BeeProfile;
  season?: string | SeasonTheme | null;
  missionTags?: string[];
  hooks?: Record<string, string>;
  explicitStatus?: string;
  reducedMotion?: boolean;
  now?: Date;
}

export interface SelectionMeta {
  entryId: string;
  source: "explicit" | "contextual" | "bank";
  phase: HivePhase;
  seasonId?: string;
  beeId?: string;
  renderedText: string;
  weight: number;
  probabilityApprox: number;
  at: number;
}

export interface EngineOptions {
  statuses: StatusEntry[];
  seasons?: SeasonTheme[];
  minSwapMs?: number;
  maxSwapMs?: number;
  recentWindow?: number;
  seed?: string | number;
  random?: () => number;
  onExposure?: (meta: SelectionMeta) => void;
}

export interface HiveActivitySnapshot {
  text: string;
  motionCue: MotionCue;
  seasonId?: string;
  beeId?: string;
  meta?: SelectionMeta;
}
