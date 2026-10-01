import React from "react";
import {AbsoluteFill, interpolate, useCurrentFrame} from "remotion";
import {clamp, EASE, pop, sp} from "../anim";
import {C, FONT, MONO} from "../theme";
import {FPS, Scene, TIMELINE, tokens, tokenTimes} from "../timeline";

// Persistent backdrop: cool paper tone, a faint dot grid and three slow colour fields.
export const Background: React.FC = () => {
  const frame = useCurrentFrame();
  const t = frame / FPS;
  const blob = (x: number, y: number, r: number, color: string, phase: number) => {
    const dx = Math.sin(t * 0.11 + phase) * 90;
    const dy = Math.cos(t * 0.09 + phase * 1.7) * 60;
    return (
      <div
        style={{
          position: "absolute",
          left: x - r + dx,
          top: y - r + dy,
          width: r * 2,
          height: r * 2,
          borderRadius: "50%",
          background: `radial-gradient(circle at 50% 50%, ${color} 0%, rgba(255,255,255,0) 68%)`,
        }}
      />
    );
  };
  return (
    <AbsoluteFill style={{background: C.bg, overflow: "hidden"}}>
      {blob(260, 180, 620, "rgba(63,81,181,0.10)", 0)}
      {blob(1700, 860, 700, "rgba(123,91,211,0.08)", 2.1)}
      {blob(1500, 120, 460, "rgba(227,155,47,0.07)", 4.2)}
      <svg width="1920" height="1080" style={{position: "absolute", inset: 0}}>
        <defs>
          <pattern id="dots" width="32" height="32" patternUnits="userSpaceOnUse">
            <circle cx="16" cy="16" r="1.4" fill="#B9BFD0" />
          </pattern>
          <radialGradient id="fadeDots" cx="50%" cy="45%" r="70%">
            <stop offset="0%" stopColor="#fff" stopOpacity="0.55" />
            <stop offset="100%" stopColor="#fff" stopOpacity="0" />
          </radialGradient>
          <mask id="dotMask">
            <rect width="1920" height="1080" fill="url(#fadeDots)" />
          </mask>
        </defs>
        <rect width="1920" height="1080" fill="url(#dots)" mask="url(#dotMask)" />
      </svg>
    </AbsoluteFill>
  );
};

// Chapter heading: a numbered tile and the chapter title sliding up from behind a mask.
export const Heading: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const s = pop(frame, 0);
  const title = sp(frame, 5);
  return (
    <div style={{position: "absolute", left: 120, top: 70, display: "flex", alignItems: "center", gap: 22}}>
      <div
        style={{
          width: 64,
          height: 64,
          borderRadius: 18,
          background: C.indigo,
          color: "#fff",
          display: "grid",
          placeItems: "center",
          fontFamily: MONO,
          fontWeight: 600,
          fontSize: 28,
          transform: `scale(${0.5 + 0.5 * s}) rotate(${(1 - s) * -20}deg)`,
          opacity: Math.min(1, s * 2),
          boxShadow: "0 10px 24px -10px rgba(63,81,181,0.7)",
        }}
      >
        {String(scene.number).padStart(2, "0")}
      </div>
      <div style={{overflow: "hidden", paddingBottom: 6}}>
        <div
          style={{
            fontSize: 48,
            fontWeight: 800,
            letterSpacing: "-0.02em",
            color: C.ink,
            transform: `translateY(${(1 - title) * 70}px)`,
            lineHeight: 1.15,
          }}
        >
          {scene.chapter}
        </div>
      </div>
    </div>
  );
};

// Every scene sits in this frame: heading, a slow push-in on the stage, and a soft exit.
export const SceneFrame: React.FC<{scene: Scene; children: React.ReactNode; push?: number}> = ({
  scene,
  children,
  push = 0.018,
}) => {
  const frame = useCurrentFrame();
  const out = interpolate(frame, [scene.frames - 15, scene.frames - 1], [0, 1], {...clamp, easing: EASE});
  const zoom = 1 + push * (frame / scene.frames);
  return (
    <AbsoluteFill
      style={{
        opacity: 1 - out,
        transform: `translateY(${-26 * out}px)`,
        filter: out > 0.01 ? `blur(${out * 10}px)` : undefined,
        fontFamily: FONT,
        color: C.ink,
        fontVariantLigatures: "no-contextual",
      }}
    >
      <AbsoluteFill style={{transform: `scale(${zoom})`, transformOrigin: "50% 55%"}}>{children}</AbsoluteFill>
      {scene.chapter ? <Heading scene={scene} /> : null}
    </AbsoluteFill>
  );
};

// Segmented chapter progress, top right.
export const Progress: React.FC = () => {
  const frame = useCurrentFrame();
  const scenes = TIMELINE.scenes.filter((s) => s.chapter);
  const current = TIMELINE.scenes.find((s) => frame >= s.from && frame < s.from + s.frames);
  if (!current || !current.chapter) return null;
  const local = frame - current.from;
  const vis =
    interpolate(local, [0, 12], [0, 1], clamp) * interpolate(local, [current.frames - 14, current.frames - 2], [1, 0], clamp);
  const firstChapter = scenes[0].from;
  const enter = interpolate(frame, [firstChapter, firstChapter + 20], [0, 1], clamp);
  return (
    <div
      style={{
        position: "absolute",
        right: 120,
        top: 92,
        display: "flex",
        alignItems: "center",
        gap: 18,
        fontFamily: FONT,
        opacity: enter,
      }}
    >
      <div style={{fontFamily: MONO, fontSize: 20, color: C.ink3, opacity: vis, fontVariantNumeric: "tabular-nums"}}>
        {String(current.number).padStart(2, "0")} / {String(TIMELINE.chapters).padStart(2, "0")}
      </div>
      <div style={{display: "flex", gap: 5}}>
        {scenes.map((s) => {
          const fill = frame >= s.from + s.frames ? 1 : frame < s.from ? 0 : (frame - s.from) / s.frames;
          return (
            <div key={s.id} style={{width: 22, height: 6, borderRadius: 3, background: "#DCE0EA", overflow: "hidden"}}>
              <div style={{width: `${fill * 100}%`, height: "100%", background: C.indigo}} />
            </div>
          );
        })}
      </div>
    </div>
  );
};

// ---------------------------------------------------------------------------------------------
// Captions: each narration line is split into readable chunks (at most two lines on screen),
// and the words brighten as they are spoken.

type Chunk = {tokens: string[]; start: number; times: number[]};

const MAX_CHARS = 64;
const PUNCT = /[.,:;?!–]$/;

const chunkLine = (words: string[], times: number[]): Chunk[] => {
  const chunks: Chunk[] = [];
  let cur: number[] = [];
  const len = (idx: number[]) => idx.reduce((a, k) => a + words[k].length + 1, 0);
  const flush = (upto: number) => {
    const take = cur.slice(0, upto);
    cur = cur.slice(upto);
    chunks.push({tokens: take.map((k) => words[k]), start: times[take[0]], times: take.map((k) => times[k])});
  };
  for (let k = 0; k < words.length; k++) {
    cur.push(k);
    const L = len(cur);
    const sentenceEnd = /[.?!]$/.test(words[k]) && L >= 26 && k < words.length - 1;
    if (sentenceEnd) {
      flush(cur.length);
      continue;
    }
    if (L > MAX_CHARS) {
      // Prefer the last punctuation break that keeps both parts readable.
      let cut = -1;
      for (let j = cur.length - 2; j >= 0; j--) {
        if (PUNCT.test(words[cur[j]]) && len(cur.slice(0, j + 1)) >= 22) {
          cut = j + 1;
          break;
        }
      }
      flush(cut > 0 ? cut : cur.length - 1);
    }
  }
  if (cur.length) flush(cur.length);
  // Merge a dangling short tail into the previous chunk when the result still fits.
  if (chunks.length > 1) {
    const last = chunks[chunks.length - 1];
    const prev = chunks[chunks.length - 2];
    const joined = [...prev.tokens, ...last.tokens].join(" ").length;
    if (last.tokens.join(" ").length < 14 && joined <= MAX_CHARS + 14) {
      prev.tokens.push(...last.tokens);
      prev.times.push(...last.times);
      chunks.pop();
    }
  }
  return chunks;
};

export const Captions: React.FC = () => {
  const frame = useCurrentFrame();
  const scene = TIMELINE.scenes.find((s) => frame >= s.from && frame < s.from + s.frames);
  if (!scene) return null;
  const local = frame - scene.from;
  const idx = scene.lines.findIndex((l, i) => {
    const next = scene.lines[i + 1];
    const until = next ? next.from : scene.frames - 10;
    return local >= l.from - 2 && local < Math.min(until, l.from + l.frames + 12);
  });
  if (idx < 0) return null;
  const line = scene.lines[idx];
  const words = tokens(line);
  const times = tokenTimes(line);
  const chunks = chunkLine(words, times);
  const tSec = (local - line.from) / FPS;
  let c = 0;
  for (let k = 0; k < chunks.length; k++) if (tSec >= chunks[k].start - 0.12) c = k;
  const chunk = chunks[c];
  const chunkStart = line.from + Math.round((chunk.start - 0.12) * FPS);
  const lineEnd = Math.min(
    scene.lines[idx + 1] ? scene.lines[idx + 1].from : scene.frames - 10,
    line.from + line.frames + 12,
  );
  const enter = c === 0 ? interpolate(local, [line.from - 2, line.from + 6], [0, 1], clamp) : 1;
  const leave = interpolate(local, [lineEnd - 8, lineEnd], [1, 0], clamp);
  const swap = interpolate(local, [chunkStart, chunkStart + 6], [0, 1], clamp);
  const opacity = enter * leave;
  if (opacity <= 0.01) return null;
  return (
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        bottom: 54,
        display: "flex",
        justifyContent: "center",
        fontFamily: FONT,
        opacity,
        transform: `translateY(${(1 - enter) * 16}px)`,
      }}
    >
      <div
        style={{
          maxWidth: 1480,
          padding: "14px 30px 16px",
          borderRadius: 18,
          background: "rgba(24,28,43,0.86)",
          boxShadow: "0 18px 40px -18px rgba(24,28,43,0.55)",
          color: "#fff",
          fontSize: 36,
          fontWeight: 500,
          lineHeight: 1.36,
          textAlign: "center",
          textWrap: "balance",
        }}
      >
        <span style={{display: "inline", opacity: 0.35 + 0.65 * swap}}>
          {chunk.tokens.map((w, k) => {
            const lit = interpolate(tSec, [chunk.times[k] - 0.1, chunk.times[k] + 0.08], [0, 1], clamp);
            return (
              <span key={k} style={{opacity: 0.52 + 0.48 * lit}}>
                {w}
                {k < chunk.tokens.length - 1 ? " " : ""}
              </span>
            );
          })}
        </span>
      </div>
    </div>
  );
};

// Small caption used on schematic visuals so they are not read as data.
export const Illustrative: React.FC<{x: number; y: number; at?: number; text?: string}> = ({
  x,
  y,
  at = 0,
  text = "Minh họa",
}) => {
  const frame = useCurrentFrame();
  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: y,
        fontSize: 18,
        fontWeight: 600,
        color: C.ink3,
        letterSpacing: "0.06em",
        textTransform: "uppercase",
        opacity: interpolate(frame, [at, at + 12], [0, 0.9], clamp),
      }}
    >
      {text}
    </div>
  );
};
