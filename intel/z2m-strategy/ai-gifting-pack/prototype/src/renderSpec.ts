import { PrintSpec } from "./types";

export const printSpecs: Record<string, PrintSpec> = {
  "card-a5": {
    sku: "card-a5",
    widthPx: 1819,
    heightPx: 2551,
    bleedPx: 36,
    safeMarginPx: 72,
    format: "pdf",
  },
  "ornament-round": {
    sku: "ornament-round",
    widthPx: 1200,
    heightPx: 1200,
    bleedPx: 30,
    safeMarginPx: 60,
    format: "png",
  },
};

/**
 * IMPORTANT:
 * Values above are placeholders for development.
 * Replace with the exact current template dimensions/bleeds from the selected
 * fulfilment provider before submitting a real print order.
 */
