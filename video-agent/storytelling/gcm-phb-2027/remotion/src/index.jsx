import React from 'react';
import {registerRoot, Composition, staticFile} from 'remotion';
import {Sheet} from './Sheet.jsx';
import {Video, TOTAL} from './Video.jsx';
const fontCss = `
@font-face{font-family:'Archivo Black';src:url(${staticFile('fonts/ArchivoBlack.ttf')})}
@font-face{font-family:'Bowlby';src:url(${staticFile('fonts/BowlbyOneSC.ttf')})}
@font-face{font-family:'InterV';src:url(${staticFile('fonts/Inter.ttf')})}
@font-face{font-family:'JBMono';src:url(${staticFile('fonts/JetBrainsMono.ttf')})}`;
const Fonts = () => <style>{fontCss}</style>;
const Root = () => (<>
  <Composition id="Sheet" component={() => <><Fonts/><Sheet/></>} durationInFrames={30} fps={30} width={1080} height={1920}/>
  <Composition id="Video" component={() => <><Fonts/><Video/></>} durationInFrames={TOTAL} fps={30} width={1080} height={1920}/>
</>);
registerRoot(Root);
