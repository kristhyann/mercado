// Kit base: cenário do cerrado, macaco-prego, utilidades de animação (three.js, low-poly)
import * as THREE from 'three';

export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const lerp = (a, b, t) => a + (b - a) * t;
export const ease = t => { t = clamp(t); return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; };
export const easeOut = t => { t = clamp(t); return 1 - Math.pow(1 - t, 3); };
// pop: 0 -> 1.1 -> 1 em dur segundos
export const pop = (t, dur = .3) => {
  if (t <= 0) return 0; const x = t / dur; if (x >= 1) return 1;
  if (x < .65) return 1.12 * easeOut(x / .65); return lerp(1.12, 1, ease((x - .65) / .35));
};
// quique ao cair
export const bounce = x => {
  x = clamp(x); const n = 7.5625, d = 2.75;
  if (x < 1 / d) return n * x * x; if (x < 2 / d) return n * (x -= 1.5 / d) * x + .75;
  if (x < 2.5 / d) return n * (x -= 2.25 / d) * x + .9375; return n * (x -= 2.625 / d) * x + .984375;
};

let seed = 7;
export const rnd = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
export const rr = (a, b) => a + (b - a) * rnd();

export const M = (color, o = {}) => new THREE.MeshStandardMaterial({ color, flatShading: true, roughness: .85, metalness: 0, ...o });
export function mesh(geo, mat, x = 0, y = 0, z = 0, parent) {
  const m = new THREE.Mesh(geo, mat); m.position.set(x, y, z); m.castShadow = true; m.receiveShadow = true;
  if (parent) parent.add(m); return m;
}
export const ball = (r, mat, d = 1) => new THREE.Mesh(new THREE.IcosahedronGeometry(r, d), mat);

// ---------- Cenário do cerrado ----------
export function buildWorld(scene) {
  // céu em degradê
  const c = document.createElement('canvas'); c.width = 4; c.height = 512; const g = c.getContext('2d');
  const gr = g.createLinearGradient(0, 0, 0, 512); gr.addColorStop(0, '#3E9BE8'); gr.addColorStop(.55, '#8FD0FF'); gr.addColorStop(1, '#DDF3FF');
  g.fillStyle = gr; g.fillRect(0, 0, 4, 512);
  const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace;
  const sky = new THREE.Mesh(new THREE.SphereGeometry(400, 24, 16), new THREE.MeshBasicMaterial({ map: tex, side: THREE.BackSide, fog: false }));
  scene.add(sky);
  scene.fog = new THREE.Fog(0xCFEAFB, 60, 230);

  const sun = new THREE.DirectionalLight(0xFFF0D0, 2.7); sun.position.set(14, 26, 18); sun.castShadow = true;
  sun.shadow.mapSize.set(1536, 1536); const sc = sun.shadow.camera; sc.left = -30; sc.right = 30; sc.top = 30; sc.bottom = -30; sc.far = 120;
  sun.shadow.bias = -0.0005; sun.shadow.radius = 4; scene.add(sun); scene.add(sun.target);
  const hemi = new THREE.HemisphereLight(0xBFE6FF, 0x7A6A3A, 1.25); scene.add(hemi);
  const rim = new THREE.DirectionalLight(0xFFE2B0, 1.3); rim.position.set(-10, 8, -16); scene.add(rim);

  // chão low-poly
  const geo = new THREE.PlaneGeometry(400, 400, 90, 90); geo.rotateX(-Math.PI / 2);
  const pos = geo.attributes.position; const cols = [];
  const ca = new THREE.Color(0xB7C24E), cb = new THREE.Color(0x9DB443), cc = new THREE.Color(0xD4BE62);
  for (let i = 0; i < pos.count; i++) {
    const x = pos.getX(i), z = pos.getZ(i); const d = Math.hypot(x, z);
    pos.setY(i, d < 14 ? rr(-.03, .03) : rr(-.15, .15) + Math.max(0, (d - 60) * .05) * Math.sin(x * .05) * Math.cos(z * .04) * 3);
  }
  const ng = geo.toNonIndexed(); const p2 = ng.attributes.position;
  for (let i = 0; i < p2.count; i += 3) {
    const k = rnd(); const col = k < .45 ? ca : k < .8 ? cb : cc; for (let j = 0; j < 3; j++) cols.push(col.r, col.g, col.b);
  }
  ng.setAttribute('color', new THREE.Float32BufferAttribute(cols, 3)); ng.computeVertexNormals();
  const ground = new THREE.Mesh(ng, new THREE.MeshStandardMaterial({ vertexColors: true, flatShading: true, roughness: 1 }));
  ground.receiveShadow = true; scene.add(ground);

  // tufos de capim (instanciados: um único desenho por cor)
  const tuftG = new THREE.ConeGeometry(.09, .55, 4); const tuftCols = [0xC9B24A, 0x8FAE3A, 0xE0C766];
  const inst = tuftCols.map(c => { const im = new THREE.InstancedMesh(tuftG, M(c), 800); im.count = 0; im.receiveShadow = true; scene.add(im); return im; });
  const dm = new THREE.Object3D();
  for (let i = 0; i < 520; i++) {
    const a = rnd() * Math.PI * 2, d = 2.2 + Math.pow(rnd(), .7) * 60; const x = Math.cos(a) * d, z = Math.sin(a) * d;
    if (Math.abs(x) < 3.2 && z > -2 && z < 6) continue;
    const im = inst[i % 3]; const sc = rr(.7, 1.4);
    for (let k = 0; k < 4; k++) { dm.position.set(x + rr(-.1, .1) * sc, .22 * sc, z + rr(-.1, .1) * sc); dm.rotation.set(rr(-.4, .4), 0, rr(-.4, .4)); dm.scale.setScalar(sc); dm.updateMatrix(); im.setMatrixAt(im.count++, dm.matrix); }
  }
  inst.forEach(im => im.instanceMatrix.needsUpdate = true);

  // pedras grandes
  const rockMats = [M(0xB9A897), M(0xA39383), M(0xC7B6A2), M(0x9A8676)];
  const rock = (x, z, sx, sy, sz, ry = 0, m = 0, det = 0) => {
    const r = new THREE.Mesh(new THREE.DodecahedronGeometry(1, det), rockMats[m % 4]); r.scale.set(sx, sy, sz);
    r.position.set(x, sy * .55, z); r.rotation.y = ry; r.castShadow = r.receiveShadow = true; scene.add(r); return r;
  };
  rock(-5.5, -4, 2.2, 1.7, 1.8, .4, 0); rock(-3.6, -5.2, 1.2, 1, 1.1, 1, 1); rock(6, -6, 2.8, 2.2, 2.2, .2, 2);
  rock(4.2, -4.4, 1.1, .8, 1, 2, 3); rock(-9, -10, 3.5, 2.6, 3, 1.3, 1); rock(11, -12, 4, 3.2, 3, .8, 0);
  rock(-14, 2, 2.5, 1.8, 2, .3, 2); rock(13, 3, 2, 1.5, 2.2, 1.8, 3); rock(0, -16, 5, 3.5, 3, .5, 0);
  rock(-20, -22, 6, 5, 5, 1, 1); rock(22, -26, 7, 6, 6, .3, 2);

  // palmeiras
  const trunkM = M(0x8C6A48), trunkM2 = M(0x7A5A3C), leafM = M(0x3D9A3E, { side: THREE.DoubleSide }), leafM2 = M(0x2F8436, { side: THREE.DoubleSide });
  const palm = (x, z, h = 7, lean = .15, ry = 0) => {
    const p = new THREE.Group(); p.position.set(x, 0, z); p.rotation.y = ry; let y = 0, ox = 0; const n = 7;
    for (let i = 0; i < n; i++) {
      const seg = mesh(new THREE.CylinderGeometry(.22 - i * .012, .26 - i * .012, h / n, 6), i % 2 ? trunkM : trunkM2, ox, y + h / n / 2, 0, p);
      seg.rotation.z = -lean * .6; y += h / n * .98; ox += lean * h / n * .6;
    }
    const crown = new THREE.Group(); crown.position.set(ox, y, 0); p.add(crown);
    for (let i = 0; i < 9; i++) {
      const lg = new THREE.Group(); lg.rotation.y = i / 9 * Math.PI * 2 + rr(-.2, .2); crown.add(lg);
      const leaf = new THREE.Mesh(new THREE.ConeGeometry(.55, 3.6, 4, 1), i % 2 ? leafM : leafM2);
      leaf.scale.z = .18; leaf.rotation.z = -Math.PI / 2 + .25; leaf.rotation.x = 0; leaf.position.set(1.7, -.35, 0);
      const bend = new THREE.Group(); bend.rotation.z = -rr(.25, .55); bend.add(leaf); lg.add(bend); leaf.castShadow = true;
    }
    for (let i = 0; i < 6; i++) { const cnut = ball(.16, M(0xC98A2E), 0); cnut.position.set(Math.cos(i) * .3, -.35 - (i % 2) * .15, Math.sin(i) * .3); crown.add(cnut); }
    scene.add(p); return p;
  };
  palm(-4.2, -7.5, 8, .2, 0); palm(7.5, -9, 9, -.15, 1); palm(-11, -6, 7, .1, 2); palm(15, -4, 8.5, .25, 3);
  palm(-17, -14, 9, -.1, 1); palm(3, -22, 10, .1, 0); palm(-8, 6, 7.5, .2, 2); palm(10, 8, 8, -.2, 1); palm(26, -8, 9, 0, 2);

  // árvores tortas do cerrado + ipê amarelo
  const barkM = M(0x6E4B30), crownMs = [M(0x5FA83C), M(0x76B843), M(0xF2C230)];
  const tree = (x, z, s = 1, kind = 0) => {
    const t = new THREE.Group(); t.position.set(x, 0, z); t.scale.setScalar(s);
    const a = mesh(new THREE.CylinderGeometry(.16, .26, 2.4, 5), barkM, 0, 1.2, 0, t); a.rotation.z = .25;
    const b = mesh(new THREE.CylinderGeometry(.1, .16, 1.6, 5), barkM, .55, 2.6, 0, t); b.rotation.z = -.5;
    const c2 = mesh(new THREE.CylinderGeometry(.1, .14, 1.4, 5), barkM, -.35, 2.5, .1, t); c2.rotation.z = .7;
    const cm = crownMs[kind];
    [[.9, 3.4, 0, 1.3], [-.8, 3.2, .2, 1.1], [.1, 3.8, -.2, 1.2]].forEach(([cx, cy, cz, r]) => { const cr = mesh(new THREE.IcosahedronGeometry(r, 0), cm, cx, cy, cz, t); cr.scale.y = .55; });
    scene.add(t); return t;
  };
  tree(-7.5, -1.5, 1.1, 0); tree(9, -2, 1.2, 2); tree(-16, -5, 1.4, 1); tree(18, -14, 1.6, 0); tree(-3, -26, 2, 2); tree(-24, -2, 1.5, 0); tree(12, 14, 1.3, 1);

  // cupinzeiro
  const tm = M(0xB8693C);
  const mound = new THREE.Group(); mound.position.set(-7.2, 0, -12);
  mesh(new THREE.ConeGeometry(1.3, 3.2, 7), tm, 0, 1.6, 0, mound); mesh(new THREE.ConeGeometry(.6, 1.8, 6), tm, .7, .9, .4, mound);
  scene.add(mound);

  // nuvens
  const cloudM = new THREE.MeshStandardMaterial({ color: 0xffffff, flatShading: true, roughness: 1, emissive: 0xffffff, emissiveIntensity: .35, fog: false });
  const clouds = [];
  [[-40, 55, -150], [30, 62, -170], [80, 48, -140], [-90, 50, -130], [0, 75, -200], [55, 70, -110], [-60, 66, -90]].forEach(([x, y, z], i) => {
    const cl = new THREE.Group(); cl.position.set(x, y, z);
    for (let k = 0; k < 5; k++) { const b = new THREE.Mesh(new THREE.IcosahedronGeometry(rr(5, 9), 0), cloudM); b.position.set(k * 6 - 12, rr(-1, 2), rr(-2, 2)); b.scale.y = .6; cl.add(b); }
    scene.add(cl); clouds.push(cl);
  });
  return { sun, clouds };
}

// ---------- Macaco-prego ----------
export function buildMonkey() {
  const C = { body: 0x8E5B2C, limb: 0x74471F, cap: 0x2B190B, face: 0xF0CFA0, muzzle: 0xF7DDB8, hand: 0x3B2312 };
  const mBody = M(C.body), mLimb = M(C.limb), mCap = M(C.cap), mFace = M(C.face), mMuz = M(C.muzzle), mHand = M(C.hand);
  const mWhite = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: .3 }), mBlack = new THREE.MeshStandardMaterial({ color: 0x111111, roughness: .2 });
  const root = new THREE.Group();
  const hips = new THREE.Group(); hips.position.y = .78; root.add(hips);
  const torso = mesh(new THREE.IcosahedronGeometry(.42, 1), mBody, 0, .36, 0, hips); torso.scale.set(1, 1.25, .88);
  const belly = mesh(new THREE.IcosahedronGeometry(.32, 2), mMuz, 0, .3, .2, hips); belly.scale.set(.95, 1.2, .62);
  const neck = new THREE.Group(); neck.position.y = .82; hips.add(neck);
  const head = new THREE.Group(); head.position.y = .3; neck.add(head);
  mesh(new THREE.IcosahedronGeometry(.44, 1), mBody, 0, 0, 0, head);
  const face = mesh(new THREE.IcosahedronGeometry(.34, 1), mFace, 0, -.04, .22, head); face.scale.set(1.02, 1.05, .62);
  const muz = mesh(new THREE.IcosahedronGeometry(.18, 1), mMuz, 0, -.17, .37, head); muz.scale.set(1.25, .8, .8);
  mesh(new THREE.IcosahedronGeometry(.045, 0), mHand, -.035, -.1, .51, head); mesh(new THREE.IcosahedronGeometry(.045, 0), mHand, .035, -.1, .51, head);
  // boca (sorriso)
  const mouth = new THREE.Mesh(new THREE.TorusGeometry(.085, .018, 4, 10, Math.PI), new THREE.MeshStandardMaterial({ color: 0x3a1a0a }));
  mouth.position.set(0, -.2, .5); mouth.rotation.z = Math.PI; mouth.rotation.x = -.3; head.add(mouth);
  const mouthO = mesh(new THREE.IcosahedronGeometry(.06, 1), new THREE.MeshStandardMaterial({ color: 0x5a1a10 }), 0, -.22, .5, head); mouthO.scale.set(1, .2, .5); mouthO.visible = true;
  // olhos
  const eyes = [];
  for (const s of [-1, 1]) {
    const e = new THREE.Group(); e.position.set(s * .135, .04, .41); head.add(e);
    const w = mesh(new THREE.IcosahedronGeometry(.1, 2), mWhite, 0, 0, 0, e); w.scale.z = .6;
    const p = mesh(new THREE.IcosahedronGeometry(.062, 2), mBlack, 0, -.005, .05, e);
    const h = mesh(new THREE.IcosahedronGeometry(.02, 1), new THREE.MeshBasicMaterial({ color: 0xffffff }), .022 * s + .01, .025, .1, e);
    const lid = mesh(new THREE.IcosahedronGeometry(.105, 2), mFace, 0, .0, .0, e); lid.scale.set(1.05, 1, .65); lid.visible = false;
    const brow = mesh(new THREE.BoxGeometry(.14, .03, .04), mCap, 0, .13, .04, e); brow.rotation.z = -s * .15;
    eyes.push({ g: e, lid, brow, s, p });
  }
  // bochechas (vergonha)
  const blushM = new THREE.MeshBasicMaterial({ color: 0xff7a8a, transparent: true, opacity: 0 });
  const blush = [-1, 1].map(s => { const b = mesh(new THREE.CircleGeometry(.07, 10), blushM, s * .24, -.1, .44, head); b.rotation.y = s * .4; return b; });
  // orelhas
  for (const s of [-1, 1]) { const ear = mesh(new THREE.CylinderGeometry(.11, .11, .05, 8), mFace, s * .43, .02, -.02, head); ear.rotation.z = Math.PI / 2; ear.rotation.x = .2; }
  // boné escuro + tufinho
  const cap = mesh(new THREE.SphereGeometry(.455, 10, 6, 0, Math.PI * 2, 0, Math.PI * .42), mCap, 0, .03, -.04, head); cap.rotation.x = -.35;
  const tufts = new THREE.Group(); tufts.position.set(0, .42, .02); head.add(tufts);
  for (const [x, rz, h] of [[-.11, .35, .26], [.11, -.35, .26], [0, 0, .2], [-.05, .15, .22], [.05, -.15, .22]]) {
    const t = mesh(new THREE.ConeGeometry(.07, h, 5), mCap, x, h / 2 - .03, 0, tufts); t.rotation.z = rz; t.rotation.x = -.15;
  }
  // braços
  const arm = s => {
    const sh = new THREE.Group(); sh.position.set(s * .38, .62, 0); hips.add(sh);
    mesh(new THREE.IcosahedronGeometry(.12, 1), mBody, 0, 0, 0, sh);
    const up = mesh(new THREE.CylinderGeometry(.09, .1, .42, 6), mLimb, 0, -.21, 0, sh);
    const el = new THREE.Group(); el.position.y = -.42; sh.add(el);
    mesh(new THREE.IcosahedronGeometry(.09, 0), mLimb, 0, 0, 0, el);
    mesh(new THREE.CylinderGeometry(.075, .09, .4, 6), mLimb, 0, -.2, 0, el);
    const hand = new THREE.Group(); hand.position.y = -.43; el.add(hand);
    const hm = mesh(new THREE.IcosahedronGeometry(.12, 1), mHand, 0, 0, 0, hand); hm.scale.set(1.1, 1.2, .8);
    return { sh, el, hand };
  };
  const armL = arm(1), armR = arm(-1);
  const leg = s => {
    const hp = new THREE.Group(); hp.position.set(s * .2, .05, 0); hips.add(hp);
    mesh(new THREE.CylinderGeometry(.11, .12, .4, 6), mLimb, 0, -.2, 0, hp);
    const kn = new THREE.Group(); kn.position.y = -.4; hp.add(kn);
    mesh(new THREE.CylinderGeometry(.08, .1, .36, 6), mLimb, 0, -.18, 0, kn);
    const ft = mesh(new THREE.BoxGeometry(.17, .08, .3), mHand, 0, -.38, .08, kn);
    return { hp, kn };
  };
  const legL = leg(1), legR = leg(-1);
  // cauda
  const tail = new THREE.Group(); tail.position.set(0, .05, -.32); hips.add(tail);
  const tsegs = []; let par = tail;
  for (let i = 0; i < 9; i++) {
    const g = new THREE.Group(); g.position.y = i ? .2 : 0; par.add(g);
    mesh(new THREE.CylinderGeometry(.06 - i * .004, .07 - i * .004, .22, 5), i > 6 ? mCap : mLimb, 0, .1, 0, g); tsegs.push(g); par = g;
  }
  tail.rotation.x = -2.0;

  const mk = { root, hips, neck, head, eyes, mouth, mouthO, blushM, armL, armR, legL, legR, tail, tsegs, tufts };
  return mk;
}

// Poses (ângulos em radianos)
export const POSES = {
  idle: { lx: .15, lz: .25, le: -.35, rx: .15, rz: -.25, re: -.35, hl: 0, kl: 0, hr: 0, kr: 0, hx: 0, hy: 0, hz: 0, lean: .05, y: 0 },
  wave: { lx: .1, lz: .3, le: -.3, rx: -.2, rz: -2.6, re: -.6, hl: 0, kl: 0, hr: 0, kr: 0, hx: -.1, hy: 0, hz: .1, lean: 0, y: 0 },
  cover: { ik: 1, lx: -2.25, lz: -.85, le: -.5, rx: -2.25, rz: .85, re: -.5, hl: .1, kl: .2, hr: .1, kr: .2, hx: .08, hy: 0, hz: 0, lean: .2, y: -.04 },
  think: { lx: .15, lz: .25, le: -.35, rx: -1.25, rz: .55, re: -2.15, hl: 0, kl: 0, hr: 0, kr: 0, hx: -.25, hy: .15, hz: .12, lean: 0, y: 0 },
  proud: { lx: .1, lz: .35, le: -1.4, rx: .1, rz: -.35, re: -1.4, hl: 0, kl: 0, hr: 0, kr: 0, hx: -.2, hy: 0, hz: 0, lean: -.1, y: 0 },
  hold: { lx: -1.1, lz: -.35, le: -.9, rx: -1.1, rz: .35, re: -.9, hl: 0, kl: 0, hr: 0, kr: 0, hx: .25, hy: 0, hz: 0, lean: .1, y: 0 },
  bite: { lx: -1.2, lz: -.45, le: -1.9, rx: -1.2, rz: .45, re: -1.9, hl: 0, kl: 0, hr: 0, kr: 0, hx: -.05, hy: 0, hz: 0, lean: .1, y: 0 },
  lift: { lx: -3.0, lz: -.1, le: -.12, rx: -3.0, rz: .1, re: -.12, hl: .25, kl: .5, hr: .25, kr: .5, hx: -.35, hy: 0, hz: 0, lean: -.05, y: -.1 },
  smash: { lx: -1.15, lz: -.2, le: -.25, rx: -1.15, rz: .2, re: -.25, hl: .7, kl: 1.0, hr: .7, kr: 1.0, hx: .45, hy: 0, hz: 0, lean: .45, y: -.25 },
  scared: { lx: -2.4, lz: .7, le: -.6, rx: -2.4, rz: -.7, re: -.6, hl: 0, kl: 0, hr: 0, kr: 0, hx: -.2, hy: 0, hz: 0, lean: -.2, y: .05 },
  rub: { lx: -.6, lz: -.9, le: -1.5, rx: .15, rz: -.3, re: -.5, hl: 0, kl: 0, hr: 0, kr: 0, hx: .1, hy: -.2, hz: 0, lean: .05, y: 0 },
  sit: { lx: -.9, lz: -.25, le: -1.2, rx: .2, rz: -.35, re: -.6, hl: -1.5, kl: 1.35, hr: -1.5, kr: 1.35, hx: -.1, hy: 0, hz: 0, lean: 0, y: -.4 },
  eat: { lx: -1.25, lz: -.5, le: -2.1, rx: .2, rz: -.35, re: -.6, hl: -1.5, kl: 1.35, hr: -1.5, kr: 1.35, hx: -.05, hy: 0, hz: 0, lean: .05, y: -.4 },
  sitWatch: { lx: -.5, lz: -.1, le: -1.3, rx: -.5, rz: .1, re: -1.3, hl: -1.5, kl: 1.35, hr: -1.5, kr: 1.35, hx: .25, hy: .4, hz: 0, lean: .15, y: -.4 },
  thumbs: { lx: -1.25, lz: -.5, le: -2.1, rx: -.5, rz: -1.1, re: -1.6, hl: -1.5, kl: 1.35, hr: -1.5, kr: 1.35, hx: -.15, hy: 0, hz: .08, lean: 0, y: -.4 },
};
export function mixPose(a, b, t) { const o = {}; for (const k of new Set([...Object.keys(a), ...Object.keys(b)])) o[k] = lerp(a[k] ?? 0, b[k] ?? 0, t); return o; }
const _down = new THREE.Vector3(0, -1, 0), _q = new THREE.Quaternion(), _qe = new THREE.Quaternion(), _d = new THREE.Vector3();
export function applyPose(mk, p) {
  mk.armL.sh.rotation.set(p.lx, 0, p.lz); mk.armL.el.rotation.x = p.le;
  mk.armR.sh.rotation.set(p.rx, 0, p.rz); mk.armR.el.rotation.x = p.re;
  const ik = p.ik || 0;
  if (ik > 0) for (const [a, s] of [[mk.armL, 1], [mk.armR, -1]]) {
    // mão vai até a frente dos olhos (coordenadas do quadril)
    _d.set(s * .1 - s * .38, 1.17 - .62, .62).normalize(); _q.setFromUnitVectors(_down, _d);
    _qe.copy(a.sh.quaternion); a.sh.quaternion.slerpQuaternions(_qe, _q, ik); a.el.rotation.x = lerp(a.el.rotation.x, -.15, ik);
  }
  mk.legL.hp.rotation.x = p.hl; mk.legL.kn.rotation.x = p.kl; mk.legR.hp.rotation.x = p.hr; mk.legR.kn.rotation.x = p.kr;
  mk.head.rotation.set(p.hx, p.hy, p.hz); mk.hips.rotation.x = p.lean; mk.hips.position.y = .78 + p.y;
}
