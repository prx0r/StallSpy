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
  { id: "card-collectible", requiredInputs: ["photos", "name"], generationSteps: ["identity", "card-art"], physicalSku: "GLOBAL-GRE-MOH-7X5-BLA", creditsGranted: 10, unlocks: ["portal"] },
  { id: "card-ar", requiredInputs: ["photos", "name"], generationSteps: ["identity", "card-art", "ar"], physicalSku: "GLOBAL-GRE-MOH-7X5-BLA", creditsGranted: 10, unlocks: ["portal", "ar"] },
  { id: "mug", requiredInputs: ["photos", "name"], generationSteps: ["identity", "mug-art"], physicalSku: "GLOBAL-MUG-W", creditsGranted: 10, unlocks: ["portal"] },
  { id: "mug-ar", requiredInputs: ["photos", "name"], generationSteps: ["identity", "mug-art", "ar"], physicalSku: "GLOBAL-MUG-W", creditsGranted: 10, unlocks: ["portal", "ar"] },
  { id: "ornament", requiredInputs: ["photos", "name"], generationSteps: ["identity", "ornament-art"], physicalSku: "XMAS-PORC-BAUB", creditsGranted: 10, unlocks: ["portal"] },
  { id: "character-pack", requiredInputs: ["photos", "name", "identity"], generationSteps: ["identity", "turnaround", "glb"], creditsGranted: 20, unlocks: ["rig", "ar", "games"] },
];

export function recipeFor(id: string): ProductRecipe {
  const r = CATALOGUE.find((p) => p.id === id);
  if (!r) throw new Error(`unknown product ${id}`);
  return r;
}

// THE TEN — launch lineup. Verified SKUs, prodigi.com 2026-09-12. See docs/prodigi/THE_TEN.md.
export type LaunchProduct = { slot: number; name: string; sku: string; printArea: string; ships: string; seasonal?: boolean };

export const LAUNCH_TEN: LaunchProduct[] = [
  { slot: 1, name: "Photo mug 11oz", sku: "GLOBAL-MUG-W", printArea: "229x95mm", ships: "UK/EU/US" },
  { slot: 2, name: "Magic mug 11oz", sku: "H-MUG-MAGIC-B", printArea: "94x122mm", ships: "UK" },
  { slot: 3, name: "Card direct-send 7x5", sku: "GLOBAL-GRE-MOH-7X5-DIR", printArea: "178x127mm", ships: "UK" },
  { slot: 4, name: "Card self-send 7x5", sku: "GLOBAL-GRE-MOH-7X5-BLA", printArea: "178x127mm", ships: "UK/EU" },
  { slot: 5, name: "Canvas cushion 12in", sku: "GLOBAL-CUSH-12X12-CAN", printArea: "305mm", ships: "UK/US" },
  { slot: 6, name: "Bandana M", sku: "PET-BANDANA-MED", printArea: "220x140mm", ships: "UK/US" },
  { slot: 7, name: "Kiss-cut sticker M", sku: "M-STI-5_5X5_5", printArea: "140x140mm", ships: "UK" },
  { slot: 8, name: "Fine-art print 16x24", sku: "GLOBAL-FAP-16x24", printArea: "16x24in", ships: "Global" },
  { slot: 9, name: "Ceramic ornament", sku: "XMAS-PORC-BAUB", printArea: "75x75mm", ships: "UK", seasonal: true },
  { slot: 10, name: "Bauble", sku: "XMAS-PLAS-BAUB", printArea: "79x84mm", ships: "UK", seasonal: true },
];
