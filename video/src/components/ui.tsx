import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {clamp, EASE, pop, sp, vi} from "../anim";
import {C, FONT, MONO, shadow} from "../theme";
import {Icon, IconName} from "./Icon";

export type Tone = "indigo" | "red" | "green" | "amber" | "violet" | "neutral" | "ink";

export const TONE: Record<Tone, {fg: string; bg: string; solid: string}> = {
  indigo: {fg: C.indigoDeep, bg: C.indigoSoft, solid: C.indigo},
  red: {fg: "#A8322C", bg: C.redSoft, solid: C.red},
  green: {fg: "#1D7560", bg: C.greenSoft, solid: C.green},
  amber: {fg: "#95600F", bg: C.amberSoft, solid: C.amber},
  violet: {fg: "#5A3DAE", bg: C.violetSoft, solid: C.violet},
  neutral: {fg: C.ink2, bg: C.soft, solid: C.ink3},
  ink: {fg: "#FFFFFF", bg: C.ink, solid: C.ink},
};

type Box = {x: number; y: number; w?: number; h?: number};

// Absolutely positioned layer, the unit every scene is composed of.
export const At: React.FC<Box & {children: React.ReactNode; style?: React.CSSProperties; center?: boolean}> = ({
  x,
  y,
  w,
  h,
  children,
  style,
  center,
}) => (
  <div
    style={{
      position: "absolute",
      left: x,
      top: y,
      width: w,
      height: h,
      ...(center ? {transform: "translate(-50%, -50%)"} : null),
      ...style,
    }}
  >
    {children}
  </div>
);

export const Card: React.FC<{
  children?: React.ReactNode;
  style?: React.CSSProperties;
  pad?: number;
  radius?: number;
}> = ({children, style, pad = 28, radius = 24}) => (
  <div
    style={{
      background: C.panel,
      borderRadius: radius,
      padding: pad,
      boxShadow: shadow,
      outline: "1px solid rgba(29,34,51,0.06)",
      ...style,
    }}
  >
    {children}
  </div>
);

export const Chip: React.FC<{
  children: React.ReactNode;
  tone?: Tone;
  icon?: IconName;
  size?: number;
  solid?: boolean;
  style?: React.CSSProperties;
}> = ({children, tone = "indigo", icon, size = 26, solid, style}) => {
  const t = TONE[tone];
  return (
    <div
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: size * 0.4,
        padding: `${size * 0.32}px ${size * 0.7}px`,
        borderRadius: 999,
        background: solid ? t.solid : t.bg,
        color: solid ? "#fff" : t.fg,
        fontSize: size,
        fontWeight: 600,
        lineHeight: 1.2,
        whiteSpace: "nowrap",
        ...style,
      }}
    >
      {icon ? <Icon name={icon} size={size * 1.05} stroke={2.2} /> : null}
      {children}
    </div>
  );
};

export const Overline: React.FC<{children: React.ReactNode; color?: string; style?: React.CSSProperties}> = ({
  children,
  color = C.ink3,
  style,
}) => (
  <div
    style={{
      fontSize: 20,
      fontWeight: 700,
      letterSpacing: "0.08em",
      textTransform: "uppercase",
      color,
      ...style,
    }}
  >
    {children}
  </div>
);

export const Mono: React.FC<{children: React.ReactNode; size?: number; color?: string; style?: React.CSSProperties}> = ({
  children,
  size = 28,
  color = C.ink,
  style,
}) => <span style={{fontFamily: MONO, fontSize: size, color, whiteSpace: "pre", ...style}}>{children}</span>;

// One test result: a rounded tile with a tick or a cross.
export const TestTile: React.FC<{ok: boolean; size?: number; t?: number; ghost?: boolean}> = ({
  ok,
  size = 44,
  t = 1,
  ghost,
}) => {
  const tone = ok ? C.green : C.red;
  return (
    <div
      style={{
        width: size,
        height: size,
        borderRadius: size * 0.26,
        background: ghost ? C.soft : ok ? C.greenSoft : C.redSoft,
        boxShadow: ghost ? "none" : `inset 0 0 0 ${Math.max(1.5, size * 0.04)}px ${tone}33`,
        display: "grid",
        placeItems: "center",
        opacity: t,
        transform: `scale(${0.4 + 0.6 * t})`,
        flex: "none",
      }}
    >
      {ghost ? null : <Icon name={ok ? "check" : "x"} size={size * 0.56} color={tone} stroke={3} />}
    </div>
  );
};

// A row of test results that pops in tile by tile from frame `at`.
export const TestRow: React.FC<{
  results: boolean[];
  at?: number;
  size?: number;
  gap?: number;
  every?: number;
  labels?: string[];
}> = ({results, at = -1000, size = 44, gap, every = 5, labels}) => {
  const frame = useCurrentFrame();
  return (
    <div style={{display: "flex", gap: gap ?? size * 0.22}}>
      {results.map((ok, i) => (
        <div key={i} style={{display: "flex", flexDirection: "column", alignItems: "center", gap: 8}}>
          <TestTile ok={ok} size={size} t={Math.min(1, pop(frame, at + i * every))} />
          {labels ? (
            <div style={{fontSize: size * 0.36, color: C.ink3, fontWeight: 600, whiteSpace: "nowrap", opacity: sp(frame, at + i * every)}}>
              {labels[i]}
            </div>
          ) : null}
        </div>
      ))}
    </div>
  );
};

// A sheet of paper standing for one submission.
export const Paper: React.FC<{
  w?: number;
  tone?: "plain" | "red" | "green" | "indigo" | "amber" | "violet";
  mark?: "check" | "x" | null;
  markT?: number;
  lines?: number;
  style?: React.CSSProperties;
}> = ({w = 64, tone = "plain", mark = null, markT = 1, lines = 4, style}) => {
  const h = w * 1.28;
  const edge =
    tone === "red"
      ? C.red
      : tone === "green"
        ? C.green
        : tone === "indigo"
          ? C.indigo
          : tone === "amber"
            ? C.amber
            : tone === "violet"
              ? C.violet
              : "#C9CEDC";
  const fill =
    tone === "red"
      ? "#FFF7F6"
      : tone === "green"
        ? "#F4FBF8"
        : tone === "indigo"
          ? "#F6F7FD"
          : tone === "amber"
            ? "#FFFAF1"
            : tone === "violet"
              ? "#F8F5FE"
              : "#FFFFFF";
  return (
    <div
      style={{
        position: "relative",
        width: w,
        height: h,
        borderRadius: w * 0.12,
        background: fill,
        boxShadow: `0 1px 2px rgba(29,34,51,0.08), 0 ${w * 0.1}px ${w * 0.3}px -${w * 0.12}px rgba(29,34,51,0.25), inset 0 0 0 ${Math.max(1, w * 0.025)}px ${edge}${tone === "plain" ? "" : "88"}`,
        padding: `${w * 0.2}px ${w * 0.16}px`,
        display: "flex",
        flexDirection: "column",
        gap: w * 0.1,
        flex: "none",
        ...style,
      }}
    >
      {Array.from({length: lines}).map((_, i) => (
        <div
          key={i}
          style={{
            height: Math.max(2, w * 0.055),
            width: `${[100, 78, 90, 60, 84, 70][i % 6]}%`,
            borderRadius: 99,
            background: tone === "plain" ? "#DCE0EA" : `${edge}40`,
          }}
        />
      ))}
      {mark ? (
        <div
          style={{
            position: "absolute",
            right: -w * 0.16,
            bottom: -w * 0.12,
            width: w * 0.5,
            height: w * 0.5,
            borderRadius: 999,
            background: mark === "check" ? C.green : C.red,
            display: "grid",
            placeItems: "center",
            boxShadow: "0 4px 10px -4px rgba(29,34,51,0.4)",
            transform: `scale(${markT})`,
            opacity: Math.min(1, markT * 2),
          }}
        >
          <Icon name={mark} size={w * 0.3} color="#fff" stroke={3.2} />
        </div>
      ) : null}
    </div>
  );
};

// Counts from `from` to `to` between frames [at, at+dur] with ease-out.
export const Counter: React.FC<{
  from?: number;
  to: number;
  at: number;
  dur?: number;
  digits?: number;
  suffix?: string;
  style?: React.CSSProperties;
}> = ({from = 0, to, at, dur = 40, digits = 0, suffix = "", style}) => {
  const frame = useCurrentFrame();
  const v = interpolate(frame, [at, at + dur], [from, to], {...clamp, easing: EASE});
  return (
    <span style={{fontVariantNumeric: "tabular-nums", ...style}}>
      {vi(v, digits)}
      {suffix}
    </span>
  );
};

// A rubber stamp that lands with a small overshoot.
export const Stamp: React.FC<{
  children: React.ReactNode;
  at: number;
  tone?: Tone;
  rotate?: number;
  size?: number;
}> = ({children, at, tone = "red", rotate = -8, size = 40}) => {
  const frame = useCurrentFrame();
  const s = pop(frame, at);
  const t = TONE[tone];
  return (
    <div
      style={{
        display: "inline-block",
        padding: `${size * 0.22}px ${size * 0.5}px`,
        border: `${size * 0.09}px solid ${t.solid}`,
        borderRadius: size * 0.28,
        color: t.solid,
        fontWeight: 800,
        fontSize: size,
        letterSpacing: "0.04em",
        whiteSpace: "nowrap",
        background: "rgba(255,255,255,0.86)",
        transform: `rotate(${rotate}deg) scale(${interpolate(s, [0, 1], [1.9, 1])})`,
        opacity: interpolate(frame, [at, at + 5], [0, 1], clamp),
      }}
    >
      {children}
    </div>
  );
};

// A straight arrow drawn from (x1,y1) to (x2,y2), revealed by `t` in 0..1.
export const Arrow: React.FC<{
  x1: number;
  y1: number;
  x2: number;
  y2: number;
  t?: number;
  color?: string;
  width?: number;
  dashed?: boolean;
  head?: boolean;
}> = ({x1, y1, x2, y2, t = 1, color = C.ink3, width = 3, dashed, head = true}) => {
  if (t <= 0.001) return null;
  const len = Math.hypot(x2 - x1, y2 - y1);
  const ang = Math.atan2(y2 - y1, x2 - x1);
  const ex = x1 + (x2 - x1) * t;
  const ey = y1 + (y2 - y1) * t;
  const hs = 7 + width * 2.2;
  return (
    <svg style={{position: "absolute", left: 0, top: 0, overflow: "visible", pointerEvents: "none"}} width={1} height={1}>
      <line
        x1={x1}
        y1={y1}
        x2={ex}
        y2={ey}
        stroke={color}
        strokeWidth={width}
        strokeLinecap="round"
        strokeDasharray={dashed ? `${width * 2.4} ${width * 2.6}` : undefined}
      />
      {head && t > 0.02 && len > 0 ? (
        <path
          d={`M ${ex - hs * Math.cos(ang - 0.5)} ${ey - hs * Math.sin(ang - 0.5)} L ${ex} ${ey} L ${ex - hs * Math.cos(ang + 0.5)} ${ey - hs * Math.sin(ang + 0.5)}`}
          fill="none"
          stroke={color}
          strokeWidth={width}
          strokeLinecap="round"
          strokeLinejoin="round"
          opacity={Math.min(1, t * 4)}
        />
      ) : null}
    </svg>
  );
};

// A labelled tray that submissions are sorted into.
export const Bin: React.FC<{
  label: React.ReactNode;
  tone: Tone;
  w: number;
  h: number;
  children?: React.ReactNode;
  style?: React.CSSProperties;
}> = ({label, tone, w, h, children, style}) => {
  const t = TONE[tone];
  return (
    <div
      style={{
        width: w,
        height: h,
        borderRadius: 26,
        background: `linear-gradient(180deg, ${t.bg}, #ffffff)`,
        boxShadow: `inset 0 0 0 2px ${t.solid}40, ${shadow}`,
        position: "relative",
        ...style,
      }}
    >
      <div
        style={{
          position: "absolute",
          top: 16,
          left: 0,
          right: 0,
          textAlign: "center",
          fontSize: 24,
          fontWeight: 700,
          color: t.fg,
        }}
      >
        {label}
      </div>
      {children}
    </div>
  );
};

// A code listing with optional per-line highlights.
export const Code: React.FC<{
  lines: {text: string; tone?: "add" | "del" | "mark" | "dim"; t?: number}[];
  size?: number;
  style?: React.CSSProperties;
  title?: string;
}> = ({lines, size = 24, style, title}) => (
  <div
    style={{
      background: "#FBFBFD",
      borderRadius: 20,
      boxShadow: `inset 0 0 0 1px ${C.line}`,
      padding: "18px 0",
      fontFamily: MONO,
      fontSize: size,
      lineHeight: 1.6,
      ...style,
    }}
  >
    {title ? (
      <div style={{fontFamily: FONT, fontSize: 18, fontWeight: 700, color: C.ink3, padding: "0 24px 8px", letterSpacing: "0.06em", textTransform: "uppercase"}}>
        {title}
      </div>
    ) : null}
    {lines.map((l, i) => {
      const bg =
        l.tone === "add" ? C.greenSoft : l.tone === "del" ? C.redSoft : l.tone === "mark" ? C.amberSoft : "transparent";
      const sign = l.tone === "add" ? "+" : l.tone === "del" ? "−" : " ";
      const t = l.t ?? 1;
      return (
        <div
          key={i}
          style={{
            display: "flex",
            gap: 14,
            padding: "0 24px",
            background: bg,
            opacity: l.tone === "dim" ? 0.4 : 1,
            color: C.ink,
            whiteSpace: "pre",
            clipPath: t < 1 ? `inset(0 ${100 - t * 100}% 0 0)` : undefined,
          }}
        >
          <span style={{color: l.tone === "add" ? C.green : l.tone === "del" ? C.red : C.ink3, width: size * 0.6}}>{sign}</span>
          <span>{l.text}</span>
        </div>
      );
    })}
  </div>
);

// Opacity + rise helper as a wrapper component.
export const Rise: React.FC<{at: number; children: React.ReactNode; dist?: number; style?: React.CSSProperties}> = ({
  at,
  children,
  dist = 30,
  style,
}) => {
  const frame = useCurrentFrame();
  const s = sp(frame, at);
  return <div style={{opacity: s, transform: `translateY(${(1 - s) * dist}px)`, ...style}}>{children}</div>;
};

export const Pop: React.FC<{at: number; children: React.ReactNode; style?: React.CSSProperties; from?: number}> = ({
  at,
  children,
  style,
  from = 0.5,
}) => {
  const frame = useCurrentFrame();
  const s = pop(frame, at);
  return (
    <div style={{opacity: Math.min(1, s * 1.5), transform: `scale(${from + (1 - from) * s})`, ...style}}>{children}</div>
  );
};

// Fades a block in at `at` and (optionally) out at `out`.
export const Show: React.FC<{
  at: number;
  out?: number;
  children: React.ReactNode;
  dur?: number;
  style?: React.CSSProperties;
  dy?: number;
}> = ({at, out, children, dur = 12, style, dy = 0}) => {
  const frame = useCurrentFrame();
  const a = interpolate(frame, [at, at + dur], [0, 1], {...clamp, easing: EASE});
  const b = out === undefined ? 0 : interpolate(frame, [out, out + dur], [0, 1], {...clamp, easing: EASE});
  const o = a * (1 - b);
  if (o <= 0.001) return null;
  return <div style={{opacity: o, transform: `translateY(${(1 - a) * dy - b * dy}px)`, ...style}}>{children}</div>;
};
