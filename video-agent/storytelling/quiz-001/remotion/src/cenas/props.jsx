import React from 'react';
import {random} from 'remotion';
import {INK, C, WindowDrops, Rain, Steam, Dust} from '../kit.jsx';

const UI = 'InterV, Inter, sans-serif';
const MONO = 'JBMono, "JetBrains Mono", monospace';

// Phone, local origin = center, 300x600. screen: 'clock' | 'result' | 'edital' | 'off'
export const Phone = ({screen = 'off', on = 1, t = 0, faceDown = false}) => {
  if (faceDown) return (
    <g>
      <rect x="-150" y="-300" width="300" height="600" rx="44" fill="#2A2F3D" stroke={INK} strokeWidth="9" />
      <rect x="-90" y="-250" width="90" height="120" rx="24" fill="#1A1E28" stroke={INK} strokeWidth="5" />
      <circle cx="-62" cy="-215" r="20" fill="#0C0E14" stroke="#556" strokeWidth="4" /><circle cx="-62" cy="-162" r="20" fill="#0C0E14" stroke="#556" strokeWidth="4" />
      <path d="M100 -280 L130 -250 L130 270" stroke="#4A5266" strokeWidth="8" fill="none" opacity="0.7" />
    </g>
  );
  return (
    <g>
      <rect x="-150" y="-300" width="300" height="600" rx="44" fill="#151821" stroke={INK} strokeWidth="9" />
      <clipPath id={`ph${screen}`}><rect x="-132" y="-282" width="264" height="564" rx="32" /></clipPath>
      <g clipPath={`url(#ph${screen})`}>
        <rect x="-132" y="-282" width="264" height="564" fill="#0B0F1C" />
        <g opacity={on}>
          {screen === 'clock' && (
            <g>
              <defs><linearGradient id="lockbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stopColor="#24356B" /><stop offset="1" stopColor="#0E1530" /></linearGradient></defs>
              <rect x="-132" y="-282" width="264" height="564" fill="url(#lockbg)" />
              <circle cx="60" cy="140" r="160" fill="#3B5AA8" opacity="0.35" />
              <text x="0" y="-150" fill="#DCE8FF" fontFamily={UI} fontSize="22" fontWeight="600" textAnchor="middle" opacity="0.85">quinta-feira, 14 de março</text>
              <text x="0" y="-50" fill="#fff" fontFamily={UI} fontSize="104" fontWeight="300" textAnchor="middle" letterSpacing="-3">22:43</text>
              <g transform="translate(0 70)">
                <rect x="-118" y="-46" width="236" height="92" rx="22" fill="#fff" opacity="0.18" />
                <circle cx="-82" cy="0" r="22" fill="#E8B84A" />
                <text x="-82" y="8" fill={INK} fontFamily={UI} fontSize="22" fontWeight="800" textAnchor="middle">!</text>
                <text x="-48" y="-8" fill="#fff" fontFamily={UI} fontSize="19" fontWeight="700">Resultado final</text>
                <text x="-48" y="18" fill="#DCE8FF" fontFamily={UI} fontSize="16">Concurso publicado</text>
              </g>
            </g>
          )}
          {screen === 'result' && (
            <g>
              <rect x="-132" y="-282" width="264" height="564" fill="#F3F5F9" />
              <rect x="-132" y="-282" width="264" height="110" fill="#22325E" />
              <text x="0" y="-212" fill="#fff" fontFamily={UI} fontSize="24" fontWeight="800" textAnchor="middle">RESULTADO FINAL</text>
              {[0, 1, 2, 3, 4].map((i) => (
                <g key={i} transform={`translate(-110 ${-140 + i * 50})`}>
                  <rect width="220" height="34" rx="6" fill="#E3E7EF" />
                  <rect x="12" y="12" width={110 + (i * 37) % 60} height="10" rx="5" fill="#9AA3B5" />
                </g>
              ))}
              <g transform="translate(0 150)">
                <rect x="-118" y="-56" width="236" height="112" rx="16" fill="#FDE8E6" stroke={C.red} strokeWidth="5" />
                <text x="0" y="-12" fill="#7A1F1A" fontFamily={UI} fontSize="22" fontWeight="700" textAnchor="middle">Lucas S. Araújo</text>
                <text x="0" y="26" fill={C.red} fontFamily={UI} fontSize="25" fontWeight="900" textAnchor="middle">Não classificado</text>
              </g>
            </g>
          )}
          {screen === 'edital' && (
            <g>
              <defs><linearGradient id="dawnbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stopColor="#F6B26B" /><stop offset="1" stopColor="#E66A7A" /></linearGradient></defs>
              <rect x="-132" y="-282" width="264" height="564" fill="url(#dawnbg)" />
              <text x="0" y="-150" fill="#fff" fontFamily={UI} fontSize="92" fontWeight="300" textAnchor="middle" letterSpacing="-3">06:12</text>
              <g transform={`translate(0 ${10 - Math.max(0, 1 - t * 3) * 60})`} opacity={Math.min(1, t * 3)}>
                <rect x="-122" y="-70" width="244" height="150" rx="24" fill="#fff" />
                <circle cx="-84" cy="-26" r="24" fill={C.navy} />
                <path d="M-94 -26 l8 8 l14 -16" stroke={C.gold} strokeWidth="6" fill="none" strokeLinecap="round" />
                <text x="-52" y="-30" fill={C.navy} fontFamily={UI} fontSize="17" fontWeight="900">EDITAL PUBLICADO</text>
                <text x="-50" y="-4" fill="#55607A" fontFamily={UI} fontSize="17" fontWeight="600">agora</text>
                <text x="0" y="44" fill={INK} fontFamily={UI} fontSize="24" fontWeight="800" textAnchor="middle">Inscrições abertas</text>
              </g>
            </g>
          )}
        </g>
        {/* glass sheen */}
        <path d="M-132 -282 L40 -282 L-132 60Z" fill="#fff" opacity="0.06" />
      </g>
      <rect x="-40" y="-276" width="80" height="18" rx="9" fill="#05060A" />
    </g>
  );
};

export const Lamp = ({on = 1}) => (
  // origin = base center on desk
  <g>
    <ellipse cx="0" cy="0" rx="90" ry="22" fill="#1E2236" stroke={INK} strokeWidth="7" />
    <path d="M-10 -10 L-60 -260 L-46 -264 L4 -12Z" fill="#30364F" stroke={INK} strokeWidth="6" />
    <path d="M-56 -258 L60 -360 L70 -346 L-46 -250Z" fill="#30364F" stroke={INK} strokeWidth="6" />
    <g transform="translate(66 -352) rotate(28)">
      <path d="M-70 0 L70 0 L44 -120 L-44 -120Z" fill="#3D4566" stroke={INK} strokeWidth="7" strokeLinejoin="round" />
      <ellipse cx="0" cy="0" rx="70" ry="16" fill={on > 0 ? C.lampHot : '#556'} stroke={INK} strokeWidth="6" />
    </g>
  </g>
);

export const Mug = ({t, steam = true}) => (
  <g>
    <path d="M-60 -130 L60 -130 L54 0 Q0 14 -54 0Z" fill="#C9473F" stroke={INK} strokeWidth="7" strokeLinejoin="round" />
    <path d="M60 -100 Q110 -96 104 -56 Q98 -22 56 -30" fill="none" stroke={INK} strokeWidth="18" />
    <path d="M60 -100 Q110 -96 104 -56 Q98 -22 56 -30" fill="none" stroke="#C9473F" strokeWidth="8" />
    <ellipse cx="0" cy="-130" rx="60" ry="14" fill="#5A3020" stroke={INK} strokeWidth="6" />
    <path d="M-60 -130 L-30 -130 L-30 4 Q-46 4 -54 0Z" fill={INK} opacity="0.25" />
    {steam && <Steam t={t} x={0} y={-150} scale={0.8} opacity={0.45} />}
  </g>
);

const BOOKC = ['#8E3B46', '#2F5D8C', '#C98B2B', '#3F6E4F', '#6B4C8A', '#B5523B'];
export const BookStack = ({n = 5, seed = 'bk', labels = true}) => (
  <g>
    {Array.from({length: n}).map((_, i) => {
      const w = 300 + random(seed + i) * 80, h = 52 + random(seed + 'h' + i) * 20;
      const x = -w / 2 + (random(seed + 'x' + i) - 0.5) * 50;
      const y = -(i + 1) * 64;
      const col = BOOKC[(i + Math.floor(random(seed) * 6)) % 6];
      return (
        <g key={i} transform={`rotate(${(random(seed + 'r' + i) - 0.5) * 5} 0 ${y})`}>
          <rect x={x} y={y} width={w} height={h} rx="6" fill={col} stroke={INK} strokeWidth="6" />
          <rect x={x + w - 26} y={y + 6} width="16" height={h - 12} fill={C.paper} opacity="0.85" />
          {labels && <rect x={x + 40} y={y + h / 2 - 7} width={w * 0.4} height="14" rx="4" fill={C.paper} opacity="0.7" />}
          <rect x={x} y={y + h - 14} width={w} height="14" fill={INK} opacity="0.2" />
        </g>
      );
    })}
  </g>
);

// wall calendar, origin top-left, 300x330. crossed = number of X'd days, tear = 0..1 top page lifting
export const Calendar = ({crossed = 12, month = 'MARÇO', tear = 0, t = 0}) => (
  <g>
    <rect x="0" y="0" width="300" height="340" fill={C.paper} stroke={INK} strokeWidth="7" />
    <rect x="0" y="0" width="300" height="70" fill={C.red} stroke={INK} strokeWidth="7" />
    <text x="150" y="50" fill="#fff" fontFamily="'Archivo Black', sans-serif" fontSize="34" textAnchor="middle">{month}</text>
    {Array.from({length: 28}).map((_, i) => {
      const cx = 22 + (i % 7) * 38, cy = 96 + Math.floor(i / 7) * 58;
      return (
        <g key={i}>
          <rect x={cx - 14} y={cy - 18} width="32" height="44" fill="none" stroke={INK} strokeWidth="2" opacity="0.3" />
          {i < crossed && <path d={`M${cx - 10} ${cy - 12} L${cx + 14} ${cy + 18} M${cx + 14} ${cy - 12} L${cx - 10} ${cy + 18}`} stroke={C.red} strokeWidth="4.5" strokeLinecap="round" />}
        </g>
      );
    })}
    <circle cx="70" cy="-6" r="10" fill="#555" stroke={INK} strokeWidth="4" />
    <circle cx="230" cy="-6" r="10" fill="#555" stroke={INK} strokeWidth="4" />
  </g>
);

// cork board with messy notes, origin top-left 420x360
export const Corkboard = ({ripped = 0, t = 0}) => (
  <g>
    <rect x="0" y="0" width="420" height="360" fill="#B88A5A" stroke={INK} strokeWidth="9" />
    <rect x="0" y="0" width="420" height="360" fill="url(#halftoneFine)" opacity="0.6" />
    <rect x="10" y="10" width="400" height="340" fill="none" stroke="#7E5734" strokeWidth="10" />
    {[[40, 40, -6, '#FFF59A'], [170, 30, 5, '#FFFFFF'], [290, 60, -3, '#A6E3F2'], [60, 180, 4, '#FFFFFF'], [200, 170, -8, '#F7B9C8'], [300, 210, 6, '#FFF59A']].map(([x, y, r, col], i) => {
      const fly = ripped > 0 ? ripped : 0;
      return (
        <g key={i} transform={`translate(${x + fly * (i - 2.5) * 160} ${y + fly * fly * 600}) rotate(${r + fly * (i % 2 ? 140 : -120)})`} opacity={1 - fly * 0.6}>
          <rect x="0" y="0" width="100" height="110" fill={col} stroke={INK} strokeWidth="4" />
          {[24, 44, 64, 84].map((ly) => <path key={ly} d={`M12 ${ly} L${70 + ((i * 13 + ly) % 20)} ${ly}`} stroke="#5A5A7A" strokeWidth="4" strokeLinecap="round" opacity="0.6" />)}
          <circle cx="50" cy="8" r="9" fill={C.red} stroke={INK} strokeWidth="3" />
        </g>
      );
    })}
  </g>
);

// window with sky; origin top-left. mode 'night' | 'dawn'
export const RoomWindow = ({t, w = 420, h = 620, mode = 'night', rain = true, dawnK = 0}) => {
  const id = `win${mode}${w}`;
  return (
    <g>
      <defs>
        <linearGradient id={`${id}n`} x1="0" y1="0" x2="0" y2="1"><stop offset="0" stopColor="#0B1026" /><stop offset="1" stopColor="#24305A" /></linearGradient>
        <linearGradient id={`${id}d`} x1="0" y1="0" x2="0" y2="1"><stop offset="0" stopColor="#5B78B8" /><stop offset="0.6" stopColor="#F2A06A" /><stop offset="1" stopColor="#FFD58A" /></linearGradient>
        <clipPath id={`${id}c`}><rect x="0" y="0" width={w} height={h} /></clipPath>
      </defs>
      <g clipPath={`url(#${id}c)`}>
        <rect width={w} height={h} fill={`url(#${id}n)`} />
        <rect width={w} height={h} fill={`url(#${id}d)`} opacity={dawnK} />
        {/* distant city */}
        {Array.from({length: 9}).map((_, i) => {
          const bw = 50 + random('cw' + i) * 60, bh = 140 + random('ch' + i) * 260;
          const bx = i * 52 - 20;
          return (
            <g key={i}>
              <rect x={bx} y={h - bh} width={bw} height={bh} fill={dawnK > 0.5 ? '#3B3F6B' : '#121935'} />
              {Array.from({length: 12}).map((__, j) => random('wl' + i + j) > 0.55 && (
                <rect key={j} x={bx + 8 + (j % 3) * 14} y={h - bh + 16 + Math.floor(j / 3) * 30} width="8" height="12" fill={C.lamp} opacity={(1 - dawnK) * 0.85} />
              ))}
            </g>
          );
        })}
        {dawnK > 0 && <circle cx={w * 0.7} cy={h * 0.78} r="70" fill="#FFE7A8" opacity={dawnK} filter="url(#blur8)" />}
        {rain && <Rain t={t} n={50} area={[-60, -60, w + 120, h + 120]} len={50} speed={1500} opacity={0.4} seed={id} width={2.5} />}
        {rain && <WindowDrops t={t} x={0} y={0} w={w} h={h} n={18} seed={id + 'd'} />}
        <rect width={w} height={h} fill="#8FB0FF" opacity="0.06" />
      </g>
      <rect x="-18" y="-18" width={w + 36} height={h + 36} fill="none" stroke="#3B4364" strokeWidth="36" />
      <rect x="-18" y="-18" width={w + 36} height={h + 36} fill="none" stroke={INK} strokeWidth="7" />
      <rect x="0" y="0" width={w} height={h} fill="none" stroke={INK} strokeWidth="6" />
      <path d={`M${w / 2} 0 L${w / 2} ${h} M0 ${h * 0.45} L${w} ${h * 0.45}`} stroke="#3B4364" strokeWidth="18" />
      <path d={`M${w / 2} 0 L${w / 2} ${h} M0 ${h * 0.45} L${w} ${h * 0.45}`} stroke={INK} strokeWidth="4" opacity="0.6" />
      <rect x="-40" y={h + 14} width={w + 80} height="30" fill="#4A5274" stroke={INK} strokeWidth="6" />
    </g>
  );
};

export const Laptop = ({on = 1, t = 0, scrollK = 0}) => (
  // origin = hinge center, screen faces the viewer
  <g>
    <path d="M-260 -360 L260 -360 L260 0 L-260 0Z" fill="#2E3446" stroke={INK} strokeWidth="8" strokeLinejoin="round" />
    <rect x="-236" y="-338" width="472" height="316" fill="#0E1426" />
    <g opacity={on}>
      <rect x="-236" y="-338" width="472" height="316" fill="#DCE6F5" />
      <rect x="-236" y="-338" width="472" height="40" fill="#22325E" />
      <g transform={`translate(0 ${-scrollK * 120})`}>
        {Array.from({length: 9}).map((_, i) => (
          <g key={i}>
            <rect x="-200" y={-280 + i * 44} width={i % 3 === 0 ? 240 : 380} height="14" rx="7" fill={i % 3 === 0 ? '#22325E' : '#94A0B8'} />
          </g>
        ))}
      </g>
    </g>
    <path d="M-300 0 L300 0 L330 30 L-330 30Z" fill="#3A4157" stroke={INK} strokeWidth="7" strokeLinejoin="round" />
  </g>
);

export const DeskClock = ({text = '00:17'}) => (
  <g>
    <rect x="-110" y="-80" width="220" height="90" rx="14" fill="#1A1D28" stroke={INK} strokeWidth="7" />
    <text x="0" y="-18" fill="#FF5A4E" fontFamily={MONO} fontSize="56" fontWeight="800" textAnchor="middle" letterSpacing="2">{text}</text>
    <rect x="-90" y="10" width="20" height="14" fill={INK} /><rect x="70" y="10" width="20" height="14" fill={INK} />
  </g>
);
