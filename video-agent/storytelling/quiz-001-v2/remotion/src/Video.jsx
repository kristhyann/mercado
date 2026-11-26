import React from 'react';
import {AbsoluteFill, Sequence, useCurrentFrame, interpolate} from 'remotion';
import {SceneCtx, FPS, C} from './kit.jsx';
import * as Q2 from './cenas/Quiz2.jsx';

export const TIMELINE = Q2.buildTimeline();
export const TOTAL = 10974;

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
      <Sequence key={id} from={s - ov} durationInFrames={e - s + ov + (id === 'FIM' ? 0 : 1)} name={id}>
        <SceneCtx.Provider value={ov / FPS}>
          <Trans type={tr} ov={ov}><Comp dur={(e - s) / FPS} /></Trans>
        </SceneCtx.Provider>
      </Sequence>
    ))}
    <Q2.Captions2 />
    <Overlays />
  </AbsoluteFill>
);
