export type Tone =
  | "funny"
  | "sentimental"
  | "premium"
  | "minimal"
  | "absurd"
  | "nostalgic";

export interface Recipient {
  id: string;
  displayName: string;
  relation: string;
  preferences: string[];
  avoid?: string[];
  importantDates?: Record<string, string>;
}

export interface CreativeBrief {
  recipient: Recipient;
  occasion: string;
  country: string;
  language: string;
  budgetMinor: number;
  currency: string;
  tone: Tone[];
  memories: string[];
  exactText?: string[];
  assetIds: string[];
}

export interface CreativeConcept {
  id: string;
  title: string;
  rationale: string;
  styleId: string;
  visualPrompt: string;
  exactCopy: string[];
  suggestedProducts: string[];
  ipRisk: "low" | "review" | "blocked";
}

export interface PrintSpec {
  sku: string;
  widthPx: number;
  heightPx: number;
  bleedPx: number;
  safeMarginPx: number;
  format: "png" | "jpg" | "pdf";
}

export interface RenderQA {
  passed: boolean;
  errors: string[];
  warnings: string[];
  sha256?: string;
}

export interface Quote {
  provider: string;
  productMinor: number;
  shippingMinor: number;
  taxMinor: number;
  currency: string;
  estimatedDelivery?: string;
  reliabilityScore: number;
}
