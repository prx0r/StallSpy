
import { describe, expect, it } from "vitest";
import { HiveActivityEngine } from "../src/engine.js";
import { DEFAULT_BEES, DEFAULT_SEASONS, DEFAULT_STATUSES } from "../src/defaults.js";

describe("HiveActivityEngine", () => {
  it("is deterministic under a seed", () => {
    const make = () => new HiveActivityEngine({
      statuses: DEFAULT_STATUSES,
      seasons: DEFAULT_SEASONS,
      seed: "same",
    });
    const a = make().select({ phase: "ideate", season: "christmas" }).text;
    const b = make().select({ phase: "ideate", season: "christmas" }).text;
    expect(a).toBe(b);
  });

  it("can render contextual hooks", () => {
    const engine = new HiveActivityEngine({
      statuses: [{
        id: "x",
        text: "Reconsidering {hook}…",
        phases: ["understand"],
        contextualSlots: ["hook"],
      }],
      seed: 1,
    });
    expect(engine.select({ phase: "understand", hooks: { hook: "the Wembley incident" } }).text)
      .toContain("Wembley");
  });

  it("honours explicit status", () => {
    const engine = new HiveActivityEngine({ statuses: [], seed: 1 });
    expect(engine.select({ phase: "generic", explicitStatus: "Printing now…" }).text)
      .toBe("Printing now…");
  });

  it("supports bee preference weighting without changing API", () => {
    const engine = new HiveActivityEngine({
      statuses: DEFAULT_STATUSES,
      seasons: DEFAULT_SEASONS,
      seed: "martin",
    });
    const snapshot = engine.select({
      phase: "package",
      bee: DEFAULT_BEES.find(b => b.id === "martin"),
    });
    expect(snapshot.text.length).toBeGreaterThan(0);
  });
});
