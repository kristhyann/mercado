import React from 'react';
import {AbsoluteFill, Sequence, useCurrentFrame, interpolate} from 'remotion';
import {SceneCtx, FPS, C} from './kit.jsx';
import * as E from './cenas/Estudo.jsx';
import * as F from './cenas/Final.jsx';
import * as X from './cenas/Reels.jsx';

// [id, component, startFrame, endFrame, transitionIn, overlapFrames]
export const TIMELINE = [
  ['R1', X.R1, 0, 112, 'cut', 0],
  ['R2', X.R2, 112, 190, 'flash', 0],
  ['R3', X.R3, 190, 255, 'cut', 0],
  ['R4a', X.R4a, 255, 282, 'whipX', 5],
  ['R4b', E.S08c, 282, 307, 'cut', 0],
  ['R4c', E.S08b, 307, 343, 'cut', 0],
  ['R4d', F.S08d, 343, 385, 'cut', 0],
  ['R5a', X.R5a, 385, 433, 'whipY', 5],
  ['R5b', X.R5b, 433, 502, 'cut', 0],
  ['R6a', X.R6a, 502, 586, 'whipX', 5],
  ['R6b', X.R6b, 586, 666, 'flash', 0],
  ['R7', X.R7, 666, 882, 'flash', 0],
];
export const TOTAL = 882;

const Trans = ({type, ov, children}) => {
  const f = useCurrentFrame();
  if (!ov || type === 'cut') return <AbsoluteFill>{children}</AbsoluteFill>;
  const k = interpolate(f, [0, ov], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  if (type === 'fade') return <AbsoluteFill style={{opacity: k}}>{children}</AbsoluteFill>;
  if (type === 'whipX' || type === 'whipY') {
    const d = (1 - k) * 1080;
    const tr = type === 'whipX' ? `translateX(${d}px)` : `translateY(${-d * 1.6}px)`;
    return <AbsoluteFill style={{transform: tr, filter: `blur(${(1 - k) * 30}px)`}}>{children}</AbsoluteFill>;
  }
  if (type === 'flash') return <AbsoluteFill style={{opacity: k}}>{children}</AbsoluteFill>;
  return <AbsoluteFill>{children}</AbsoluteFill>;
};

// flashes / whip blur layered on top at cut points
const Overlays = () => {
  const f = useCurrentFrame();
  const flashes = TIMELINE.filter((s) => s[4] === 'flash').map((s) => s[2]);
  let a = 0;
  for (const st of flashes) a = Math.max(a, interpolate(f, [st - 6, st, st + 10], [0, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
  return a > 0 ? <AbsoluteFill style={{background: '#FFF1CF', opacity: a * 0.9}} /> : null;
};

export const Video = () => (
  <AbsoluteFill style={{background: C.night0}}>
    {TIMELINE.map(([id, Comp, s, e, tr, ov]) => (
      <Sequence key={id} from={s - ov} durationInFrames={e - s + ov + (id === 'R7' ? 0 : 1)} name={id}>
        <SceneCtx.Provider value={ov / FPS}>
          <Trans type={tr} ov={ov}><Comp dur={(e - s) / FPS} /></Trans>
        </SceneCtx.Provider>
      </Sequence>
    ))}
    <X.Captions />
    <Overlays />
  </AbsoluteFill>
);
