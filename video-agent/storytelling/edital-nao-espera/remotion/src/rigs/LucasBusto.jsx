import React from 'react';
import {INK} from '../kit.jsx';
import {LUCAS, EXPR} from './lucas.js';

const SW = 7; // ink line weight

// limb segment pointing down from (0,0), length len, width w, rounded
const seg = (len, w, w2 = w) => `M${-w / 2} 0 Q${-w / 2} ${-w / 2} 0 ${-w / 2} Q${w / 2} ${-w / 2} ${w / 2} 0 L${w2 / 2} ${len} Q${w2 / 2} ${len + w2 / 2} 0 ${len + w2 / 2} Q${-w2 / 2} ${len + w2 / 2} ${-w2 / 2} ${len}Z`;
const end = (a, len) => [Math.sin((a * Math.PI) / 180) * len, Math.cos((a * Math.PI) / 180) * len];

// auto blink, deterministic
export const blinkAt = (t, seed = 0) => {
  const period = 3.1 + (seed % 3) * 0.4;
  const p = (t + seed * 0.77) % period;
  return p < 0.07 ? p / 0.07 : p < 0.16 ? 1 - (p - 0.07) / 0.09 : 0;
};

const Hand = ({fist = 0, side = 1, shade, L}) => (
  <g>
    <path d="M-34 -6 Q-40 40 -20 62 Q0 74 22 62 Q40 44 34 -6 Q0 -18 -34 -6Z" fill={L.skin} stroke={INK} strokeWidth={SW - 1} strokeLinejoin="round" />
    <path d={`M${side * 30} 8 Q${side * 56} 22 ${side * 48} 44 Q${side * 40} 50 ${side * 30} 38`} fill={L.skin} stroke={INK} strokeWidth={SW - 2} strokeLinejoin="round" />
    {!fist && [-16, 0, 16].map((x) => <path key={x} d={`M${x} 46 L${x} 66`} stroke={INK} strokeWidth="3" opacity="0.5" />)}
    <path d="M-34 -6 Q-40 40 -20 62 Q-8 68 0 68 Q-22 40 -18 -10Z" fill={shade} opacity="0.5" />
  </g>
);

const Arm = ({sx, sy, a1, a2, sleeve, sleeveShade, side, prop, handFist, L}) => {
  const U = 230, F = 215;
  const [ex, ey] = end(a1, U);
  return (
    <g transform={`translate(${sx} ${sy})`}>
      <g transform={`rotate(${-a1})`}>
        <path d={seg(U, 112, 92)} fill={L.skin} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
        <path d={seg(U, 112, 92)} fill={L.skinShade} opacity="0.35" clipPath="none" transform={`translate(${side * 22} 0) scale(0.6 1)`} />
        {/* sleeve */}
        <path d={`M-60 -48 Q0 -70 60 -48 L64 120 Q0 140 -64 120Z`} fill={sleeve} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
        <path d={`M${side * 10} -60 Q${side * 62} -50 ${side * 64} 120 Q${side * 40} 132 ${side * 18} 136Z`} fill={sleeveShade} opacity="0.85" />
      </g>
      <g transform={`translate(${ex} ${ey}) rotate(${-a2})`}>
        <path d={seg(F, 90, 74)} fill={L.skin} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
        <path d={`M${side * 8} 0 L${side * 40} 0 L${side * 34} ${F} L${side * 10} ${F}Z`} fill={L.skinShade} opacity="0.45" />
        <g transform={`translate(0 ${F + 8})`}>
          {prop === 'phone' && <Phone />}
          <Hand side={side} fist={handFist} shade={L.skinShade} L={L} />
        </g>
      </g>
    </g>
  );
};

const Phone = () => (
  <g transform="translate(0 40) rotate(180)">
    <rect x="-52" y="-96" width="104" height="192" rx="16" fill="#151821" stroke={INK} strokeWidth={SW} />
  </g>
);

/*
 LucasBusto: origin = base of the neck. Head center at (0,-235).
 props: t, expr (obj), turn (-1..1), tilt (deg), look {x,y} (-1..1), nod (px, + = looking down),
 outfit 'polo'|'tee', light {side:1|-1, color, rim}, under {color, k} (light from below, e.g. phone),
 arms {l:[a1,a2,prop], r:[a1,a2,prop]} or null, sweat (0..1), blink (0..1 forced), shoulders (px drop)
*/
export const LucasBusto = ({t = 0, expr = EXPR.neutro, turn = 0, tilt = 0, look = {x: 0, y: 0}, nod = 0, outfit = 'polo', light = {side: 1, color: '#FFE1A3', rim: 0.8}, under = null, arms = null, sweat = 0, blink: forcedBlink = 0, shoulders = 0, armsBehind = false, id = 'lb', tears = 0, pal = null, hair = 'crespo'}) => {
  const L = pal ? {...LUCAS, ...pal} : LUCAS;
  const E = typeof expr === 'string' ? EXPR[expr] : expr;
  const breath = Math.sin(t * 1.7) * 6;
  const bl = Math.max(blinkAt(t, 1), forcedBlink);
  const ft = turn * 40; // feature shift
  const side = light.side;
  const shirt = outfit === 'polo' ? L.polo : L.tee, shirtShade = outfit === 'polo' ? L.poloShade : L.teeShade, shirtLight = outfit === 'polo' ? L.poloLight : L.teeLight;
  const sh = shoulders;
  const torso = `M-410 760 L-390 ${150 + sh} Q-370 ${40 + sh} -190 ${10 + sh} L-70 -10 L70 -10 L190 ${10 + sh} Q370 ${40 + sh} 390 ${150 + sh} L410 760Z`;
  const face = `M-140 -50 Q-148 70 -100 140 Q-50 196 ${ft * 0.15} 200 Q50 196 100 140 Q148 70 140 -50 Q132 -178 0 -186 Q-132 -178 -140 -50Z`;
  const lidY = (k) => -18 + Math.min(1, k) * 36;
  const eye = (cx, far) => {
    const sx = far ? 1 - Math.abs(turn) * 0.28 : 1;
    const lid = Math.min(1, E.lid + bl);
    return (
      <g transform={`translate(${cx} ${-8 + nod * 0.5}) scale(${sx} 1)`}>
        <clipPath id={`${id}eye${cx}`}><path d="M-34 0 Q-16 -22 4 -21 Q28 -18 36 2 Q14 18 -6 17 Q-26 14 -34 0Z" /></clipPath>
        <path d="M-34 0 Q-16 -22 4 -21 Q28 -18 36 2 Q14 18 -6 17 Q-26 14 -34 0Z" fill={L.eyeWhite} />
        <g clipPath={`url(#${id}eye${cx})`}>
          <circle cx={look.x * 13 + turn * 6} cy={look.y * 7 + 1} r="15" fill={L.iris} />
          <circle cx={look.x * 13 + turn * 6} cy={look.y * 7 + 1} r="7" fill="#0C0806" />
          <circle cx={look.x * 13 + turn * 6 + 5} cy={look.y * 7 - 5} r="4.5" fill="#fff" />
          {under && <circle cx={look.x * 13 + turn * 6 - 4} cy={look.y * 7 + 6} r="3" fill={under.color} opacity={under.k} />}
          {/* upper lid */}
          <rect x="-40" y={-40} width="80" height={22 + lidY(lid) + 18} fill={L.skin} />
          <rect x="-40" y={-40} width="80" height={22 + lidY(lid) + 18} fill={L.skinShade} opacity="0.3" />
          <path d="M-34 0 Q-16 -22 4 -21 Q28 -18 36 2" fill="none" stroke={INK} strokeWidth="2" opacity={0} />
        </g>
        {/* lid line */}
        <path d={`M-36 ${Math.max(-20, lidY(lid) - 2) * 0.2} Q0 ${lidY(lid) - 6} 38 ${lidY(lid) * 0.2 + 2}`} fill="none" stroke={INK} strokeWidth="6" strokeLinecap="round" />
        <path d="M-30 6 Q-6 22 30 8" fill="none" stroke={INK} strokeWidth="2.5" opacity="0.45" />
        {E.lid > 0.25 && <path d="M-26 22 Q0 32 26 22" fill="none" stroke={L.skinShade} strokeWidth="4" opacity={Math.min(1, (E.lid - 0.25) * 3)} />}
      </g>
    );
  };
  const brow = (cx, s) => {
    const inner = -E.browIn * 14; // inner end vertical offset (neg = up)
    const y = -62 - E.brow * 16 + nod * 0.5;
    return (
      <g transform={`translate(${cx} ${y})`}>
        <path d={`M${-s * 44} ${inner} Q${-s * 4} ${-10 + inner * 0.4} ${s * 46} ${6 - inner * 0.3}`} fill="none" stroke={L.hair} strokeWidth="15" strokeLinecap="round"
          transform={s > 0 ? '' : ''} />
      </g>
    );
  };
  // mouth
  const my = 108 + nod * 0.6, mx = ft * 1.15;
  const cv = E.smile * 22;
  const mouthW = 40 - E.open * 6;
  const mouth = E.open > 0.05 ? (
    <g transform={`translate(${mx} ${my})`}>
      <path d={`M${-mouthW} 0 Q0 ${cv - 6} ${mouthW} 0 Q0 ${cv + 10 + E.open * 30} ${-mouthW} 0Z`} fill="#3B1612" stroke={INK} strokeWidth="5" strokeLinejoin="round" />
      <path d={`M${-mouthW * 0.6} ${cv * 0.3 + 2} Q0 ${cv * 0.3 + 6} ${mouthW * 0.6} ${cv * 0.3 + 2}`} stroke="#fff" strokeWidth="5" opacity="0.6" fill="none" />
    </g>
  ) : (
    <g transform={`translate(${mx} ${my})`}>
      <path d={`M${-mouthW} ${-cv * 0.15} Q0 ${cv} ${mouthW} ${-cv * 0.15}`} fill="none" stroke={INK} strokeWidth="6" strokeLinecap="round" />
      <path d={`M${-mouthW * 0.5} ${14 + cv * 0.4} Q0 ${20 + cv * 0.4} ${mouthW * 0.5} ${14 + cv * 0.4}`} fill="none" stroke={L.lip} strokeWidth="5" strokeLinecap="round" opacity="0.7" />
      {E.smile > 0.3 && <path d={`M${mouthW + 2} ${-cv * 0.2 - 4} q8 -4 10 -12`} stroke={INK} strokeWidth="4" fill="none" strokeLinecap="round" opacity="0.6" />}
    </g>
  );

  const lightCol = light.color;
  return (
    <g>
      <defs>
        <clipPath id={`${id}face`}><path d={face} /></clipPath>
        <clipPath id={`${id}torso`}><path d={torso} /></clipPath>
        <clipPath id={`${id}half`}><path d={side > 0 ? 'M60 -260 L260 -260 L260 260 L40 260 Q120 40 60 -260Z' : 'M-60 -260 L-260 -260 L-260 260 L-40 260 Q-120 40 -60 -260Z'} /></clipPath>
        <radialGradient id={`${id}under`} cx="50%" cy="100%" r="80%">
          <stop offset="0" stopColor={under ? under.color : '#fff'} stopOpacity="1" />
          <stop offset="1" stopColor={under ? under.color : '#fff'} stopOpacity="0" />
        </radialGradient>
      </defs>

      {armsBehind && arms && arms.l && <Arm sx={-300} sy={110 + sh} a1={arms.l[0]} a2={arms.l[1]} prop={arms.l[2]} handFist={arms.l[3]} sleeve={shirt} sleeveShade={shirtShade} side={-1} L={L} />}

      {/* torso */}
      <g transform={`translate(0 ${breath * 0.3}) scale(1 ${1 + breath * 0.0012})`}>
        <path d={torso} fill={shirt} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
        <g clipPath={`url(#${id}torso)`}>
          <path d={`M${-side * 60} -40 Q${-side * 140} 300 ${-side * 90} 800 L${-side * 500} 800 L${-side * 500} -40Z`} fill={shirtShade} />
          <rect x={-side * 500} y="-40" width="500" height="900" fill="url(#hatch)" opacity="0.5" transform={side > 0 ? '' : 'translate(500 0)'} />
          <path d={`M${side * 200} 30 Q${side * 380} 60 ${side * 395} 200`} stroke={lightCol} strokeWidth="18" fill="none" opacity={light.rim * 0.6} />
          {/* folds */}
          <path d="M-120 420 Q-60 470 -20 560" stroke={INK} strokeWidth="4" fill="none" opacity="0.35" />
          <path d="M150 380 Q110 470 130 600" stroke={INK} strokeWidth="4" fill="none" opacity="0.3" />
          {under && <ellipse cx="0" cy="300" rx="420" ry="360" fill={under.color} opacity={under.k * 0.28} style={{mixBlendMode: 'screen'}} />}
        </g>
        {/* neck */}
        <path d="M-62 -120 L-66 30 Q0 70 66 30 L62 -120Z" fill={L.skin} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
        <path d="M-62 -120 L-66 30 Q0 70 66 30 L62 -60 Q0 -10 -62 -60Z" fill={L.skinShade} opacity="0.6" />
        {outfit === 'polo' ? (
          <g>
            <path d="M-88 -6 L-6 70 L-30 120 L-150 20Z" fill={shirt} stroke={INK} strokeWidth={SW - 1} strokeLinejoin="round" />
            <path d="M88 -6 L6 70 L30 120 L150 20Z" fill={shirt} stroke={INK} strokeWidth={SW - 1} strokeLinejoin="round" />
            <path d="M-88 -6 L-150 20 M88 -6 L150 20" stroke={L.collarTrim} strokeWidth="6" />
            <path d="M-20 70 L-20 250 L20 250 L20 70" fill="none" stroke={INK} strokeWidth="5" />
            <circle cx="0" cy="130" r="8" fill={L.collarTrim} stroke={INK} strokeWidth="3" />
            <circle cx="0" cy="200" r="8" fill={L.collarTrim} stroke={INK} strokeWidth="3" />
            <rect x="150" y="190" width="92" height="56" rx="8" fill="#F4F1EA" stroke={INK} strokeWidth="5" />
            <path d="M166 210 L226 210 M166 226 L206 226" stroke={L.polo} strokeWidth="6" strokeLinecap="round" />
          </g>
        ) : (
          <path d="M-96 0 Q0 90 96 0" fill="none" stroke={L.teeShade} strokeWidth="22" />
        )}
        {outfit !== 'polo' && <path d="M-100 -6 Q0 96 100 -6" fill="none" stroke={INK} strokeWidth={SW - 1} />}
        {sweat > 0 && <path d="M-200 40 Q-150 140 -160 300" stroke={shirtShade} strokeWidth="40" opacity={sweat * 0.5} fill="none" filter="url(#blur8)" />}
      </g>

      {/* head */}
      <g transform={`translate(${turn * 6} ${-235 + breath * 0.5}) rotate(${tilt})`}>
        {/* ears */}
        {turn < 0.55 && <g transform={`translate(${-140 + turn * 18} 10)`}><path d="M6 -40 Q-36 -46 -30 6 Q-26 44 8 40" fill={L.skin} stroke={INK} strokeWidth={SW - 1} /><path d="M-2 -20 Q-18 -10 -10 16" stroke={INK} strokeWidth="4" fill="none" opacity="0.6" /></g>}
        {turn > -0.55 && <g transform={`translate(${140 + turn * 18} 10) scale(-1 1)`}><path d="M6 -40 Q-36 -46 -30 6 Q-26 44 8 40" fill={L.skin} stroke={INK} strokeWidth={SW - 1} /><path d="M-2 -20 Q-18 -10 -10 16" stroke={INK} strokeWidth="4" fill="none" opacity="0.6" /></g>}
        <path d={face} fill={L.skin} />
        <g clipPath={`url(#${id}face)`}>
          {/* cel shadow, away from light */}
          <ellipse cx={-side * 175 + ft * 0.6} cy="40" rx="150" ry="260" fill={L.skinShade} opacity="0.75" />
          <ellipse cx={-side * 175 + ft * 0.6} cy="40" rx="150" ry="260" fill="url(#halftoneFine)" />
          {/* under-eye/brow socket shade */}
          <ellipse cx={ft} cy="-40" rx="150" ry="40" fill={L.skinShade} opacity="0.22" />
          {/* stubble */}
          <path d={`M-120 70 Q-80 190 ${ft * 0.15} 200 Q80 190 120 70 Q100 130 ${ft + 60} 120 Q${ft} 80 ${ft - 60} 120 Q-100 130 -120 70Z`} fill={L.hair} opacity={L.stubble ?? 0.2} />
          <path d={`M${ft - 46} 86 Q${ft} 74 ${ft + 46} 86 L${ft + 40} 94 Q${ft} 84 ${ft - 40} 94Z`} fill={L.hair} opacity="0.14" filter="url(#blur2)" />
          {under && <rect x="-200" y="-200" width="400" height="420" fill={`url(#${id}under)`} opacity={under.k * 0.75} style={{mixBlendMode: 'screen'}} />}
          {/* rim light on the lit side only */}
          <g clipPath={`url(#${id}half)`}>
            <path d={face} fill="none" stroke={lightCol} strokeWidth="26" opacity={light.rim} />
          </g>
        </g>
        <path d={face} fill="none" stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
        {/* nose */}
        <g transform={`translate(${ft * 1.35} ${42 + nod * 0.6})`}>
          <path d={`M${-side * 4} -40 Q${-side * 2} 0 ${-side * 18} 16`} fill="none" stroke={L.skinShade} strokeWidth="7" strokeLinecap="round" opacity="0.8" />
          <path d="M-22 14 Q-12 26 0 22 Q12 26 22 14" fill="none" stroke={INK} strokeWidth="5" strokeLinecap="round" />
          <ellipse cx="-10" cy="16" rx="5" ry="3" fill={INK} opacity="0.7" />
          <ellipse cx="12" cy="16" rx="5" ry="3" fill={INK} opacity="0.7" />
          <ellipse cx={side * 6} cy="-2" rx="6" ry="9" fill={L.skinLight} opacity="0.8" />
        </g>
        {eye(-62 + ft, turn > 0.15)}
        {eye(62 + ft, turn < -0.15)}
        {brow(-62 + ft, -1)}
        {brow(62 + ft, 1)}
        {mouth}
        {tears > 0 && <path d={`M${-58 + ft} 14 Q${-64 + ft} 50 ${-60 + ft} ${14 + tears * 70}`} stroke="#CFE8FF" strokeWidth="6" fill="none" opacity="0.8" strokeLinecap="round" />}
        {sweat > 0 && <g opacity={sweat}><path d={`M${108 + ft * 0.5} -70 q-10 22 0 30 q10 -8 0 -30Z`} fill="#D9F0FF" stroke={INK} strokeWidth="3" /><path d={`M${-118 + ft * 0.5} -20 q-8 18 0 24 q8 -6 0 -24Z`} fill="#D9F0FF" stroke={INK} strokeWidth="3" /></g>}
        {/* hair: faded sides + curly top */}
        <path d="M-142 -40 Q-150 -120 -120 -150 L-108 -60 Q-120 -50 -142 -40Z" fill={L.hairFade} opacity="0.9" />
        <path d="M142 -40 Q150 -120 120 -150 L108 -60 Q120 -50 142 -40Z" fill={L.hairFade} opacity="0.9" />
        {hair === 'liso' ? (
          <g>
            <path d={`M-150 -40 Q-160 -170 -80 -214 Q0 -244 90 -210 Q156 -176 150 -40 Q140 -90 120 -110 L110 -60 Q96 -120 60 -128 Q${30 + ft * 0.3} -86 ${ft * 0.3 - 10} -70 Q-10 -110 -40 -120 Q-60 -80 -100 -66 Q-96 -110 -112 -116 Q-134 -90 -150 -40Z`} fill={L.hair} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
            {[-80, -30, 20, 70].map((x) => <path key={x} d={`M${x} -200 Q${x + 14} -160 ${x + 6} -120`} stroke="#5A4232" strokeWidth="5" fill="none" strokeLinecap="round" opacity="0.7" />)}
          </g>
        ) : (<g>
        <path d={`M-128 -96 Q-140 -150 -110 -176 Q-100 -206 -64 -206 Q-44 -230 -12 -220 Q14 -238 40 -222 Q74 -232 92 -206 Q126 -204 130 -170 Q150 -146 132 -96 Q120 -122 96 -124 Q60 -138 ${20 + ft * 0.3} -128 Q-30 -140 -66 -126 Q-108 -126 -128 -96Z`} fill={L.hair} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
        {[-90, -50, -10, 30, 70, 104].map((x, i) => <path key={x} d={`M${x} ${-176 - (i % 2) * 14} q12 -10 24 0`} stroke="#4A3A32" strokeWidth="5" fill="none" strokeLinecap="round" opacity="0.7" />)}
        </g>)}
        <path d={`M${side * 30} -214 Q${side * 96} -210 ${side * 118} -168`} stroke={lightCol} strokeWidth="9" fill="none" opacity={light.rim * 0.7} strokeLinecap="round" />
      </g>

      {!armsBehind && arms && arms.l && <Arm sx={-300} sy={110 + sh} a1={arms.l[0]} a2={arms.l[1]} prop={arms.l[2]} handFist={arms.l[3]} sleeve={shirt} sleeveShade={shirtShade} side={-1} L={L} />}
      {arms && arms.r && <Arm sx={300} sy={110 + sh} a1={arms.r[0]} a2={arms.r[1]} prop={arms.r[2]} handFist={arms.r[3]} sleeve={shirt} sleeveShade={shirtShade} side={1} L={L} />}
    </g>
  );
};
