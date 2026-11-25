import React from 'react';
import {random} from 'remotion';
import {INK, C, W, H, Frame, Finish, Camera, Layer, Glow, Beam, Dust, Rain, kf, useST, lerp, wobble} from '../kit.jsx';
import {LucasBusto} from '../rigs/LucasBusto.jsx';
import {EXPR, mixExpr} from '../rigs/lucas.js';
import {Phone, Lamp, Mug, BookStack, Calendar, Corkboard, RoomWindow, Laptop, DeskClock} from './props.jsx';

// ---------------------------------------------------------------- Room (world layout at 1080x1920)
export const LAMP_HEAD = [126, 1000];
export const CHAR_POS = [560, 1215];
export const CHAR_SCALE = 0.55;

export const RoomBack = ({t, dawnK = 0, crossed = 12, calTear = 0, ripped = 0, rain = true}) => (
  <g>
    <rect x="-600" y="-600" width="2300" height="2200" fill={C.night2} />
    {Array.from({length: 40}).map((_, i) => <rect key={i} x={-600 + i * 60} y="-600" width="22" height="2200" fill="#fff" opacity="0.025" />)}
    <rect x="-600" y="-600" width="2300" height="2200" filter="url(#paperTex)" opacity="0.5" />
    {/* skirting & floor */}
    <rect x="-600" y="1480" width="2300" height="40" fill="#2A3358" stroke={INK} strokeWidth="6" />
    <rect x="-600" y="1520" width="2300" height="1000" fill="#2B2230" />
    {Array.from({length: 14}).map((_, i) => <path key={i} d={`M${-600 + i * 180} 1520 L${-900 + i * 260} 2600`} stroke={INK} strokeWidth="4" opacity="0.35" />)}
    {/* shelf with books */}
    <rect x="60" y="250" width="480" height="26" fill={C.woodDark} stroke={INK} strokeWidth="6" />
    {Array.from({length: 11}).map((_, i) => {
      const bh = 120 + random('sb' + i) * 60, bw = 30 + random('sw' + i) * 14;
      const cols = ['#8E3B46', '#2F5D8C', '#C98B2B', '#3F6E4F', '#6B4C8A', '#B5523B'];
      return <rect key={i} x={80 + i * 40} y={250 - bh} width={bw} height={bh} fill={cols[i % 6]} stroke={INK} strokeWidth="5" transform={i === 9 ? `rotate(14 ${80 + i * 40} 250)` : ''} />;
    })}
    <g transform="translate(90 340)"><Corkboard ripped={ripped} t={t} /></g>
    <g transform="translate(150 770)"><Calendar crossed={crossed} tear={calTear} t={t} /></g>
    <g transform="translate(630 300)"><RoomWindow t={t} w={380} h={560} rain={rain} dawnK={dawnK} /></g>
    {/* window light patch on the wall */}
    <path d="M600 900 L1030 900 L1180 1300 L700 1300Z" fill={dawnK > 0 ? C.dawnGold : '#6F86C9'} opacity={0.06 + dawnK * 0.12} filter="url(#blur14)" />
  </g>
);

// desk top + front, drawn in front of the character
export const Desk = ({children}) => (
  <g>
    <path d="M-300 1300 L1380 1300 L1380 1372 L-300 1372Z" fill={C.wood} stroke={INK} strokeWidth="8" />
    {[1318, 1340, 1358].map((y, i) => <path key={y} d={`M-300 ${y} Q300 ${y + (i - 1) * 4} 1380 ${y}`} stroke={C.woodDark} strokeWidth="3" fill="none" opacity="0.6" />)}
    <path d="M-300 1300 L1380 1300" stroke={C.woodLight} strokeWidth="6" />
    <rect x="-300" y="1372" width="1680" height="90" fill={C.woodDark} stroke={INK} strokeWidth="8" />
    <rect x="-300" y="1462" width="1680" height="600" fill="#1A1420" />
    <rect x="-300" y="1372" width="1680" height="90" fill="url(#hatch)" />
    {children}
  </g>
);

// room lighting overlays
export const RoomLight = ({lamp = 1, dawnK = 0, t = 0}) => {
  const flick = 1 - 0.12 * Math.max(0, Math.sin(t * 23) * Math.sin(t * 7.3));
  return (
    <g>
      <Glow id="lampg" x={LAMP_HEAD[0] + 40} y={LAMP_HEAD[1] + 80} r={560} color={C.lamp} opacity={0.55 * lamp * flick} />
      <Beam x={LAMP_HEAD[0] + 30} y={LAMP_HEAD[1] + 10} angle={-28} len={520} spread={520} color={C.lamp} opacity={0.35 * lamp * flick} />
      <Dust t={t} n={26} x={160} y={1000} w={420} h={340} size={3.5} rise={14} color={C.lampHot} opacity={0.6 * lamp} seed="qd" />
      {dawnK > 0 && <Glow id="dawng" x={820} y={700} r={900} color={C.dawn} opacity={0.45 * dawnK} />}
      <rect x="-600" y="-600" width="2300" height="2600" fill={C.night0} opacity={0.18 * (1 - dawnK)} style={{mixBlendMode: 'multiply'}} />
    </g>
  );
};

// ---------------------------------------------------------------- S01 · 22:43 phone lights up
export const S01 = () => {
  const t = useST();
  const on = kf(t, [0.05, 0.3], [0, 1], 'o');
  const vib = t > 0.08 && t < 0.75 ? Math.sin(t * 95) * 7 : 0;
  const z = kf(t, [0, 2.1], [1.0, 1.16], 'sine');
  const handX = kf(t, [1.35, 2.1], [1100, 250], 'o');
  return (
    <Frame bg="#140F18">
      <Camera z={z} r={kf(t, [0, 2], [-4, -2])} x={0} y={-30}>
        {/* desk wood seen from above */}
        <rect x="-300" y="-300" width="1700" height="2600" fill="#5E3C2A" />
        {Array.from({length: 22}).map((_, i) => (
          <g key={i}>
            <rect x="-300" y={-300 + i * 130} width="1700" height="128" fill={i % 2 ? '#63412E' : '#5A3A28'} />
            <path d={`M-300 ${-240 + i * 130} Q200 ${-260 + i * 130 + (i % 3) * 14} 700 ${-236 + i * 130} T1400 ${-244 + i * 130}`} stroke="#3E271B" strokeWidth="3" fill="none" opacity="0.7" />
            <path d={`M-300 ${-300 + i * 130} L1400 ${-300 + i * 130}`} stroke={INK} strokeWidth="5" opacity="0.6" />
          </g>
        ))}
        {/* scattered papers */}
        <g transform="translate(120 1450) rotate(-14)"><rect width="420" height="540" fill={C.paper} stroke={INK} strokeWidth="6" />{[60, 100, 140, 180, 220, 260].map((y) => <rect key={y} x="40" y={y} width={300 - (y % 70)} height="12" rx="6" fill="#8D8270" />)}<text x="40" y="44" fontFamily="'Archivo Black'" fontSize="26" fill="#5C5245">SIMULADO 07</text></g>
        {/* glow of the screen on the desk */}
        <Glow id="s1g" x={560} y={980} r={620} color={C.screen} opacity={0.55 * on} />
        <g transform={`translate(${560 + vib} 980) rotate(-9) scale(1.55)`}>
          <rect x="-150" y="-300" width="300" height="600" rx="44" transform="translate(16 22)" fill="#000" opacity="0.5" filter="url(#blur8)" />
          <Phone screen="clock" on={on} t={t} />
        </g>
        {/* vibration marks */}
        {t > 0.08 && t < 0.75 && [0, 1].map((i) => (
          <path key={i} d={`M${290 - i * 30} ${760 + i * 40} q-30 40 0 80 M${830 + i * 30} ${760 + i * 40} q30 40 0 80`} stroke={C.screen} strokeWidth="8" fill="none" strokeLinecap="round" opacity={0.8 * (1 - ((t * 4 + i * 0.5) % 1))} />
        ))}
        {/* hand reaching */}
        <g transform={`translate(${handX + 300} ${1500}) rotate(-38)`}>
          <path d="M-70 0 L-60 520 L70 520 L80 0Z" fill="#A8714F" stroke={INK} strokeWidth="8" />
          <path d="M-90 -10 Q-100 -150 -40 -190 Q20 -210 70 -170 Q100 -120 90 -10Z" fill="#A8714F" stroke={INK} strokeWidth="8" />
          <path d="M-60 -20 Q-70 -120 -30 -160" stroke="#7A4A30" strokeWidth="10" fill="none" opacity="0.6" />
          <path d="M-70 40 L80 40 L80 260 L-64 260Z" fill="#2F6E73" stroke={INK} strokeWidth="8" />
        </g>
        {/* foreground mug, out of focus */}
        <g transform="translate(940 380) scale(1.9)" filter="url(#blur14)" opacity="0.9"><Mug t={t} steam={false} /></g>
      </Camera>
      {/* rain bokeh at the top (window reflections) */}
      <g filter="url(#blur8)" opacity="0.5">
        {Array.from({length: 14}).map((_, i) => <circle key={i} cx={random('bk' + i) * W} cy={(random('by' + i) * 380 + t * 40) % 420} r={16 + random('br' + i) * 30} fill={i % 3 ? '#6F86C9' : C.lamp} opacity="0.5" />)}
      </g>
      <Finish vignette={1} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S02 · reads the result
export const S02 = ({dur}) => {
  const t = useST();
  const sad = kf(t, [0.75, 1.35], [0, 1]);
  const expr = mixExpr('cansado', 'abatido', sad);
  const close = kf(t, [1.9, 2.5], [0, 0.75]);
  const z = kf(t, [-0.3, dur], [1.0, 1.13], 'sine');
  const pulse = 0.75 + Math.sin(t * 5) * 0.08;
  return (
    <Frame bg={C.night1}>
      <Camera z={z} x={kf(t, [0, dur], [-10, 30])} y={kf(t, [0, dur], [0, -60])}>
        {/* background room, blurred */}
        <g filter="url(#blur8)" transform="translate(-260 -380) scale(1.5)">
          <RoomBack t={t} />
          <Glow id="s2lamp" x={LAMP_HEAD[0]} y={LAMP_HEAD[1]} r={420} color={C.lamp} opacity={0.4} />
        </g>
        <rect x="-300" y="-300" width="1700" height="2600" fill={C.night0} opacity="0.35" />
        <g transform="translate(470 1340) scale(1.3)">
          <LucasBusto t={t} id="s2" expr={expr} look={{x: 0.55, y: kf(t, [0, 0.6], [0.4, 0.9])}} nod={kf(t, [0, 1.5], [10, 26])} tilt={kf(t, [0, 2.5], [2, 6])}
            blink={close} shoulders={kf(t, [1.3, 2.0], [0, 34])} light={{side: -1, color: C.lamp, rim: 0.55}} under={{color: C.screen, k: pulse}} />
        </g>
        {/* phone in the foreground */}
        <g transform={`translate(${770} ${1400 + kf(t, [1.3, 2.0], [0, 30])}) rotate(-12) scale(1.12)`}>
          <Glow id="s2pg" x={0} y={0} r={420} color={C.screen} opacity={0.35} />
          <Phone screen="result" on={1} t={t} />
          <path d="M-160 120 Q-190 260 -130 330 L140 330 Q180 250 150 160 Q60 200 -160 120Z" fill="#A8714F" stroke={INK} strokeWidth="8" />
          <path d="M-150 150 Q-60 190 40 180" stroke={INK} strokeWidth="5" fill="none" opacity="0.5" />
        </g>
      </Camera>
      <Finish vignette={1.1} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S03 · wide room, another attempt
const ARM_DESK = {l: [-10, 96], r: [10, -96]};
const ARM_HEAD = {l: [-168, 128], r: [168, -128]};
export const S03 = ({dur}) => {
  const t = useST();
  const flip = kf(t, [0.55, 0.95], [0, 1]);
  const toHead = kf(t, [2.2, 2.85], [0, 1]);
  const arms = {
    l: [lerp(ARM_DESK.l[0], ARM_HEAD.l[0], toHead), lerp(ARM_DESK.l[1], ARM_HEAD.l[1], toHead), null, 1],
    r: [lerp(ARM_DESK.r[0] + 6, ARM_HEAD.r[0], toHead), lerp(ARM_DESK.r[1] + (1 - flip) * 30, ARM_HEAD.r[1], toHead), flip < 0.5 ? 'phone' : null, 1],
  };
  const cam = {
    z: kf(t, [-0.3, 3.6], [1.75, 1.12], 'io'),
    x: kf(t, [-0.3, 3.6], [40, 0], 'io'),
    y: kf(t, [-0.3, 3.6], [180, 40], 'io'),
  };
  return (
    <Frame bg={C.night1}>
      <Camera {...cam} r={kf(t, [0, dur], [1.5, 0])}>
        <Layer d={0.82} cx={cam.x} cy={cam.y}><RoomBack t={t + 4} /></Layer>
        <g transform={`translate(${CHAR_POS[0]} ${CHAR_POS[1] + toHead * 26}) scale(${CHAR_SCALE})`}>
          <LucasBusto t={t} id="s3" expr={mixExpr('abatido', {...EXPR.abatido, lid: 0.8}, toHead)} look={{x: 0.3, y: 0.9}} nod={20 + toHead * 14} tilt={-4 - toHead * 6}
            arms={arms} light={{side: -1, color: C.lamp, rim: 0.6}} shoulders={20} />
        </g>
        <Desk>
          <g transform="translate(70 1335)"><Lamp /></g>
          <g transform="translate(250 1340)"><BookStack n={4} seed="s3b" /></g>
          <g transform="translate(940 1340)"><Mug t={t} /></g>
          {flip >= 0.5 && <g transform="translate(700 1330) scale(0.5 0.16)"><Phone faceDown /></g>}
          <g transform="translate(1080 1336) rotate(-6)"><rect x="-120" y="-24" width="240" height="24" fill={C.paper} stroke={INK} strokeWidth="5" /></g>
        </Desk>
        <RoomLight t={t} />
      </Camera>
      {/* foreground rain streak on lens-side glass for depth */}
      <Finish vignette={1} />
    </Frame>
  );
};
