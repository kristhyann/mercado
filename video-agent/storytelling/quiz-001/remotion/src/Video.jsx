import React from 'react';
import {AbsoluteFill, Sequence, useCurrentFrame, interpolate} from 'remotion';
import {SceneCtx, FPS, C} from './kit.jsx';
import * as Q from './cenas/Quiz.jsx';

// [id, component, startFrame, endFrame, transitionIn, overlapFrames]
export const TIMELINE = [
  ['I0', Q.Intro, 0, 111, 'cut', 0],
  ['T1', Q.T1, 111, 156, 'cut', 0],
  ['S1', Q.S1, 156, 375, 'whipX', 5],
  ['P1', Q.P1, 375, 1227, 'fade', 6],
  ['E1', Q.E1, 1227, 1344, 'whipY', 5],
  ['T2', Q.T2, 1344, 1386, 'cut', 0],
  ['S2', Q.S2, 1386, 1542, 'whipX', 5],
  ['P2', Q.P2, 1542, 2265, 'fade', 6],
  ['E2', Q.E2, 2265, 2400, 'whipY', 5],
  ['O', Q.Outro, 2400, 2640, 'flash', 0],
];
export const TOTAL = 2640;

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
      <Sequence key={id} from={s - ov} durationInFrames={e - s + ov + (id === 'O' ? 0 : 1)} name={id}>
        <SceneCtx.Provider value={ov / FPS}>
          <Trans type={tr} ov={ov}><Comp dur={(e - s) / FPS} /></Trans>
        </SceneCtx.Provider>
      </Sequence>
    ))}
    <Q.Captions />
    <Overlays />
  </AbsoluteFill>
);
