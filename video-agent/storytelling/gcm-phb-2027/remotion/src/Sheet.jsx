import React from 'react';
import {Frame, Finish, C} from './kit.jsx';
import {LucasPerfil, runPose, walkPose, standPose} from './rigs/LucasPerfil.jsx';
const push = {torso: 63, head: 20, thighF: -63, shinF: -63, thighB: -64, shinB: -64, armF: -4, foreF: 4, armB: 2, foreB: 6, bob: 0, foot: -60};
export const Sheet = () => (
  <Frame bg={C.night3}>
    <g transform="translate(200 820) scale(0.42)"><LucasPerfil t={0} pose={standPose} outfit="prova" expr="confiante"/></g>
    <g transform="translate(520 820) scale(0.42)"><LucasPerfil t={0} pose={walkPose(1.2)} outfit="polo" carry="box" expr="cansado"/></g>
    <g transform="translate(860 820) scale(0.42)"><LucasPerfil t={0} pose={runPose(0.6)} outfit="treino" expr="determinado"/></g>
    <g transform="translate(220 1500) scale(0.42)"><LucasPerfil t={0} pose={runPose(2.2)} outfit="treino" expr="esforco"/></g>
    <g transform="translate(700 1500) scale(0.42)"><LucasPerfil t={0} pose={push} outfit="treino" expr="esforco" sweat={1}/></g>
    <Finish/>
  </Frame>
);
