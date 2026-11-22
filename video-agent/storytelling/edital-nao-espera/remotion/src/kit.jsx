import React from 'react';
import {interpolate, Easing, random, useCurrentFrame, useVideoConfig} from 'remotion';

export const FPS = 30;
export const W = 1080, H = 1920;
export const INK = '#1A1420';

export const C = {
  night0: '#0E1328', night1: '#141B33', night2: '#1F2A4D', night3: '#2E3D6B', night4: '#46598F',
  lamp: '#F2B65A', lampHot: '#FFE1A3', screen: '#8FD3FF', screenHot: '#E4F6FF',
  dawn: '#F28C4B', dawnPink: '#E66A7A', dawnGold: '#FFD27A', sky: '#7FA7D9',
  navy: '#0F1A36', gold: '#E8B84A', goldHot: '#FFE29A',
  wood: '#7A4E35', woodDark: '#4F3122', woodLight: '#9C6A48',
  paper: '#F1E6CF', paperShade: '#CDBE9F', red: '#D94B45', siren: '#4AA8FF',
  sodium: '#F5A04A', concrete: '#8A8F9C', concreteDark: '#5D6270',
};

// seconds of the current Sequence
export const useT = () => useCurrentFrame() / FPS;

const EASES = {
  io: Easing.inOut(Easing.cubic), o: Easing.out(Easing.cubic), i: Easing.in(Easing.cubic),
  lin: (x) => x, back: Easing.out(Easing.back(1.6)), sine: Easing.inOut(Easing.sin),
};
// keyframes in seconds, clamped, eased between each pair
export const kf = (t, times, values, ease = 'io') =>
  interpolate(t, times, values, {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: EASES[ease] || ease});

export const lerp = (a, b, x) => a + (b - a) * x;
export const clamp01 = (x) => Math.max(0, Math.min(1, x));
export const wobble = (t, speed = 1, amp = 1, seed = 0) =>
  amp * (Math.sin(t * speed * 2.1 + seed) * 0.6 + Math.sin(t * speed * 3.7 + seed * 2.3) * 0.4);

// Camera: transforms a full-frame group. x/y = where the camera looks (offset px), z = zoom, r = roll (deg)
export const Camera = ({x = 0, y = 0, z = 1, r = 0, children}) => (
  <g transform={`translate(${W / 2} ${H / 2}) rotate(${r}) scale(${z}) translate(${-W / 2 - x} ${-H / 2 - y})`}>
    {children}
  </g>
);

// Layer at depth d: d=1 moves with the camera, d<1 farther (moves less), d>1 nearer (moves more)
export const Layer = ({d = 1, cx = 0, cy = 0, blur = 0, children, opacity = 1}) => (
  <g transform={`translate(${cx * (1 - d)} ${cy * (1 - d)})`} filter={blur ? `url(#blur${blur})` : undefined} opacity={opacity}>
    {children}
  </g>
);

// shared defs: textures, blurs, gradients used across scenes
export const Defs = () => (
  <defs>
    <filter id="grain" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="3" />
      <feColorMatrix values="0 0 0 0 0.5  0 0 0 0 0.45  0 0 0 0 0.4  0 0 0 0.55 0" />
    </filter>
    <filter id="paperTex" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.018 0.03" numOctaves="3" seed="8" />
      <feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.35 0" />
    </filter>
    {[2, 4, 8, 14, 24].map((b) => (
      <filter key={b} id={`blur${b}`} x="-30%" y="-30%" width="160%" height="160%">
        <feGaussianBlur stdDeviation={b} />
      </filter>
    ))}
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="18" result="b" />
      <feMerge><feMergeNode in="b" /><feMergeNode in="SourceGraphic" /></feMerge>
    </filter>
    <pattern id="halftone" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(30)">
      <circle cx="7" cy="7" r="2.6" fill={INK} opacity="0.35" />
    </pattern>
    <pattern id="halftoneFine" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(30)">
      <circle cx="4.5" cy="4.5" r="1.5" fill={INK} opacity="0.3" />
    </pattern>
    <pattern id="hatch" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(-35)">
      <line x1="0" y1="0" x2="0" y2="12" stroke={INK} strokeWidth="2.2" opacity="0.28" />
    </pattern>
    <radialGradient id="vignette" cx="50%" cy="50%" r="75%">
      <stop offset="55%" stopColor="#000" stopOpacity="0" />
      <stop offset="100%" stopColor="#000" stopOpacity="0.75" />
    </radialGradient>
  </defs>
);

// grain + vignette over everything (screen space)
export const Finish = ({vignette = 0.85, grain = 0.5}) => (
  <g pointerEvents="none">
    <rect width={W} height={H} fill="url(#vignette)" opacity={vignette} />
    <rect width={W} height={H} filter="url(#grain)" opacity={grain} style={{mixBlendMode: 'overlay'}} />
  </g>
);

export const Frame = ({bg = C.night1, children}) => (
  <svg viewBox={`0 0 ${W} ${H}`} width={W} height={H} style={{position: 'absolute', inset: 0, background: bg}}>
    <Defs />
    {children}
  </svg>
);

// ---------- effects ----------
export const Rain = ({t, n = 140, color = '#A9BEF5', speed = 2600, len = 70, angle = 10, opacity = 0.5, seed = 'r', area = [-200, -200, W + 400, H + 400], width = 3}) => {
  const dx = Math.tan((angle * Math.PI) / 180) * len;
  return (
    <g opacity={opacity}>
      {Array.from({length: n}).map((_, i) => {
        const s = 0.6 + random(seed + 's' + i) * 0.8;
        const x0 = area[0] + random(seed + 'x' + i) * area[2];
        const y = area[1] + ((random(seed + 'y' + i) * area[3] + t * speed * s) % area[3]);
        const x = x0 - ((t * speed * s) % area[3]) * Math.tan((angle * Math.PI) / 180);
        return <line key={i} x1={x} y1={y} x2={x - dx * s} y2={y + len * s} stroke={color} strokeWidth={width * s} strokeLinecap="round" opacity={0.4 + 0.6 * s - 0.4} />;
      })}
    </g>
  );
};

// raindrops sliding on a window pane, within a rect
export const WindowDrops = ({t, x, y, w, h, n = 26, seed = 'wd', color = '#BFD0FF'}) => (
  <g>
    {Array.from({length: n}).map((_, i) => {
      const px = x + random(seed + i) * w;
      const sp = 40 + random(seed + 'v' + i) * 160;
      const py = y + ((random(seed + 'p' + i) * h + t * sp) % h);
      const r = 4 + random(seed + 'r' + i) * 7;
      return (
        <g key={i} opacity="0.8">
          <line x1={px} y1={py - r * 6} x2={px} y2={py} stroke={color} strokeWidth={r * 0.5} opacity="0.35" strokeLinecap="round" />
          <ellipse cx={px} cy={py} rx={r * 0.8} ry={r} fill={color} opacity="0.55" />
          <ellipse cx={px - r * 0.25} cy={py - r * 0.3} rx={r * 0.25} ry={r * 0.3} fill="#fff" opacity="0.8" />
        </g>
      );
    })}
  </g>
);

// floating dust / embers / light particles
export const Dust = ({t, n = 40, x = 0, y = 0, w = W, h = H, color = '#FFE6B0', size = 4, rise = 30, seed = 'd', opacity = 0.7}) => (
  <g opacity={opacity}>
    {Array.from({length: n}).map((_, i) => {
      const s = 0.4 + random(seed + 's' + i);
      const px = x + random(seed + 'x' + i) * w + Math.sin(t * 0.8 * s + i) * 18;
      const py = y + ((random(seed + 'y' + i) * h - t * rise * s) % h + h) % h;
      const tw = 0.5 + 0.5 * Math.sin(t * 3 * s + i * 1.7);
      return <circle key={i} cx={px} cy={py} r={size * s} fill={color} opacity={0.25 + 0.75 * tw} />;
    })}
  </g>
);

export const Steam = ({t, x, y, scale = 1, opacity = 0.5, seed = 0}) => (
  <g transform={`translate(${x} ${y}) scale(${scale})`} opacity={opacity} filter="url(#blur4)">
    {[0, 1, 2].map((i) => {
      const ph = (t * 0.45 + i / 3 + seed) % 1;
      const yy = -ph * 220;
      const xx = Math.sin(ph * 6 + i * 2) * 26;
      return <ellipse key={i} cx={xx} cy={yy} rx={20 + ph * 30} ry={34 + ph * 24} fill="#fff" opacity={(1 - ph) * 0.55} />;
    })}
  </g>
);

// a soft light beam (cone) from a point
export const Beam = ({x, y, angle = 0, len = 900, spread = 380, color = C.lamp, opacity = 0.25}) => (
  <g transform={`translate(${x} ${y}) rotate(${angle})`} opacity={opacity} style={{mixBlendMode: 'screen'}}>
    <defs>
      <linearGradient id={`beam${Math.round(x)}${Math.round(y)}`} x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stopColor={color} stopOpacity="0.9" />
        <stop offset="1" stopColor={color} stopOpacity="0" />
      </linearGradient>
    </defs>
    <path d={`M-20 0 L20 0 L${spread / 2} ${len} L${-spread / 2} ${len}Z`} fill={`url(#beam${Math.round(x)}${Math.round(y)})`} filter="url(#blur14)" />
  </g>
);

// radial glow
export const Glow = ({x, y, r = 300, color = C.lamp, opacity = 0.5, id}) => (
  <g style={{mixBlendMode: 'screen'}} opacity={opacity}>
    <defs>
      <radialGradient id={id}>
        <stop offset="0" stopColor={color} stopOpacity="1" />
        <stop offset="1" stopColor={color} stopOpacity="0" />
      </radialGradient>
    </defs>
    <circle cx={x} cy={y} r={r} fill={`url(#${id})`} />
  </g>
);

// fade helper for scene in/out
export const fadeIO = (t, dur, fin = 0.25, fout = 0.25) =>
  Math.min(fin ? clamp01(t / fin) : 1, fout ? clamp01((dur - t) / fout) : 1);

// on-screen title text with ink shadow
export const Title = ({x, y, children, size = 90, color = '#fff', weight = 900, anchor = 'middle', opacity = 1, spacing = 2, font = 'Anton, Impact, "Arial Narrow", sans-serif', stroke = INK, sw = 0}) => (
  <g opacity={opacity}>
    <text x={x + 5} y={y + 7} fontFamily={font} fontSize={size} fontWeight={weight} textAnchor={anchor} letterSpacing={spacing} fill={INK} opacity="0.55">{children}</text>
    <text x={x} y={y} fontFamily={font} fontSize={size} fontWeight={weight} textAnchor={anchor} letterSpacing={spacing} fill={color} stroke={sw ? stroke : 'none'} strokeWidth={sw} paintOrder="stroke">{children}</text>
  </g>
);

// scene-local time (seconds since the scene's own start, negative during an incoming overlap)
export const SceneCtx = React.createContext(0);
export const useST = () => useCurrentFrame() / FPS - React.useContext(SceneCtx);
