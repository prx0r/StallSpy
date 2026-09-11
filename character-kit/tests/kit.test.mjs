import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { gradeReferences } from "../src/character.ts";
import { COPY } from "../src/conversion.ts";
import { phrasesFor } from "../src/loading.ts";

describe("character-kit", () => {
  it("grades without blocking sale", () => {
    assert.equal(gradeReferences(4, true), "A");
    assert.equal(gradeReferences(1, true), "C");
    assert.equal(gradeReferences(6, false), "REJECT");
  });
  it("never says buy/mint", () => {
    assert.ok(!COPY.bringToLife("Buster").toLowerCase().includes("buy"));
    assert.ok(!COPY.bringToLife("Buster").toLowerCase().includes("mint"));
    assert.equal(COPY.alive("Royal Buster"), "Royal Buster is alive.");
  });
  it("serves character loading packs", () => {
    assert.ok(phrasesFor("buster").some((p) => p.includes("Dave")));
    assert.ok(phrasesFor("bartholomew").some((p) => p.includes("hive")));
  });
});
