import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { PET_LISTING_FIELDS, selectReferences } from "../src/onboarding.ts";
import { CATALOGUE, LAUNCH_TEN, recipeFor } from "../src/products.ts";
import { buildProdigiOrder, resolverUrl, shareUrl, isFreeTier } from "../src/fulfillment.ts";

const photo = (over = {}) => ({ petDetected: true, petCount: 1, faceVisible: true, bodyVisible: true, occlusion: false, blur: false, resolution: 1080, viewAngle: "front", ...over });

describe("mogmug funnel", () => {
  it("etsy collects at checkout: upload + 4 companions", () => {
    assert.equal(PET_LISTING_FIELDS.length, 5);
    assert.equal(PET_LISTING_FIELDS[0].kind, "upload");
  });
  it("photo pipeline picks refs, asks only when needed", () => {
    const good = selectReferences([photo(), photo({ viewAngle: "body", faceVisible: false }), photo({ viewAngle: "side" })]);
    assert.ok(good.primary && !good.needsMore);
    const bad = selectReferences([photo({ faceVisible: false, viewAngle: "other", resolution: 400 })]);
    assert.ok(bad.needsMore);
  });
  it("one pipeline: ten recipes, no bespoke backends", () => {
    assert.equal(CATALOGUE.length, 10);
    assert.equal(recipeFor("mug").physicalSku, "GLOBAL-MUG-W");
  });
  it("prodigi needs hosted URL + exact SKU; portals resolve, never files", () => {
    assert.throws(() => buildProdigiOrder("MUG-11OZ", "/tmp/local.png", "Mum"));
    const o = buildProdigiOrder("MUG-11OZ", "https://cdn.mogmug.com/print/buster-mug.png", "Mum");
    assert.equal(o.sku, "MUG-11OZ");
    assert.equal(resolverUrl("81F2"), "https://mogmug.com/x/81F2");
    assert.equal(shareUrl("abc"), "https://mogmug.com/v/abc");
  });
  it("the ten: 8 heroes + 2 xmas, all with real SKUs", () => {
    assert.equal(LAUNCH_TEN.length, 10);
    assert.ok(LAUNCH_TEN.every((p) => p.sku && p.printArea && p.ships));
    assert.deepEqual(LAUNCH_TEN.filter((p) => p.seasonal).map((p) => p.sku), ["XMAS-PORC-BAUB", "XMAS-PLAS-BAUB"]);
  });
  it("identity free, actions paid", () => {
    assert.ok(isFreeTier("create-character"));
    assert.ok(!isFreeTier("video"));
  });
});
