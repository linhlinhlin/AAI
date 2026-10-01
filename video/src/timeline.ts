import data from "./timeline.json";

export type Line = {
  file: string;
  from: number; // frame, relative to the scene
  frames: number;
  show: string;
  words: (number | string)[][]; // [start, end, spoken text], seconds relative to the clip
};

export type Scene = {
  id: string;
  chapter: string;
  number: number;
  index: number;
  from: number; // frame, absolute
  frames: number;
  lines: Line[];
};

export const TIMELINE = data as {
  fps: number;
  width: number;
  height: number;
  total: number;
  chapters: number;
  scenes: Scene[];
};

export const FPS = TIMELINE.fps;

export const tokens = (line: Line) => line.show.split(/\s+/).filter(Boolean);

const norm = (s: string) => s.toLocaleLowerCase("vi").normalize("NFC").replace(/[^\p{L}\p{N}]+/gu, "");

// Longest common subsequence of two token lists, as index pairs.
const lcs = (a: string[], b: string[]): [number, number][] => {
  const n = a.length;
  const m = b.length;
  const dp = Array.from({length: n + 1}, () => new Array<number>(m + 1).fill(0));
  for (let i = n - 1; i >= 0; i--)
    for (let j = m - 1; j >= 0; j--) dp[i][j] = a[i] && a[i] === b[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
  const pairs: [number, number][] = [];
  let i = 0;
  let j = 0;
  while (i < n && j < m) {
    if (a[i] && a[i] === b[j]) {
      pairs.push([i, j]);
      i++;
      j++;
    } else if (dp[i + 1][j] >= dp[i][j + 1]) i++;
    else j++;
  }
  return pairs;
};

const cache = new Map<Line, number[]>();

// Start time (seconds from the clip start) of every displayed token. The spoken text can
// differ from the displayed one ("89" is read "tám mươi chín", "test" is read "tét"), so the
// displayed tokens are aligned to the synthesised words: identical words anchor the alignment
// and the tokens between two anchors share the spoken words between them. Lines without word
// timings are spread evenly.
export const tokenTimes = (line: Line): number[] => {
  const hit = cache.get(line);
  if (hit) return hit;
  const shown = tokens(line);
  const n = shown.length;
  const w = line.words;
  let times: number[];
  if (w.length === 0) {
    const speech = Math.max(0.5, line.frames / FPS - 0.35);
    times = shown.map((_, i) => 0.1 + (i / n) * speech);
  } else if (w[0].length < 3) {
    times = shown.map((_, i) => w[Math.min(w.length - 1, Math.floor((i * w.length) / n))][0] as number);
  } else {
    const spoken = w.map((x) => norm(String(x[2])));
    const pairs = lcs(shown.map(norm), spoken);
    const start = (j: number) => w[Math.max(0, Math.min(w.length - 1, j))][0] as number;
    times = new Array<number>(n);
    const anchors: [number, number][] = [[-1, -1], ...pairs, [n, w.length]];
    for (let a = 0; a < anchors.length - 1; a++) {
      const [i0, j0] = anchors[a];
      const [i1, j1] = anchors[a + 1];
      if (i0 >= 0 && i0 < n) times[i0] = start(j0);
      const run = i1 - i0 - 1;
      const span = j1 - j0 - 1;
      for (let k = 0; k < run; k++) {
        times[i0 + 1 + k] = span > 0 ? start(j0 + 1 + Math.floor((k * span) / run)) : start(j1);
      }
    }
  }
  cache.set(line, times);
  return times;
};

// Beat helpers for a scene: b(i) is the frame line i starts; w(i, k) is the frame the k-th
// displayed token of line i is spoken (scene-relative, so they plug into useCurrentFrame()).
export const beats = (scene: Scene) => {
  const b = (i: number) => scene.lines[i].from;
  const end = (i: number) => scene.lines[i].from + scene.lines[i].frames;
  const w = (i: number, k: number) => {
    const line = scene.lines[i];
    const times = tokenTimes(line);
    return Math.round(line.from + times[Math.max(0, Math.min(times.length - 1, k))] * FPS);
  };
  // Frame at which a given word (first match, case-insensitive, punctuation ignored) is spoken.
  const at = (i: number, word: string, nth = 0) => {
    const norm = (s: string) => s.toLocaleLowerCase("vi").replace(/[.,:;?!"“”()]/g, "");
    const shown = tokens(scene.lines[i]).map(norm);
    let seen = 0;
    for (let k = 0; k < shown.length; k++) {
      if (shown[k] === norm(word)) {
        if (seen === nth) return w(i, k);
        seen++;
      }
    }
    throw new Error(`"${word}" not in line ${i} of ${scene.id}`);
  };
  return {b, end, w, at, total: scene.frames};
};

export const sceneById = (id: string) => {
  const s = TIMELINE.scenes.find((x) => x.id === id);
  if (!s) throw new Error(`unknown scene ${id}`);
  return s;
};
