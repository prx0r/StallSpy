import { CreativeBrief } from "./types";

export function buildConceptPrompt(b: CreativeBrief): string {
  return `
You are a senior gift creative director.

Create six DISTINCT finished gift concepts for:
recipient: ${b.recipient.displayName}
relationship: ${b.recipient.relation}
occasion: ${b.occasion}
country: ${b.country}
language: ${b.language}
budget: ${b.currency} ${(b.budgetMinor / 100).toFixed(2)}
tone: ${b.tone.join(", ")}
preferences: ${b.recipient.preferences.join(", ")}
avoid: ${(b.recipient.avoid || []).join(", ")}
memories: ${b.memories.join(" | ")}

Return structured JSON only.

Every concept needs:
- title
- one-sentence emotional idea
- visual direction
- exact short copy
- 2-4 suitable physical products
- IP/trademark risk note

Rules:
- never invent a name/date not supplied
- do not imitate protected characters/logos
- concepts must look intentionally art-directed, not generic AI art
- exact customer names/text will later be rendered deterministically
- make concepts meaningfully different
`.trim();
}
