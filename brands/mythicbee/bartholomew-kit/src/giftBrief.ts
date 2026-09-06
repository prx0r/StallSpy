export type GiftBriefStatus =
  | "collecting"
  | "ready_for_concept"
  | "concept_ready"
  | "preview_ready"
  | "checkout_ready";

export interface Interest {
  label: string;
  detail: string | null;
  importance: number;
}

export interface GiftBrief {
  schemaVersion: "1.0";
  briefId?: string | null;
  status: GiftBriefStatus;
  occasion: {
    type: string | null;
    label?: string | null;
    date?: string | null;
    locale?: string | null;
  };
  recipient: {
    relationship: string | null;
    name?: string | null;
    age?: number | null;
    pronouns?: string | null;
  };
  interests: Interest[];
  personality: Array<{ trait: string; evidence?: string | null }>;
  memories: Array<{
    summary: string;
    emotionalWeight?: number;
    place?: string | null;
    date?: string | null;
  }>;
  tone: {
    primary: string | null;
    secondary: string[];
    avoid: string[];
  };
  creativeDirection?: {
    concept?: string | null;
    format?: string | null;
    mustInclude?: string[];
    mustAvoid?: string[];
  };
  product?: {
    recommendedProductIds?: string[];
    selectedProductId?: string | null;
  };
  assets: {
    photos: MediaAsset[];
    videos: MediaAsset[];
    audio: MediaAsset[];
  };
  budget?: { currency: string; maxAmount?: number | null } | null;
  deadline?: { date?: string | null; hard: boolean } | null;
  consent?: { hasPermissionToUseUploadedMedia?: boolean | null };
  confidence: Record<string, number>;
}

export interface MediaAsset {
  id: string;
  kind: "photo" | "video" | "audio";
  caption?: string | null;
  url?: string | null;
}

export const createEmptyGiftBrief = (): GiftBrief => ({
  schemaVersion: "1.0",
  status: "collecting",
  occasion: { type: null, label: null, date: null, locale: null },
  recipient: { relationship: null, name: null, age: null, pronouns: null },
  interests: [],
  personality: [],
  memories: [],
  tone: { primary: null, secondary: [], avoid: [] },
  creativeDirection: { concept: null, format: null, mustInclude: [], mustAvoid: [] },
  product: { recommendedProductIds: [], selectedProductId: null },
  assets: { photos: [], videos: [], audio: [] },
  budget: null,
  deadline: null,
  consent: { hasPermissionToUseUploadedMedia: null },
  confidence: {
    occasion: 0,
    recipient: 0,
    interests: 0,
    personality: 0,
    memories: 0,
    tone: 0,
    creativeDirection: 0
  }
});

/** Merge a sparse tool-call patch. Arrays are replaced, not concatenated. */
export function mergeGiftBrief(current: GiftBrief, patch: Partial<GiftBrief>): GiftBrief {
  const next: GiftBrief = {
    ...current,
    ...patch,
    occasion: { ...current.occasion, ...(patch.occasion ?? {}) },
    recipient: { ...current.recipient, ...(patch.recipient ?? {}) },
    tone: { ...current.tone, ...(patch.tone ?? {}) },
    creativeDirection: { ...current.creativeDirection, ...(patch.creativeDirection ?? {}) },
    product: { ...current.product, ...(patch.product ?? {}) },
    assets: { ...current.assets, ...(patch.assets ?? {}) },
    consent: { ...current.consent, ...(patch.consent ?? {}) },
    confidence: { ...current.confidence, ...(patch.confidence ?? {}) }
  };
  next.status = inferStatus(next);
  return next;
}

export function readinessScore(brief: GiftBrief): number {
  const values = [
    brief.occasion.type ? 1 : 0,
    brief.recipient.relationship ? 1 : 0,
    Math.min(1, brief.interests.length / 2),
    Math.min(1, brief.personality.length),
    Math.min(1, brief.memories.length),
    brief.tone.primary ? 1 : 0
  ];
  return values.reduce((a, b) => a + b, 0) / values.length;
}

export function inferStatus(brief: GiftBrief): GiftBriefStatus {
  if (brief.product?.selectedProductId && brief.status === "checkout_ready") return "checkout_ready";
  if (brief.status === "preview_ready") return "preview_ready";
  if (brief.creativeDirection?.concept) return "concept_ready";
  return readinessScore(brief) >= 0.67 ? "ready_for_concept" : "collecting";
}

/** Deterministic fallback if the LLM needs a nudge on the next highest-value question. */
export function suggestNextQuestion(brief: GiftBrief): string | null {
  if (!brief.occasion.type) return "What's the occasion?";
  if (!brief.recipient.relationship) return "Who are we making this for?";
  if (brief.interests.length === 0 && brief.personality.length === 0)
    return "What are they obsessed with, or what makes them unmistakably them?";
  if (brief.memories.length === 0)
    return "What's one story, running joke, or memory that instantly feels like them?";
  if (!brief.tone.primary)
    return "Should this land funny, properly emotional, epic, or somewhere dangerously between the two?";
  return null;
}
