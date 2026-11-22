import React from 'react';
import {random} from 'remotion';
import {INK, C, W, H, Frame, Finish, Camera, Layer, Glow, Beam, Dust, Rain, Steam, kf, useST, lerp, clamp01} from '../kit.jsx';
import {LucasBusto} from '../rigs/LucasBusto.jsx';
import {LucasPerfil} from '../rigs/LucasPerfil.jsx';
import {EXPR, mixExpr} from '../rigs/lucas.js';
import {Phone, Mug, DeskClock, Calendar, Corkboard, RoomWindow} from './props.jsx';
import {RoomBack, LAMP_HEAD} from './Quarto.jsx';

const UI = 'InterV, Inter, sans-serif';
const BLURRED_ROOM = ({t, dawnK = 0, k = 1.5, ox = -260, oy = -380, blur = 8, crossed = 12, ripped = 0}) => (
  <g filter={blur ? `url(#blur${blur})` : undefined} transform={`translate(${ox} ${oy}) scale(${k})`}>
    <RoomBack t={t} dawnK={dawnK} crossed={crossed} ripped={ripped} />
    <Glow id={`brl${k}${ox}`} x={LAMP_HEAD[0]} y={LAMP_HEAD[1]} r={420} color={C.lamp} opacity={0.4 * (1 - dawnK * 0.6)} />
  </g>
);

// ---------------------------------------------------------------- S06b · late night at the laptop (00:17)
export const S06b = ({dur}) => {
  const t = useST();
  const rub = kf(t, [0.0, 0.25, 0.95, 1.25], [0, 1, 1, 0]);
  const rubWig = Math.sin(t * 18) * 6 * rub;
  const lA = lerp(-12, -170, rub), lB = lerp(98, 116 + rubWig, rub);
  const cam = {x: kf(t, [-0.3, dur], [-70, 60], 'lin'), z: 1.06};
  return (
    <Frame bg={C.night1}>
      <Camera {...cam}>
        <Layer d={0.6} cx={cam.x}><BLURRED_ROOM t={t + 9} /></Layer>
        <rect x="-300" y="-300" width="1700" height="2600" fill={C.night0} opacity="0.35" />
        <g transform="translate(540 1330) scale(1.0)">
          <LucasBusto t={t} id="s6b" expr={mixExpr('focado', {...EXPR.cansado, lid: 0.55}, rub)} look={{x: 0.15 + Math.sin(t * 2.3) * 0.25, y: 0.55 + (t > 1.3 ? Math.sin(t * 6) * 0.08 : 0)}}
            nod={14} tilt={rub * -6} blink={rub * 0.9} light={{side: -1, color: C.lamp, rim: 0.5}} under={{color: '#CFE6FF', k: 0.75}}
            arms={{l: [lA, lB, null, 0]}} />
        </g>
        {/* laptop seen from behind */}
        <g transform="translate(560 1900)">
          <Glow id="s6bl" x={0} y={-430} r={520} color="#CFE6FF" opacity={0.5} />
          <path d="M-430 -470 L430 -470 Q450 -470 452 -450 L470 0 L-470 0 L-452 -450 Q-450 -470 -430 -470Z" fill="#2B3142" stroke={INK} strokeWidth="9" />
          <path d="M-430 -470 L-200 -470 L-460 -60Z" fill="#fff" opacity="0.06" />
          <circle cx="0" cy="-250" r="34" fill="#3A4157" />
          <path d="M-420 -470 L420 -470" stroke="#CFE6FF" strokeWidth="6" opacity="0.7" />
        </g>
        <g transform="translate(790 1700) scale(1.15)"><DeskClock text="00:17" /></g>
        <g transform="translate(150 1820) scale(1.3)"><Mug t={t} /></g>
      </Camera>
      <Finish vignette={1.1} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S07 · the decision
export const S07 = ({dur}) => {
  const t = useST();
  const D = 1.47; // "decidiu"
  const det = kf(t, [D - 0.1, D + 0.2], [0, 1]);
  const reach = kf(t, [D - 0.35, D - 0.05, D + 0.15, D + 0.6], [0, 1, 1, 0]);
  const ripped = kf(t, [D - 0.02, D + 1.1], [0, 1], 'o');
  const nodK = kf(t, [2.85, 3.05, 3.25], [0, 1, 0]);
  const punch = kf(t, [D - 0.05, D + 0.25], [0, 1], 'o');
  const shake = t > D && t < D + 0.35 ? Math.sin(t * 80) * 8 * (1 - (t - D) / 0.35) : 0;
  const warm = kf(t, [D, D + 0.8], [0, 1]);
  const cam = {z: 1.0 + punch * 0.14 + kf(t, [D + 0.3, dur], [0, 0.05]), x: shake, y: kf(t, [0, dur], [40, 0])};
  return (
    <Frame bg={C.night1}>
      <Camera {...cam} r={-2}>
        <Layer d={0.7} cx={cam.x} cy={cam.y}>
          <rect x="-300" y="-300" width="1700" height="2600" fill={C.night2} />
          <g transform="translate(-40 160) scale(1.6)"><Corkboard ripped={ripped} t={t} /></g>
          <g transform="translate(700 260) scale(1.1)" filter="url(#blur4)"><RoomWindow t={t} w={380} h={560} /></g>
        </Layer>
        <Glow id="s7lamp" x={60} y={1300} r={900} color={C.lamp} opacity={0.3 + warm * 0.35} />
        <g transform="translate(560 1480) scale(1.38)">
          <LucasBusto t={t} id="s7" expr={mixExpr('focado', 'determinado', det)} look={{x: lerp(-0.6, 0.05, det), y: lerp(-0.5, 0, det)}} turn={lerp(-0.35, 0, det)}
            tilt={lerp(-3, 0, det)} nod={nodK * 22 - det * 6} light={{side: -1, color: C.lamp, rim: 0.5 + warm * 0.4}}
            arms={{l: [lerp(-15, -150, reach), lerp(100, -175, reach), null, 1]}} />
        </g>
        {/* papers flying toward camera */}
        {ripped > 0 && [0, 1, 2, 3].map((i) => (
          <g key={i} transform={`translate(${200 + i * 160 + ripped * (i - 1.5) * 500} ${500 + ripped * ripped * 1400 - Math.sin(ripped * 3 + i) * 200}) rotate(${ripped * (i % 2 ? 300 : -260)}) scale(${1.2 + ripped})`} opacity={1 - ripped * 0.5}>
            <rect x="-60" y="-70" width="120" height="140" fill={['#FFF59A', '#FFFFFF', '#A6E3F2', '#F7B9C8'][i]} stroke={INK} strokeWidth="5" />
            {[-30, -10, 10, 30].map((y) => <path key={y} d={`M-40 ${y} L40 ${y}`} stroke="#5A5A7A" strokeWidth="5" opacity="0.6" />)}
          </g>
        ))}
      </Camera>
      <rect width={W} height={H} fill={C.lamp} opacity={warm * 0.08} style={{mixBlendMode: 'screen'}} />
      <Finish vignette={1} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S08a · weekly planner fills up
const DAYS = ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SÁB', 'DOM'];
const SLOTS = ['06h', '08h', '19h', '21h'];
const BLOCKS = [
  [0, 0, 'TREINO', '#E8743B'], [0, 2, 'LEGISLAÇÃO', '#2F5D8C'], [0, 3, 'REVISÃO', '#3F6E4F'],
  [1, 0, 'TREINO', '#E8743B'], [1, 2, 'PORTUGUÊS', '#8E3B46'], [1, 3, 'QUESTÕES', '#6B4C8A'],
  [2, 0, 'TREINO', '#E8743B'], [2, 2, 'MATEMÁTICA', '#C98B2B'], [2, 3, 'REVISÃO', '#3F6E4F'],
  [3, 0, 'TREINO', '#E8743B'], [3, 2, 'LEGISLAÇÃO', '#2F5D8C'], [3, 3, 'QUESTÕES', '#6B4C8A'],
  [4, 0, 'TREINO', '#E8743B'], [4, 2, 'PORTUGUÊS', '#8E3B46'], [4, 3, 'REVISÃO', '#3F6E4F'],
  [5, 1, 'SIMULADO', '#D94B45'], [6, 1, 'DESCANSO', '#7A8496'],
];
export const S08a = ({dur}) => {
  const t = useST();
  const cw = 132, rh = 200, x0 = 110, y0 = 560;
  return (
    <Frame bg="#E9DFC8">
      <Camera z={kf(t, [-0.2, dur], [0.98, 1.05])} x={kf(t, [-0.2, dur], [30, -30], 'lin')} r={1}>
        <rect x="-300" y="-300" width="1700" height="2600" fill="#3A4570" />
        <rect x="-300" y="-300" width="1700" height="2600" filter="url(#paperTex)" opacity="0.5" />
        <rect x="70" y="340" width="980" height="1260" fill="#FBF6EA" stroke={INK} strokeWidth="10" transform="rotate(-1.5 540 960)" />
        <g transform="rotate(-1.5 540 960)">
          <text x="110" y="440" fontFamily="'Archivo Black'" fontSize="64" fill={INK}>MINHA ROTINA</text>
          <text x="1010" y="440" fontFamily={UI} fontSize="34" fontWeight="800" fill="#8A8170" textAnchor="end">SEMANA 1</text>
          {DAYS.map((d, i) => <text key={d} x={x0 + 70 + i * cw} y={y0 - 20} fontFamily={UI} fontSize="28" fontWeight="900" fill="#55607A" textAnchor="middle">{d}</text>)}
          {SLOTS.map((s, r) => <text key={s} x={x0 - 10} y={y0 + r * rh + 110} fontFamily={UI} fontSize="24" fontWeight="800" fill="#8A8170" textAnchor="end" opacity="0">{s}</text>)}
          {Array.from({length: 8}).map((_, i) => <path key={i} d={`M${x0 + 4 + i * cw} ${y0} L${x0 + 4 + i * cw} ${y0 + 4 * rh}`} stroke="#D8CDB4" strokeWidth="3" />)}
          {Array.from({length: 5}).map((_, i) => <path key={i} d={`M${x0 + 4} ${y0 + i * rh} L${x0 + 4 + 7 * cw} ${y0 + i * rh}`} stroke="#D8CDB4" strokeWidth="3" />)}
          {BLOCKS.map(([d, s, label, col], i) => {
            const k = kf(t, [0.05 + i * 0.065, 0.2 + i * 0.065], [0, 1], 'back');
            return (
              <g key={i} transform={`translate(${x0 + 4 + d * cw + cw / 2} ${y0 + s * rh + rh / 2}) scale(${k}) rotate(${(i % 3 - 1) * 2})`} opacity={clamp01(k * 3)}>
                <rect x={-cw / 2 + 8} y={-rh / 2 + 10} width={cw - 16} height={rh - 20} rx="12" fill={col} stroke={INK} strokeWidth="5" />
                <text x="0" y="8" fill="#fff" fontFamily={UI} fontSize={label.length > 8 ? 17 : 21} fontWeight="900" textAnchor="middle" transform="rotate(-90)">{label}</text>
              </g>
            );
          })}
        </g>
        {/* hand placing the last note */}
        <g transform={`translate(${kf(t, [0.9, 1.25], [1400, 980], 'o')} ${kf(t, [0.9, 1.25], [1300, 860], 'o')}) rotate(-30)`}>
          <path d="M-70 0 L-60 700 L70 700 L80 0Z" fill="#A8714F" stroke={INK} strokeWidth="8" />
          <path d="M-90 10 Q-100 -130 -40 -170 Q20 -186 70 -140 Q100 -90 90 10Z" fill="#A8714F" stroke={INK} strokeWidth="8" />
          <path d="M-70 160 L80 160 L80 380 L-66 380Z" fill={'#8C96A3'} stroke={INK} strokeWidth="8" />
        </g>
      </Camera>
      <Finish vignette={0.7} grain={0.6} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S08b · practice questions, ticks
export const S08b = ({dur}) => {
  const t = useST();
  const ticks = [0.12, 0.34, 0.56, 0.78];
  const done = ticks.filter((x) => t > x).length;
  const cur = Math.min(3, done);
  const penX = 820, penY = 640 + cur * 230 + Math.sin(t * 40) * 10;
  return (
    <Frame bg="#E9DFC8">
      <Camera z={1.1} r={kf(t, [-0.2, dur], [3, -1])}>
        <rect x="-300" y="-300" width="1700" height="2600" fill="#7A5A40" />
        <rect x="120" y="260" width="860" height="1420" fill="#FBF8F0" stroke={INK} strokeWidth="9" />
        <text x="170" y="370" fontFamily="'Archivo Black'" fontSize="54" fill={INK}>QUESTÕES</text>
        <text x="170" y="420" fontFamily={UI} fontSize="30" fontWeight="700" fill="#8A8170">Legislação · bloco 3</text>
        {[0, 1, 2, 3].map((i) => (
          <g key={i} transform={`translate(170 ${560 + i * 230})`}>
            <text x="0" y="0" fontFamily={UI} fontSize="34" fontWeight="900" fill={INK}>{i + 1}.</text>
            <rect x="60" y="-26" width="520" height="16" rx="8" fill="#B9B3A6" /><rect x="60" y="6" width="420" height="16" rx="8" fill="#B9B3A6" />
            {['A', 'B', 'C', 'D'].map((l, j) => <g key={l} transform={`translate(${70 + j * 130} 80)`}><circle r="22" fill="none" stroke="#8A8170" strokeWidth="4" /><text y="9" fontFamily={UI} fontSize="24" fontWeight="800" fill="#8A8170" textAnchor="middle">{l}</text>{t > ticks[i] && j === (i * 2 + 1) % 4 && <circle r="16" fill={INK} />}</g>)}
            {t > ticks[i] && <path d="M640 40 l30 34 l60 -80" stroke="#2E9E5B" strokeWidth="16" fill="none" strokeLinecap="round" strokeLinejoin="round" strokeDasharray="200" strokeDashoffset={200 * (1 - clamp01((t - ticks[i]) / 0.1))} />}
          </g>
        ))}
        <g transform={`translate(${penX} ${penY}) rotate(35)`}>
          <rect x="-18" y="0" width="36" height="420" rx="10" fill="#2F5D8C" stroke={INK} strokeWidth="6" />
          <path d="M-18 0 L0 -50 L18 0Z" fill="#E9DFC8" stroke={INK} strokeWidth="5" />
          <rect x="-18" y="300" width="36" height="20" fill="#E8B84A" />
        </g>
      </Camera>
      <Finish vignette={0.7} grain={0.6} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S08c · review: flashcards + highlighter
export const S08c = ({dur}) => {
  const t = useST();
  const flip = kf(t, [0.08, 0.38], [0, 1]);
  const hl = kf(t, [0.42, 0.85], [0, 1], 'o');
  const sx = Math.cos(flip * Math.PI);
  return (
    <Frame bg="#2A3358">
      <Camera z={kf(t, [-0.2, dur], [1.0, 1.22], 'o')} y={-40}>
        <rect x="-300" y="-300" width="1700" height="2600" fill="#6A4A35" />
        {[3, 2, 1].map((i) => <rect key={i} x={170 + i * 14} y={560 + i * 16} width="740" height="500" rx="20" fill="#F4EEDD" stroke={INK} strokeWidth="7" />)}
        <g transform={`translate(540 810) scale(${Math.abs(sx)} 1)`}>
          <rect x="-370" y="-250" width="740" height="500" rx="20" fill={sx > 0 ? '#FFF6C9' : '#FFFFFF'} stroke={INK} strokeWidth="8" />
          {sx > 0 ? (
            <g><text x="0" y="-60" fontFamily="'Archivo Black'" fontSize="54" fill={INK} textAnchor="middle">ARTIGO 5º</text><text x="0" y="20" fontFamily={UI} fontSize="34" fontWeight="700" fill="#6B655A" textAnchor="middle">O que garante?</text></g>
          ) : (
            <g>
              <rect x="-310" y={-90} width={620 * hl} height="60" fill="#FFE24A" opacity="0.85" transform="skewX(-8)" />
              <text x="0" y="-48" fontFamily={UI} fontSize="38" fontWeight="900" fill={INK} textAnchor="middle">Igualdade perante a lei</text>
              {[30, 80, 130].map((y) => <rect key={y} x="-280" y={y} width={460 + (y % 60)} height="16" rx="8" fill="#B9B3A6" />)}
            </g>
          )}
        </g>
        <g transform={`translate(${240 + hl * 620} ${kf(t, [0.3, 0.45], [1300, 790])}) rotate(30)`}>
          <rect x="-34" y="0" width="68" height="380" rx="16" fill="#FFE24A" stroke={INK} strokeWidth="7" />
          <path d="M-34 0 L-20 -60 L20 -60 L34 0Z" fill="#E8C62A" stroke={INK} strokeWidth="6" />
          <rect x="-34" y="60" width="68" height="40" fill={INK} opacity="0.2" />
        </g>
      </Camera>
      <Glow id="s8cg" x={200} y={300} r={700} color={C.lamp} opacity={0.35} />
      <Finish vignette={0.9} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S09 · heavier days, push-ups, calendar flying
const plank = (k) => ({torso: lerp(63, 71, k), head: lerp(18, 26, k), thighF: lerp(-63, -71, k), shinF: lerp(-63, -71, k), thighB: lerp(-64, -72, k), shinB: lerp(-64, -72, k),
  armF: lerp(-4, -52, k), foreF: lerp(4, 30, k), armB: lerp(2, -48, k), foreB: lerp(6, 32, k), bob: 0, foot: -62});
export const S09 = ({dur}) => {
  const t = useST();
  const CUT = 2.95;
  if (t < CUT) {
    const k = 0.5 - 0.5 * Math.cos(t * Math.PI * 2 * 0.95);
    const cam = {z: 1.04, x: kf(t, [-0.3, CUT], [-40, 40], 'lin'), y: Math.sin(t * Math.PI * 2 * 0.95) * 6};
    return (
      <Frame bg={C.night1}>
        <Camera {...cam}>
          <Layer d={0.6} cx={cam.x}>
            <rect x="-300" y="-300" width="1700" height="2600" fill={C.night2} />
            {Array.from({length: 30}).map((_, i) => <rect key={i} x={-300 + i * 60} y="-300" width="22" height="2600" fill="#fff" opacity="0.025" />)}
            <g transform="translate(560 220) scale(0.85)"><RoomWindow t={t} w={420} h={640} /></g>
            <g transform="translate(110 380) scale(1.25)"><Calendar crossed={20 + Math.floor(t * 2)} month="ABRIL" /></g>
          </Layer>
          {/* calendar pages flying off */}
          {Array.from({length: 7}).map((_, i) => {
            const p = (t - i * 0.38) / 1.6;
            if (p < 0 || p > 1) return null;
            return (
              <g key={i} transform={`translate(${300 + p * 900} ${520 + Math.sin(p * 3) * -200 + p * p * 500}) rotate(${p * (i % 2 ? 340 : -280)}) scale(${1.1 - p * 0.3})`} opacity={1 - p * 0.4}>
                <rect x="-160" y="-170" width="320" height="340" fill={C.paper} stroke={INK} strokeWidth="6" />
                <rect x="-160" y="-170" width="320" height="64" fill={C.red} stroke={INK} strokeWidth="6" />
                <text x="0" y="40" fontFamily="'Archivo Black'" fontSize="120" fill={INK} textAnchor="middle" opacity="0.8">{12 + i}</text>
              </g>
            );
          })}
          <rect x="-300" y="1500" width="1700" height="900" fill="#3A2A2A" />
          {Array.from({length: 10}).map((_, i) => <path key={i} d={`M-300 ${1530 + i * 50 + i * i * 6} L1400 ${1530 + i * 50 + i * i * 6}`} stroke={INK} strokeWidth="4" opacity="0.4" />)}
          <ellipse cx="560" cy="1840" rx="520" ry="40" fill="#000" opacity="0.35" />
          <g transform={`translate(400 ${1527 + 85 * k * 0.78}) scale(0.78)`}>
            <LucasPerfil t={t} pose={plank(k)} outfit="treino" expr="esforco" sweat={0.9} light={{color: '#8FB0FF', rim: 0.6}} />
          </g>
          <Glow id="s9lamp" x={-60} y={1100} r={800} color={C.lamp} opacity={0.4} />
          <Rain t={t} n={30} area={[560, 220, 360, 540]} opacity={0.0} />
        </Camera>
        <Finish vignette={1.1} />
      </Frame>
    );
  }
  const u = t - CUT;
  return (
    <Frame bg={C.night1}>
      <Camera z={kf(u, [0, dur - CUT], [1.0, 1.12], 'o')} y={-40}>
        <Layer d={0.6}><BLURRED_ROOM t={t} crossed={26} /></Layer>
        <rect x="-300" y="-300" width="1700" height="2600" fill={C.night0} opacity="0.3" />
        <g transform={`translate(540 ${1460 + Math.sin(u * 6) * 12}) scale(1.32)`}>
          <LucasBusto t={t} id="s9" expr={mixExpr('esforco', 'determinado', kf(u, [0.1, 0.5], [0, 1]))} outfit="tee" sweat={1} look={{x: 0, y: -0.05}}
            light={{side: 1, color: '#8FB0FF', rim: 0.85}} />
        </g>
      </Camera>
      <Finish vignette={1.1} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S10a · the opportunity arrives (callback to S02, now at dawn)
export const S10a = ({dur}) => {
  const t = useST();
  const joy = kf(t, [0.35, 1.2], [0, 1]);
  return (
    <Frame bg={C.night2}>
      <Camera z={kf(t, [-0.2, dur], [1.0, 1.12], 'sine')} x={kf(t, [0, dur], [-10, 20])} y={kf(t, [0, dur], [0, -60])}>
        <BLURRED_ROOM t={t} dawnK={1} crossed={30} />
        <Glow id="s10sun" x={980} y={500} r={1100} color={C.dawn} opacity={0.55} />
        <Beam x={1100} y={300} angle={50} len={1800} spread={600} color={C.dawnGold} opacity={0.35} />
        <g transform="translate(470 1340) scale(1.3)">
          <LucasBusto t={t} id="s10a" outfit="tee" expr={mixExpr('focado', 'esperanca', joy)} look={{x: lerp(0.55, 0.15, joy), y: lerp(0.9, 0.2, joy)}} nod={lerp(22, 4, joy)} tilt={lerp(4, 0, joy)}
            light={{side: 1, color: C.dawnGold, rim: 0.9}} under={{color: '#FFD9A0', k: 0.5}} />
        </g>
        <g transform={`translate(770 1400) rotate(-12) scale(1.12)`}>
          <Glow id="s10pg" x={0} y={0} r={420} color="#FFD9A0" opacity={0.35} />
          <Phone screen="edital" on={1} t={t} />
          <path d="M-160 120 Q-190 260 -130 330 L140 330 Q180 250 150 160 Q60 200 -160 120Z" fill="#A8714F" stroke={INK} strokeWidth="8" />
        </g>
        <Dust t={t} n={40} color={C.dawnGold} size={4} rise={20} seed="s10d" />
      </Camera>
      <Finish vignette={0.8} />
    </Frame>
  );
};
