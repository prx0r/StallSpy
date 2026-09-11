// One pipeline, ProductRecipe config — never ten backends.
export type ProductRecipe = {
  id: string;
  requiredInputs: string[];
  generationSteps: string[];
  physicalSku?: string;
  creditsGranted: number;
  unlocks: string[];
};

export const CATALOGUE: ProductRecipe[] = [
  { id: "video-comes-alive", requiredInputs: ["photos", "name"], generationSteps: ["identity", "video"], creditsGranted: 0, unlocks: ["share-page"] },
  { id: "video-wizard", requiredInputs: ["photos", "name"], generationSteps: ["identity", "video"], creditsGranted: 0, unlocks: ["share-page"] },
  { id: "video-birthday", requiredInputs: ["photos", "name", "message"], generationSteps: ["identity", "video"], creditsGranted: 0, unlocks: ["share-page"] },
  { id: "talking-message", requiredInputs: ["photos", "name", "message"], generationSteps: ["identity", "voice", "video"], creditsGranted: 0, unlocks: ["share-page"] },
  { id: "card-collectible", requiredInputs: ["photos", "name"], generationSteps: ["identity", "card-art"], physicalSku: "CARD-A6", creditsGranted: 10, unlocks: ["portal"] },
  { id: "card-ar", requiredInputs: ["photos", "name"], generationSteps: ["identity", "card-art", "ar"], physicalSku: "CARD-A6", creditsGranted: 10, unlocks: ["portal", "ar"] },
  { id: "mug", requiredInputs: ["photos", "name"], generationSteps: ["identity", "mug-art"], physicalSku: "MUG-11OZ", creditsGranted: 10, unlocks: ["portal"] },
  { id: "mug-ar", requiredInputs: ["photos", "name"], generationSteps: ["identity", "mug-art", "ar"], physicalSku: "MUG-11OZ", creditsGranted: 10, unlocks: ["portal", "ar"] },
  { id: "ornament", requiredInputs: ["photos", "name"], generationSteps: ["identity", "ornament-art"], physicalSku: "ORNAMENT", creditsGranted: 10, unlocks: ["portal"] },
  { id: "character-pack", requiredInputs: ["photos", "name", "identity"], generationSteps: ["identity", "turnaround", "glb"], creditsGranted: 20, unlocks: ["rig", "ar", "games"] },
];

export function recipeFor(id: string): ProductRecipe {
  const r = CATALOGUE.find((p) => p.id === id);
  if (!r) throw new Error(`unknown product ${id}`);
  return r;
}
