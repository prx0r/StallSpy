// Etsy personalization: 5 typed fields, 1 upload ≤10 files. Collect at checkout, not Messages.
export type EtsyField =
  | { kind: "upload"; title: string; maxFiles: number; required: true }
  | { kind: "text"; title: string; required: boolean; hint?: string }
  | { kind: "dropdown"; title: string; required: boolean; options: string[] };

export const PET_LISTING_FIELDS: EtsyField[] = [
  { kind: "upload", title: "Photos of your pet", maxFiles: 8, required: true },
  { kind: "text", title: "Pet's name", required: true },
  { kind: "text", title: "Tell us what makes them THEM", required: false, hint: "Food, habits, enemies, nicknames, crimes." },
  { kind: "dropdown", title: "Choose their adventure", required: false, options: ["Surprise me", "Wizard", "Royal", "Astronaut", "Pirate", "Superhero-style original", "Movie star", "Christmas", "Birthday"] },
  { kind: "dropdown", title: "Pet personality", required: false, options: ["Sweet", "Chaotic", "Serious", "Dramatic", "Tiny menace", "Surprise me"] },
];

export type PhotoAssessment = {
  petDetected: boolean; petCount: number; faceVisible: boolean; bodyVisible: boolean;
  occlusion: boolean; blur: boolean; resolution: number; duplicateOf?: string; viewAngle: "front" | "side" | "body" | "other";
};

// Select canonical references; request more photos only when validation fails.
export function selectReferences(photos: PhotoAssessment[]) {
  const good = photos.filter((p) => p.petDetected && !p.blur && p.resolution >= 720);
  const pick = (angle: PhotoAssessment["viewAngle"]) => good.find((p) => p.viewAngle === angle && (angle === "front" ? p.faceVisible : true));
  const primary = pick("front") ?? good[0] ?? null;
  return {
    primary,
    fullBody: pick("body"),
    side: pick("side"),
    needsMore: !primary || !primary.faceVisible,
  };
}
