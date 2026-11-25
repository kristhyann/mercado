import React from 'react';
import {random} from 'remotion';
import {INK, C, W, H, Frame, Finish, Camera, Layer, Glow, Beam, Dust, Rain, Steam, kf, useST, lerp, Title} from '../kit.jsx';
import {LucasBusto} from '../rigs/LucasBusto.jsx';
import {LucasPerfil, walkPose} from '../rigs/LucasPerfil.jsx';
import {EXPR, mixExpr} from '../rigs/lucas.js';

const UI = 'InterV, Inter, sans-serif';

// ---------------------------------------------------------------- S04a · warehouse, carrying boxes
const Shelf = ({x, y, h = 900, seed}) => (
  <g transform={`translate(${x} ${y})`}>
    <rect x="0" y={-h} width="20" height={h} fill="#E07B2E" stroke={INK} strokeWidth="5" />
    <rect x="560" y={-h} width="20" height={h} fill="#E07B2E" stroke={INK} strokeWidth="5" />
    {[0, 1, 2, 3].map((r) => (
      <g key={r}>
        <rect x="0" y={-h + r * (h / 4) + h / 4 - 18} width="580" height="18" fill="#2F5D8C" stroke={INK} strokeWidth="5" />
        {Array.from({length: 3}).map((_, i) => {
          const bw = 140 + random(seed + r + i) * 40, bh = 110 + random(seed + 'h' + r + i) * 60;
          const bx = 30 + i * 180;
          return random(seed + 'e' + r + i) > 0.15 && (
            <g key={i}>
              <rect x={bx} y={-h + r * (h / 4) + h / 4 - 18 - bh} width={bw} height={bh} fill={i % 2 ? '#C89A62' : '#B8864F'} stroke={INK} strokeWidth="5" />
              <rect x={bx + bw / 2 - 14} y={-h + r * (h / 4) + h / 4 - 18 - bh} width="28" height={bh} fill="#E0C79C" opacity="0.6" />
              <rect x={bx} y={-h + r * (h / 4) + h / 4 - 18 - bh} width="30" height={bh} fill={INK} opacity="0.18" />
            </g>
          );
        })}
      </g>
    ))}
  </g>
);

export const S04a = ({dur}) => {
  const t = useST();
  const sx = (t + 0.5) * 430; // camera travel
  const pose = {...walkPose((t + 0.5) * 6.4), armF: 32, foreF: 100, armB: 26, foreB: 96, torso: -3};
  return (
    <Frame bg="#C9D3DC">
      <Camera z={1.02} x={0} y={kf(t, [0, dur], [10, -10])}>
        {/* far wall */}
        <rect x="-300" y="-300" width="1700" height="2600" fill="#AEB9C6" />
        <g transform={`translate(${-sx * 0.25} 0)`}>
          {Array.from({length: 8}).map((_, i) => <rect key={i} x={-300 + i * 420} y="-300" width="10" height="1500" fill="#8E9AAA" />)}
          <g transform="translate(760 330)">
            <circle r="80" fill="#F4F1EA" stroke={INK} strokeWidth="8" />
            <path d="M0 0 L0 -54 M0 0 L42 18" stroke={INK} strokeWidth="9" strokeLinecap="round" />
            <text y="120" fill="#4C5566" fontFamily={UI} fontSize="30" fontWeight="800" textAnchor="middle">14:20</text>
          </g>
          <g transform="translate(80 420)"><rect width="300" height="90" fill="#F2C230" stroke={INK} strokeWidth="6" /><text x="150" y="60" fontFamily="'Archivo Black'" fontSize="40" textAnchor="middle" fill={INK}>DOCA 3</text></g>
        </g>
        {/* ceiling lamps */}
        <g transform={`translate(${-(sx * 0.6) % 600} 0)`}>
          {[0, 1, 2, 3].map((i) => (
            <g key={i} transform={`translate(${i * 600 - 100} 120)`}>
              <path d="M0 -500 L0 0" stroke={INK} strokeWidth="5" />
              <path d="M-90 0 L90 0 L60 -40 L-60 -40Z" fill="#3B4255" stroke={INK} strokeWidth="6" />
              <Beam x={0} y={0} len={1500} spread={700} color="#F4FBFF" opacity={0.5} />
            </g>
          ))}
        </g>
        {/* shelves mid */}
        <g transform={`translate(${-(sx * 0.7) % 1400} 0)`}>
          {[0, 1, 2].map((i) => <Shelf key={i} x={-200 + i * 700} y={1180} h={900} seed={'sh' + (i % 2)} />)}
        </g>
        {/* floor */}
        <rect x="-300" y="1180" width="1700" height="1200" fill="#8F959F" />
        <rect x="-300" y="1180" width="1700" height="14" fill={INK} opacity="0.5" />
        <g transform={`translate(${-(sx) % 300} 0)`}>
          {Array.from({length: 8}).map((_, i) => <rect key={i} x={-300 + i * 300} y="1700" width="180" height="22" fill="#F2C230" />)}
        </g>
        <ellipse cx="560" cy="1720" rx="270" ry="34" fill={INK} opacity="0.25" />
        <g transform="translate(560 1170) scale(0.72)">
          <LucasPerfil t={t} pose={pose} outfit="polo" carry="box" expr="cansado" light={{color: '#FFFFFF', rim: 0.5}} />
        </g>
        <Dust t={t} n={40} color="#FFFFFF" size={3} rise={10} opacity={0.6} seed="wh" />
        {/* foreground pillar passing */}
        <g transform={`translate(${1500 - ((sx * 1.6 + 1300) % 2400)} 0)`} filter="url(#blur8)">
          <rect x="0" y="-300" width="90" height="2600" fill="#E07B2E" />
          <rect x="0" y="-300" width="30" height="2600" fill={INK} opacity="0.3" />
        </g>
      </Camera>
      <Finish vignette={0.6} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S04b · bills on the kitchen table
const Bill = ({title, value, due, color = '#2F5D8C', hot = false}) => (
  <g>
    <rect x="-200" y="-260" width="400" height="520" fill="#FBF8F0" stroke={INK} strokeWidth="7" />
    <rect x="-200" y="-260" width="400" height="90" fill={color} />
    <text x="0" y="-200" fill="#fff" fontFamily={UI} fontSize="34" fontWeight="900" textAnchor="middle">{title}</text>
    {[-130, -95, -60].map((y) => <rect key={y} x="-160" y={y} width={230 + (y % 40)} height="14" rx="7" fill="#B9B3A6" />)}
    <text x="-160" y="30" fill="#6B655A" fontFamily={UI} fontSize="26" fontWeight="700">TOTAL A PAGAR</text>
    <text x="-160" y="100" fill={INK} fontFamily={UI} fontSize="66" fontWeight="900">{value}</text>
    {due && <g transform="translate(0 190)"><rect x="-160" y="-40" width="320" height="64" rx="10" fill={hot ? '#FDE2DF' : '#EEE'} stroke={hot ? C.red : '#999'} strokeWidth="5" /><text x="0" y="5" fill={hot ? C.red : '#555'} fontFamily={UI} fontSize="34" fontWeight="900" textAnchor="middle">{due}</text></g>}
  </g>
);

export const S04b = ({dur}) => {
  const t = useST();
  const stamp = kf(t, [0.62, 0.78], [0, 1], 'back');
  const slide = kf(t, [-0.1, 0.5], [260, 0], 'o');
  return (
    <Frame bg="#7B5A40">
      <Camera z={kf(t, [-0.2, dur], [1.04, 1.16])} r={kf(t, [-0.2, dur], [-3, 2])}>
        <rect x="-300" y="-300" width="1700" height="2600" fill="#9A7350" />
        {Array.from({length: 9}).map((_, i) => <rect key={i} x={-300 + i * 220} y="-300" width="216" height="2600" fill={i % 2 ? '#94704D' : '#A07A55'} stroke={INK} strokeWidth="4" />)}
        <g transform="translate(250 520) rotate(-12)"><Bill title="ÁGUA" value="R$ 96,40" due="VENCE DIA 20" color="#2C8FB8" /></g>
        <g transform="translate(860 700) rotate(9)"><Bill title="ALUGUEL" value="R$ 850,00" due="VENCE DIA 5" color="#6B4C8A" /></g>
        <g transform={`translate(${520 + slide} ${1060}) rotate(-3) scale(1.3)`}>
          <rect x="-200" y="-260" width="400" height="520" transform="translate(14 18)" fill="#000" opacity="0.35" filter="url(#blur8)" />
          <Bill title="CONTA DE LUZ" value="R$ 487,90" due="VENCE HOJE" color="#D98A1E" hot />
          <g transform={`translate(40 -100) rotate(-16) scale(${lerp(2.2, 0.85, stamp)})`} opacity={stamp}>
            <rect x="-150" y="-60" width="300" height="120" rx="12" fill="none" stroke="#2E9E5B" strokeWidth="12" />
            <text x="0" y="34" fill="#2E9E5B" fontFamily="'Archivo Black'" fontSize="92" textAnchor="middle">PAGO</text>
          </g>
          {/* hand sliding it */}
          <g transform="translate(-230 330) rotate(38)">
            <path d="M-60 0 L-50 700 L80 700 L90 0Z" fill="#A8714F" stroke={INK} strokeWidth="8" />
            <path d="M-80 10 Q-96 -120 -30 -160 Q30 -176 76 -130 Q100 -80 90 10Z" fill="#A8714F" stroke={INK} strokeWidth="8" />
            <path d="M-60 120 L90 120 L90 340 L-56 340Z" fill="#2F6E73" stroke={INK} strokeWidth="8" />
          </g>
        </g>
        {/* coffee from above */}
        <g transform="translate(830 1550)">
          <circle r="120" fill="#F4F1EA" stroke={INK} strokeWidth="8" />
          <circle r="86" fill="#4A2A18" stroke={INK} strokeWidth="5" />
          <ellipse cx="-24" cy="-26" rx="30" ry="14" fill="#fff" opacity="0.25" />
          <path d="M118 -20 Q190 -10 180 50 Q170 90 112 40" fill="none" stroke={INK} strokeWidth="26" />
          <path d="M118 -20 Q190 -10 180 50 Q170 90 112 40" fill="none" stroke="#F4F1EA" strokeWidth="12" />
          <Steam t={t} x={0} y={-60} scale={1.2} opacity={0.5} />
        </g>
        {/* keys */}
        <g transform="translate(200 1500) rotate(30)"><circle r="40" fill="none" stroke="#C9CFD8" strokeWidth="10" /><rect x="30" y="-12" width="130" height="24" rx="8" fill="#D8C46A" stroke={INK} strokeWidth="5" /></g>
      </Camera>
      <Glow id="s4bg" x={W * 0.3} y={H * 0.2} r={900} color={C.dawn} opacity={0.3} />
      <Finish vignette={1} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S04c · bus window at night
export const S04c = ({dur}) => {
  const t = useST() + 0.2;
  const shake = Math.sin(t * 15) * 3 + Math.sin(t * 6.3) * 2;
  return (
    <Frame bg={C.night0}>
      <Camera z={1.05} y={shake} x={kf(t, [0, dur], [0, 30])}>
        {/* outside: streaks of light passing */}
        <rect x="-300" y="-300" width="1700" height="2600" fill="#0B1024" />
        <g filter="url(#blur4)">
          {Array.from({length: 34}).map((_, i) => {
            const x = 1600 - ((t * 1900 + random('lx' + i) * 2400) % 2400);
            return <rect key={i} x={x} y={300 + random('ly' + i) * 900} width={120 + random('lw' + i) * 320} height={26 + random('lh' + i) * 50} rx="14" fill={i % 3 ? C.sodium : '#FFFFFF'} opacity="0.9" />;
          })}
        </g>
        <g>
          {Array.from({length: 7}).map((_, i) => {
            const x = 1700 - ((t * 900 + i * 420) % 2900);
            return <rect key={i} x={x} y={500 + (i % 3) * 120} width={260} height={1100} fill="#151C38" stroke="#0A0E1E" strokeWidth="6" />;
          })}
        </g>
        {/* window frame */}
        <path d="M-300 -300 L1400 -300 L1400 2300 L-300 2300Z M60 180 L1020 180 Q1060 180 1060 220 L1060 1500 L60 1500 Z" fill="#2C3247" fillRule="evenodd" stroke={INK} strokeWidth="10" />
        <rect x="60" y="180" width="1000" height="1320" fill="#7FA0FF" opacity="0.06" />
        <rect x="-300" y="1500" width="1700" height="900" fill="#23283A" />
        {/* passing light across everything */}
        <g transform="translate(330 1420) scale(1.05)">
          <LucasBusto t={t} id="s4c" expr={{...EXPR.cansado, lid: 0.62}} tilt={13} turn={0.25} look={{x: 0.9, y: 0.1}} light={{side: 1, color: C.sodium, rim: 0.4 + 0.4 * Math.max(0, Math.sin(t * 7))}} />
        </g>
        {/* seat */}
        <path d="M-200 1500 Q-120 1180 60 1200 L80 2300 L-200 2300Z" fill="#9C2F35" stroke={INK} strokeWidth="9" />
        <path d="M-200 1500 Q-150 1300 0 1260 L20 2300 L-200 2300Z" fill={INK} opacity="0.25" />
        {/* glass reflection + rain */}
        <Rain t={t} n={30} area={[60, 180, 1000, 1320]} angle={-55} len={40} speed={700} opacity={0.35} seed="bus" />
        <rect x={-600 + ((t * 2600) % 2600)} y="-300" width="260" height="2600" fill={C.sodium} opacity="0.22" transform="skewX(-15)" filter="url(#blur24)" />
      </Camera>
      <Finish vignette={1.1} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S05 · bus stop, patrol car passes
const PatrolCar = ({t}) => {
  const blue = Math.sin(t * 22) > 0;
  return (
    <g>
      <ellipse cx="0" cy="300" rx="760" ry="50" fill="#000" opacity="0.4" />
      <path d="M-720 250 L-720 60 Q-700 -10 -560 -20 L-380 -170 Q-330 -210 -230 -214 L260 -214 Q350 -210 420 -150 L560 -20 Q720 -10 740 60 L740 250Z" fill="#F2F4F7" stroke={INK} strokeWidth="10" strokeLinejoin="round" />
      <path d="M-340 -150 L-260 -186 L-40 -186 L-40 -30 L-450 -30Z" fill="#1C2440" stroke={INK} strokeWidth="7" />
      <path d="M0 -186 L240 -186 Q320 -180 380 -120 L460 -30 L0 -30Z" fill="#1C2440" stroke={INK} strokeWidth="7" />
      <path d="M-300 -150 L-200 -180 L-280 -40Z" fill="#fff" opacity="0.12" />
      <rect x="-720" y="40" width="1460" height="80" fill="#1E4FA8" />
      <rect x="-720" y="120" width="1460" height="22" fill="#F2C230" />
      <text x="0" y="96" fill="#fff" fontFamily="'Archivo Black'" fontSize="58" textAnchor="middle" letterSpacing="3">GUARDA MUNICIPAL</text>
      <path d="M-720 160 L740 160" stroke={INK} strokeWidth="5" opacity="0.4" />
      {[-460, 470].map((x) => (
        <g key={x} transform={`translate(${x} 250)`}><circle r="112" fill="#15161C" stroke={INK} strokeWidth="9" /><circle r="56" fill="#9AA0AE" stroke={INK} strokeWidth="6" /><circle r="16" fill="#555" /></g>
      ))}
      <rect x="-200" y="-252" width="400" height="40" rx="14" fill="#2A2F3E" stroke={INK} strokeWidth="6" />
      <rect x="-190" y="-246" width="180" height="28" rx="10" fill={blue ? '#59B6FF' : '#1A3E88'} />
      <rect x="10" y="-246" width="180" height="28" rx="10" fill={blue ? '#1A3E88' : '#59B6FF'} />
      <Glow id="sirA" x={blue ? -100 : 100} y={-232} r={520} color={C.siren} opacity={0.9} />
      <path d="M700 40 L740 40 L740 110 L700 110Z" fill="#FFE9A8" />
      <Beam x={760} y={70} angle={-100} len={900} spread={300} color="#FFF4C8" opacity={0.35} />
      <path d="M-720 0 L-700 0 L-700 90 L-720 90Z" fill={C.red} />
    </g>
  );
};

export const S05 = ({dur}) => {
  const t = useST();
  const carX = kf(t, [1.8, 3.8], [1900, -1700], 'lin');
  const passing = t > 1.8 && t < 3.9;
  const blueK = passing ? (0.5 + 0.5 * Math.sin(t * 22)) * kf(t, [1.8, 2.3, 3.4, 3.9], [0, 1, 1, 0]) : 0;
  const followK = kf(t, [1.7, 3.8], [0, 1], 'io');
  const lookUp = kf(t, [4.15, 4.7], [0, 1]);
  const expr = mixExpr(mixExpr('cansado', 'desejo', kf(t, [1.9, 2.6], [0, 1])), 'esperanca', lookUp * 0.55);
  const cam = {z: kf(t, [-0.2, 3.4, dur], [1.0, 1.06, 1.42], 'sine'), x: kf(t, [-0.2, dur], [0, 20]), y: kf(t, [-0.2, 3.4, dur], [0, 20, 190], 'sine')};
  return (
    <Frame bg={C.night0}>
      <Camera {...cam}>
        <Layer d={0.5} cx={cam.x} cy={cam.y}>
          <rect x="-400" y="-400" width="1900" height="2600" fill="#0D1330" />
          <circle cx="840" cy="180" r="70" fill="#E9EEFF" opacity="0.9" filter="url(#blur2)" />
          {Array.from({length: 7}).map((_, i) => {
            const bw = 220 + random('bw5' + i) * 120, bh = 700 + random('bh5' + i) * 600, bx = -300 + i * 250;
            return (
              <g key={i}>
                <rect x={bx} y={1300 - bh} width={bw} height={bh + 300} fill={i % 2 ? '#18204A' : '#141B3E'} stroke={INK} strokeWidth="5" />
                {Array.from({length: 24}).map((__, j) => random('w5' + i + j) > 0.6 && <rect key={j} x={bx + 24 + (j % 4) * 50} y={1340 - bh + Math.floor(j / 4) * 90} width="28" height="44" fill={C.lamp} opacity="0.7" />)}
              </g>
            );
          })}
        </Layer>
        {/* sidewalk + shelter */}
        <rect x="-400" y="1300" width="1900" height="1000" fill="#2C2B3A" />
        <rect x="-400" y="1300" width="1900" height="20" fill={INK} opacity="0.6" />
        <g transform="translate(70 300)">
          <rect x="0" y="0" width="30" height="1300" fill="#5E6680" stroke={INK} strokeWidth="6" />
          <rect x="-80" y="-40" width="900" height="60" fill="#3A4260" stroke={INK} strokeWidth="7" />
          <rect x="60" y="120" width="360" height="560" fill="#E8E2D2" stroke={INK} strokeWidth="7" />
          <rect x="60" y="120" width="360" height="560" fill={C.lamp} opacity="0.25" />
          <rect x="60" y="120" width="360" height="330" fill="#F6A85E" />
          <circle cx="240" cy="380" r="90" fill="#FFE29A" />
          <rect x="60" y="400" width="360" height="160" fill="#2C8FB8" />
          <path d="M60 430 Q150 410 240 430 T420 430" stroke="#fff" strokeWidth="6" fill="none" opacity="0.7" />
          <rect x="60" y="560" width="360" height="120" fill="#F1E2B8" />
          <text x="240" y="220" fontFamily="'Archivo Black'" fontSize="58" textAnchor="middle" fill="#fff">PARNAÍBA</text>
          <text x="240" y="640" fontFamily={UI} fontSize="30" fontWeight="800" textAnchor="middle" fill="#7A4E35">Delta do Parnaíba</text>
        </g>
        {/* street lamp */}
        <g transform="translate(930 0)">
          <rect x="-16" y="120" width="32" height="1200" fill="#3A4260" stroke={INK} strokeWidth="6" />
          <path d="M0 140 Q0 70 -120 70 L-220 70" stroke="#3A4260" strokeWidth="26" fill="none" />
          <path d="M-300 60 L-150 60 L-170 100 L-280 100Z" fill="#2A2F45" stroke={INK} strokeWidth="6" />
          <Beam x={-225} y={100} len={1500} spread={1100} color={C.sodium} opacity={0.4} />
          <Glow id="s5lamp" x={-225} y={110} r={300} color={C.sodium} opacity={0.8} />
          <Dust t={t} n={10} x={-340} y={60} w={240} h={160} size={5} rise={0} color="#FFE7B0" seed="moth" opacity={0.8} />
        </g>
        <g transform="translate(560 1330) scale(0.86)">
          <LucasBusto t={t} id="s5" expr={expr} turn={lerp(0.35, -0.3, followK) * (1 - lookUp) + 0.05 * lookUp}
            look={{x: lerp(0.9, -0.9, followK) * (1 - lookUp), y: lerp(0.1, -0.9, lookUp)}} tilt={lerp(2, -6, lookUp)} nod={lerp(8, -10, lookUp)}
            light={{side: 1, color: blueK > 0.3 ? C.siren : C.sodium, rim: 0.6 + blueK * 0.4}} outfit="polo" />
        </g>
        <Rain t={t} n={70} opacity={0.3} len={50} speed={1800} seed="s5r" />
        {/* car in the foreground */}
        <g transform={`translate(${carX} 1560) scale(1.1)`}><PatrolCar t={t} /></g>
      </Camera>
      <rect width={W} height={H} fill={C.siren} opacity={blueK * 0.22} style={{mixBlendMode: 'screen'}} />
      <Finish vignette={1} />
    </Frame>
  );
};

// ---------------------------------------------------------------- S06a · building at night, windows go dark
export const S06a = ({dur}) => {
  const t = useST();
  const cols = 5, rows = 10, mine = [3, 7];
  const z = kf(t, [-0.2, 2.2, dur], [1.0, 1.05, 2.4], 'io');
  const fx = 300 + 140 + mine[0] * 150 + 40, fy = 260 + mine[1] * 150 + 50;
  const cx = kf(t, [-0.2, 2.2, dur], [0, 0, fx - W / 2], 'io');
  const cy = kf(t, [-0.2, 2.2, dur], [-520, 0, fy - H / 2], 'io');
  return (
    <Frame bg={C.night0}>
      <Camera z={z} x={cx} y={cy}>
        <Layer d={0.3} cx={cx} cy={cy}>
          <defs><linearGradient id="sky6" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stopColor="#070B1E" /><stop offset="1" stopColor="#1C2550" /></linearGradient></defs>
          <rect x="-800" y="-1400" width="2700" height="4200" fill="url(#sky6)" />
          {Array.from({length: 60}).map((_, i) => <circle key={i} cx={-600 + random('st' + i) * 2300} cy={-1200 + random('sy' + i) * 1800} r={1.5 + random('sr' + i) * 2.5} fill="#fff" opacity={0.4 + 0.6 * Math.abs(Math.sin(t * 2 + i))} />)}
          <circle cx="220" cy="-300" r="110" fill="#F2F0E4" filter="url(#glow)" />
          <circle cx="250" cy="-320" r="22" fill="#D9D6C6" /><circle cx="190" cy="-260" r="14" fill="#D9D6C6" />
          {[0, 1, 2].map((i) => <ellipse key={i} cx={((-400 + i * 700 + t * 40) % 2200) - 400} cy={-500 + i * 260} rx="380" ry="60" fill="#2A3366" opacity="0.6" filter="url(#blur14)" />)}
        </Layer>
        <Layer d={0.7} cx={cx} cy={cy}>
          <rect x="-500" y="500" width="600" height="2400" fill="#121836" stroke={INK} strokeWidth="6" />
          <rect x="1050" y="700" width="700" height="2200" fill="#121836" stroke={INK} strokeWidth="6" />
          {Array.from({length: 20}).map((_, i) => <rect key={i} x={(i % 2 ? 1120 : -420) + (i % 4) * 60} y={800 + i * 90} width="34" height="50" fill={C.lamp} opacity={t > 0.4 + i * 0.07 ? 0.05 : 0.5} />)}
        </Layer>
        {/* main building */}
        <rect x="300" y="160" width="900" height="2600" fill="#1E2852" stroke={INK} strokeWidth="9" />
        <rect x="300" y="160" width="900" height="2600" fill="url(#hatch)" opacity="0.4" />
        <rect x="280" y="130" width="940" height="40" fill="#2A3566" stroke={INK} strokeWidth="7" />
        {Array.from({length: cols * rows}).map((_, i) => {
          const c = i % cols, r = Math.floor(i / cols);
          const isMine = c === mine[0] && r === mine[1];
          const off = 0.4 + random('off' + i) * 1.6;
          const lit = isMine || t < off;
          const x = 340 + c * 150, y = 260 + r * 150;
          return (
            <g key={i}>
              <rect x={x} y={y} width="90" height="100" fill={lit ? (isMine ? '#FFD27A' : C.lamp) : '#0E1330'} stroke={INK} strokeWidth="6" />
              {lit && <rect x={x} y={y} width="90" height="100" fill="#fff" opacity={isMine ? 0.25 : 0} />}
              <path d={`M${x + 45} ${y} L${x + 45} ${y + 100}`} stroke={INK} strokeWidth="4" />
              {lit && <rect x={x - 20} y={y - 20} width="130" height="140" fill={C.lamp} opacity={isMine ? 0.35 : 0.12} filter="url(#blur14)" />}
              {isMine && <g><rect x={x + 50} y={y + 50} width="30" height="40" fill="#1F2A4D" /><circle cx={x + 64} cy={y + 46} r="10" fill="#1F2A4D" /></g>}
            </g>
          );
        })}
        {/* trees foreground */}
        <Layer d={1.25} cx={cx} cy={cy}>
          {[0, 1, 2, 3].map((i) => <circle key={i} cx={-100 + i * 420} cy={1860 + (i % 2) * 60} r={260} fill="#080B18" />)}
        </Layer>
      </Camera>
      <Finish vignette={1.1} />
    </Frame>
  );
};
