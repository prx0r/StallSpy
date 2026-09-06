
import statuses from "./data/base.statuses.json";
import bees from "./data/bee-profiles.json";
import seasons from "./data/seasons/index.json";
import type { BeeProfile, SeasonTheme, StatusEntry } from "./types.js";

export const DEFAULT_STATUSES = statuses as StatusEntry[];
export const DEFAULT_BEES = bees as BeeProfile[];
export const DEFAULT_SEASONS = seasons as SeasonTheme[];
