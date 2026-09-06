import * as THREE from 'three';
import fs from 'fs';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 100);
camera.position.set(0, 0.5, 3); camera.lookAt(0, 0, 0);

scene.add(new THREE.DirectionalLight(0xffffff, 1));
scene.add(new THREE.DirectionalLight(0xffd700, 0.5));

const bartholomew = new THREE.Group();
bartholomew.name = 'BartholomewRoot';

const gold = new THREE.MeshStandardMaterial({ color: 0xffd700, metalness: 0.3, roughness: 0.4 });
const stripe = new THREE.MeshStandardMaterial({ color: 0x1a1a2e });
const eye = new THREE.MeshStandardMaterial({ color: 0x6b3fa0, emissive: 0x6b3fa0, emissiveIntensity: 0.5 });
const wingMat = new THREE.MeshStandardMaterial({ color: 0xe8f0ff, transparent: true, opacity: 0.5, side: THREE.DoubleSide });
const capeMat = new THREE.MeshStandardMaterial({ color: 0xcc3333, side: THREE.DoubleSide });
const tipMat = new THREE.MeshStandardMaterial({ color: 0xffd700, emissive: 0xffd700, emissiveIntensity: 0.4 });

const body = new THREE.Mesh(new THREE.CapsuleGeometry(0.3, 0.5, 8, 16), gold);
body.rotation.z = Math.PI/2; body.name = 'Body'; bartholomew.add(body);

[-0.15, 0, 0.15].forEach((z, i) => {
  const s = new THREE.Mesh(new THREE.CapsuleGeometry(0.31, 0.06, 8, 16), stripe);
  s.rotation.z = Math.PI/2; s.position.z = z; s.name = `Stripe_${i}`; bartholomew.add(s);
});

const head = new THREE.Mesh(new THREE.SphereGeometry(0.24, 16, 16), gold);
head.position.set(0.42, 0.12, 0); head.name = 'Head'; bartholomew.add(head);

[0.09, -0.09].forEach((z, i) => {
  const e = new THREE.Mesh(new THREE.SphereGeometry(0.06, 16, 16), eye);
  e.position.set(0.56, 0.18, z); e.name = `Eye_${i===0?'L':'R'}`; bartholomew.add(e);
  const h = new THREE.Mesh(new THREE.SphereGeometry(0.022, 8, 8), new THREE.MeshBasicMaterial({ color: 0xffffff }));
  h.position.set(0.6, 0.21, z > 0 ? 0.11 : -0.11); bartholomew.add(h);
});

const smile = new THREE.Mesh(new THREE.TorusGeometry(0.06, 0.012, 8, 16, Math.PI), stripe);
smile.position.set(0.6, 0.06, 0); smile.rotation.y = Math.PI/2; smile.rotation.z = Math.PI;
smile.name = 'Smile'; bartholomew.add(smile);

[0.1, -0.1].forEach((z, i) => {
  const a = new THREE.Mesh(new THREE.CylinderGeometry(0.01, 0.016, 0.3, 8), stripe);
  a.position.set(0.38, 0.42, z); a.rotation.z = -0.3; a.rotation.x = z > 0 ? 0.25 : -0.25;
  a.name = `Antenna_${i===0?'L':'R'}`; bartholomew.add(a);
  const t = new THREE.Mesh(new THREE.SphereGeometry(0.03, 8, 8), tipMat);
  t.position.set(0.28, 0.58, z * 1.4); t.name = `AntennaTip_${i===0?'L':'R'}`; bartholomew.add(t);
});

const ws = new THREE.Shape();
ws.moveTo(0, 0); ws.bezierCurveTo(0.18, 0.14, 0.4, 0.16, 0.45, 0.04);
ws.bezierCurveTo(0.4, -0.08, 0.18, -0.14, 0, 0);
const wg = new THREE.ShapeGeometry(ws);
[[-0.12,0.22,0.18,-0.5,1.4],[-0.18,0.2,0.22,-0.3,1],[-0.12,0.22,-0.18,0.5,1.4],[-0.18,0.2,-0.22,0.3,1]].forEach(([x,y,z,rx,s],i) => {
  const w = new THREE.Mesh(wg, wingMat);
  w.position.set(x,y,z); w.rotation.x = rx; w.scale.set(s,s,s); w.name = `Wing_${i}`; bartholomew.add(w);
});

const cp = new THREE.Mesh(new THREE.PlaneGeometry(0.4, 0.5, 8, 8), capeMat);
cp.position.set(-0.18, 0.12, 0); cp.rotation.y = Math.PI; cp.rotation.x = 0.15;
cp.name = 'Cape'; bartholomew.add(cp);

bartholomew.position.y = 0.1; bartholomew.rotation.y = -0.15; scene.add(bartholomew);

console.log('Created:', bartholomew.children.length, 'meshes');

// Export using toJSON
const json = scene.toJSON();
fs.writeFileSync('bartholomew-scene.json', JSON.stringify(json, null, 2));
console.log('Exported bartholomew-scene.json');
console.log('Size:', JSON.stringify(json).length, 'bytes');
