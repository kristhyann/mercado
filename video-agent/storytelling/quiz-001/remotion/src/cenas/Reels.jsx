import React from 'react';
import {random, useCurrentFrame} from 'remotion';
import {INK, C, W, H, FPS, Frame, Finish, Camera, Layer, Glow, Beam, Dust, Rain, kf, useST, lerp, clamp01} from '../kit.jsx';
import {LucasBusto} from '../rigs/LucasBusto.jsx';
import {EXPR, mixExpr, DIEGO} from '../rigs/lucas.js';
import {BookStack, Mug} from './props.jsx';
import {RoomBack, LAMP_HEAD} from './Quarto.jsx';
import {DawnSky, City, Shield} from './Final.jsx';
import {WORDS} from '../words.js';

export const NAVY = '#0F1A36', NAVY2 = '#1B2C5C', YEL = '#F5C518', WHITE = '#FFFFFF';
const UI = 'InterV, Inter, sans-serif';
const HEAD = "'Archivo Black', sans-serif";

// ---------------------------------------------------------------- captions (word by word)
const CHUNKS = [
  [0, 2], [3, 5], [6, 7], [8, 9], [10, 11], [12, 14], [15, 16], [17, 19], [20, 22], [23, 23], [24, 25], [26, 27], [28, 30],
  [31, 33], [34, 35], [36, 37], [38, 39], [40, 42], [43, 44], [45, 45], [46, 48], [49, 51],
];
const KEY = new Set(['amanhã.', 'zero,', 'TAF.', 'edital?', 'depois.', 'pronto.', 'questões', 'revisando,', 'treinando', 'aprovação,']);
export const Captions = () => {
  const t = useCurrentFrame() / FPS;
  for (let c = 0; c < CHUNKS.length; c++) {
    const [a, b] = CHUNKS[c];
    const start = WORDS[a].s - 0.06;
    const end = c + 1 < CHUNKS.length ? WORDS[CHUNKS[c + 1][0]].s - 0.06 : WORDS[b].e + 0.35;
    if (t < start || t >= end) continue;
    const pop = kf(t, [start, start + 0.12], [0.86, 1], 'back');
    const words = WORDS.slice(a, b + 1);
    return (
      <svg viewBox={`0 0 ${W} ${H}`} width={W} height={H} style={{position: 'absolute', inset: 0}}>
        <g transform={`translate(540 1520) scale(${pop})`}>
          <text x="0" y="0" textAnchor="middle" fontFamily={HEAD} fontSize="70" letterSpacing="1" fill={NAVY} stroke={NAVY} strokeWidth="18" strokeLinejoin="round">
            {words.map((w, i) => w.w.toUpperCase()).join(' ')}
          </text>
          <text x="0" y="0" textAnchor="middle" fontFamily={HEAD} fontSize="70" letterSpacing="1">
            {words.map((w, i) => {
              const active = t >= w.s - 0.04;
              const cur = active && (i === words.length - 1 || t < words[i + 1].s - 0.04);
              const col = KEY.has(w.w) && active ? YEL : cur ? YEL : WHITE;
              return <tspan key={i} fill={col} fillOpacity={active ? 1 : 0.55}>{w.w.toUpperCase()}{i < words.length - 1 ? ' ' : ''}</tspan>;
            })}
          </text>
        </g>
      </svg>
    );
  }
  return null;
};

// navy grade to unify the series look with the reels palette
const Grade = ({k = 0.12}) => <rect width={W} height={H} fill={NAVY2} opacity={k} style={{mixBlendMode: 'multiply'}} />;

// ---------------------------------------------------------------- R1 · phone with a (fictional) news alert + hook
const NewsPhone = ({t, zoomK}) => {
  const banner = kf(t, [0.15, 0.4], [-120, 0], 'back');
  return (
    <g>
      <rect x="-150" y="-300" width="300" height="600" rx="44" fill="#151821" stroke={INK} strokeWidth="9" />
      <clipPath id="newsclip"><rect x="-132" y="-282" width="264" height="564" rx="32" /></clipPath>
      <g clipPath="url(#newsclip)">
        <rect x="-132" y="-282" width="264" height="564" fill="#F4F6FA" />
        <rect x="-132" y="-282" width="264" height="74" fill={NAVY} />
        <text x="-112" y="-236" fill={WHITE} fontFamily={UI} fontSize="17" fontWeight="900">CONCURSOS · AGORA</text>
        <g transform="translate(-112 -186)">
          <rect width="104" height="28" rx="6" fill={YEL} />
          <text x="52" y="20" fill={NAVY} fontFamily={UI} fontSize="15" fontWeight="900" textAnchor="middle">SIMULAÇÃO</text>
        </g>
        <text fill={NAVY} fontFamily={UI} fontSize="25" fontWeight="900">
          <tspan x="-112" y="-118">E se o edital</tspan><tspan x="-112" y="-86">da GCM Parnaíba</tspan><tspan x="-112" y="-54">saísse amanhã?</tspan>
        </text>
        <rect x="-112" y="-30" width="224" height="150" rx="10" fill={NAVY2} />
        <g transform="translate(0 46) scale(0.2)"><Shield k={1} /></g>
        {[150, 176, 202, 228].map((y, i) => <rect key={y} x="-112" y={y} width={i === 3 ? 120 : 224} height="12" rx="6" fill="#C5CBD8" />)}
        <g transform={`translate(0 ${-232 + banner})`} opacity={clamp01(t * 6)}>
          <rect x="-124" y="-34" width="248" height="68" rx="18" fill={WHITE} stroke="#D8DCE6" strokeWidth="3" />
          <circle cx="-94" cy="0" r="18" fill={YEL} />
          <text x="-94" y="7" fill={NAVY} fontFamily={UI} fontSize="20" fontWeight="900" textAnchor="middle">!</text>
          <text x="-66" y="-5" fill={NAVY} fontFamily={UI} fontSize="15" fontWeight="900">Alerta de concurso</text>
          <text x="-66" y="16" fill="#55607A" fontFamily={UI} fontSize="13" fontWeight="600">e se fosse amanhã?</text>
        </g>
      </g>
      <rect x="-40" y="-276" width="80" height="18" rx="9" fill="#05060A" />
    </g>
  );
};
export const R1 = ({dur}) => {
  const t = useST();
  const punch = kf(t, [0, 0.22], [1.3, 1.0], 'o');
  const zoomK = kf(t, [1.75, 2.3], [0, 1], 'io');
  const vib = t > 0.15 && t < 0.7 ? Math.sin(t * 100) * 6 : 0;
  const hook = kf(t, [0.0, 0.18], [0, 1], 'back');
  return (
    <Frame bg={NAVY}>
      <Camera z={punch * lerp(1, 1.85, zoomK)} x={lerp(0, -10, zoomK)} y={lerp(0, -40, zoomK)} r={lerp(-2, -4, zoomK)}>
        <rect x="-400" y="-400" width="1900" height="2700" fill={NAVY} />
        <g filter="url(#blur14)" opacity="0.8">
          {Array.from({length: 18}).map((_, i) => <circle key={i} cx={random('r1x' + i) * W} cy={random('r1y' + i) * H} r={40 + random('r1r' + i) * 90} fill={i % 3 ? NAVY2 : YEL} opacity={i % 3 ? 0.9 : 0.25} />)}
        </g>
        <Glow id="r1g" x={540} y={980} r={700} color="#BFD8FF" opacity={0.35} />
        <g transform={`translate(${540 + vib} 1000) rotate(-6) scale(1.95)`}>
          <NewsPhone t={t} zoomK={zoomK} />
          {/* hand */}
          <path d="M-170 140 Q-210 300 -140 370 L150 370 Q190 280 160 170 Q60 220 -170 140Z" fill="#A8714F" stroke={INK} strokeWidth="8" />
          <path d="M150 170 Q200 120 190 60 Q176 40 156 60 L150 120" fill="#A8714F" stroke={INK} strokeWidth="7" />
        </g>
      </Camera>
      {/* hook */}
      <g transform={`translate(540 300) scale(${hook})`} opacity={kf(t, [1.65, 1.95], [1, 0])}>
        <text x="0" y="0" textAnchor="middle" fontFamily={HEAD} fontSize="92" fill={WHITE} stroke={NAVY} strokeWidth="18" paintOrder="stroke" strokeLinejoin="round">E SE O EDITAL</text>
        <text x="0" y="112" textAnchor="middle" fontFamily={HEAD} fontSize="112" fill={YEL} stroke={NAVY} strokeWidth="20" paintOrder="stroke" strokeLinejoin="round">SAIR AMANHÃ?</text>
      </g>
      <Finish vignette={0.9} />
    </Frame>
  );
};

// ---------------------------------------------------------------- R2 · unprepared candidate vs the pile of books (dolly zoom)
export const R2 = ({dur}) => {
  const t = useST();
  const z = kf(t, [0, dur], [1.0, 1.32], 'io');
  const bgS = kf(t, [0, dur], [1.18, 0.88], 'io');
  const scare = kf(t, [0.05, 0.35], [0, 1], 'o');
  const shake = Math.sin(t * 40) * 2 * scare;
  return (
    <Frame bg="#1A2448">
      <Camera z={z} y={-120 + shake}>
        <g transform={`translate(540 900) scale(${bgS}) translate(-540 -900)`} filter="url(#blur4)">
          <g transform="translate(-200 -300) scale(1.4)"><RoomBack t={t} rain={false} crossed={0} /></g>
        </g>
        <rect x="-300" y="-300" width="1700" height="2600" fill="#24366E" opacity="0.35" style={{mixBlendMode: 'multiply'}} />
        <g transform="translate(560 1520) scale(1.18)">
          <LucasBusto t={t} id="r2" pal={DIEGO} hair="liso" outfit="tee" expr={mixExpr('perdido', 'assustado', scare)} look={{x: -0.55, y: -0.65}} turn={-0.25}
            tilt={2} sweat={kf(t, [1.2, 1.6], [0, 1])} light={{side: -1, color: '#BFD8FF', rim: 0.8}} shoulders={-10} />
        </g>
        {/* towers of books in the foreground */}
        <g transform="translate(150 1950) scale(1.5)"><BookStack n={13} seed="r2a" /></g>
        <g transform="translate(980 1980) scale(1.3)"><BookStack n={10} seed="r2b" /></g>
        <Glow id="r2g" x={150} y={500} r={600} color="#BFD8FF" opacity={0.25} />
      </Camera>
      <Grade k={0.15} />
      <Finish vignette={1.1} />
    </Frame>
  );
};

// ---------------------------------------------------------------- R3 · chapter 1, page 1 of 847
export const R3 = ({dur}) => {
  const t = useST();
  const drop = kf(t, [0.9, 1.3], [0, 1], 'i');
  const splash = kf(t, [1.3, 1.7], [0, 1], 'o');
  return (
    <Frame bg="#5E4433">
      <Camera z={kf(t, [-0.2, dur], [1.0, 1.35], 'io')} y={kf(t, [-0.2, dur], [0, -120])} r={kf(t, [-0.2, dur], [-3, 1])}>
        <rect x="-300" y="-300" width="1700" height="2600" fill="#6A4A35" />
        {/* open book */}
        <path d="M40 520 Q290 470 540 540 Q790 470 1040 520 L1040 1500 Q790 1450 540 1520 Q290 1450 40 1500Z" fill="#FBF6EA" stroke={INK} strokeWidth="9" />
        <path d="M540 540 L540 1520" stroke={INK} strokeWidth="6" />
        <path d="M470 540 Q540 560 610 540 L610 1520 Q540 1540 470 1520Z" fill={INK} opacity="0.08" />
        <text x="290" y="700" fontFamily={HEAD} fontSize="58" fill={NAVY} textAnchor="middle">CAPÍTULO 1</text>
        <rect x="120" y="740" width="340" height="10" fill={YEL} />
        {Array.from({length: 13}).map((_, i) => <rect key={i} x="110" y={800 + i * 46} width={330 - (i * 37) % 90} height="14" rx="7" fill="#B9B3A6" />)}
        {Array.from({length: 17}).map((_, i) => <rect key={i} x="620" y={620 + i * 46} width={340 - (i * 53) % 110} height="14" rx="7" fill="#B9B3A6" />)}
        <text x="290" y="1440" fontFamily={UI} fontSize="30" fontWeight="800" fill="#8A8170" textAnchor="middle">pág. 1 de 847</text>
        {/* sweat drop falling */}
        {drop < 1 && <path d={`M300 ${200 + drop * 820} q-16 34 0 46 q16 -12 0 -46Z`} fill="#CFE8FF" stroke={INK} strokeWidth="4" />}
        {splash > 0 && <g opacity={1 - splash}>{[0, 1, 2, 3, 4, 5].map((i) => <circle key={i} cx={300 + Math.cos(i) * 60 * splash} cy={1060 + Math.sin(i * 2) * 30 * splash} r="8" fill="#CFE8FF" />)}<ellipse cx="300" cy="1066" rx={40 * splash + 10} ry={14 * splash + 4} fill="#CFE8FF" opacity="0.6" /></g>}
        {/* red sleeve hands at the edges */}
        <path d="M-80 1350 Q60 1300 140 1400 L120 1700 L-80 1700Z" fill="#D9A47E" stroke={INK} strokeWidth="8" />
        <path d="M-80 1480 L130 1500 L110 1800 L-80 1800Z" fill="#B5463C" stroke={INK} strokeWidth="8" />
        <path d="M1160 1350 Q1020 1300 940 1400 L960 1700 L1160 1700Z" fill="#D9A47E" stroke={INK} strokeWidth="8" />
        <path d="M1160 1480 L950 1500 L970 1800 L1160 1800Z" fill="#B5463C" stroke={INK} strokeWidth="8" />
        <Glow id="r3g" x={540} y={300} r={800} color="#FFE8B0" opacity={0.25} />
      </Camera>
      <Grade k={0.1} />
      <Finish vignette={1} />
    </Frame>
  );
};

// ---------------------------------------------------------------- R4a · the prepared one, already at it
export const R4a = ({dur}) => {
  const t = useST();
  return (
    <Frame bg={C.night2}>
      <Camera z={kf(t, [-0.2, dur], [1.0, 1.12], 'o')} y={-80}>
        <g filter="url(#blur8)" transform="translate(-260 -380) scale(1.5)"><RoomBack t={t} dawnK={0.85} crossed={24} rain={false} /></g>
        <Glow id="r4ag" x={980} y={500} r={1000} color={C.dawn} opacity={0.45} />
        <g transform="translate(540 1470) scale(1.25)">
          <LucasBusto t={t} id="r4a" outfit="tee" expr={mixExpr('focado', 'confiante', kf(t, [0, 0.4], [0.3, 1]))} look={{x: kf(t, [0, 0.5], [0.4, 0]), y: kf(t, [0, 0.5], [0.6, 0])}}
            light={{side: 1, color: C.dawnGold, rim: 0.9}} />
        </g>
      </Camera>
      <Finish vignette={0.8} />
    </Frame>
  );
};

// ---------------------------------------------------------------- R5a · scrolling on the couch, books closed
export const R5a = ({dur}) => {
  const t = useST();
  const scroll = Math.sin(t * 9) * 5;
  return (
    <Frame bg="#141B33">
      <Camera z={1.08} x={kf(t, [-0.2, dur], [-60, 60], 'lin')}>
        <rect x="-300" y="-300" width="1700" height="2600" fill="#1C2547" />
        <rect x="-300" y="-300" width="1700" height="2600" filter="url(#paperTex)" opacity="0.4" />
        {/* TV glow and shelf */}
        <rect x="620" y="300" width="380" height="240" rx="10" fill="#0B0F1E" stroke={INK} strokeWidth="7" />
        <rect x="636" y="316" width="348" height="208" fill="#6FA8FF" opacity={0.35 + Math.sin(t * 13) * 0.08} />
        <Glow id="tvg" x={810} y={420} r={500} color="#6FA8FF" opacity={0.3} />
        {/* couch back */}
        <path d="M-200 1000 Q-200 880 -60 880 L1140 880 Q1280 880 1280 1000 L1280 2200 L-200 2200Z" fill="#5A4E6E" stroke={INK} strokeWidth="9" />
        <path d="M-200 1000 Q-200 880 -60 880 L1140 880 Q1280 880 1280 1000 L1280 1060 L-200 1060Z" fill="#6E6286" />
        {/* side table with closed books gathering dust */}
        <g transform="translate(110 1430)">
          <rect x="-160" y="0" width="320" height="30" fill={C.woodDark} stroke={INK} strokeWidth="6" />
          <BookStack n={4} seed="r5" labels={false} />
          <Dust t={t * 0.3} n={14} x={-170} y={-300} w={340} h={300} color="#D8D2C2" size={3} rise={6} seed="r5d" opacity={0.7} />
        </g>
        <g transform="translate(620 1500) scale(1.1)">
          <LucasBusto t={t} id="r5a" pal={DIEGO} hair="liso" outfit="tee" expr="distraido" tilt={16} turn={0.15} look={{x: 0.3, y: 0.8}} nod={16}
            light={{side: 1, color: '#9CC2FF', rim: 0.7}} under={{color: '#BFD8FF', k: 0.7}}
            arms={{r: [-20, -150 + scroll, 'phone', 1]}} />
        </g>
      </Camera>
      <Grade k={0.12} />
      <Finish vignette={1.1} />
    </Frame>
  );
};

// ---------------------------------------------------------------- R5b · stopwatch, time running
export const R5b = ({dur}) => {
  const t = useST();
  const ang = 360 * (t * 0.5 + t * t * 0.55);
  const tick = Math.floor(t * 2.5);
  const kick = 1 + 0.03 * Math.exp(-((t * 2.5) % 1) * 8);
  return (
    <Frame bg={NAVY}>
      <Camera z={kf(t, [-0.2, dur], [1.0, 1.28], 'io') * kick} r={Math.sin(tick) * 1.2}>
        <rect x="-300" y="-300" width="1700" height="2600" fill={NAVY} />
        {Array.from({length: 24}).map((_, i) => <path key={i} d={`M540 860 L${540 + Math.cos((i / 24) * Math.PI * 2) * 1600} ${860 + Math.sin((i / 24) * Math.PI * 2) * 1600}`} stroke={i % 2 ? YEL : WHITE} strokeWidth="50" opacity="0.04" />)}
        <Glow id="swg" x={540} y={860} r={700} color={YEL} opacity={0.18} />
        <g transform="translate(540 860)">
          <rect x="-50" y="-500" width="100" height="90" rx="14" fill="#C9CFD8" stroke={INK} strokeWidth="9" />
          <rect x="-90" y="-540" width="180" height="56" rx="20" fill="#E3E7EE" stroke={INK} strokeWidth="9" />
          <g transform="rotate(-38)"><rect x="-26" y="-470" width="52" height="60" rx="10" fill="#C9CFD8" stroke={INK} strokeWidth="8" /></g>
          <circle r="420" fill="#D9DEE6" stroke={INK} strokeWidth="12" />
          <circle r="372" fill={WHITE} stroke={INK} strokeWidth="8" />
          <path d="M-372 0 A372 372 0 0 1 0 -372 L0 0Z" fill={YEL} opacity="0.18" />
          {Array.from({length: 60}).map((_, i) => <path key={i} d={`M0 -350 L0 ${i % 5 ? -330 : -305}`} stroke={NAVY} strokeWidth={i % 5 ? 4 : 10} transform={`rotate(${i * 6})`} />)}
          {[0, 15, 30, 45].map((n, i) => <text key={n} x={Math.sin((i * Math.PI) / 2) * 250} y={-Math.cos((i * Math.PI) / 2) * 250 + 22} fontFamily={HEAD} fontSize="64" fill={NAVY} textAnchor="middle">{n}</text>)}
          <g transform={`rotate(${ang})`}>
            <path d="M-10 60 L0 -340 L10 60Z" fill={C.red} stroke={INK} strokeWidth="5" />
          </g>
          <g transform={`rotate(${ang - 8})`} opacity="0.25"><path d="M-10 60 L0 -340 L10 60Z" fill={C.red} /></g>
          <circle r="26" fill={NAVY} stroke={INK} strokeWidth="6" />
          <path d="M-300 -160 Q-200 -330 0 -360" stroke={WHITE} strokeWidth="18" fill="none" opacity="0.7" strokeLinecap="round" />
        </g>
      </Camera>
      <Finish vignette={1} />
    </Frame>
  );
};

// ---------------------------------------------------------------- R6a · fly-through of preparation objects
const Notebook = () => (
  <g>
    <rect x="-150" y="-200" width="300" height="400" rx="16" fill={NAVY2} stroke={INK} strokeWidth="9" />
    <rect x="-150" y="-200" width="40" height="400" fill={YEL} stroke={INK} strokeWidth="6" />
    <rect x="-80" y="-120" width="200" height="90" rx="8" fill={WHITE} stroke={INK} strokeWidth="5" />
    <text x="20" y="-62" fontFamily={HEAD} fontSize="36" fill={NAVY} textAnchor="middle">PLANO</text>
  </g>
);
const Sneaker = () => (
  <g>
    <path d="M-200 40 Q-210 -40 -150 -60 L-40 -80 Q20 -150 90 -110 L120 -60 Q210 -40 230 30 L230 60 L-200 60Z" fill={WHITE} stroke={INK} strokeWidth="9" strokeLinejoin="round" />
    <path d="M-200 40 L230 40 L230 70 L-200 70Z" fill={YEL} stroke={INK} strokeWidth="7" />
    <path d="M-80 -40 Q20 -10 120 -40" stroke={NAVY} strokeWidth="14" fill="none" strokeLinecap="round" />
  </g>
);
const Whistle = () => (
  <g>
    <path d="M-120 -50 L60 -50 Q140 -50 140 30 Q140 100 60 100 Q-10 100 -20 40 L-120 40Z" fill="#E3E7EE" stroke={INK} strokeWidth="9" />
    <circle cx="70" cy="30" r="30" fill={NAVY} />
    <path d="M140 0 Q220 -60 260 40" stroke={YEL} strokeWidth="14" fill="none" />
  </g>
);
const MiniWatch = () => (
  <g>
    <circle r="150" fill="#D9DEE6" stroke={INK} strokeWidth="9" />
    <circle r="120" fill={WHITE} stroke={INK} strokeWidth="6" />
    <path d="M0 0 L0 -100 M0 0 L60 30" stroke={C.red} strokeWidth="10" strokeLinecap="round" />
    <rect x="-24" y="-200" width="48" height="50" rx="8" fill="#C9CFD8" stroke={INK} strokeWidth="7" />
  </g>
);
const Books = () => <g transform="translate(0 130)"><BookStack n={4} seed="r6" /></g>;
const OBJS = [
  [Books, -260, -320, 1500, -8], [Notebook, 300, 260, 1650, 10], [MiniWatch, 280, -420, 1850, 0], [Sneaker, -300, 420, 2050, -12],
  [Whistle, -180, -40, 2300, 14], [Books, 340, -60, 2550, 6], [Notebook, -320, 300, 2800, -10], [MiniWatch, 0, 520, 3050, 0],
];
export const R6a = ({dur}) => {
  const t = useST();
  const speed = 900;
  const shieldK = kf(t, [1.4, 2.6], [0, 1], 'io');
  return (
    <Frame bg={NAVY}>
      <rect width={W} height={H} fill={NAVY} />
      {Array.from({length: 40}).map((_, i) => {
        const a = random('ra' + i) * Math.PI * 2, z = ((random('rz' + i) * 3000 - t * speed * 1.5) % 3000 + 3000) % 3000 + 100;
        const s = 600 / z, r = 900 * s;
        return <line key={i} x1={540 + Math.cos(a) * r} y1={860 + Math.sin(a) * r} x2={540 + Math.cos(a) * r * 1.15} y2={860 + Math.sin(a) * r * 1.15} stroke={i % 3 ? WHITE : YEL} strokeWidth={3 + s * 6} opacity={Math.min(0.8, s)} />;
      })}
      <Glow id="r6g" x={540} y={860} r={500} color={YEL} opacity={0.25 + shieldK * 0.35} />
      <g transform={`translate(540 860) scale(${0.25 + shieldK * 0.55})`} opacity={shieldK}><Shield k={shieldK} /></g>
      {OBJS.map(([Obj, x, y, z0, rot], i) => ({Obj, x, y, rot, i, z: z0 - t * speed})).filter((o) => o.z > 120 && o.z < 3200).sort((a, b) => b.z - a.z).map(({Obj, x, y, rot, i, z}) => {
        const s = 700 / z;
        const op = clamp01((3200 - z) / 400) * clamp01((z - 120) / 200);
        return (
          <g key={i} transform={`translate(${540 + x * s * 1.6} ${860 + y * s * 1.6}) scale(${s}) rotate(${rot + t * (i % 2 ? 12 : -12)})`} opacity={op} filter={s > 1.6 ? 'url(#blur4)' : undefined}>
            <Obj />
          </g>
        );
      })}
      <Finish vignette={1} />
    </Frame>
  );
};

// ---------------------------------------------------------------- R6b · arriving more ready
export const R6b = ({dur}) => {
  const t = useST();
  return (
    <Frame bg="#F29A5A">
      <Camera z={kf(t, [-0.2, dur], [1.0, 1.12], 'sine')} y={-70}>
        <g filter="url(#blur8)"><DawnSky t={t} sunY={1000} id="r6sky" /><g transform="translate(0 200)"><City t={t} /></g></g>
        <g transform="translate(540 1500) scale(1.32)">
          <LucasBusto t={t} id="r6b" outfit="tee" expr={mixExpr('determinado', 'confiante', kf(t, [0.2, 0.9], [0, 1]))} light={{side: 1, color: '#FFD27A', rim: 1}} />
        </g>
        <Dust t={t} n={40} color="#FFE6B0" size={4} rise={20} seed="r6bd" />
      </Camera>
      <Finish vignette={0.6} />
    </Frame>
  );
};

// ---------------------------------------------------------------- R7 · end card + CTA
export const R7 = ({dur}) => {
  const t = useST();
  const T0 = 22.2; // absolute start of this scene
  const at = (abs) => abs - T0;
  const g1 = kf(t, [at(22.3), at(22.6)], [0, 1], 'back');
  const g2 = kf(t, [at(23.9), at(24.15)], [0, 1], 'back');
  const hit = kf(t, [at(23.9), at(24.0), at(24.6)], [0, 1, 0]);
  const l1 = kf(t, [at(25.6), at(25.85)], [0, 1], 'o');
  const l2 = kf(t, [at(26.4), at(26.65)], [0, 1], 'o');
  const now = kf(t, [at(27.25), at(27.45)], [0, 1], 'back');
  const cta = kf(t, [at(27.8), at(28.1)], [0, 1], 'o');
  const arrow = Math.sin(t * 8) * 8;
  return (
    <Frame bg={NAVY}>
      <defs><radialGradient id="r7bg" cx="50%" cy="30%" r="75%"><stop offset="0" stopColor="#24386E" /><stop offset="1" stopColor={NAVY} /></radialGradient></defs>
      <Camera z={kf(t, [-0.2, dur], [1.0, 1.05], 'sine')} y={hit * -6}>
        <rect x="-300" y="-300" width="1700" height="2600" fill="url(#r7bg)" />
        {Array.from({length: 14}).map((_, i) => <path key={i} d={`M540 520 L${540 + Math.cos((i / 14) * Math.PI * 2 + t * 0.1) * 1600} ${520 + Math.sin((i / 14) * Math.PI * 2 + t * 0.1) * 1600}`} stroke={YEL} strokeWidth="60" opacity="0.035" />)}
        <Dust t={t} n={50} color="#FFE9A0" size={4} rise={50} seed="r7d" opacity={0.6} />
        <Glow id="r7g" x={540} y={520} r={560} color={YEL} opacity={0.22 + hit * 0.4} />
        <g transform="translate(540 500) scale(0.72)"><Shield k={kf(t, [-0.2, 1.0], [0, 1], 'io')} /></g>
        <g transform={`translate(540 960) scale(${g1})`}>
          <text x="0" y="0" fontFamily={HEAD} fontSize="176" fill={WHITE} textAnchor="middle" stroke={INK} strokeWidth="10" paintOrder="stroke">GCM PHB</text>
        </g>
        <g transform={`translate(540 1150) scale(${g2 * (1 + hit * 0.06)})`}>
          <text x="0" y="0" fontFamily={HEAD} fontSize="190" fill={YEL} textAnchor="middle" stroke={INK} strokeWidth="10" paintOrder="stroke">2027</text>
        </g>
        <g opacity={l1} transform={`translate(0 ${(1 - l1) * 20})`}><text x="540" y="1290" fontFamily={HEAD} fontSize="66" fill={WHITE} textAnchor="middle" letterSpacing="2">SUA PREPARAÇÃO</text></g>
        <g opacity={l2} transform={`translate(0 ${(1 - l2) * 20})`}>
          <text x="540" y="1375" fontFamily={HEAD} fontSize="66" fill={WHITE} textAnchor="middle" letterSpacing="2">COMEÇA <tspan fill={YEL} fillOpacity={0.35 + 0.65 * now}>AGORA</tspan></text>
        </g>
        <g opacity={cta} transform={`translate(540 ${1490 + (1 - cta) * 30})`}>
          <rect x="-400" y="-50" width="800" height="100" rx="50" fill={YEL} stroke={INK} strokeWidth="6" />
          <text x="-20" y="16" fontFamily={UI} fontWeight="900" fontSize="40" fill={NAVY} textAnchor="middle">Conheça o Projeto GCM PHB 2027</text>
          <path d={`M${330 + arrow} -18 L${360 + arrow} 0 L${330 + arrow} 18`} stroke={NAVY} strokeWidth="9" fill="none" strokeLinecap="round" strokeLinejoin="round" />
        </g>
        <g opacity={cta} transform="translate(540 1615)">
          <text x="0" y="0" fontFamily={UI} fontWeight="800" fontSize="40" fill={WHITE} textAnchor="middle">Comenta <tspan fill={YEL} fontWeight="900">COMEÇO HOJE</tspan></text>
          <path d={`M0 ${30 + arrow * 0.6} l-18 -18 M0 ${30 + arrow * 0.6} l18 -18 M0 ${30 + arrow * 0.6} l0 -40`} stroke={YEL} strokeWidth="7" strokeLinecap="round" transform="translate(0 30)" />
        </g>
      </Camera>
      <Finish vignette={0.9} />
    </Frame>
  );
};
