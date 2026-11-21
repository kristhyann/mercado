import React from 'react';
import {AbsoluteFill, Sequence, useCurrentFrame, interpolate} from 'remotion';
import {SceneCtx, FPS, C} from './kit.jsx';
import * as Q from './cenas/Quarto.jsx';
import * as R from './cenas/Rua.jsx';
import * as E from './cenas/Estudo.jsx';
import * as F from './cenas/Final.jsx';

// [id, component, startFrame, endFrame, transitionIn, overlapFrames]
export const TIMELINE = [
  ['S01', Q.S01, 0, 60, 'cut', 0],
  ['S02', Q.S02, 60, 137, 'cut', 0],
  ['S03', Q.S03, 137, 254, 'fade', 9],
  ['S04a', R.S04a, 254, 324, 'whipX', 7],
  ['S04b', R.S04b, 324, 366, 'cut', 0],
  ['S04c', R.S04c, 366, 413, 'cut', 0],
  ['S05', R.S05, 413, 563, 'fade', 8],
  ['S06a', R.S06a, 563, 683, 'cut', 0],
  ['S06b', E.S06b, 683, 761, 'fade', 8],
  ['S07', E.S07, 761, 873, 'cut', 0],
  ['S08a', E.S08a, 873, 924, 'whipY', 6],
  ['S08b', E.S08b, 924, 955, 'cut', 0],
  ['S08c', E.S08c, 955, 986, 'cut', 0],
  ['S08d', F.S08d, 986, 1062, 'whipX', 6],
  ['S09', E.S09, 1062, 1184, 'fade', 10],
  ['S10a', E.S10a, 1184, 1253, 'fade', 6],
  ['S10b', F.S10b, 1253, 1349, 'flash', 0],
  ['S11', F.S11, 1349, 1490, 'fade', 10],
  ['S12', F.S12, 1490, 1710, 'flash', 0],
];
export const TOTAL = 1710;

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
      <Sequence key={id} from={s - ov} durationInFrames={e - s + ov + (id === 'S12' ? 0 : 1)} name={id}>
        <SceneCtx.Provider value={ov / FPS}>
          <Trans type={tr} ov={ov}><Comp dur={(e - s) / FPS} /></Trans>
        </SceneCtx.Provider>
      </Sequence>
    ))}
    <Overlays />
  </AbsoluteFill>
);
