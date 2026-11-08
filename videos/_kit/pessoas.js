// Personagens humanos low-poly com poses simples + IK de braço
import * as THREE from 'three';
import { M, mesh, lerp, clamp } from '/_kit/kit.js';

export function buildPerson(o) {
  const C = Object.assign({ skin: 0xD9A27A, shirt: 0x2A9D8F, pants: 0x3B5B92, shoes: 0x2b2b2b, hair: 0x2B1A10, hairStyle: 'short', glasses: false, tie: null, tag: false }, o);
  const mSkin = M(C.skin), mShirt = M(C.shirt), mPants = M(C.pants), mShoe = M(C.shoes), mHair = M(C.hair);
  const root = new THREE.Group();
  const hips = new THREE.Group(); hips.position.y = .92; root.add(hips);
  mesh(new THREE.CylinderGeometry(.17, .16, .16, 8), mPants, 0, .02, 0, hips);
  const torso = mesh(new THREE.CylinderGeometry(.21, .17, .56, 8), mShirt, 0, .34, 0, hips); torso.scale.z = .72;
  if (C.tie) { mesh(new THREE.BoxGeometry(.06, .3, .02), M(C.tie), 0, .42, .13, hips); }
  if (C.tag) { mesh(new THREE.BoxGeometry(.09, .05, .02), M(0xffffff), .1, .5, .125, hips); }
  mesh(new THREE.CylinderGeometry(.06, .07, .1, 6), mSkin, 0, .66, 0, hips);
  const neck = new THREE.Group(); neck.position.y = .7; hips.add(neck);
  const head = new THREE.Group(); head.position.y = .15; neck.add(head);
  const hd = mesh(new THREE.IcosahedronGeometry(.16, 1), mSkin, 0, 0, 0, head); hd.scale.set(.95, 1.1, 1);
  mesh(new THREE.IcosahedronGeometry(.035, 0), mSkin, 0, -.02, .16, head);
  for (const s of [-1, 1]) mesh(new THREE.IcosahedronGeometry(.04, 0), mSkin, s * .155, 0, 0, head).scale.set(.5, 1, .8);
  // cabelo
  if (C.hairStyle !== 'bald') {
    const cap = mesh(new THREE.SphereGeometry(.172, 9, 6, 0, Math.PI * 2, 0, Math.PI * .45), mHair, 0, .015, -.01, head); cap.scale.set(.97, 1.12, 1.02); cap.rotation.x = -.2;
    if (C.hairStyle === 'short') { for (let i = -2; i <= 2; i++) { const f = mesh(new THREE.BoxGeometry(.07, .05, .06), mHair, i * .055, .12, .12, head); f.rotation.x = -.5; f.rotation.z = i * .1; } }
    if (C.hairStyle === 'bun') { mesh(new THREE.IcosahedronGeometry(.08, 1), mHair, 0, .12, -.15, head); const back = mesh(new THREE.SphereGeometry(.17, 9, 6, 0, Math.PI * 2, 0, Math.PI * .7), mHair, 0, .02, -.03, head); back.rotation.x = -.6; }
  } else { const r = mesh(new THREE.SphereGeometry(.168, 9, 6, 0, Math.PI * 2, Math.PI * .45, Math.PI * .25), mHair, 0, .0, -.02, head); }
  // rosto
  const eyeM = new THREE.MeshStandardMaterial({ color: 0x1a1a1a, roughness: .3 });
  const eyes = [-1, 1].map(s => mesh(new THREE.IcosahedronGeometry(.022, 1), eyeM, s * .058, .03, .145, head));
  const brows = [-1, 1].map(s => { const b = mesh(new THREE.BoxGeometry(.06, .013, .015), mHair, s * .058, .085, .148, head); return b; });
  const mouthM = new THREE.MeshStandardMaterial({ color: 0x6a2a20 });
  const smile = new THREE.Mesh(new THREE.TorusGeometry(.04, .009, 4, 10, Math.PI), mouthM); smile.position.set(0, -.065, .152); smile.rotation.z = Math.PI; head.add(smile);
  const flat = mesh(new THREE.BoxGeometry(.06, .012, .01), mouthM, 0, -.07, .155, head);
  const open = mesh(new THREE.IcosahedronGeometry(.03, 1), mouthM, 0, -.075, .148, head); open.scale.set(1, 1.1, .4);
  if (C.glasses) { const gm = M(0x222222); for (const s of [-1, 1]) { const g = mesh(new THREE.TorusGeometry(.035, .006, 4, 12), gm, s * .058, .03, .158, head); } mesh(new THREE.BoxGeometry(.05, .006, .006), gm, 0, .035, .16, head); }
  // braços
  const arm = s => {
    const sh = new THREE.Group(); sh.position.set(s * .24, .55, 0); hips.add(sh);
    mesh(new THREE.IcosahedronGeometry(.07, 0), mShirt, 0, 0, 0, sh);
    mesh(new THREE.CylinderGeometry(.058, .055, .3, 6), mShirt, 0, -.15, 0, sh);
    const el = new THREE.Group(); el.position.y = -.3; sh.add(el);
    mesh(new THREE.CylinderGeometry(.045, .05, .27, 6), mSkin, 0, -.135, 0, el);
    const hand = new THREE.Group(); hand.position.y = -.3; el.add(hand);
    mesh(new THREE.IcosahedronGeometry(.052, 1), mSkin, 0, 0, 0, hand).scale.set(.9, 1.15, .7);
    return { sh, el, hand };
  };
  const armL = arm(1), armR = arm(-1);
  const leg = s => {
    const hp = new THREE.Group(); hp.position.set(s * .09, 0, 0); hips.add(hp);
    mesh(new THREE.CylinderGeometry(.075, .065, .45, 6), mPants, 0, -.225, 0, hp);
    const kn = new THREE.Group(); kn.position.y = -.45; hp.add(kn);
    mesh(new THREE.CylinderGeometry(.062, .055, .42, 6), mPants, 0, -.21, 0, kn);
    mesh(new THREE.BoxGeometry(.1, .07, .22), mShoe, 0, -.45, .05, kn);
    return { hp, kn };
  };
  const legL = leg(1), legR = leg(-1);
  return { root, hips, neck, head, eyes, brows, smile, flat, open, armL, armR, legL, legR, mats: { mShirt, mPants } };
}

export const PP = {
  stand: { lx: .05, lz: .12, le: -.15, rx: .05, rz: -.12, re: -.15, hl: 0, kl: 0, hr: 0, kr: 0, hx: 0, hy: 0, hz: 0, lean: 0, y: 0 },
  sit: { lx: -.2, lz: .1, le: -1.0, rx: -.2, rz: -.1, re: -1.0, hl: -1.5, kl: 1.5, hr: -1.5, kr: 1.5, hx: 0, hy: 0, hz: 0, lean: 0, y: -.42 },
  type: { lx: -.6, lz: -.05, le: -.9, rx: -.6, rz: .05, re: -.9, hl: -1.5, kl: 1.5, hr: -1.5, kr: 1.5, hx: .18, hy: 0, hz: 0, lean: .12, y: -.42 },
  sitHead: { lx: -2.5, lz: -.5, le: -2.2, rx: -2.5, rz: .5, re: -2.2, hl: -1.5, kl: 1.5, hr: -1.5, kr: 1.5, hx: .35, hy: 0, hz: 0, lean: .35, y: -.42 },
  sitThink: { lx: -.2, lz: .1, le: -1.0, rx: -1.0, rz: .35, re: -2.3, hl: -1.5, kl: 1.5, hr: -1.5, kr: 1.5, hx: -.12, hy: .2, hz: .1, lean: 0, y: -.42 },
  sitCheer: { lx: -2.9, lz: .4, le: -.4, rx: -2.9, rz: -.4, re: -.4, hl: -1.5, kl: 1.5, hr: -1.5, kr: 1.5, hx: -.2, hy: 0, hz: 0, lean: -.1, y: -.42 },
  sitSlump: { lx: .1, lz: .15, le: -.3, rx: .1, rz: -.15, re: -.3, hl: -1.5, kl: 1.5, hr: -1.5, kr: 1.5, hx: .45, hy: 0, hz: 0, lean: .3, y: -.44 },
  sitCup: { lx: -.5, lz: .0, le: -1.2, rx: -.5, rz: -.0, re: -1.2, hl: -1.5, kl: 1.5, hr: -1.5, kr: 1.5, hx: .25, hy: 0, hz: 0, lean: .15, y: -.42 },
  sitTalk: { lx: -.3, lz: .1, le: -1.4, rx: -.9, rz: -.3, re: -1.1, hl: -1.5, kl: 1.5, hr: -1.5, kr: 1.5, hx: -.05, hy: 0, hz: 0, lean: .05, y: -.42 },
  fold: { lx: -.9, lz: -.05, le: -.6, rx: -.9, rz: .05, re: -.6, hl: 0, kl: 0, hr: 0, kr: 0, hx: .35, hy: 0, hz: 0, lean: .15, y: 0 },
  think: { lx: .05, lz: .12, le: -.15, rx: -1.0, rz: .35, re: -2.3, hl: 0, kl: 0, hr: 0, kr: 0, hx: -.15, hy: .2, hz: .1, lean: 0, y: 0 },
  phone: { lx: .05, lz: .12, le: -.15, rx: -.9, rz: .25, re: -1.6, hl: 0, kl: 0, hr: 0, kr: 0, hx: .4, hy: 0, hz: 0, lean: .05, y: 0 },
  lie: { lx: .1, lz: .25, le: -.2, rx: .1, rz: -.25, re: -.2, hl: 0, kl: 0, hr: 0, kr: 0, hx: -.1, hy: 0, hz: 0, lean: 0, y: 0 },
  lieThink: { lx: -2.6, lz: -.4, le: -2.3, rx: -2.6, rz: .4, re: -2.3, hl: 0, kl: 0, hr: 0, kr: 0, hx: -.1, hy: 0, hz: 0, lean: 0, y: 0 },
  shrug: { lx: .1, lz: .7, le: -1.3, rx: .1, rz: -.7, re: -1.3, hl: 0, kl: 0, hr: 0, kr: 0, hx: 0, hy: 0, hz: .12, lean: 0, y: 0 },
  arms: { lx: -.5, lz: -.6, le: -1.9, rx: -.5, rz: .6, re: -1.9, hl: 0, kl: 0, hr: 0, kr: 0, hx: -.05, hy: 0, hz: 0, lean: -.03, y: 0 },
  sitArms: { lx: -.5, lz: -.6, le: -1.9, rx: -.5, rz: .6, re: -1.9, hl: -1.5, kl: 1.5, hr: -1.5, kr: 1.5, hx: 0, hy: 0, hz: 0, lean: 0, y: -.42 },
  sitDesk: { lx: -.55, lz: -.1, le: -1.0, rx: -.55, rz: .1, re: -1.0, hl: -1.5, kl: 1.5, hr: -1.5, kr: 1.5, hx: 0, hy: 0, hz: 0, lean: .05, y: -.42 },
  cheer: { lx: -2.9, lz: .4, le: -.4, rx: -2.9, rz: -.4, re: -.4, hl: 0, kl: 0, hr: 0, kr: 0, hx: -.2, hy: 0, hz: 0, lean: -.05, y: 0 },
  sitBench: { lx: -.3, lz: .1, le: -.8, rx: -.3, rz: -.1, re: -.8, hl: -1.5, kl: 1.5, hr: -1.5, kr: 1.5, hx: -.1, hy: 0, hz: 0, lean: -.05, y: -.45 },
  point: { lx: .05, lz: .12, le: -.15, rx: -1.5, rz: -.3, re: -.1, hl: 0, kl: 0, hr: 0, kr: 0, hx: 0, hy: -.3, hz: 0, lean: 0, y: 0 },
};
export function mixP(a, b, t) { const o = {}; for (const k of new Set([...Object.keys(a), ...Object.keys(b)])) o[k] = lerp(a[k] ?? 0, b[k] ?? 0, t); return o; }
export function poseP(p, P, walk = 0, t = 0) {
  p.armL.sh.rotation.set(P.lx, 0, P.lz); p.armL.el.rotation.x = P.le;
  p.armR.sh.rotation.set(P.rx, 0, P.rz); p.armR.el.rotation.x = P.re;
  p.legL.hp.rotation.x = P.hl; p.legL.kn.rotation.x = P.kl; p.legR.hp.rotation.x = P.hr; p.legR.kn.rotation.x = P.kr;
  p.head.rotation.set(P.hx, P.hy, P.hz); p.hips.rotation.x = P.lean; p.hips.position.y = .92 + P.y;
  if (walk > 0) {
    const s = Math.sin(t * 7) * .5 * walk;
    p.legL.hp.rotation.x += s; p.legR.hp.rotation.x -= s; p.legL.kn.rotation.x += Math.max(0, -s) * .9; p.legR.kn.rotation.x += Math.max(0, s) * .9;
    p.armL.sh.rotation.x -= s * .7; p.armR.sh.rotation.x += s * .7; p.hips.position.y += Math.abs(Math.cos(t * 7)) * .03 * walk;
  }
}
export function face(p, e, t = 0) {
  const blink = (t % 3.7) > 3.6;
  p.eyes.forEach(x => x.scale.y = blink ? .15 : 1);
  p.smile.visible = e === 'happy' || e === 'calm'; p.smile.scale.set(1, e === 'calm' ? .55 : 1, 1);
  p.flat.visible = e === 'neutral' || e === 'angry' || e === 'sad'; p.flat.rotation.z = 0;
  p.open.visible = e === 'shock' || e === 'talk';
  if (e === 'talk') p.open.scale.y = .4 + Math.abs(Math.sin(t * 11)) * .9; else p.open.scale.y = 1.1;
  const br = { happy: [.08, 0], calm: [.08, 0], neutral: [.085, 0], sad: [.08, -.35], angry: [.075, .35], shock: [.1, 0], talk: [.085, 0] }[e] || [.085, 0];
  p.brows.forEach((b, i) => { b.position.y = br[0]; b.rotation.z = (i ? -1 : 1) * br[1]; });
}
