import React from "react";
import {AbsoluteFill, Audio, Sequence, staticFile} from "remotion";
import {Background, Captions, Progress} from "./components/frame";
import {SCENES} from "./scenes";
import {TIMELINE} from "./timeline";

// Music sits about 20 dB under the voice while someone is speaking and lifts a little in the
// pauses; the envelope is computed once for the whole film.
const SPEECH = TIMELINE.scenes.flatMap((s) => s.lines.map((l) => [s.from + l.from, s.from + l.from + l.frames] as const));
const RAMP = 10;
const MUSIC = (() => {
  const v = new Float32Array(TIMELINE.total);
  for (let f = 0; f < TIMELINE.total; f++) {
    let duck = 0;
    for (const [a, b] of SPEECH) {
      if (f < a - RAMP || f > b + RAMP) continue;
      const d = f < a ? (a - f) / RAMP : f > b ? (f - b) / RAMP : 0;
      duck = Math.max(duck, 1 - d);
    }
    const fadeIn = Math.min(1, f / 45);
    const fadeOut = Math.min(1, Math.max(0, (TIMELINE.total - 6 - f) / 110));
    v[f] = (0.17 - 0.08 * duck) * fadeIn * fadeOut;
  }
  return v;
})();

export const Explainer: React.FC = () => (
  <AbsoluteFill>
    <Background />
    {TIMELINE.scenes.map((scene) => {
      const entry = SCENES[scene.id];
      const Comp = entry.component;
      return (
        <Sequence key={scene.id} from={scene.from} durationInFrames={scene.frames} name={scene.id}>
          <Comp scene={scene} />
        </Sequence>
      );
    })}
    <Progress />
    <Captions />

    <Audio
      src={staticFile("audio/music.wav")}
      loop
      loopVolumeCurveBehavior="extend"
      volume={(f) => MUSIC[Math.max(0, Math.min(MUSIC.length - 1, Math.round(f)))]}
    />
    {TIMELINE.scenes.map((scene) =>
      scene.lines.map((line, i) => (
        <Sequence key={`${scene.id}-${i}`} from={scene.from + line.from} durationInFrames={line.frames + 4} layout="none">
          <Audio src={staticFile(line.file)} />
        </Sequence>
      )),
    )}
    {TIMELINE.scenes.slice(1).map((scene) => (
      <Sequence key={`w-${scene.id}`} from={Math.max(0, scene.from - 6)} durationInFrames={40} layout="none">
        <Audio src={staticFile("audio/whoosh.wav")} volume={0.32} />
      </Sequence>
    ))}
    {TIMELINE.scenes.flatMap((scene) =>
      (SCENES[scene.id].pops?.(scene) ?? []).map((f, k) => (
        <Sequence key={`p-${scene.id}-${k}`} from={scene.from + f} durationInFrames={20} layout="none">
          <Audio src={staticFile("audio/pop.wav")} volume={0.26} />
        </Sequence>
      )),
    )}
  </AbsoluteFill>
);
