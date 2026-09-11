// Character — canonical persistent identity (cheap creation: refs + identity + 1 portrait).
export type Character = {
  id: string; slug: string; ownerId: string | null;
  origin: { source: "etsy" | "mogmug" | "pogtown" | "share"; orderId?: string; listingId?: string; referralCharacterId?: string };
  identity: {
    name: string; species?: string; breed?: string; age?: string; pronouns?: string;
    physicalTraits: string[]; markings: string[]; colors: string[];
    personalityTraits: string[]; likes: string[]; dislikes: string[]; enemies: string[];
    habits: string[]; nicknames: string[]; runningJokes: string[]; freeformStory?: string;
  };
  references: { primaryImage: string; images: string[] };
  assets?: { portrait?: string; transparentPortrait?: string; modelGlb?: string; modelUsdz?: string; voiceId?: string };
  state?: { outfit?: string; mood?: string; level?: number; xp?: number };
  permissions: { public: boolean; remixable: boolean; allowMessages: boolean };
  createdAt: string; updatedAt: string;
};

export type ReferenceGrade = "A" | "B" | "C" | "REJECT";

// Grade photo references without blocking sale: A=4+ views, B=2-3, C=1 usable, REJECT=obscured.
export function gradeReferences(usableViews: number, readable: boolean): ReferenceGrade {
  if (!readable) return "REJECT";
  if (usableViews >= 4) return "A";
  if (usableViews >= 2) return "B";
  return "C";
}
