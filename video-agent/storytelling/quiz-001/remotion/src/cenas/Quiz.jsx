import React from 'react';
import {random, useCurrentFrame} from 'remotion';
import {INK, C, W, H, FPS, Frame, Finish, Camera, Glow, Dust, kf, useST, lerp, clamp01} from '../kit.jsx';
import {LucasBusto} from '../rigs/LucasBusto.jsx';
import {mixExpr, DIEGO, PROFESSORA} from '../rigs/lucas.js';
import {Shield, Houses, DawnSky} from './Final.jsx';
import {NAVY, NAVY2, YEL, WHITE} from './Reels.jsx';
import {WORDS} from '../words.js';

const UI = 'InterV, Inter, sans-serif';
const HEAD = "'Archivo Black', sans-serif";
const GREEN = '#2EB872', RED = '#E5484D';

// audio time -> video time (5 s countdowns inserted in silence)
export const CUTS = [29.85, 59.65];
export const GAP = 5;
export const v = (a) => a + CUTS.filter((c) => a >= c).length * GAP;

// ---------------------------------------------------------------- captions (narrative parts only)
const WINDOWS = [[5.2, 12.4], [35.9, 39.6], [41.2, 46.4], [65.4, 69.95]];
const buildChunks = () => {
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
    const next = out[i + 1];
    const end = next && next.words[0].s < c.win ? next.words[0].s : Math.min(c.win, c.words[c.words.length - 1].e + 0.35);
    return {...c, start: v(c.words[0].s) - 0.05, end: v(end) - 0.05};
  });
};
const CHUNKS = buildChunks();
export const Captions = () => {
  const t = useCurrentFrame() / FPS;
  const c = CHUNKS.find((x) => t >= x.start && t < x.end);
  if (!c) return null;
  const pop = kf(t, [c.start, c.start + 0.12], [0.86, 1], 'back');
  const txt = c.words.map((w) => w.w.toUpperCase().replace('GCMPHB', 'GCM PHB')).join(' ');
  return (
    <svg viewBox={`0 0 ${W} ${H}`} width={W} height={H} style={{position: 'absolute', inset: 0}}>
      <g transform={`translate(540 1540) scale(${pop})`}>
        <text textAnchor="middle" fontFamily={HEAD} fontSize="66" fill={NAVY} stroke={NAVY} strokeWidth="18" strokeLinejoin="round">{txt}</text>
        <text textAnchor="middle" fontFamily={HEAD} fontSize="66">
          {c.words.map((w, i) => {
            const on = t >= v(w.s) - 0.04;
            const cur = on && (i === c.words.length - 1 || t < v(c.words[i + 1].s) - 0.04);
            return <tspan key={i} fill={cur ? YEL : WHITE} fillOpacity={on ? 1 : 0.5}>{w.w.toUpperCase().replace('GCMPHB', 'GCM PHB')}{i < c.words.length - 1 ? ' ' : ''}</tspan>;
          })}
        </text>
      </g>
    </svg>
  );
};

// ---------------------------------------------------------------- shared bits
const Rays = ({t, cy = 860, col = YEL, op = 0.04}) => (
  <g>{Array.from({length: 16}).map((_, i) => <path key={i} d={`M540 ${cy} L${540 + Math.cos((i / 16) * Math.PI * 2 + t * 0.12) * 1700} ${cy + Math.sin((i / 16) * Math.PI * 2 + t * 0.12) * 1700}`} stroke={col} strokeWidth="70" opacity={op} />)}</g>
);
const Card = ({w = 170, h = 230, label = '?', back = true}) => (
  <g>
    <rect x={-w / 2} y={-h / 2} width={w} height={h} rx="16" fill={back ? NAVY2 : WHITE} stroke={INK} strokeWidth="7" />
    {back && <rect x={-w / 2 + 14} y={-h / 2 + 14} width={w - 28} height={h - 28} rx="10" fill="none" stroke={YEL} strokeWidth="4" />}
    <text y="26" fontFamily={HEAD} fontSize="80" fill={back ? YEL : NAVY} textAnchor="middle">{label}</text>
  </g>
);
const wrap = (s, n) => {
  const words = s.split(' '); const lines = []; let cur = '';
  for (const w of words) { if ((cur + ' ' + w).trim().length > n) { lines.push(cur.trim()); cur = w; } else cur += ' ' + w; }
  if (cur.trim()) lines.push(cur.trim());
  return lines;
};

// ---------------------------------------------------------------- intro
export const Intro = ({dur}) => {
  const t = useST();
  const a = kf(t, [0.0, 0.2], [0, 1], 'back');
  const b = kf(t, [0.9, 1.15], [0, 1], 'back');
  const cai = kf(t, [2.5, 2.7], [0, 1], 'back');
  const flip = (ph) => Math.cos(Math.max(0, Math.min(1, ph)) * Math.PI);
  return (
    <Frame bg={NAVY}>
      <Camera z={kf(t, [0, dur], [1.0, 1.08])}>
        <rect x="-300" y="-300" width="1700" height="2600" fill={NAVY} />
        <Rays t={t} cy={900} />
        <Glow id="ig" x={540} y={900} r={700} color={YEL} opacity={0.18} />
        <g transform="translate(540 190)"><rect x="-330" y="-40" width="660" height="70" rx="35" fill={YEL} /><text y="12" fontFamily={UI} fontWeight="900" fontSize="34" fill={NAVY} textAnchor="middle">QUIZ 01 · DIREITO CONSTITUCIONAL</text></g>
        <g transform={`translate(540 360) scale(${a})`}><text fontFamily={HEAD} fontSize="100" fill={WHITE} textAnchor="middle" stroke={INK} strokeWidth="10" paintOrder="stroke">2 PEGADINHAS</text></g>
        <g transform={`translate(540 470) scale(${b})`}><text fontFamily={HEAD} fontSize="70" fill={WHITE} textAnchor="middle" stroke={INK} strokeWidth="8" paintOrder="stroke">CLÁSSICAS DE PROVA</text></g>
        {[-1, 1].map((s, i) => {
          const f = flip((t - 0.5 - i * 0.4) * 2) ;
          return <g key={s} transform={`translate(${540 + s * 170} ${860 + Math.sin(t * 3 + i) * 12}) rotate(${s * 8}) scale(${Math.abs(f)} 1)`}><Card w={260} h={360} label={f > 0 ? '?' : 'X'} back={f > 0} /></g>;
        })}
        <g transform={`translate(540 1200) scale(${cai}) rotate(-6)`}>
          <rect x="-300" y="-90" width="600" height="150" rx="20" fill={YEL} stroke={INK} strokeWidth="8" />
          <text y="30" fontFamily={HEAD} fontSize="104" fill={NAVY} textAnchor="middle">VOCÊ CAI?</text>
        </g>
      </Camera>
      <Finish vignette={0.9} />
    </Frame>
  );
};

// ---------------------------------------------------------------- "QUESTÃO N" slam
export const QTitle = ({n}) => ({dur}) => {
  const t = useST();
  const k = kf(t, [0, 0.18], [2.2, 1], 'o');
  return (
    <Frame bg={YEL}>
      <rect width={W} height={H} fill={YEL} />
      {Array.from({length: 12}).map((_, i) => <rect key={i} x={-400 + i * 200 + ((t * 600) % 200)} y="-200" width="90" height="2400" fill={NAVY} opacity="0.08" transform="rotate(20 540 960)" />)}
      <g transform={`translate(540 940) scale(${k})`}>
        <text y="-40" fontFamily={HEAD} fontSize="110" fill={NAVY} textAnchor="middle">QUESTÃO</text>
        <circle cy="150" r="140" fill={NAVY} stroke={INK} strokeWidth="10" />
        <text y="210" fontFamily={HEAD} fontSize="180" fill={YEL} textAnchor="middle">{n}</text>
      </g>
      <Finish vignette={0.5} grain={0.4} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S1 · school fair, the columns of the Republic
const Temple = ({t, wob = 0, cols = 4, labels = null, w = 640}) => {
  const gap = w / cols;
  return (
    <g>
      <path d={`M${-w / 2 - 60} -360 L0 -520 L${w / 2 + 60} -360Z`} fill="#F1E6CF" stroke={INK} strokeWidth="8" strokeLinejoin="round" />
      <text y="-395" fontFamily={HEAD} fontSize="44" fill={NAVY} textAnchor="middle">REPÚBLICA</text>
      <rect x={-w / 2 - 60} y="-360" width={w + 120} height="46" fill="#E3D5B8" stroke={INK} strokeWidth="7" />
      {Array.from({length: cols}).map((_, i) => {
        const x = -w / 2 + gap * (i + 0.5);
        const wb = i === 2 ? wob : 0;
        return (
          <g key={i} transform={`translate(${x} 0) rotate(${Math.sin(t * 30) * 4 * wb} 0 -10)`}>
            <rect x="-38" y="-314" width="76" height="304" fill="#F7EEDB" stroke={wb > 0.5 ? RED : INK} strokeWidth="7" />
            {[-20, 0, 20].map((dx) => <line key={dx} x1={dx} y1="-300" x2={dx} y2="-24" stroke="#CDBE9F" strokeWidth="4" />)}
            {labels && <text transform="rotate(-90)" x="160" y="10" fontFamily={UI} fontWeight="900" fontSize={labels[i].length > 14 ? 17 : 27} fill={NAVY} textAnchor="middle">{labels[i]}</text>}
          </g>
        );
      })}
      <rect x={-w / 2 - 80} y="-10" width={w + 160} height="40" fill="#E3D5B8" stroke={INK} strokeWidth="7" />
      <rect x={-w / 2 - 110} y="30" width={w + 220} height="40" fill="#D6C6A6" stroke={INK} strokeWidth="7" />
    </g>
  );
};
export const S1 = ({dur}) => {
  const t = useST();
  const prof = kf(t, [2.9, 3.4], [-600, 0], 'o');
  const finger = kf(t, [3.6, 4.0], [0, 1]);
  const wob = kf(t, [5.0, 5.3], [0, 1]);
  const cam = {z: kf(t, [-0.1, 5.0, dur], [1.0, 1.0, 1.25], 'io'), y: kf(t, [5.0, dur], [0, -120], 'io'), x: kf(t, [5.0, dur], [0, -60], 'io')};
  return (
    <Frame bg="#D9E4EE">
      <Camera {...cam}>
        <rect x="-300" y="-300" width="1700" height="2600" fill="#CFDDEA" />
        <rect x="-300" y="-300" width="1700" height="2600" filter="url(#paperTex)" opacity="0.4" />
        {/* bunting + banner */}
        {Array.from({length: 14}).map((_, i) => <path key={i} d={`M${-100 + i * 100} ${150 + Math.sin(i) * 6} l50 0 l-25 60Z`} fill={[YEL, '#2F5D8C', RED, GREEN][i % 4]} stroke={INK} strokeWidth="4" />)}
        <path d="M-100 150 Q540 190 1300 150" stroke={INK} strokeWidth="4" fill="none" />
        <g transform="translate(540 320)"><rect x="-360" y="-60" width="720" height="110" rx="12" fill={NAVY} stroke={INK} strokeWidth="7" /><text y="18" fontFamily={HEAD} fontSize="56" fill={WHITE} textAnchor="middle">FEIRA DE CIÊNCIAS</text></g>
        {/* table */}
        <rect x="-200" y="1200" width="1480" height="60" fill={C.wood} stroke={INK} strokeWidth="8" />
        <rect x="-200" y="1260" width="1480" height="900" fill="#E9E1D2" stroke={INK} strokeWidth="8" />
        <g transform="translate(470 1190) scale(0.95)"><Temple t={t} wob={wob} /></g>
        {/* professora */}
        <g transform={`translate(${120 + prof} 1560) scale(0.9)`}>
          <LucasBusto t={t} id="prof" pal={PROFESSORA} hair="coque" outfit="tee" expr={mixExpr('neutro', {brow: 0.3, browIn: -0.2, lid: 0.1, smile: 0.1, open: finger * 0.2}, finger)} turn={0.4} look={{x: 0.8, y: 0}}
            light={{side: 1, color: '#FFFFFF', rim: 0.6}} arms={{r: [lerp(10, -160, finger), lerp(-10, 170, finger), null, 1]}} />
        </g>
        {/* Diego with four cards */}
        <g transform="translate(960 1600) scale(0.9)">
          <LucasBusto t={t} id="dg1" pal={DIEGO} hair="liso" outfit="tee" expr={mixExpr('neutro', 'perdido', kf(t, [3.6, 4.3], [0, 1]))} turn={-0.45} look={{x: lerp(-0.4, -0.9, finger), y: 0.2}}
            light={{side: -1, color: '#FFFFFF', rim: 0.6}} arms={{l: [-20, 130, null, 1]}} />
        </g>
        <g transform="translate(700 1470)">
          {[0, 1, 2, 3].map((i) => <g key={i} transform={`rotate(${-24 + i * 16} 0 120) translate(0 -40)`}><Card w={120} h={170} /></g>)}
        </g>
      </Camera>
      <Finish vignette={0.6} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S2 · delivery: "para a Capital Federal"
export const S2 = ({dur}) => {
  const t = useST();
  const close = kf(t, [2.2, 2.6], [0, 1], 'io');
  return (
    <Frame bg="#F29A5A">
      <Camera z={lerp(1.0, 2.4, close)} x={lerp(0, 20, close)} y={lerp(0, 495, close)}>
        <rect x="-300" y="-300" width="1700" height="2600" fill="#9CC8E8" />
        <circle cx="880" cy="260" r="90" fill="#FFE9A8" filter="url(#glow)" />
        <g transform={`translate(${-t * 20} 0)`}><Houses seed="q2h" n={7} y={1250} sp={330} /></g>
        <rect x="-300" y="1250" width="1700" height="1000" fill="#8C8C96" />
        <rect x="-300" y="1250" width="1700" height="22" fill="#C9C9CF" stroke={INK} strokeWidth="6" />
        {/* scooter */}
        <g transform="translate(250 1500)">
          <circle cx="-150" cy="140" r="80" fill="#1E1E24" stroke={INK} strokeWidth="8" /><circle cx="-150" cy="140" r="30" fill="#999" />
          <circle cx="170" cy="140" r="80" fill="#1E1E24" stroke={INK} strokeWidth="8" /><circle cx="170" cy="140" r="30" fill="#999" />
          <path d="M-220 120 Q-200 20 -60 20 L120 20 Q200 30 230 120Z" fill={RED} stroke={INK} strokeWidth="8" />
          <rect x="-260" y="-200" width="220" height="200" fill={YEL} stroke={INK} strokeWidth="8" />
          <text x="-150" y="-90" fontFamily={HEAD} fontSize="34" fill={NAVY} textAnchor="middle">ENTREGAS</text>
          <path d="M160 20 L200 -120 L250 -130" stroke={INK} strokeWidth="14" fill="none" strokeLinecap="round" />
        </g>
        <g transform="translate(720 1620) scale(0.95)">
          <LucasBusto t={t} id="dg2" pal={DIEGO} hair="liso" outfit="tee" expr={mixExpr('neutro', 'perdido', kf(t, [1.3, 2.0], [0, 1]))} turn={-0.2} look={{x: -0.3, y: 0.6}}
            light={{side: 1, color: '#FFE9A8', rim: 0.8}} arms={{r: [-25, -160, null, 1]}} />
        </g>
        {/* envelope */}
        <g transform={`translate(560 1430) rotate(${lerp(-8, -3, close)})`}>
          <rect x="-190" y="-120" width="380" height="240" fill="#FBF6EA" stroke={INK} strokeWidth="7" />
          <path d="M-190 -120 L0 20 L190 -120" stroke="#CDBE9F" strokeWidth="6" fill="none" />
          <rect x="110" y="-100" width="60" height="70" fill={RED} stroke={INK} strokeWidth="4" />
          <text x="-160" y="44" fontFamily={UI} fontWeight="700" fontSize="24" fill="#555">Para:</text>
          <text x="-160" y="88" fontFamily={HEAD} fontSize="34" fill={NAVY}>CAPITAL FEDERAL</text>
        </g>
      </Camera>
      <Finish vignette={0.6} />
    </Frame>
  );
};

// ---------------------------------------------------------------- question screen: question, alternatives, countdown, reveal
export const QuestionScreen = ({q, alts, at, cd, rv, hl, correct, Bg}) => ({dur}) => {
  const t = useST();
  const qk = kf(t, [0.05, 0.3], [0, 1], 'o');
  const inCount = t >= cd && t < cd + 5;
  const n = Math.max(1, 5 - Math.floor(t - cd));
  const sub = (t - cd) % 1;
  const revealed = t >= hl;
  const rk = kf(t, [hl, hl + 0.25], [0, 1], 'back');
  const lines = wrap(q, 30);
  return (
    <Frame bg={NAVY}>
      <rect width={W} height={H} fill={NAVY} />
      <g filter="url(#blur14)" opacity="0.35"><Bg t={t} /></g>
      <rect width={W} height={H} fill={NAVY} opacity="0.55" />
      <Rays t={t} cy={300} op={0.03} />
      {/* question */}
      <g opacity={qk} transform={`translate(0 ${(1 - qk) * 30})`}>
        <rect x="60" y="150" width="960" height={90 + lines.length * 62} rx="26" fill={WHITE} stroke={INK} strokeWidth="7" />
        <rect x="60" y="150" width="20" height={90 + lines.length * 62} fill={YEL} />
        <text fontFamily={UI} fontWeight="800" fontSize="46" fill={NAVY}>
          {lines.map((l, i) => <tspan key={i} x="110" y={225 + i * 62}>{l}</tspan>)}
        </text>
      </g>
      {/* alternatives */}
      {alts.map((txt, i) => {
        const k = kf(t, [at[i] - 0.05, at[i] + 0.2], [0, 1], 'back');
        const y = 560 + i * 200;
        const isC = i === correct;
        const fill = revealed ? (isC ? GREEN : '#2A3560') : WHITE;
        const tc = revealed ? (isC ? WHITE : '#8A93B5') : NAVY;
        const al = wrap(txt, 30);
        return (
          <g key={i} transform={`translate(${(1 - k) * 600} ${y}) scale(${revealed && isC ? 1 + rk * 0.04 : 1})`} opacity={clamp01(k * 2) * (revealed && !isC ? 0.75 : 1)}>
            <rect x="60" y="0" width="960" height="170" rx="26" fill={fill} stroke={INK} strokeWidth="7" />
            <circle cx="150" cy="85" r="52" fill={revealed && isC ? WHITE : YEL} stroke={INK} strokeWidth="6" />
            <text x="150" y="108" fontFamily={HEAD} fontSize="62" fill={NAVY} textAnchor="middle">{'ABCD'[i]}</text>
            <text fontFamily={UI} fontWeight="800" fontSize={al.length > 1 ? 38 : 44} fill={tc}>
              {al.map((l, j) => <tspan key={j} x="232" y={al.length > 1 ? 72 + j * 46 : 100}>{l}</tspan>)}
            </text>
            {revealed && isC && <path d="M930 85 l24 28 l46 -60" stroke={WHITE} strokeWidth="14" fill="none" strokeLinecap="round" strokeLinejoin="round" />}
            {revealed && !isC && <path d="M940 60 l50 50 M990 60 l-50 50" stroke={RED} strokeWidth="11" strokeLinecap="round" />}
          </g>
        );
      })}
      {/* countdown */}
      {inCount && (
        <g transform="translate(540 1440)">
          <circle r="120" fill={NAVY} stroke={YEL} strokeWidth="10" />
          <circle r="120" fill="none" stroke={WHITE} strokeWidth="14" strokeDasharray={754} strokeDashoffset={754 * sub} transform="rotate(-90)" />
          <text y={52 * (1 + (1 - Math.min(1, sub * 4)) * 0.25)} fontFamily={HEAD} fontSize={150 * (1 + (1 - Math.min(1, sub * 4)) * 0.25)} fill={YEL} textAnchor="middle">{n}</text>
          <text y="200" fontFamily={UI} fontWeight="900" fontSize="40" fill={WHITE} textAnchor="middle">PENSE RÁPIDO!</text>
        </g>
      )}
      {t >= rv && (
        <g transform={`translate(540 1440) scale(${kf(t, [rv, rv + 0.2], [0.6, 1], 'back')})`}>
          <rect x="-360" y="-70" width="720" height="130" rx="65" fill={revealed ? GREEN : YEL} stroke={INK} strokeWidth="8" />
          <text y="22" fontFamily={HEAD} fontSize="58" fill={revealed ? WHITE : NAVY} textAnchor="middle">{revealed ? `RESPOSTA: ${'ABCD'[correct]}` : 'RESPOSTA...'}</text>
        </g>
      )}
      <Finish vignette={0.8} />
    </Frame>
  );
};

export const BgTemple = ({t}) => <g transform="translate(540 1300)"><Temple t={t} /></g>;
export const BgMap = ({t}) => (
  <g>
    <rect width={W} height={H} fill="#DDE6D2" />
    {Array.from({length: 12}).map((_, i) => <path key={i} d={`M${-100 + i * 120} -100 L${300 + i * 60} 2100`} stroke="#FFFFFF" strokeWidth="26" />)}
    <circle cx="540" cy="900" r="40" fill={RED} />
  </g>
);

// ---------------------------------------------------------------- E1 · fundamento x objetivo
export const E1 = ({dur}) => {
  const t = useST();
  const fly = kf(t, [0.3, 1.2], [0, 1], 'io');
  const sign = kf(t, [1.5, 1.9], [0, 1], 'back');
  const cx = lerp(540, 600, fly), cy = lerp(560, 1290, fly);
  return (
    <Frame bg={NAVY}>
      <rect width={W} height={H} fill={NAVY} />
      <Rays t={t} cy={500} op={0.03} />
      <g transform="translate(540 130)"><text fontFamily={HEAD} fontSize="58" fill={WHITE} textAnchor="middle">FUNDAMENTOS <tspan fill={YEL}>· art. 1º</tspan></text>
        <text y="58" fontFamily={UI} fontWeight="800" fontSize="38" fill="#C9D6F2" textAnchor="middle">o que o país JÁ É</text></g>
      <g transform="translate(540 820) scale(0.88)"><Temple t={t} cols={5} w={760} labels={['SOBERANIA', 'CIDADANIA', 'DIGNIDADE', 'TRABALHO E LIVRE INICIATIVA', 'PLURALISMO POLÍTICO']} /></g>
      {/* road / destination */}
      <path d="M-100 1480 Q540 1300 1180 1180 L1180 1400 Q540 1460 -100 1600Z" fill="#46598F" stroke={INK} strokeWidth="7" />
      <path d="M0 1520 Q540 1370 1180 1290" stroke={YEL} strokeWidth="10" strokeDasharray="50 40" fill="none" />
      <g transform="translate(600 1150)">
        <rect x="-10" y="0" width="20" height="200" fill="#8A93B5" stroke={INK} strokeWidth="5" />
        <path d="M-270 -170 L230 -170 L280 -100 L230 -30 L-270 -30Z" fill={YEL} stroke={INK} strokeWidth="7" />
        <text x="-10" y="-120" fontFamily={HEAD} fontSize="40" fill={NAVY} textAnchor="middle">OBJETIVOS</text>
        <text x="-10" y="-62" fontFamily={UI} fontWeight="900" fontSize="30" fill={NAVY} textAnchor="middle">art. 3º · aonde QUER CHEGAR</text>
      </g>
      <g transform={`translate(${cx} ${cy}) rotate(${Math.sin(fly * Math.PI) * 10})`}>
        <rect x="-230" y="-60" width="460" height="120" rx="16" fill={WHITE} stroke={GREEN} strokeWidth="8" />
        <text y="-8" fontFamily={UI} fontWeight="900" fontSize="30" fill={NAVY} textAnchor="middle">ERRADICAR A POBREZA</text>
        <text y="32" fontFamily={UI} fontWeight="900" fontSize="30" fill={NAVY} textAnchor="middle">E A MARGINALIZAÇÃO</text>
      </g>
      <g opacity={sign} transform="translate(540 1720)"><text fontFamily={UI} fontWeight="800" fontSize="32" fill="#C9D6F2" textAnchor="middle">CF, art. 1º e art. 3º, III</text></g>
      <Finish vignette={0.8} />
    </Frame>
  );
};

// ---------------------------------------------------------------- E2 · Brasília x Distrito Federal
export const E2 = ({dur}) => {
  const t = useST();
  const pin = kf(t, [0.0, 0.3], [-400, 0], 'back');
  const df = kf(t, [0.75, 1.1], [0, 1], 'o');
  return (
    <Frame bg={NAVY}>
      <rect width={W} height={H} fill={NAVY} />
      <Rays t={t} cy={880} op={0.03} />
      <Camera z={kf(t, [0, dur], [1.0, 1.06])}>
        {/* DF square */}
        <g transform="translate(540 880)">
          <rect x="-360" y="-280" width="720" height="560" fill="#E7E1C8" stroke={df > 0 ? YEL : INK} strokeWidth={8 + df * 8} />
          <rect x="-360" y="-280" width="720" height="560" fill="url(#hatch)" opacity="0.25" />
          <path d="M-300 -120 Q-100 -200 120 -140 Q260 -100 300 40" stroke="#7FB2D9" strokeWidth="34" fill="none" opacity="0.8" />
          {/* plano piloto */}
          <g transform={`translate(0 ${pin * 0}) rotate(-10)`} opacity={kf(t, [0.0, 0.2], [0, 1])}>
            <path d="M-210 20 Q0 -40 210 20" stroke="#8A8F9C" strokeWidth="22" fill="none" />
            <path d="M0 -150 L0 170" stroke="#8A8F9C" strokeWidth="26" />
          </g>
          <g transform={`translate(0 ${-30 + pin})`}>
            <path d="M0 0 C-60 -70 -60 -150 0 -150 C60 -150 60 -70 0 0Z" fill={RED} stroke={INK} strokeWidth="6" />
            <circle cy="-104" r="20" fill={WHITE} />
          </g>
        </g>
        <g opacity={kf(t, [0.15, 0.45], [0, 1])} transform="translate(540 330)">
          <rect x="-380" y="-70" width="760" height="140" rx="24" fill={GREEN} stroke={INK} strokeWidth="7" />
          <text y="-8" fontFamily={HEAD} fontSize="52" fill={WHITE} textAnchor="middle">BRASÍLIA</text>
          <text y="44" fontFamily={UI} fontWeight="900" fontSize="34" fill={WHITE} textAnchor="middle">= Capital Federal (art. 18, § 1º)</text>
        </g>
        <g opacity={df} transform="translate(540 1300)">
          <rect x="-400" y="-70" width="800" height="140" rx="24" fill={WHITE} stroke={INK} strokeWidth="7" />
          <text y="-8" fontFamily={HEAD} fontSize="46" fill={NAVY} textAnchor="middle">DISTRITO FEDERAL</text>
          <text y="42" fontFamily={UI} fontWeight="900" fontSize="34" fill={NAVY} textAnchor="middle">= ente da Federação</text>
        </g>
      </Camera>
      <Finish vignette={0.8} />
    </Frame>
  );
};

// ---------------------------------------------------------------- outro
export const Outro = ({dur}) => {
  const t = useST();
  const a = kf(t, [0.05, 0.3], [0, 1], 'back');
  const card = kf(t, [2.4, 2.8], [0, 1], 'io');
  const g = kf(t, [3.3, 3.6], [0, 1], 'back');
  const y27 = kf(t, [5.1, 5.35], [0, 1], 'back');
  const cta = kf(t, [5.6, 5.9], [0, 1], 'o');
  const arrow = Math.sin(t * 8) * 8;
  return (
    <Frame bg={NAVY}>
      <rect width={W} height={H} fill={NAVY} />
      <Rays t={t} cy={560} />
      <Dust t={t} n={40} color="#FFE9A0" size={4} rise={40} seed="od" opacity={0.6} />
      <g opacity={1 - card} transform={`translate(540 640) scale(${a})`}>
        <text fontFamily={HEAD} fontSize="104" fill={WHITE} textAnchor="middle" stroke={INK} strokeWidth="10" paintOrder="stroke">ACERTOU</text>
        <text y="120" fontFamily={HEAD} fontSize="104" fill={YEL} textAnchor="middle" stroke={INK} strokeWidth="10" paintOrder="stroke">AS DUAS?</text>
        {['0/2', '1/2', '2/2'].map((s, i) => (
          <g key={s} transform={`translate(${(i - 1) * 260} 360)`}>
            <rect x="-110" y="-70" width="220" height="130" rx="20" fill={i === 2 ? YEL : NAVY2} stroke={INK} strokeWidth="6" />
            <text y="22" fontFamily={HEAD} fontSize="64" fill={i === 2 ? NAVY : WHITE} textAnchor="middle">{s}</text>
          </g>
        ))}
        <text y="580" fontFamily={UI} fontWeight="900" fontSize="46" fill={WHITE} textAnchor="middle">Comenta o seu placar</text>
        <path d={`M0 ${640 + arrow} l-22 -22 M0 ${640 + arrow} l22 -22 M0 ${640 + arrow} l0 -50`} stroke={YEL} strokeWidth="8" strokeLinecap="round" />
      </g>
      <g opacity={card}>
        <Glow id="og" x={540} y={520} r={560} color={YEL} opacity={0.25} />
        <g transform="translate(540 500) scale(0.72)"><Shield k={card} /></g>
        <g transform={`translate(540 960) scale(${g})`}><text fontFamily={HEAD} fontSize="176" fill={WHITE} textAnchor="middle" stroke={INK} strokeWidth="10" paintOrder="stroke">GCM PHB</text></g>
        <g transform={`translate(540 1150) scale(${y27})`}><text fontFamily={HEAD} fontSize="190" fill={YEL} textAnchor="middle" stroke={INK} strokeWidth="10" paintOrder="stroke">2027</text></g>
        <g opacity={cta} transform={`translate(540 ${1330 + (1 - cta) * 30})`}>
          <rect x="-400" y="-50" width="800" height="100" rx="50" fill={YEL} stroke={INK} strokeWidth="6" />
          <text x="-20" y="16" fontFamily={UI} fontWeight="900" fontSize="40" fill={NAVY} textAnchor="middle">Conheça o Projeto GCM PHB 2027</text>
          <path d={`M${330 + arrow} -18 L${360 + arrow} 0 L${330 + arrow} 18`} stroke={NAVY} strokeWidth="9" fill="none" strokeLinecap="round" strokeLinejoin="round" />
        </g>
      </g>
      <Finish vignette={0.9} />
    </Frame>
  );
};

// ---------------------------------------------------------------- the two question screens with their timings (scene-local seconds)
export const P1 = QuestionScreen({
  q: 'Segundo o art. 1º da CF, são fundamentos da República Federativa do Brasil, EXCETO:',
  alts: ['Erradicar a pobreza e a marginalização', 'A dignidade da pessoa humana', 'A soberania', 'O pluralismo político'],
  at: [4.94, 9.0, 12.18, 14.02], cd: 17.35, rv: 22.46, hl: 24.02, correct: 0, Bg: BgTemple,
});
export const P2 = QuestionScreen({
  q: 'Segundo o art. 18, § 1º, da CF, a Capital Federal é:',
  alts: ['A cidade do Rio de Janeiro', 'O Distrito Federal', 'Brasília', 'A cidade onde estiver a sede do Congresso Nacional'],
  at: [3.2, 5.8, 7.74, 10.28], cd: 13.25, rv: 18.5, hl: 19.86, correct: 2, Bg: BgMap,
});
export const T1 = QTitle({n: 1});
export const T2 = QTitle({n: 2});
