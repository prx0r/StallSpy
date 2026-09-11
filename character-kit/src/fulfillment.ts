// Prodigi fulfillment: hosted asset URLs at exact SKU dims. Creds via vault refs only — never here.
export type ProdigiOrder = { sku: string; assetUrl: string; copies: number; recipient: { name: string } };

export function buildProdigiOrder(sku: string, assetUrl: string, recipientName: string, copies = 1): ProdigiOrder {
  if (!/^https:\/\//.test(assetUrl)) throw new Error("asset must be a hosted https URL, never ephemeral/local");
  if (!sku) throw new Error("exact Prodigi SKU required (no central cropping fallback)");
  return { sku, assetUrl, copies, recipient: { name: recipientName } };
}

// Physical object ≠ content: mug → trigger → character → experience resolver. Object never points at a file.
export type TriggerMap = { triggerId: string; characterId: string };

export function resolverUrl(triggerId: string): string {
  return `https://mogmug.com/x/${triggerId}`;
}

// Share loop attribution: source character/share/owner → recipient character.
export type ShareAttribution = { sourceCharacterId: string; sourceShareId: string; sourceOwnerId: string; recipientCharacterId?: string };

export function shareUrl(shareId: string): string {
  return `https://mogmug.com/v/${shareId}`;
}

// Free identity, paid actions: creation + thumbnail free; videos/premium/rig/GLB/voice/AR/physical cost.
export function isFreeTier(action: string): boolean {
  return ["create-character", "thumbnail"].includes(action);
}
