import React from 'react';
import {random} from 'remotion';
import {INK, C, W, H, Frame, Finish, Camera, Layer, Glow, Beam, Dust, kf, useST, lerp, clamp01} from '../kit.jsx';
import {LucasBusto} from '../rigs/LucasBusto.jsx';
import {LucasPerfil, runPose, walkPose, standPose} from '../rigs/LucasPerfil.jsx';
import {EXPR, mixExpr} from '../rigs/lucas.js';

const UI = 'InterV, Inter, sans-serif';

const DawnSky = ({t, sunY = 900, id = 'ds'}) => (
  <g>
    <defs>
      <linearGradient id={id} x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stopColor="#3D4F8F" /><stop offset="0.45" stopColor="#C7718A" /><stop offset="0.75" stopColor="#F29A5A" /><stop offset="1" stopColor="#FFD58A" />
      </linearGradient>
    </defs>
    <rect x="-800" y="-800" width="2700" height="3000" fill={`url(#${id})`} />
    <circle cx="700" cy={sunY} r="150" fill="#FFF1C2" filter="url(#glow)" />
    <Glow id={id + 'g'} x={700} y={sunY} r={800} color="#FFD27A" opacity={0.6} />
    {[0, 1, 2, 3].map((i) => <ellipse key={i} cx={((i * 600 + t * 30) % 2400) - 600} cy={260 + i * 150} rx={300 + i * 40} ry="38" fill="#F7B7A3" opacity="0.55" filter="url(#blur8)" />)}
  </g>
);

// colorful colonial-style row houses
const Houses = ({seed, y = 1250, n = 8, x0 = -400, sp = 330}) => {
  const cols = ['#E9B44C', '#4F9D9A', '#D9705A', '#7FA7D9', '#E8D8A8', '#B56576', '#8DB580'];
  return (
    <g>
      {Array.from({length: n}).map((_, i) => {
        const w = sp - 10, h = 380 + random(seed + i) * 160, x = x0 + i * sp, col = cols[(i + Math.floor(random(seed) * 7)) % 7];
        return (
          <g key={i}>
            <rect x={x} y={y - h} width={w} height={h} fill={col} stroke={INK} strokeWidth="7" />
            <rect x={x - 10} y={y - h - 30} width={w + 20} height="34" fill="#F4EEDD" stroke={INK} strokeWidth="6" />
            <path d={`M${x + w * 0.38} ${y} L${x + w * 0.38} ${y - 170} Q${x + w * 0.5} ${y - 220} ${x + w * 0.62} ${y - 170} L${x + w * 0.62} ${y}Z`} fill="#5A3A28" stroke={INK} strokeWidth="6" />
            {[0.12, 0.72].map((f) => <rect key={f} x={x + w * f} y={y - h + 90} width={w * 0.18} height="120" fill="#2F3A5C" stroke={INK} strokeWidth="5" />)}
            <rect x={x} y={y - h} width={w * 0.22} height={h} fill={INK} opacity="0.15" />
          </g>
        );
      })}
    </g>
  );
};

// ---------------------------------------------------------------- S08d · morning run
export const S08d = ({dur}) => {
  const t = useST();
  const sx = (t + 1) * 900;
  const ph = (t + 1) * 9.2;
  return (
    <Frame bg="#F29A5A">
      <Camera z={1.0} y={kf(t, [-0.3, dur], [0, -20])}>
        <DawnSky t={t} sunY={kf(t, [-0.3, dur], [980, 860])} id="s8sky" />
        <g transform={`translate(${-(sx * 0.08) % 600} 0)`}>
          {Array.from({length: 9}).map((_, i) => <rect key={i} x={-400 + i * 300} y={950 - (i % 3) * 90} width="240" height="400" fill="#8E5C78" opacity="0.6" />)}
        </g>
        <g transform={`translate(${-((sx * 0.4) % 2640)} 0)`}><Houses seed="h1" n={16} y={1300} sp={330} /></g>
        <rect x="-300" y="1300" width="1700" height="1000" fill="#7D6B6B" />
        <rect x="-300" y="1300" width="1700" height="26" fill="#C9B9A8" stroke={INK} strokeWidth="6" />
        <g transform={`translate(${-(sx % 260)} 0)`}>{Array.from({length: 9}).map((_, i) => <path key={i} d={`M${-300 + i * 260} 1326 L${-340 + i * 260} 1900`} stroke={INK} strokeWidth="5" opacity="0.4" />)}</g>
        <g transform={`translate(${-(sx * 1.0) % 900} 0)`}>
          {[0, 1, 2].map((i) => (
            <g key={i} transform={`translate(${200 + i * 900} 0)`}>
              <rect x="-14" y="420" width="28" height="900" fill="#3A4260" stroke={INK} strokeWidth="6" />
              <path d="M0 440 Q0 380 -90 380" stroke="#3A4260" strokeWidth="20" fill="none" />
              <rect x="-150" y="370" width="80" height="30" fill="#2A2F45" stroke={INK} strokeWidth="5" />
            </g>
          ))}
        </g>
        <ellipse cx="520" cy="1755" rx="230" ry="26" fill={INK} opacity="0.3" />
        <g transform="translate(500 1225) scale(0.66)">
          <LucasPerfil t={t} pose={runPose(ph)} outfit="treino" expr="determinado" light={{color: '#FFD27A', rim: 0.9}} />
        </g>
        <Dust t={t} n={40} color="#FFE6B0" size={4} rise={12} seed="s8dd" opacity={0.8} />
        {[0, 1, 2].map((i) => {
          const bx = ((t * 160 + i * 300) % 1400) - 200, by = 400 + i * 70 + Math.sin(t * 3 + i) * 20, wf = Math.sin(t * 14 + i) * 14;
          return <path key={i} d={`M${bx - 30} ${by + wf} Q${bx - 12} ${by - 8} ${bx} ${by} Q${bx + 12} ${by - 8} ${bx + 30} ${by + wf}`} stroke="#3A2A3A" strokeWidth="6" fill="none" strokeLinecap="round" />;
        })}
        <g transform={`translate(${1600 - ((sx * 1.7 + 600) % 2600)} 0)`} filter="url(#blur8)">
          <ellipse cx="0" cy="1880" rx="300" ry="200" fill="#3D5A3A" /><ellipse cx="180" cy="1840" rx="200" ry="160" fill="#4E7048" />
        </g>
      </Camera>
      <Finish vignette={0.7} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S10b · walking to the exam, the next step
export const S10b = ({dur}) => {
  const t = useST();
  const STEP = 2.09;
  const ph = t < STEP ? Math.PI / 2 + (t - STEP) * 5.6 : Math.PI / 2;
  const travel = t < STEP ? (t - STEP) * 330 : 0;
  const low = kf(t, [1.6, 2.3], [0, 1], 'io');
  const hipX = 470, hipY = 1180, s = 0.66;
  const footX = hipX + 200 * s + 40, footY = 1745;
  const cam = {z: lerp(1.0, 2.1, low), x: lerp(0, footX - W / 2 + 60, low), y: lerp(0, footY - H / 2 - 260, low), r: lerp(0, -4, low)};
  const puff = kf(t, [STEP, STEP + 0.6], [0, 1], 'o');
  return (
    <Frame bg="#F29A5A">
      <Camera {...cam}>
        <Layer d={0.25} cx={cam.x} cy={cam.y}><DawnSky t={t} sunY={760} id="s10sky" /></Layer>
        <Layer d={0.6} cx={cam.x} cy={cam.y}>
          <g transform={`translate(${-travel * 0.5} 0)`}>
            {/* school building + gate with banner */}
            <rect x="300" y="700" width="1300" height="620" fill="#E8D8A8" stroke={INK} strokeWidth="8" />
            <rect x="280" y="660" width="1340" height="50" fill="#C9473F" stroke={INK} strokeWidth="7" />
            {Array.from({length: 6}).map((_, i) => <rect key={i} x={360 + i * 200} y="800" width="110" height="150" fill="#2F3A5C" stroke={INK} strokeWidth="6" />)}
            <rect x="300" y="700" width="1300" height="620" fill="url(#hatch)" opacity="0.3" />
            <g transform="translate(560 1000)">
              <rect x="-20" y="-60" width="40" height="380" fill="#3A4260" stroke={INK} strokeWidth="6" />
              <rect x="560" y="-60" width="40" height="380" fill="#3A4260" stroke={INK} strokeWidth="6" />
              <rect x="20" y="-20" width="540" height="130" fill="#F4F1EA" stroke={INK} strokeWidth="7" />
              <text x="290" y="68" fontFamily="'Archivo Black'" fontSize="64" fill={C.navy} textAnchor="middle">LOCAL DE PROVA</text>
            </g>
            {[0, 1].map((i) => (
              <g key={i} transform={`translate(${900 + i * 260 + t * 60} 1080) scale(0.32)`} opacity="0.75">
                <LucasPerfil t={t + i} pose={walkPose(t * 5 + i * 2)} outfit="prova" expr="neutro" light={{color: '#FFD27A', rim: 0.3}} />
              </g>
            ))}
          </g>
        </Layer>
        <rect x="-600" y="1320" width="2400" height="1200" fill="#9C8A7E" />
        <rect x="-600" y="1320" width="2400" height="20" fill={INK} opacity="0.4" />
        <g transform={`translate(${-(travel % 220)} 0)`}>{Array.from({length: 14}).map((_, i) => <rect key={i} x={-600 + i * 220} y="1720" width="200" height="14" fill="#B5A396" stroke={INK} strokeWidth="3" />)}</g>
        <ellipse cx={hipX + 20} cy="1765" rx="230" ry="26" fill={INK} opacity="0.3" />
        <g transform={`translate(${hipX} ${hipY}) scale(${s})`}>
          <LucasPerfil t={t} pose={walkPose(ph)} outfit="prova" expr={mixExpr('determinado', 'confiante', 0.5)} light={{color: '#FFD27A', rim: 0.9}} />
        </g>
        {puff > 0 && puff < 1 && [0, 1, 2, 3].map((i) => <circle key={i} cx={footX + 40 + (i - 1.5) * 60 * (0.4 + puff)} cy={footY + 10 - puff * 40} r={20 + puff * 30} fill="#F4E2C8" opacity={(1 - puff) * 0.7} />)}
        <Dust t={t} n={36} color="#FFE6B0" size={4} rise={14} seed="s10bd" opacity={0.8} />
      </Camera>
      <Glow id="flare" x={W * 0.75} y={H * 0.3} r={700} color="#FFE2A0" opacity={0.25 + low * 0.2} />
      <Finish vignette={0.7} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S11 · viewpoint at sunrise; turns to the viewer
const City = ({t}) => (
  <g>
    <path d="M-600 1350 Q300 1300 1800 1380 L1800 1520 L-600 1520Z" fill="#E7A27A" />
    <path d="M-600 1430 Q200 1380 1800 1460 L1800 1600 Q300 1540 -600 1600Z" fill="#5E8FB8" />
    <path d="M-500 1470 Q300 1440 1700 1500" stroke="#FFE1A8" strokeWidth="8" fill="none" opacity="0.8" />
    {Array.from({length: 26}).map((_, i) => {
      const w = 60 + random('cty' + i) * 80, h = 60 + random('cth' + i) * 160, x = -600 + i * 95;
      return <rect key={i} x={x} y={1350 - h + (i % 3) * 10} width={w} height={h} fill={['#B56576', '#E9B44C', '#4F9D9A', '#D9705A', '#E8D8A8'][i % 5]} opacity="0.75" stroke={INK} strokeWidth="3" />;
    })}
    <rect x="980" y="980" width="44" height="380" fill="#E8D8A8" stroke={INK} strokeWidth="4" opacity="0.8" />
    <path d="M970 980 L1034 980 L1002 920Z" fill="#C9473F" stroke={INK} strokeWidth="4" opacity="0.8" />
  </g>
);
export const S11 = ({dur}) => {
  const t = useST();
  const CUT = 2.32;
  if (t < CUT) {
    const cam = {z: kf(t, [-0.3, CUT], [1.35, 1.0], 'o'), x: kf(t, [-0.3, CUT], [-160, 0], 'o'), y: kf(t, [-0.3, CUT], [-80, 0], 'o')};
    return (
      <Frame bg="#F29A5A">
        <Camera {...cam}>
          <Layer d={0.2} cx={cam.x} cy={cam.y}><DawnSky t={t} sunY={1180} id="s11sky" /></Layer>
          <Layer d={0.5} cx={cam.x} cy={cam.y}><City t={t} /></Layer>
          {[0, 1].map((i) => {
            const bx = 600 + ((t * 120 + i * 200) % 900), by = 700 + i * 80;
            return <path key={i} d={`M${bx - 26} ${by + Math.sin(t * 12 + i) * 12} Q${bx - 10} ${by - 8} ${bx} ${by} Q${bx + 10} ${by - 8} ${bx + 26} ${by + Math.sin(t * 12 + i) * 12}`} stroke="#4A2A3A" strokeWidth="5" fill="none" />;
          })}
          {/* viewpoint ground + railing */}
          <path d="M-400 1560 L1500 1500 L1500 2400 L-400 2400Z" fill="#5E4B5A" stroke={INK} strokeWidth="8" />
          <path d="M-400 1440 L1500 1400" stroke="#3A2E3A" strokeWidth="18" />
          {Array.from({length: 12}).map((_, i) => <rect key={i} x={-400 + i * 170} y={1420 - i * 3.5} width="14" height="150" fill="#3A2E3A" />)}
          <ellipse cx="380" cy="1800" rx="200" ry="24" fill={INK} opacity="0.35" />
          <g transform="translate(360 1250) scale(0.68)">
            <LucasPerfil t={t} pose={{...standPose, armF: 6, foreF: 14}} outfit="prova" expr="confiante" light={{color: '#FFD27A', rim: 1}} />
          </g>
          <Dust t={t} n={30} color="#FFE6B0" size={4} rise={10} seed="s11d" />
        </Camera>
        <Finish vignette={0.6} />
      </Frame>
    );
  }
  const u = t - CUT;
  const turn = kf(u, [0.05, 0.75], [0.95, 0.05], 'io');
  return (
    <Frame bg="#F29A5A">
      <Camera z={kf(u, [0, dur - CUT], [1.0, 1.1], 'sine')} y={-60}>
        <g filter="url(#blur8)"><DawnSky t={t} sunY={1000} id="s11sky2" /><g transform="translate(0 200)"><City t={t} /></g></g>
        <g transform="translate(540 1500) scale(1.32)">
          <LucasBusto t={t} id="s11" outfit="tee" turn={turn} expr={mixExpr('determinado', 'confiante', kf(u, [0.4, 1.0], [0, 1]))} look={{x: turn * 0.9, y: 0}} light={{side: 1, color: '#FFD27A', rim: 1}} />
        </g>
        <Glow id="s11f" x={980} y={600} r={700} color="#FFE2A0" opacity={0.35} />
      </Camera>
      <Finish vignette={0.6} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S12 · brand card
const Shield = ({k}) => {
  const d = 'M0 -330 L250 -250 Q260 60 160 200 Q80 300 0 340 Q-80 300 -160 200 Q-260 60 -250 -250Z';
  return (
    <g>
      <path d={d} fill="#14234A" opacity={clamp01(k * 2)} />
      <path d={d} fill="none" stroke={C.gold} strokeWidth="16" strokeDasharray="2400" strokeDashoffset={2400 * (1 - k)} strokeLinejoin="round" />
      <path d="M0 -270 L196 -206 Q204 40 124 160 Q62 240 0 272 Q-62 240 -124 160 Q-204 40 -196 -206Z" fill="none" stroke={C.gold} strokeWidth="5" opacity={clamp01(k * 2 - 1) * 0.7} />
      <g opacity={clamp01(k * 2 - 1)} transform={`scale(${0.8 + 0.2 * clamp01(k * 2 - 1)})`}>
        <path d="M0 -150 L36 -50 L142 -48 L58 16 L88 118 L0 58 L-88 118 L-58 16 L-142 -48 L-36 -50Z" fill={C.gold} stroke={INK} strokeWidth="6" />
      </g>
    </g>
  );
};
export const S12 = ({dur}) => {
  const t = useST();
  const w1 = kf(t, [0.08, 0.4], [0, 1], 'o');
  const w2 = kf(t, [1.04, 1.4], [0, 1], 'back');
  const w3 = kf(t, [2.56, 2.85], [0, 1], 'back');
  const hit = kf(t, [2.56, 2.7, 3.2], [0, 1, 0]);
  const words = [['Sua', 4.29], ['preparação', 4.63], ['começa', 5.23], ['hoje.', 5.83]];
  const sweep = kf(t, [3.0, 4.0], [-600, 1700], 'io');
  return (
    <Frame bg={C.navy}>
      <defs>
        <radialGradient id="s12bg" cx="50%" cy="38%" r="70%"><stop offset="0" stopColor="#24386E" /><stop offset="1" stopColor={C.navy} /></radialGradient>
        <linearGradient id="s12sw" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stopColor="#fff" stopOpacity="0" /><stop offset="0.5" stopColor="#fff" stopOpacity="0.7" /><stop offset="1" stopColor="#fff" stopOpacity="0" /></linearGradient>
        <clipPath id="s12txt"><rect x="0" y="1060" width={W} height="480" /></clipPath>
      </defs>
      <Camera z={kf(t, [-0.3, dur], [1.0, 1.07], 'sine')} y={hit * -6}>
        <rect x="-300" y="-300" width="1700" height="2600" fill="url(#s12bg)" />
        {Array.from({length: 14}).map((_, i) => <path key={i} d={`M540 700 L${540 + Math.cos((i / 14) * Math.PI * 2 + t * 0.1) * 1600} ${700 + Math.sin((i / 14) * Math.PI * 2 + t * 0.1) * 1600}`} stroke={C.gold} strokeWidth="60" opacity="0.035" />)}
        <Dust t={t} n={60} color={C.goldHot} size={4} rise={50} seed="s12d" opacity={0.7} />
        <Glow id="s12g" x={540} y={700} r={650} color={C.gold} opacity={0.25 + hit * 0.4} />
        <g transform="translate(540 680) scale(0.95)"><Shield k={kf(t, [-0.2, 1.4], [0, 1], 'io')} /></g>
        <g opacity={w1} transform={`translate(0 ${(1 - w1) * 30})`}>
          <text x="540" y="1150" fontFamily="'Archivo Black'" fontSize="64" fill="#C9D6F2" textAnchor="middle" letterSpacing="22">PROJETO</text>
        </g>
        <g transform={`translate(540 1330) scale(${w2})`}>
          <text x="6" y="10" fontFamily="'Archivo Black'" fontSize="168" fill={INK} textAnchor="middle" opacity="0.5">GCM PHB</text>
          <text x="0" y="0" fontFamily="'Archivo Black'" fontSize="168" fill="#FFFFFF" textAnchor="middle">GCM PHB</text>
        </g>
        <g transform={`translate(540 1530) scale(${w3 * (1 + hit * 0.06)})`}>
          <text x="6" y="10" fontFamily="'Archivo Black'" fontSize="200" fill={INK} textAnchor="middle" opacity="0.5">2027</text>
          <text x="0" y="0" fontFamily="'Archivo Black'" fontSize="200" fill={C.gold} textAnchor="middle" stroke={INK} strokeWidth="6" paintOrder="stroke">2027</text>
        </g>
        <g clipPath="url(#s12txt)"><rect x={sweep} y="1060" width="400" height="480" fill="url(#s12sw)" transform="skewX(-20)" style={{mixBlendMode: 'overlay'}} /></g>
        <g transform="translate(540 1720)">
          <text x="0" y="0" fontFamily="InterV, Inter, sans-serif" fontWeight="800" fontSize="68" textAnchor="middle">
            {words.map(([w, at], i) => <tspan key={w} fill={i === 3 ? C.gold : '#FFFFFF'} fillOpacity={kf(t, [at - 0.05, at + 0.2], [0, 1], 'o')}>{w}{i < 3 ? ' ' : ''}</tspan>)}
          </text>
        </g>
      </Camera>
      <Finish vignette={0.9} />
    </Frame>
  );
};
