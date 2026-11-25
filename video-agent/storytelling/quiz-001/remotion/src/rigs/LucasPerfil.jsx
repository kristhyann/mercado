import React from 'react';
import {INK} from '../kit.jsx';
import {LUCAS as L, EXPR} from './lucas.js';
import {blinkAt} from './LucasBusto.jsx';

const SW = 6;
const rad = (a) => (a * Math.PI) / 180;
// absolute angle from straight down, + = forward (to the right)
const dn = (a, len) => [Math.sin(rad(a)) * len, Math.cos(rad(a)) * len];
// torso angle from straight up, + = lean forward
const up = (a, len) => [Math.sin(rad(a)) * len, -Math.cos(rad(a)) * len];
const seg = (len, w, w2 = w) => `M${-w / 2} 0 Q${-w / 2} ${-w / 2} 0 ${-w / 2} Q${w / 2} ${-w / 2} ${w / 2} 0 L${w2 / 2} ${len} Q${w2 / 2} ${len + w2 / 2} 0 ${len + w2 / 2} Q${-w2 / 2} ${len + w2 / 2} ${-w2 / 2} ${len}Z`;

export const DIM = {torso: 500, neck: 50, thigh: 390, shin: 370, upper: 290, fore: 270};

// gait cycles -> pose
export const runPose = (ph, k = 1) => {
  const s = Math.sin(ph), c = Math.cos(ph);
  const leg = (p) => {
    const sp = Math.sin(p), cp = Math.cos(p);
    const thigh = 38 * sp + 8;
    const shin = thigh - (25 + 75 * Math.max(0, -cp)) * 1 - 10 * Math.max(0, sp);
    return [thigh, shin];
  };
  const [tF, sF] = leg(ph), [tB, sB] = leg(ph + Math.PI);
  return {torso: 12 * k, head: -6, thighF: tF * k, shinF: sF * k, thighB: tB * k, shinB: sB * k,
    armF: -40 * s * k, foreF: -40 * s * k + 85, armB: 40 * s * k, foreB: 40 * s * k + 85, bob: -Math.abs(c) * 26 * k, footF: 0, footB: 0};
};
export const walkPose = (ph) => {
  const s = Math.sin(ph);
  const leg = (p) => {const sp = Math.sin(p), cp = Math.cos(p); const th = 22 * sp; return [th, th - 6 - 30 * Math.max(0, -cp)];};
  const [tF, sF] = leg(ph), [tB, sB] = leg(ph + Math.PI);
  return {torso: 3, head: 0, thighF: tF, shinF: sF, thighB: tB, shinB: sB, armF: -18 * s, foreF: -18 * s + 18, armB: 18 * s, foreB: 18 * s + 18, bob: -Math.abs(Math.cos(ph)) * 10};
};
export const standPose = {torso: 0, head: 0, thighF: 3, shinF: 2, thighB: -3, shinB: -2, armF: 4, foreF: 10, armB: -4, foreB: 6, bob: 0};

const HeadProfile = ({E, t, light, look = 0}) => {
  const bl = blinkAt(t, 2);
  const lid = Math.min(1, E.lid + bl);
  const sm = E.smile * 10;
  // head local: origin at neck top; face to the right
  return (
    <g>
      {/* skull + face profile */}
      <path d="M-70 10 Q-128 -40 -118 -140 Q-104 -238 -6 -248 Q86 -252 108 -170 Q114 -146 112 -124 Q140 -92 132 -84 Q116 -78 112 -74 Q118 -58 110 -48 Q120 -40 104 -32 Q106 -6 86 2 Q40 16 10 26 Q-20 32 -40 30Z"
        fill={L.skin} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
      <path d="M-70 10 Q-128 -40 -118 -140 Q-112 -190 -80 -220 Q-40 -120 -20 30 Q-40 30 -70 10Z" fill={L.skinShade} opacity="0.65" />
      <path d="M100 -170 Q114 -146 112 -124 Q140 -92 132 -84" stroke={light.color} strokeWidth="8" fill="none" opacity={light.rim} strokeLinecap="round" />
      {/* stubble */}
      <path d="M10 26 Q40 16 86 2 Q106 -6 104 -32 Q80 -20 40 -40 Q10 -30 -30 10Z" fill={L.hair} opacity="0.18" />
      {/* ear */}
      <path d="M-34 -118 Q-66 -126 -64 -86 Q-62 -54 -30 -60" fill={L.skin} stroke={INK} strokeWidth={SW - 1} />
      <path d="M-40 -104 Q-54 -94 -44 -74" stroke={INK} strokeWidth="3.5" fill="none" opacity="0.6" />
      {/* eye */}
      <g transform="translate(70 -128)">
        <path d="M-14 0 Q2 -14 22 -4 Q10 10 -14 0Z" fill={L.eyeWhite} />
        <circle cx={8 + look * 4} cy="-2" r="8" fill={L.iris} />
        <circle cx={10 + look * 4} cy="-5" r="2.5" fill="#fff" />
        <path d={`M-16 ${-12 + lid * 12} Q4 ${-20 + lid * 16} 24 ${-6 + lid * 6} L24 -24 L-16 -24Z`} fill={L.skin} />
        <path d={`M-16 ${-2 + lid * 4} Q4 ${-16 + lid * 16} 24 ${-4 + lid * 4}`} stroke={INK} strokeWidth="5" fill="none" strokeLinecap="round" />
      </g>
      {/* brow */}
      <path d={`M48 ${-160 - E.brow * 10 + Math.max(0, E.browIn) * 4} Q72 ${-170 - E.brow * 10} 100 ${-158 - E.brow * 10 + E.browIn * 10}`} stroke={L.hair} strokeWidth="11" fill="none" strokeLinecap="round" />
      {/* mouth */}
      <path d={`M${92 - E.open * 4} -46 Q100 ${-44 + sm} 106 ${-48 - sm * 0.6}`} stroke={INK} strokeWidth="4.5" fill="none" strokeLinecap="round" />
      {E.open > 0.2 && <path d="M96 -44 Q104 -36 106 -46" fill="#3B1612" stroke={INK} strokeWidth="3" />}
      {/* hair */}
      <path d="M-112 -150 Q-120 -220 -60 -250 Q-10 -276 50 -262 Q100 -256 112 -196 Q100 -206 80 -200 Q40 -214 10 -204 Q-30 -196 -50 -180 Q-60 -150 -62 -128 Q-80 -110 -112 -110Z"
        fill={L.hair} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
      <path d="M-112 -110 Q-118 -60 -96 -36 L-80 -60 Q-90 -90 -76 -112Z" fill={L.hairFade} opacity="0.85" />
      {[-80, -40, 0, 40, 76].map((x, i) => <path key={x} d={`M${x} ${-236 - (i % 2) * 10} q10 -8 20 0`} stroke="#4A3A32" strokeWidth="4" fill="none" opacity="0.7" />)}
      <path d="M-20 -262 Q60 -266 104 -210" stroke={light.color} strokeWidth="7" fill="none" opacity={light.rim * 0.7} strokeLinecap="round" />
    </g>
  );
};

const Shoe = ({shade}) => (
  <g>
    <path d="M-40 -18 Q-44 30 -36 40 L118 40 Q126 20 100 8 Q60 -2 40 -26Z" fill={L.shoe} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
    <path d="M-38 30 L122 30" stroke={INK} strokeWidth="4" />
    <path d="M-38 30 L118 30 L118 40 L-36 40Z" fill={L.shoeShade} />
    <path d="M10 0 Q40 14 70 6" stroke={L.shoeStripe} strokeWidth="9" fill="none" strokeLinecap="round" />
    {shade && <path d="M-40 -18 Q-44 30 -36 40 L118 40 Q126 20 100 8 Q60 -2 40 -26Z" fill={INK} opacity={shade} />}
  </g>
);

/*
 LucasPerfil: origin = hip joint. Faces right.
 props: t, pose, outfit 'treino' | 'prova' | 'polo', expr, light, carry ('box'), bag
*/
export const LucasPerfil = ({t = 0, pose = standPose, outfit = 'treino', expr = EXPR.neutro, light = {color: '#FFE1A3', rim: 0.7}, carry = null, look = 0, sweat = 0}) => {
  const E = typeof expr === 'string' ? EXPR[expr] : expr;
  const P = pose;
  const shirt = outfit === 'polo' ? L.polo : L.tee, shirtShade = outfit === 'polo' ? L.poloShade : L.teeShade;
  const pants = outfit === 'treino' ? L.shorts : L.jeans, pantsShade = outfit === 'treino' ? L.shortsShade : L.jeansShade;
  const shortLeg = outfit === 'treino';
  const [nx, ny] = up(P.torso, DIM.torso); // neck base
  const shX = nx * 0.93, shY = ny * 0.93; // shoulder
  const breath = Math.sin(t * 1.7) * 3;

  const Leg = ({th, sh, back}) => {
    const [kx, ky] = dn(th, DIM.thigh);
    const dim = back ? 0.32 : 0;
    return (
      <g>
        <g transform={`rotate(${-th})`}>
          <path d={seg(DIM.thigh, 128, 100)} fill={shortLeg ? L.skin : pants} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
          {shortLeg && <path d="M-70 -50 L70 -50 L62 200 Q0 214 -62 200Z" fill={pants} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />}
          <path d={`M10 -40 L64 -40 L50 ${DIM.thigh} L14 ${DIM.thigh}Z`} fill={INK} opacity="0.18" />
          {dim > 0 && <path d={seg(DIM.thigh, 128, 100)} fill={INK} opacity={dim} />}
        </g>
        <g transform={`translate(${kx} ${ky}) rotate(${-sh})`}>
          <path d={seg(DIM.shin, 100, 74)} fill={shortLeg ? L.skin : pants} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
          <path d={`M8 0 L48 0 L36 ${DIM.shin} L10 ${DIM.shin}Z`} fill={INK} opacity="0.16" />
          {shortLeg && <path d="M-40 300 L40 300 L38 360 L-38 360Z" fill="#E9E6DF" stroke={INK} strokeWidth="4" />}
          {dim > 0 && <path d={seg(DIM.shin, 100, 74)} fill={INK} opacity={dim} />}
          <g transform={`translate(0 ${DIM.shin + 4}) rotate(${sh})`}><g transform={`rotate(${-(P.foot || 0)})`}><Shoe shade={dim} /></g></g>
        </g>
      </g>
    );
  };
  const Arm = ({a1, a2, back}) => {
    const [ex, ey] = dn(a1, DIM.upper);
    const dim = back ? 0.32 : 0;
    return (
      <g transform={`translate(${shX} ${shY})`}>
        <g transform={`rotate(${-a1})`}>
          <path d={seg(DIM.upper, 104, 86)} fill={L.skin} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
          <path d="M-64 -48 Q0 -70 64 -48 L62 130 Q0 148 -62 130Z" fill={shirt} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
          <path d="M10 -56 Q56 -44 54 130 Q36 140 18 142Z" fill={shirtShade} opacity="0.8" />
          {dim > 0 && <path d={seg(DIM.upper, 104, 86)} fill={INK} opacity={dim} />}
        </g>
        <g transform={`translate(${ex} ${ey}) rotate(${-a2})`}>
          <path d={seg(DIM.fore, 86, 70)} fill={L.skin} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
          <path d={`M6 0 L36 0 L28 ${DIM.fore} L8 ${DIM.fore}Z`} fill={INK} opacity="0.16" />
          <g transform={`translate(0 ${DIM.fore + 10})`}>
            <path d="M-30 -10 Q-36 34 -14 50 Q12 58 28 40 Q38 14 30 -10 Q0 -20 -30 -10Z" fill={L.skin} stroke={INK} strokeWidth={SW - 1} />
          </g>
          {dim > 0 && <path d={seg(DIM.fore, 86, 70)} fill={INK} opacity={dim} />}
        </g>
      </g>
    );
  };

  const torsoPath = `M-96 30 Q-118 -200 -108 -420 Q-98 -514 6 -520 Q104 -516 122 -430 Q146 -330 124 -220 Q110 -100 98 30 Q0 50 -96 30Z`;
  return (
    <g transform={`translate(0 ${P.bob || 0})`}>
      {/* back limbs */}
      <Arm a1={P.armB} a2={P.foreB} back />
      <Leg th={P.thighB} sh={P.shinB} back />
      {/* torso */}
      <g transform={`rotate(${P.torso})`}>
        {outfit === 'prova' && (
          <g>
            <path d="M-210 -440 Q-230 -300 -200 -110 Q-150 -80 -96 -100 L-90 -450 Q-150 -470 -210 -440Z" fill={L.bag} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
            <path d="M-200 -300 L-100 -300" stroke={INK} strokeWidth="5" />
            <path d="M-170 -300 L-170 -260" stroke="#C9CFDB" strokeWidth="6" />
            <path d="M-210 -440 Q-230 -300 -200 -110 Q-180 -100 -170 -104 Q-190 -300 -170 -452Z" fill={L.bagShade} />
          </g>
        )}
        <path d={`M-70 20 L-74 -40 L84 -40 L80 20 Q0 40 -70 20Z`} fill={pants} stroke={INK} strokeWidth={SW} />
        <g transform={`scale(1 ${1 + breath * 0.002})`}>
          <path d={torsoPath} fill={shirt} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
          <path d="M-96 30 Q-118 -200 -108 -420 Q-98 -514 -30 -518 Q-56 -260 -24 42 Q-70 40 -96 30Z" fill={shirtShade} />
          <path d="M96 -440 Q134 -320 112 -160" stroke={light.color} strokeWidth="10" fill="none" opacity={light.rim * 0.7} strokeLinecap="round" />
          <path d="M-20 -200 Q20 -170 30 -120" stroke={INK} strokeWidth="3.5" fill="none" opacity="0.3" />
          {sweat > 0 && <ellipse cx="10" cy="-330" rx="50" ry="90" fill={shirtShade} opacity={sweat * 0.6} filter="url(#blur8)" />}
          {outfit === 'prova' && <path d="M-60 -470 Q-80 -300 -64 -150" stroke={L.bagShade} strokeWidth="22" fill="none" strokeLinecap="round" />}
        </g>
        {/* neck + head */}
        <g transform={`translate(0 -500)`}>
          <path d="M-36 20 L-40 -60 L40 -60 L44 20Z" fill={L.skin} stroke={INK} strokeWidth={SW} />
          <path d="M-36 20 L-40 -60 L0 -60 L-4 20Z" fill={L.skinShade} opacity="0.6" />
          <g transform={`translate(4 -40) rotate(${(P.head || 0) - P.torso * 0.6})`}>
            <HeadProfile E={E} t={t} light={light} look={look} />
            {sweat > 0 && <path d="M40 -180 q-8 18 0 24 q8 -6 0 -24Z" fill="#D9F0FF" stroke={INK} strokeWidth="3" opacity={sweat} />}
          </g>
        </g>
      </g>
      {/* front limbs */}
      <Leg th={P.thighF} sh={P.shinF} />
      {carry === 'box' && (
        <g transform={`translate(${shX + 120} ${shY + 200}) rotate(${P.torso * 0.3})`}>
          <rect x="-150" y="-130" width="300" height="230" fill="#C89A62" stroke={INK} strokeWidth={SW} />
          <rect x="-150" y="-130" width="300" height="40" fill="#A97E4C" stroke={INK} strokeWidth="4" />
          <rect x="-30" y="-130" width="60" height="230" fill="#E0C79C" opacity="0.7" />
          <path d="M60 -10 L120 -10 M60 14 L104 14" stroke={INK} strokeWidth="5" opacity="0.6" />
          <path d="M-150 -130 L-150 100 L-110 100 L-110 -130Z" fill={INK} opacity="0.2" />
        </g>
      )}
      <Arm a1={P.armF} a2={P.foreF} />
    </g>
  );
};
