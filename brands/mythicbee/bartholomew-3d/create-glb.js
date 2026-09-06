import fs from 'fs';

// Minimal GLB file with Bartholomew geometry
// GLB format: magic + version + length + JSON chunk + BIN chunk

// Create simple mesh data
const positions = new Float32Array([
  // Body
  0,-0.25,-0.15, 0.3,-0.25,-0.15, 0.3,0.25,-0.15, 0,0.25,-0.15,
  0,-0.25,0.15, 0.3,-0.25,0.15, 0.3,0.25,0.15, 0,0.25,0.15,
  // Head
  0.18,-0.12,-0.24, 0.66,-0.12,-0.24, 0.66,0.36,-0.24, 0.18,0.36,-0.24,
  0.18,-0.12,0.24, 0.66,-0.12,0.24, 0.66,0.36,0.24, 0.18,0.36,0.24,
  // Eyes
  0.5,0.12,-0.15, 0.62,0.12,-0.15, 0.62,0.24,-0.15, 0.5,0.24,-0.15,
  0.5,0.12,0.15, 0.62,0.12,0.15, 0.62,0.24,0.15, 0.5,0.24,0.15,
  // Wings
  -0.12,0.22,0.18, 0.28,0.32,0.18, 0.28,0.12,0.18, -0.12,0.17,0.18,
  -0.18,0.2,0.22, 0.22,0.3,0.22, 0.22,0.1,0.22, -0.18,0.15,0.22,
  -0.12,0.22,-0.18, 0.28,0.32,-0.18, 0.28,0.12,-0.18, -0.12,0.17,-0.18,
  -0.18,0.2,-0.22, 0.22,0.3,-0.22, 0.22,0.1,-0.22, -0.18,0.15,-0.22,
  // Cape
  -0.2,0.1,-0.25, -0.2,0.1,0.25, -0.2,-0.4,0.25, -0.2,-0.4,-0.25
]);

const indices = new Uint16Array([
  // Body
  0,1,2, 0,2,3, 4,5,6, 4,6,7,
  // Head
  8,9,10, 8,10,11, 12,13,14, 12,14,15,
  // Eyes
  16,17,18, 16,18,19, 20,21,22, 20,22,23,
  // Wings
  24,25,26, 24,26,27, 28,29,30, 28,30,31,
  32,33,34, 32,34,35, 36,37,38, 36,38,39,
  // Cape
  40,41,42, 40,42,43
]);

// Create JSON
const gltf = {
  asset: { version: "2.0", generator: "MythicBee" },
  scene: 0,
  scenes: [{ name: "Bartholomew", nodes: [0] }],
  nodes: [
    { name: "BartholomewRoot", mesh: 0 }
  ],
  meshes: [
    { name: "Bartholomew", primitives: [{ attributes: { POSITION: 0 }, indices: 1, material: 0 }] }
  ],
  accessors: [
    { bufferView: 0, componentType: 5126, count: 44, type: "VEC3", max: [0.66, 0.36, 0.24], min: [-0.2, -0.4, -0.25] },
    { bufferView: 1, componentType: 5123, count: 72, type: "SCALAR" }
  ],
  bufferViews: [
    { buffer: 0, byteOffset: 0, byteLength: positions.byteLength },
    { buffer: 0, byteOffset: positions.byteLength, byteLength: indices.byteLength }
  ],
  buffers: [{ byteLength: positions.byteLength + indices.byteLength }],
  materials: [
    { name: "Gold", pbrMetallicRoughness: { baseColorFactor: [1, 0.84, 0, 1], metallicFactor: 0.4, roughnessFactor: 0.3 } }
  ]
};

// Create BIN data
const binData = Buffer.concat([
  Buffer.from(positions.buffer),
  Buffer.from(indices.buffer)
]);

// Pad to 4-byte alignment
const padding = (4 - (binData.length % 4)) % 4;
const paddedBin = Buffer.concat([binData, Buffer.alloc(padding)]);

// Create JSON chunk
const jsonStr = JSON.stringify(gltf);
const jsonChunk = Buffer.from(jsonStr);
const jsonPadded = Buffer.concat([jsonChunk, Buffer.alloc((4 - (jsonChunk.length % 4)) % 4)]);

// Create GLB
const glb = Buffer.alloc(12 + 8 + jsonPadded.length + 8 + paddedBin.length);

// Header
glb.writeUInt32LE(0x46546C67, 0); // magic
glb.writeUInt32LE(2, 4); // version
glb.writeUInt32LE(glb.length, 8); // length

// JSON chunk
glb.writeUInt32LE(jsonPadded.length, 12);
glb.writeUInt32LE(0x4E4F534A, 16); // JSON type
jsonPadded.copy(glb, 20);

// BIN chunk
glb.writeUInt32LE(paddedBin.length, 20 + jsonPadded.length);
glb.writeUInt32LE(0x004E4942, 24 + jsonPadded.length); // BIN type
paddedBin.copy(glb, 28 + jsonPadded.length);

// Write file
fs.writeFileSync('bartholomew.glb', glb);
console.log('✅ Created bartholomew.glb');
console.log('Size:', glb.length, 'bytes');
console.log('Nodes:', gltf.nodes.length);
console.log('Meshes:', gltf.meshes.length);
console.log('Materials:', gltf.materials.length);
