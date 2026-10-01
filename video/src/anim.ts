import {Easing, interpolate, spring} from "remotion";

export const FPS = 30;
export const clamp = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;
export const EASE = Easing.bezier(0.22, 1, 0.36, 1); // ease-out-quint, calm and precise

// A settled spring from 0 to 1 that starts at frame `at`.
export const sp = (frame: number, at: number, damping = 200, durationInFrames?: number) =>
  spring({frame: frame - at, fps: FPS, config: {damping}, durationInFrames});

// A spring with a small overshoot, for things that pop into place.
export const pop = (frame: number, at: number) =>
  spring({frame: frame - at, fps: FPS, config: {damping: 13, stiffness: 170, mass: 0.7}});

export const fade = (frame: number, at: number, dur = 14) => interpolate(frame, [at, at + dur], [0, 1], clamp);

export const tween = (frame: number, at: number, dur: number, from: number, to: number) =>
  interpolate(frame, [at, at + dur], [from, to], {...clamp, easing: EASE});

// Rise into place: opacity and a short upward move.
export const rise = (frame: number, at: number, dist = 36) => {
  const s = sp(frame, at);
  return {opacity: s, transform: `translateY(${(1 - s) * dist}px)`};
};

// Scale-in with a little overshoot.
export const zoomIn = (frame: number, at: number) => {
  const s = pop(frame, at);
  return {opacity: Math.min(1, s * 1.4), transform: `scale(${0.6 + 0.4 * s})`};
};

export const lerp = (a: number, b: number, t: number) => a + (b - a) * t;

// Deterministic pseudo-random numbers, so every render is identical.
export const rand = (seed: number) => {
  const x = Math.sin(seed * 12.9898 + 78.233) * 43758.5453;
  return x - Math.floor(x);
};

export const vi = (n: number, digits = 0) =>
  n.toLocaleString("de-DE", {minimumFractionDigits: digits, maximumFractionDigits: digits});
