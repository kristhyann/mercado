import React from 'react';
import {random, useCurrentFrame} from 'remotion';
import {INK, C, W, H, FPS, Frame, Finish, Camera, Glow, Dust, Beam, kf, useST, lerp, clamp01} from '../kit.jsx';
import {LucasBusto} from '../rigs/LucasBusto.jsx';
import {mixExpr, DIEGO, CELIA, ANTONIO, DIPLOMATA, MENINO, TURISTA, VEREADORA} from '../rigs/lucas.js';
import {Shield, DawnSky} from './Final.jsx';
import {NAVY, NAVY2, YEL, WHITE} from './Reels.jsx';
import {QuestionScreen, QTitle, Rays, Card, Temple} from './Quiz.jsx';
import {QT, META} from '../questions.js';
import {WORDS} from '../words.js';

const UI = 'InterV, Inter, sans-serif';
const HEAD = "'Archivo Black', sans-serif";
const GREEN = '#2EB872', RED = '#E5484D';
const L0 = {side: 1, color: '#FFFFFF', rim: 0.6};

// ---------------------------------------------------------------- captions (hook, situations, final challenge)
const WINDOWS = [[0, 8.0], ...QT.map((q) => [q.scene, q.q - 0.05]), [META.desafio, META.projeto - 0.05]];
const CHUNKS = (() => {
  const out = [];
  for (const [a, b] of WINDOWS) {
    let cur = [];
    const ws = WORDS.filter((w) => w.s >= a && w.s < b);
    ws.forEach((w, i) => {
      cur.push(w);
      if (cur.length >= 3 || /[.,?!]$/.test(w.w) || i === ws.length - 1) {out.push({words: cur, win: b}); cur = [];}
    });
  }
  return out.map((c, i) => {
    const n = out[i + 1];
    const end = n && n.words[0].s < c.win ? n.words[0].s : Math.min(c.win, c.words[c.words.length - 1].e + 0.35);
    return {...c, start: c.words[0].s - 0.05, end: end - 0.05};
  });
})();
const fix = (s) => s.toUpperCase().replace('SÉLIA', 'CÉLIA').replace('4º', '4º');
export const Captions2 = () => {
  const t = useCurrentFrame() / FPS;
  const c = CHUNKS.find((x) => t >= x.start && t < x.end);
  if (!c) return null;
  const pop = kf(t, [c.start, c.start + 0.12], [0.86, 1], 'back');
  const txt = c.words.map((w) => fix(w.w)).join(' ');
  return (
    <svg viewBox={`0 0 ${W} ${H}`} width={W} height={H} style={{position: 'absolute', inset: 0}}>
      <g transform={`translate(540 1540) scale(${pop})`}>
        <text textAnchor="middle" fontFamily={HEAD} fontSize={txt.length > 26 ? 56 : 66} fill={NAVY} stroke={NAVY} strokeWidth="18" strokeLinejoin="round">{txt}</text>
        <text textAnchor="middle" fontFamily={HEAD} fontSize={txt.length > 26 ? 56 : 66}>
          {c.words.map((w, i) => {
            const on = t >= w.s - 0.04;
            const cur = on && (i === c.words.length - 1 || t < c.words[i + 1].s - 0.04);
            return <tspan key={i} fill={cur ? YEL : WHITE} fillOpacity={on ? 1 : 0.5}>{fix(w.w)}{i < c.words.length - 1 ? ' ' : ''}</tspan>;
          })}
        </text>
      </g>
    </svg>
  );
};

// ---------------------------------------------------------------- helpers
const Bust = ({x, y, s = 1, ...p}) => <g transform={`translate(${x} ${y}) scale(${s})`}><LucasBusto {...p} /></g>;
const Bubble = ({x, y, text, k = 1, w = 160}) => (
  <g transform={`translate(${x} ${y}) scale(${k})`} opacity={clamp01(k * 2)}>
    <path d={`M${-w / 2} -60 Q${-w / 2} -100 ${-w / 2 + 40} -100 L${w / 2 - 40} -100 Q${w / 2} -100 ${w / 2} -60 L${w / 2} -20 Q${w / 2} 20 ${w / 2 - 40} 20 L10 20 L-20 60 L-14 20 L${-w / 2 + 40} 20 Q${-w / 2} 20 ${-w / 2} -20Z`} fill={WHITE} stroke={INK} strokeWidth="7" />
    <text y="-22" fontFamily={HEAD} fontSize="62" fill={NAVY} textAnchor="middle">{text}</text>
  </g>
);
// stylised outline of Brazil (normalised 0..1)
const BR = [[0.05, 0.3], [0.12, 0.22], [0.2, 0.2], [0.25, 0.12], [0.33, 0.1], [0.4, 0.05], [0.47, 0.08], [0.55, 0.06], [0.6, 0.12], [0.66, 0.16], [0.72, 0.18], [0.8, 0.22], [0.88, 0.26], [0.97, 0.33], [0.95, 0.4], [0.88, 0.48], [0.84, 0.56], [0.8, 0.66], [0.72, 0.74], [0.64, 0.8], [0.56, 0.86], [0.5, 0.93], [0.45, 0.99], [0.4, 0.94], [0.43, 0.86], [0.38, 0.8], [0.36, 0.7], [0.3, 0.62], [0.28, 0.52], [0.2, 0.46], [0.12, 0.44], [0.06, 0.38]];
const brPath = (sz) => 'M' + BR.map(([x, y]) => `${(x - 0.5) * sz} ${(y - 0.5) * sz}`).join(' L') + 'Z';
const BrazilMap = ({sz = 700, fill = '#7FB58A', lines = true, glow = 0, pieceOut = 0}) => (
  <g>
    <clipPath id={`brc${sz}`}><path d={brPath(sz)} /></clipPath>
    <path d={brPath(sz)} fill={fill} stroke={INK} strokeWidth="8" strokeLinejoin="round" />
    {lines && <g clipPath={`url(#brc${sz})`} stroke={INK} strokeWidth="4" opacity="0.5" fill="none">
      {[-0.25, -0.05, 0.12, 0.3].map((v) => <path key={'h' + v} d={`M${-sz} ${v * sz} Q0 ${v * sz + 30} ${sz} ${v * sz - 20}`} />)}
      {[-0.3, -0.1, 0.1, 0.25].map((v) => <path key={'v' + v} d={`M${v * sz} ${-sz} Q${v * sz + 40} 0 ${v * sz - 20} ${sz}`} />)}
    </g>}
    {glow > 0 && <path d={brPath(sz)} fill="none" stroke={YEL} strokeWidth={10 + glow * 10} opacity={glow} />}
  </g>
);
const sceneBg = (col1, col2, id) => (
  <g><defs><linearGradient id={id} x1="0" y1="0" x2="0" y2="1"><stop offset="0" stopColor={col1} /><stop offset="1" stopColor={col2} /></linearGradient></defs>
    <rect x="-300" y="-300" width="1700" height="2600" fill={`url(#${id})`} /><rect x="-300" y="-300" width="1700" height="2600" filter="url(#paperTex)" opacity="0.35" /></g>
);

// ---------------------------------------------------------------- hook
export const Hook = ({dur}) => {
  const t = useST();
  const a = kf(t, [0.0, 0.25], [0, 1], 'back');
  const b = kf(t, [0.75, 1.0], [0, 1], 'back');
  const c = kf(t, [3.85, 4.1], [0, 1], 'back');
  const d = kf(t, [6.6, 6.85], [0, 1], 'back');
  return (
    <Frame bg={NAVY}>
      <Camera z={kf(t, [0, dur], [1.0, 1.08])}>
        <rect x="-300" y="-300" width="1700" height="2600" fill={NAVY} />
        <Rays t={t} cy={820} />
        <g transform="translate(540 170)"><rect x="-330" y="-40" width="660" height="70" rx="35" fill={YEL} /><text y="12" fontFamily={UI} fontWeight="900" fontSize="34" fill={NAVY} textAnchor="middle">QUIZ 01 · DIREITO CONSTITUCIONAL</text></g>
        <g transform={`translate(300 620) scale(${a})`}>
          <g transform="scale(0.42) translate(0 300)"><Temple t={t} cols={4} /></g>
          <text y="200" fontFamily={HEAD} fontSize="58" fill={WHITE} textAnchor="middle">FUNDAMENTO</text>
        </g>
        <g transform={`translate(540 640) scale(${b})`}><circle r="70" fill={YEL} stroke={INK} strokeWidth="8" /><text y="24" fontFamily={HEAD} fontSize="70" fill={NAVY} textAnchor="middle">OU</text></g>
        <g transform={`translate(790 620) scale(${b})`}>
          <rect x="-10" y="-60" width="20" height="200" fill="#8A93B5" stroke={INK} strokeWidth="5" />
          <path d="M-150 -170 L110 -170 L150 -110 L110 -50 L-150 -50Z" fill={YEL} stroke={INK} strokeWidth="7" />
          <text x="-20" y="-96" fontFamily={HEAD} fontSize="40" fill={NAVY} textAnchor="middle">META</text>
          <text y="200" fontFamily={HEAD} fontSize="58" fill={WHITE} textAnchor="middle">OBJETIVO</text>
        </g>
        <g transform={`translate(540 1020) scale(${c})`}><text fontFamily={HEAD} fontSize="92" fill={WHITE} textAnchor="middle" stroke={INK} strokeWidth="10" paintOrder="stroke">10 DESAFIOS</text></g>
        <g transform={`translate(540 1210) scale(${d}) rotate(-5)`}>
          <rect x="-430" y="-80" width="860" height="140" rx="20" fill={YEL} stroke={INK} strokeWidth="8" />
          <text y="22" fontFamily={HEAD} fontSize="62" fill={NAVY} textAnchor="middle">VOCÊ É DO GRUPO QUE ERRA?</text>
        </g>
      </Camera>
      <Finish vignette={0.9} />
    </Frame>
  );
};

// ---------------------------------------------------------------- Q2 · bus station departures board
export const SQ2 = ({dur}) => {
  const t = useST();
  return (
    <Frame bg="#2B3550">
      <Camera z={kf(t, [0, dur], [1.0, 1.12])} y={kf(t, [0, dur], [0, -60])}>
        {sceneBg('#3A4570', '#1F2A4D', 'q2bg')}
        <g transform="translate(540 560)">
          <rect x="-460" y="-300" width="920" height="600" rx="20" fill="#14171F" stroke={INK} strokeWidth="10" />
          <text y="-215" fontFamily={HEAD} fontSize="50" fill={YEL} textAnchor="middle">DESTINOS DA REPÚBLICA</text>
          {[0, 1, 2, 3].map((i) => {
            const flip = Math.floor(((t * 6) + i * 2) % 4);
            return (
              <g key={i} transform={`translate(0 ${-120 + i * 120})`}>
                <rect x="-420" y="-46" width="840" height="92" rx="10" fill="#22262F" />
                <text x="-390" y="18" fontFamily="JBMono, monospace" fontSize="52" fontWeight="800" fill={YEL}>{'ABCD'[i]}</text>
                {[0, 1, 2, 3, 4, 5, 6, 7, 8].map((j) => <rect key={j} x={-320 + j * 62} y="-34" width="52" height="68" rx="6" fill="#2E333E" stroke="#111" strokeWidth="3" />)}
                {[0, 1, 2, 3, 4, 5, 6, 7, 8].map((j) => <text key={j} x={-294 + j * 62} y="18" fontFamily="JBMono, monospace" fontSize="44" fontWeight="800" fill={WHITE} textAnchor="middle">{t < 1.2 + i * 0.3 ? 'ZQXKWMPRT'[(j + flip + i) % 9] : '?'}</text>)}
                <text x="380" y="16" fontFamily={UI} fontSize="30" fontWeight="900" fill={i === 0 && Math.sin(t * 8) > 0 ? GREEN : '#8A93B5'} textAnchor="end">PLAT. {i + 1}</text>
              </g>
            );
          })}
        </g>
        <path d="M-300 1300 L1400 1300 L1400 2300 L-300 2300Z" fill="#545B70" />
        {Array.from({length: 8}).map((_, i) => <path key={i} d={`M${-300 + i * 240} 1300 L${-500 + i * 300} 2300`} stroke={INK} strokeWidth="4" opacity="0.4" />)}
        <Bust x={540} y={1620} s={1.0} t={t} id="q2d" pal={DIEGO} hair="liso" outfit="tee" expr={mixExpr('neutro', 'perdido', kf(t, [2.5, 3.5], [0, 1]))} turn={0.1} look={{x: Math.sin(t * 2) * 0.5, y: -0.8}} light={{side: 1, color: '#FFE9A8', rim: 0.7}} />
        <path d="M300 1500 Q260 1700 330 1900 L180 1900 Q150 1700 200 1480Z" fill="#23304F" stroke={INK} strokeWidth="7" />
        <g transform={`translate(800 1660) rotate(${-12 + Math.sin(t * 3) * 3})`}><rect x="-90" y="-50" width="180" height="100" rx="10" fill="#FBF6EA" stroke={INK} strokeWidth="6" /><text y="12" fontFamily={UI} fontWeight="900" fontSize="30" fill={NAVY} textAnchor="middle">BILHETE</text></g>
      </Camera>
      <Finish vignette={0.8} />
    </Frame>
  );
};

// ---------------------------------------------------------------- Q3 · international conference
export const SQ3 = ({dur}) => {
  const t = useST();
  const flashes = [0.9, 2.2, 3.1, 4.6].filter((f) => t > f && t < f + 0.15).length;
  const flags = ['#2E9E5B', '#D94B45', '#2F5D8C', '#F2C230', '#6B4C8A', '#E07B2E'];
  return (
    <Frame bg="#1C2547">
      <Camera z={kf(t, [0, dur], [1.0, 1.15])} y={kf(t, [0, dur], [0, -100])}>
        {sceneBg('#2A3566', '#151C3A', 'q3bg')}
        <g transform="translate(540 330)"><rect x="-430" y="-80" width="860" height="150" rx="16" fill="#E8E2D2" stroke={INK} strokeWidth="8" /><text y="-12" fontFamily={HEAD} fontSize="46" fill={NAVY} textAnchor="middle">CONFERÊNCIA</text><text y="44" fontFamily={HEAD} fontSize="40" fill={NAVY} textAnchor="middle">INTERNACIONAL</text></g>
        {flags.map((f, i) => (
          <g key={i} transform={`translate(${130 + i * 165} 560)`}>
            <rect x="-4" y="0" width="8" height="300" fill="#C9CFD8" stroke={INK} strokeWidth="3" />
            <path d={`M4 10 Q60 ${20 + Math.sin(t * 3 + i) * 12} 110 10 L110 90 Q60 ${100 + Math.sin(t * 3 + i) * 12} 4 90Z`} fill={f} stroke={INK} strokeWidth="5" />
          </g>
        ))}
        <ellipse cx="540" cy="1390" rx="720" ry="170" fill="#7A4E35" stroke={INK} strokeWidth="8" />
        <Bust x={540} y={1560} s={1.0} t={t} id="q3r" pal={DIPLOMATA} hair="coque" outfit="polo" expr={mixExpr('neutro', 'focado', kf(t, [1.5, 2.5], [0, 1]))} look={{x: 0, y: kf(t, [0, 3], [0.7, 0])}} light={{side: 1, color: '#FFFFFF', rim: 0.7}} />
        <g transform="translate(540 1330)"><rect x="-8" y="-150" width="16" height="150" fill="#333" /><ellipse cx="0" cy="-160" rx="26" ry="36" fill="#222" stroke={INK} strokeWidth="5" /></g>
        <g transform="translate(250 1420) rotate(-8)">{[0, 1, 2, 3].map((i) => <g key={i} transform={`translate(${i * 40} ${-i * 6})`}><rect x="-70" y="-90" width="140" height="180" rx="10" fill={WHITE} stroke={INK} strokeWidth="5" /><text y="16" fontFamily={HEAD} fontSize="50" fill={NAVY} textAnchor="middle">{'ABCD'[i]}</text></g>)}</g>
        <rect x="-300" y="1440" width="1700" height="800" fill="#141B33" />
      </Camera>
      {flashes > 0 && <rect width={W} height={H} fill="#fff" opacity="0.35" />}
      <Finish vignette={0.9} />
    </Frame>
  );
};

// ---------------------------------------------------------------- Q4 · Praça dos Três Poderes
export const SQ4 = ({dur}) => {
  const t = useST();
  const point = kf(t, [0.9, 1.4], [0, 1]);
  const sweep = Math.sin(t * 1.4) * 0.5;
  return (
    <Frame bg="#9CC8E8">
      <Camera z={kf(t, [0, dur], [1.0, 1.08])} x={kf(t, [0, dur], [-30, 30])}>
        {sceneBg('#8FBDE6', '#DDEBF7', 'q4bg')}
        {/* Congress: two towers + bowls */}
        <g transform="translate(540 900)">
          <rect x="-40" y="-420" width="34" height="420" fill="#E3E7EE" stroke={INK} strokeWidth="6" />
          <rect x="6" y="-420" width="34" height="420" fill="#D3D8E2" stroke={INK} strokeWidth="6" />
          <rect x="-48" y="-300" width="96" height="16" fill="#C9CFD8" stroke={INK} strokeWidth="4" />
          <path d="M-330 -10 Q-250 -150 -170 -10Z" fill="#EEF1F6" stroke={INK} strokeWidth="6" />
          <path d="M170 -110 Q250 30 330 -110Z" fill="#EEF1F6" stroke={INK} strokeWidth="6" />
          <rect x="-420" y="-10" width="840" height="30" fill="#D3D8E2" stroke={INK} strokeWidth="6" />
        </g>
        <g transform="translate(150 1060)"><rect x="-130" y="-90" width="260" height="90" fill="#F4F6FA" stroke={INK} strokeWidth="6" />{[0, 1, 2, 3, 4].map((i) => <path key={i} d={`M${-110 + i * 55} 0 Q${-90 + i * 55} -60 ${-110 + i * 55} -90`} stroke={INK} strokeWidth="5" fill="none" />)}</g>
        <g transform="translate(930 1060)"><rect x="-120" y="-90" width="240" height="90" fill="#F4F6FA" stroke={INK} strokeWidth="6" />{[0, 1, 2, 3].map((i) => <path key={i} d={`M${-90 + i * 60} 0 L${-90 + i * 60} -90`} stroke={INK} strokeWidth="5" />)}</g>
        {[0, 1, 2].map((i) => <g key={i} transform={`translate(${760 + i * 120} 900)`} opacity="0.55"><rect x="-40" y="-120" width="80" height="120" fill="#B9C2D0" stroke={INK} strokeWidth="4" /></g>)}
        <rect x="-300" y="1060" width="1700" height="1200" fill="#E7DFC9" />
        <Bubble x={720} y={1180} text="PODER?" k={kf(t, [2.6, 2.9], [0, 1], 'back')} w={300} />
        <Bust x={420} y={1720} s={0.72} t={t} id="q4m" pal={MENINO} hair="crespo" outfit="tee" expr={mixExpr('neutro', 'desejo', point)} turn={0.4} look={{x: 0.8 + sweep * 0.2, y: -0.6}} light={L0}
          arms={{r: [lerp(10, 130, point), lerp(-10, 150 + sweep * 20, point), null, 1]}} />
      </Camera>
      <Finish vignette={0.6} />
    </Frame>
  );
};

// ---------------------------------------------------------------- Q5 · votes, then signs a popular-initiative bill
export const SQ5 = ({dur}) => {
  const t = useST();
  const CUT = 2.45;
  if (t < CUT) {
    const press = kf(t, [1.4, 1.6], [0, 1]);
    return (
      <Frame bg="#E9E1D2">
        <Camera z={kf(t, [0, CUT], [1.0, 1.1])}>
          {sceneBg('#EDE6D6', '#D8CDB4', 'q5a')}
          <rect x="140" y="420" width="800" height="1000" fill="#B8C4D6" stroke={INK} strokeWidth="8" />
          <g transform="translate(700 1100)">
            <rect x="-230" y="-200" width="460" height="320" rx="16" fill="#E8E4D8" stroke={INK} strokeWidth="8" />
            <rect x="-200" y="-170" width="220" height="150" fill="#2F3A5C" stroke={INK} strokeWidth="5" />
            <text x="-90" y="-80" fontFamily={UI} fontWeight="900" fontSize="34" fill={press > 0.5 ? GREEN : WHITE} textAnchor="middle">{press > 0.5 ? 'FIM' : 'VOTO'}</text>
            {Array.from({length: 9}).map((_, i) => <rect key={i} x={50 + (i % 3) * 52} y={-170 + Math.floor(i / 3) * 46} width="44" height="38" rx="6" fill="#1E1E24" />)}
            <rect x="50" y="-30" width="150" height="40" rx="6" fill={GREEN} stroke={INK} strokeWidth="4" />
            <text x="125" y="-2" fontFamily={UI} fontWeight="900" fontSize="18" fill={WHITE} textAnchor="middle">CONFIRMA</text>
          </g>
          <Bust x={360} y={1620} s={1.0} t={t} id="q5c" pal={CELIA} hair="coque" outfit="tee" glasses expr="confiante" turn={0.35} look={{x: 0.8, y: 0.4}} light={L0}
            arms={{r: [lerp(30, 80, press), lerp(110, 100, press), null, 1]}} />
        </Camera>
        <Finish vignette={0.6} />
      </Frame>
    );
  }
  const u = t - CUT;
  const sign = kf(u, [1.6, 3.0], [0, 1]);
  return (
    <Frame bg="#F29A5A">
      <Camera z={kf(u, [0, dur - CUT], [1.0, 1.1])}>
        <g transform="translate(0 100)"><DawnSky t={t} sunY={600} id="q5sky" /></g>
        <rect x="-300" y="1200" width="1700" height="1200" fill="#C9B9A8" />
        <g transform="translate(560 1040) rotate(-4)">
          <rect x="-260" y="-340" width="520" height="680" rx="14" fill="#6A4A35" stroke={INK} strokeWidth="8" />
          <rect x="-230" y="-300" width="460" height="620" fill="#FBF8F0" stroke={INK} strokeWidth="5" />
          <text y="-230" fontFamily={HEAD} fontSize="30" fill={NAVY} textAnchor="middle">PROJETO DE LEI DE</text>
          <text y="-190" fontFamily={HEAD} fontSize="30" fill={NAVY} textAnchor="middle">INICIATIVA POPULAR</text>
          {Array.from({length: 8}).map((_, i) => <g key={i}><path d={`M-190 ${-120 + i * 52} L190 ${-120 + i * 52}`} stroke="#C9C3B6" strokeWidth="3" />{i < 6 && <path d={`M-180 ${-130 + i * 52} q30 -20 60 0 t60 0 t40 -10`} stroke="#2F5D8C" strokeWidth="4" fill="none" />}</g>)}
          <path d={`M-180 ${-130 + 6 * 52} q30 -20 60 0 t60 0 t40 -10`} stroke="#C9473F" strokeWidth="5" fill="none" strokeDasharray="220" strokeDashoffset={220 * (1 - sign)} />
        </g>
        <Bust x={330} y={1700} s={0.95} t={t} id="q5c2" pal={CELIA} hair="coque" outfit="tee" glasses expr="focado" turn={0.4} look={{x: 0.7, y: 0.7}} light={{side: -1, color: '#FFD27A', rim: 0.8}} />
      </Camera>
      <Finish vignette={0.6} />
    </Frame>
  );
};

// ---------------------------------------------------------------- Q6 · puzzle map that won't come apart
export const SQ6 = ({dur}) => {
  const t = useST();
  const pull = kf(t, [1.3, 2.4, 3.2, 3.7], [0, 1, 1, 0]);
  const glow = kf(t, [2.3, 2.8], [0, 1]);
  return (
    <Frame bg="#7A5A40">
      <Camera z={kf(t, [0, dur], [1.0, 1.15])} r={kf(t, [0, dur], [-3, 1])}>
        <rect x="-300" y="-300" width="1700" height="2600" fill="#8C6A4E" />
        {Array.from({length: 9}).map((_, i) => <rect key={i} x="-300" y={-300 + i * 300} width="1700" height="296" fill={i % 2 ? '#86654A' : '#926F52'} />)}
        <g transform="translate(540 860)">
          <rect x="-450" y="-460" width="900" height="920" rx="16" fill="#2F5D8C" stroke={INK} strokeWidth="9" />
          <BrazilMap sz={820} glow={glow} />
          <g transform={`translate(${170 + pull * 40} ${-120 - pull * 30}) rotate(${pull * 6})`}>
            <path d="M-60 -50 L20 -60 Q40 -90 60 -60 L70 20 Q100 40 70 60 L-50 60 Q-70 30 -60 -50Z" fill="#8FC79A" stroke={glow > 0.3 ? YEL : INK} strokeWidth="7" />
          </g>
        </g>
        <g transform={`translate(${780 + pull * 60} ${700 - pull * 20}) rotate(-30)`}>
          <path d="M-60 0 L-50 700 L70 700 L80 0Z" fill="#B07A55" stroke={INK} strokeWidth="8" />
          <path d="M-80 10 Q-90 -110 -30 -140 Q30 -150 70 -110 Q90 -60 80 10Z" fill="#B07A55" stroke={INK} strokeWidth="8" />
          <path d="M-60 140 L80 140 L80 340 L-56 340Z" fill="#F2C230" stroke={INK} strokeWidth="8" />
        </g>
        {glow > 0 && <Dust t={t} n={30} x={300} y={500} w={500} h={500} color={YEL} size={5} rise={30} seed="q6d" />}
      </Camera>
      <Finish vignette={0.8} />
    </Frame>
  );
};

// ---------------------------------------------------------------- Q7 · museum: crown of the past, federal map
export const SQ7 = ({dur}) => {
  const t = useST();
  const pan = kf(t, [2.6, 3.4], [0, 1], 'io');
  return (
    <Frame bg="#3A2E3A">
      <Camera z={1.05} x={lerp(-240, 260, pan)}>
        {sceneBg('#4A3A48', '#2A202A', 'q7bg')}
        <rect x="-300" y="1300" width="1900" height="1000" fill="#5A4636" />
        {/* crown display */}
        <g transform="translate(300 1000)">
          <rect x="-200" y="0" width="400" height="300" fill="#6A5446" stroke={INK} strokeWidth="7" />
          <rect x="-180" y="-360" width="360" height="360" fill="#BFD8FF" opacity="0.18" stroke={INK} strokeWidth="6" />
          <g transform="translate(0 -150)">
            <path d="M-110 60 L-120 -40 L-60 10 L0 -70 L60 10 L120 -40 L110 60Z" fill={C.gold} stroke={INK} strokeWidth="7" />
            {[-80, 0, 80].map((x) => <circle key={x} cx={x} cy="30" r="12" fill={RED} stroke={INK} strokeWidth="4" />)}
          </g>
          <rect x="-90" y="40" width="180" height="60" fill="#E8E2D2" stroke={INK} strokeWidth="5" />
          <text y="82" fontFamily={HEAD} fontSize="36" fill={NAVY} textAnchor="middle">1889</text>
          <Glow id="q7g" x={0} y={-150} r={260} color="#FFE9A8" opacity={0.35} />
        </g>
        {/* federal map */}
        <g transform="translate(900 820)">
          <rect x="-300" y="-300" width="600" height="600" fill="#E8E2D2" stroke={C.gold} strokeWidth="18" />
          <BrazilMap sz={500} glow={kf(t, [3.6, 4.2], [0, 1]) * (0.6 + 0.4 * Math.sin(t * 6))} />
        </g>
        <Bust x={600} y={1760} s={0.85} t={t} id="q7l" outfit="tee" expr="focado" turn={lerp(-0.5, 0.5, pan)} look={{x: lerp(-0.8, 0.8, pan), y: -0.4}} light={{side: 1, color: '#FFE9A8', rim: 0.7}} />
      </Camera>
      <Finish vignette={1} />
    </Frame>
  );
};

// ---------------------------------------------------------------- Q8 · airport: a tourist asks Lucas
export const SQ8 = ({dur}) => {
  const t = useST();
  const plane = kf(t, [0, dur], [-200, 1300], 'lin');
  return (
    <Frame bg="#BFD8EE">
      <Camera z={kf(t, [0, dur], [1.0, 1.1])}>
        {sceneBg('#9CC8E8', '#E3EEF7', 'q8bg')}
        <g transform={`translate(${plane} ${380 - plane * 0.12})`}>
          <path d="M-160 0 L140 -10 Q180 0 140 14 L-160 18Z" fill={WHITE} stroke={INK} strokeWidth="5" />
          <path d="M-20 0 L-80 -70 L-50 -70 L40 0Z M-20 10 L-70 70 L-40 70 L40 10Z" fill="#D3D8E2" stroke={INK} strokeWidth="4" />
          <path d="M-150 0 L-180 -50 L-150 -50 L-120 0Z" fill={RED} stroke={INK} strokeWidth="4" />
        </g>
        {[0, 1, 2, 3, 4].map((i) => <rect key={i} x={-60 + i * 260} y="140" width="14" height="900" fill="#5D6270" />)}
        <rect x="-300" y="1040" width="1700" height="40" fill="#5D6270" stroke={INK} strokeWidth="6" />
        <rect x="-300" y="1080" width="1700" height="1200" fill="#D8D4CC" />
        <g transform="translate(540 1000)"><rect x="-260" y="-70" width="520" height="90" rx="10" fill={NAVY} stroke={INK} strokeWidth="6" /><text y="-10" fontFamily={HEAD} fontSize="44" fill={YEL} textAnchor="middle">CHEGADAS</text></g>
        <Bubble x={300} y={1150} text="CAPITAL?" k={kf(t, [1.1, 1.4], [0, 1], 'back')} w={360} />
        <Bust x={290} y={1680} s={0.95} t={t} id="q8t" pal={TURISTA} hair="liso" outfit="tee" expr="desejo" turn={0.45} look={{x: 0.8, y: 0}} light={L0} />
        <g transform="translate(150 1520)"><rect x="-60" y="-40" width="120" height="80" rx="12" fill="#2A2F3E" stroke={INK} strokeWidth="5" /><circle r="26" fill="#5D6270" stroke={INK} strokeWidth="4" /></g>
        <Bust x={800} y={1700} s={0.95} t={t} id="q8l" outfit="tee" expr={mixExpr('neutro', 'focado', kf(t, [2.2, 3], [0, 1]))} turn={-0.45} look={{x: -0.8, y: 0}} light={L0} />
      </Camera>
      <Finish vignette={0.6} />
    </Frame>
  );
};

// ---------------------------------------------------------------- Q9 · Parnaíba city council approves a local law
export const SQ9 = ({dur}) => {
  const t = useST();
  const ok = kf(t, [1.2, 1.5], [0, 1], 'back');
  const rep = kf(t, [2.9, 3.4], [600, 0], 'o');
  return (
    <Frame bg="#3A2A2A">
      <Camera z={kf(t, [0, dur], [1.0, 1.1])}>
        {sceneBg('#6A4A35', '#3E2A20', 'q9bg')}
        <g transform="translate(540 300)"><rect x="-430" y="-70" width="860" height="130" rx="14" fill="#E8E2D2" stroke={INK} strokeWidth="7" /><text y="18" fontFamily={HEAD} fontSize="50" fill={NAVY} textAnchor="middle">CÂMARA DE PARNAÍBA</text></g>
        <g transform="translate(540 640)">
          <rect x="-300" y="-150" width="600" height="300" rx="14" fill="#101828" stroke={INK} strokeWidth="8" />
          <text y="-70" fontFamily={UI} fontWeight="900" fontSize="36" fill="#8A93B5" textAnchor="middle">VOTAÇÃO · LEI LOCAL</text>
          <g transform={`scale(${ok})`}><text y="40" fontFamily={HEAD} fontSize="80" fill={GREEN} textAnchor="middle">APROVADA</text></g>
        </g>
        <rect x="-300" y="1150" width="1700" height="1200" fill="#7A4E35" stroke={INK} strokeWidth="8" />
        <Bust x={400} y={1650} s={0.95} t={t} id="q9v" pal={VEREADORA} hair="coque" outfit="polo" expr={mixExpr('confiante', 'focado', kf(t, [3.5, 4.5], [0, 1]))} turn={0.35} look={{x: kf(t, [3, 3.6], [0, 0.8]), y: 0}} light={L0} />
        <g transform={`translate(${rep} 0)`}>
          <Bust x={860} y={1700} s={0.9} t={t} id="q9r" pal={DIEGO} hair="liso" outfit="tee" expr="desejo" turn={-0.4} look={{x: -0.8, y: 0}} light={L0} arms={{l: [-30, 120, null, 1]}} />
          <g transform="translate(700 1500) rotate(-30)"><rect x="-14" y="0" width="28" height="140" rx="10" fill="#222" stroke={INK} strokeWidth="5" /><circle cy="-10" r="34" fill="#444" stroke={INK} strokeWidth="6" /><rect x="-30" y="40" width="60" height="40" fill={YEL} stroke={INK} strokeWidth="4" /></g>
        </g>
        <Bubble x={640} y={1150} text="PERMISSÃO?" k={kf(t, [3.6, 3.9], [0, 1], "back")} w={440} />
      </Camera>
      <Finish vignette={0.8} />
    </Frame>
  );
};

// ---------------------------------------------------------------- Q10 · grandpa's 1993 plebiscite receipt (sepia flashback)
export const SQ10 = ({dur}) => {
  const t = useST();
  const open = kf(t, [0.4, 1.2], [0, 1], 'o');
  const sepia = kf(t, [2.6, 3.0], [0, 1]);
  return (
    <Frame bg="#3A2E26">
      <Camera z={kf(t, [0, dur], [1.0, 1.12])}>
        {sceneBg('#5A4636', '#2E241C', 'q10bg')}
        <Glow id="q10g" x={300} y={500} r={700} color={C.lamp} opacity={0.35} />
        <Bust x={360} y={1500} s={1.0} t={t} id="q10a" pal={ANTONIO} hair="crespo" outfit="polo" glasses expr="confiante" turn={0.35} look={{x: 0.7, y: 0.5}} light={{side: 1, color: C.lamp, rim: 0.7}} />
        <rect x="-300" y="1300" width="1700" height="1000" fill="#4F3122" stroke={INK} strokeWidth="8" />
        <g transform="translate(720 1330)">
          <path d="M-220 0 L220 0 L200 180 L-200 180Z" fill="#8E5C3A" stroke={INK} strokeWidth="7" />
          <path d={`M-220 0 L220 0 L${200} ${-160 * open} L${-200} ${-160 * open}Z`} fill="#A06A44" stroke={INK} strokeWidth="7" />
        </g>
        <g transform={`translate(720 ${1300 - open * 360}) rotate(${-6 + open * 4}) scale(${0.6 + open * 0.5})`} opacity={open}>
          <rect x="-230" y="-140" width="460" height="280" rx="10" fill="#F1E2B8" stroke={INK} strokeWidth="7" />
          <text y="-70" fontFamily={HEAD} fontSize="34" fill="#5A4636" textAnchor="middle">PLEBISCITO</text>
          <text y="-24" fontFamily={HEAD} fontSize="44" fill="#5A4636" textAnchor="middle">1993</text>
          <text y="30" fontFamily={UI} fontWeight="800" fontSize="24" fill="#7A6450" textAnchor="middle">COMPROVANTE DE VOTAÇÃO</text>
          {[70, 100].map((y) => <rect key={y} x="-170" y={y} width="340" height="12" rx="6" fill="#C9B48A" />)}
        </g>
      </Camera>
      {sepia > 0 && <rect width={W} height={H} fill="#B8864F" opacity={sepia * 0.35} style={{mixBlendMode: 'multiply'}} />}
      {sepia > 0 && <g opacity={sepia}>{Array.from({length: 30}).map((_, i) => <line key={i} x1={random('sc' + i) * W} y1="0" x2={random('sc' + i) * W + 8} y2={H} stroke="#3A2E26" strokeWidth="2" opacity={Math.sin(t * 20 + i) > 0.6 ? 0.3 : 0} />)}</g>}
      <Finish vignette={1.1} />
    </Frame>
  );
};

// ---------------------------------------------------------------- final challenge
export const Desafio = ({dur}) => {
  const t = useST();
  const a = kf(t, [0.0, 0.3], [0, 1], 'back');
  const typing = Math.floor(kf(t, [9.3, 10.8], [0, 18], 'lin'));
  return (
    <Frame bg={NAVY}>
      <rect width={W} height={H} fill={NAVY} />
      <Rays t={t} cy={700} />
      <Glow id="dg" x={540} y={700} r={600} color={YEL} opacity={0.2} />
      <g transform={`translate(540 360) scale(${a})`}>
        <rect x="-380" y="-90" width="760" height="160" rx="24" fill={YEL} stroke={INK} strokeWidth="8" />
        <text y="22" fontFamily={HEAD} fontSize="80" fill={NAVY} textAnchor="middle">DESAFIO FINAL</text>
      </g>
      <g opacity={kf(t, [1.2, 1.6], [0, 1])}>
        <text x="540" y="560" fontFamily={UI} fontWeight="900" fontSize="44" fill={WHITE} textAnchor="middle">Sem olhar a Constituição:</text>
        <text x="540" y="650" fontFamily={HEAD} fontSize="58" fill={YEL} textAnchor="middle">art. 4º, parágrafo único</text>
      </g>
      <g opacity={kf(t, [3.2, 3.6], [0, 1])} transform="translate(540 900)">
        <text y="0" fontFamily={UI} fontWeight="800" fontSize="44" fill={WHITE} textAnchor="middle">O que ele diz sobre o Brasil</text>
        <text y="60" fontFamily={UI} fontWeight="800" fontSize="44" fill={WHITE} textAnchor="middle">e os povos da América Latina?</text>
      </g>
      <g opacity={kf(t, [9.0, 9.4], [0, 1])} transform="translate(540 1200)">
        <rect x="-420" y="-70" width="840" height="140" rx="70" fill={WHITE} stroke={INK} strokeWidth="7" />
        <text x="-360" y="16" fontFamily={UI} fontWeight="700" fontSize="40" fill="#55607A">{'Escreva aqui sua resposta'.slice(0, typing + 7)}{Math.sin(t * 10) > 0 ? '|' : ''}</text>
        <circle cx="350" cy="0" r="48" fill={YEL} stroke={INK} strokeWidth="5" />
        <path d="M330 -16 L372 0 L330 16Z" fill={NAVY} />
      </g>
      <Finish vignette={0.9} />
    </Frame>
  );
};

// ---------------------------------------------------------------- end card
export const Fim = ({dur}) => {
  const t = useST();
  const g = kf(t, [2.1, 2.4], [0, 1], 'back');
  const y27 = kf(t, [3.6, 3.85], [0, 1], 'back');
  const cta = kf(t, [4.1, 4.4], [0, 1], 'o');
  const arrow = Math.sin(t * 8) * 8;
  return (
    <Frame bg={NAVY}>
      <rect width={W} height={H} fill={NAVY} />
      <Rays t={t} cy={520} />
      <Dust t={t} n={40} color="#FFE9A0" size={4} rise={40} seed="fd" opacity={0.6} />
      <Glow id="fg" x={540} y={520} r={560} color={YEL} opacity={0.25} />
      <g transform="translate(540 500) scale(0.72)"><Shield k={kf(t, [0, 1.0], [0, 1], 'io')} /></g>
      <g transform={`translate(540 960) scale(${g})`}><text fontFamily={HEAD} fontSize="176" fill={WHITE} textAnchor="middle" stroke={INK} strokeWidth="10" paintOrder="stroke">GCM PHB</text></g>
      <g transform={`translate(540 1150) scale(${y27})`}><text fontFamily={HEAD} fontSize="190" fill={YEL} textAnchor="middle" stroke={INK} strokeWidth="10" paintOrder="stroke">2027</text></g>
      <g opacity={cta} transform={`translate(540 ${1330 + (1 - cta) * 30})`}>
        <rect x="-400" y="-50" width="800" height="100" rx="50" fill={YEL} stroke={INK} strokeWidth="6" />
        <text x="-20" y="16" fontFamily={UI} fontWeight="900" fontSize="40" fill={NAVY} textAnchor="middle">Conheça o Projeto GCM PHB 2027</text>
        <path d={`M${330 + arrow} -18 L${360 + arrow} 0 L${330 + arrow} 18`} stroke={NAVY} strokeWidth="9" fill="none" strokeLinecap="round" strokeLinejoin="round" />
      </g>
      <g opacity={cta} transform="translate(540 1490)"><text fontFamily={UI} fontWeight="800" fontSize="40" fill={WHITE} textAnchor="middle">Comenta sua resposta do desafio</text></g>
      <Finish vignette={0.9} />
    </Frame>
  );
};

// ---------------------------------------------------------------- question data (screen text = original material, v2 order)
const DATA = {
  2: {q: 'Constitui objetivo fundamental da República, conforme o art. 3º da CF:', alts: ['A separação dos Poderes', 'A independência nacional', 'A cidadania', 'Garantir o desenvolvimento nacional'], c: 3, tag: 'Art. 3º, II · cidadania é fundamento (art. 1º, II)'},
  3: {q: 'Qual destes é princípio que rege o Brasil em suas relações internacionais (art. 4º da CF)?', alts: ['Construção de uma sociedade livre, justa e solidária', 'Pluralismo político', 'Repúdio ao terrorismo e ao racismo', 'Valores sociais do trabalho'], c: 2, tag: 'Art. 4º, VIII'},
  4: {q: 'De acordo com o art. 2º da CF, são Poderes da União, independentes e harmônicos entre si:', alts: ['O Legislativo, o Executivo e o Judiciário', 'O Executivo, o Legislativo e o Moderador', 'O Legislativo, o Executivo, o Judiciário e o Ministério Público', 'O Legislativo, o Executivo e o Tribunal de Contas'], c: 0, tag: 'Art. 2º · Poder Moderador só existiu no Império'},
  5: {q: 'Segundo o parágrafo único do art. 1º da CF, todo o poder emana do povo, que o exerce:', alts: ['Exclusivamente por meio de representantes eleitos', 'Por meio de representantes eleitos ou diretamente, nos termos da Constituição', 'Diretamente, por meio de plebiscitos obrigatórios', 'Exclusivamente pelo Congresso Nacional'], c: 1, tag: 'Art. 1º, parágrafo único · art. 14'},
  6: {q: 'A República Federativa do Brasil é formada pela união indissolúvel de:', alts: ['Estados, Territórios e Municípios', 'Estados e Distrito Federal, apenas', 'Estados, Municípios e Distrito Federal', 'União, Estados e Territórios'], c: 2, tag: 'Art. 1º, caput'},
  7: {q: 'A forma de governo e a forma de Estado adotadas no Brasil são, respectivamente:', alts: ['República e Federação', 'Presidencialismo e Federação', 'Monarquia e Federação', 'República e Estado unitário'], c: 0, tag: 'Presidencialismo = sistema de governo'},
  8: {q: 'Segundo o art. 18, § 1º, da CF, a Capital Federal é:', alts: ['A cidade onde estiver a sede do Congresso Nacional', 'O Distrito Federal', 'Brasília', 'A cidade do Rio de Janeiro'], c: 2, tag: 'Art. 18, § 1º · DF é ente da Federação'},
  9: {q: 'Sobre a organização político-administrativa (art. 18 da CF), é correto afirmar:', alts: ['União, Estados, Distrito Federal e Municípios são todos autônomos', 'O Distrito Federal é subordinado administrativamente à União', 'Apenas a União e os Estados são autônomos', 'Os Territórios Federais são entes federativos autônomos'], c: 0, tag: 'Art. 18, caput e § 2º'},
  10: {q: 'O sistema de governo adotado pela Constituição de 1988 e confirmado no plebiscito de 1993 é o:', alts: ['Parlamentarismo', 'Semipresidencialismo', 'Diretório', 'Presidencialismo'], c: 3, tag: 'Plebiscito de 1993 · ADCT, art. 2º'},
};
const SCENES = {2: SQ2, 3: SQ3, 4: SQ4, 5: SQ5, 6: SQ6, 7: SQ7, 8: SQ8, 9: SQ9, 10: SQ10};
const Plain = ({t}) => <g />;
const Tag = ({show, text}) => {
  const t = useST();
  const k = kf(t, [show, show + 0.3], [0, 1], 'o');
  if (k <= 0) return null;
  return (
    <svg viewBox={`0 0 ${W} ${H}`} width={W} height={H} style={{position: 'absolute', inset: 0}}>
      <g opacity={k} transform={`translate(540 ${1590 + (1 - k) * 20})`}>
        <rect x="-460" y="-46" width="920" height="92" rx="20" fill={WHITE} stroke={INK} strokeWidth="6" />
        <text y="13" fontFamily={UI} fontWeight="900" fontSize={text.length > 40 ? 32 : 38} fill={NAVY} textAnchor="middle">{text}</text>
      </g>
    </svg>
  );
};
const makeQS = (Q) => {
  const D = DATA[Q.n];
  const Comp = QuestionScreen({q: D.q, alts: D.alts, at: Q.letters.map((x) => x - Q.q), cd: Q.cd - Q.q, rv: Q.rv - Q.q, hl: Q.hl - Q.q, correct: D.c, Bg: Plain});
  return ({dur}) => <><Comp dur={dur} /><Tag show={Q.hl - Q.q + 0.6} text={D.tag} /></>;
};

// timeline entries: [id, Component, startFrame, endFrame, transition, overlap]
const f = (s) => Math.round(s * FPS);
export const buildTimeline = () => {
  const T = [['HOOK', Hook, 0, f(QT[0].title), 'cut', 0]];
  QT.forEach((Q) => {
    T.push([`T${Q.n}`, QTitle({n: Q.n}), f(Q.title), f(Q.scene), 'cut', 0]);
    T.push([`S${Q.n}`, SCENES[Q.n], f(Q.scene), f(Q.q), 'whipX', 5]);
    T.push([`P${Q.n}`, makeQS(Q), f(Q.q), f(Q.end), 'fade', 6]);
  });
  T.push(['DES', Desafio, f(META.desafio), f(META.projeto) - 30, 'flash', 0]);
  T.push(['FIM', Fim, f(META.projeto) - 30, f(META.total), 'fade', 8]);
  return T;
};
