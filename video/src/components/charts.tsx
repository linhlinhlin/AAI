import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {clamp, EASE, vi} from "../anim";
import {C, MONO} from "../theme";

const grow = (frame: number, at: number, dur: number) => interpolate(frame, [at, at + dur], [0, 1], {...clamp, easing: EASE});

// A ring that fills to `value` (0..1) starting at frame `at`.
export const Donut: React.FC<{
  value: number;
  at: number;
  size?: number;
  color?: string;
  track?: string;
  thickness?: number;
  label?: React.ReactNode;
  digits?: number;
  dur?: number;
}> = ({value, at, size = 260, color = C.red, track = "#E4E7F0", thickness = 30, label, digits = 0, dur = 45}) => {
  const frame = useCurrentFrame();
  const g = grow(frame, at, dur);
  const r = (size - thickness) / 2;
  const circ = 2 * Math.PI * r;
  return (
    <div style={{position: "relative", width: size, height: size}}>
      <svg width={size} height={size} style={{transform: "rotate(-90deg)"}}>
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke={track} strokeWidth={thickness} />
        <circle
          cx={size / 2}
          cy={size / 2}
          r={r}
          fill="none"
          stroke={color}
          strokeWidth={thickness}
          strokeLinecap="round"
          strokeDasharray={`${circ * value * g} ${circ}`}
          opacity={g > 0 ? 1 : 0}
        />
      </svg>
      <div
        style={{
          position: "absolute",
          inset: 0,
          display: "grid",
          placeItems: "center",
          textAlign: "center",
        }}
      >
        <div>
          <div style={{fontSize: size * 0.24, fontWeight: 800, color: C.ink, fontVariantNumeric: "tabular-nums", letterSpacing: "-0.02em", opacity: interpolate(frame, [at - 4, at + 6], [0, 1], clamp)}}>
            {vi(value * 100 * g, digits)}%
          </div>
          {label ? <div style={{fontSize: size * 0.075, color: C.ink2, fontWeight: 600, marginTop: 2}}>{label}</div> : null}
        </div>
      </div>
    </div>
  );
};

// Horizontal bar with a label on the left and the value on the right.
export const HBar: React.FC<{
  label: React.ReactNode;
  value: number;
  max: number;
  at: number;
  width: number;
  color?: string;
  height?: number;
  format?: (v: number) => string;
  labelWidth?: number;
  dur?: number;
  fontSize?: number;
}> = ({label, value, max, at, width, color = C.indigo, height = 26, format, labelWidth = 260, dur = 30, fontSize = 24}) => {
  const frame = useCurrentFrame();
  const g = grow(frame, at, dur);
  const w = Math.max(height, (value / max) * width * g);
  return (
    <div style={{display: "flex", alignItems: "center", gap: 18, opacity: interpolate(frame, [at - 6, at + 4], [0, 1], clamp)}}>
      <div style={{width: labelWidth, fontSize, color: C.ink2, fontWeight: 600, textAlign: "right", flex: "none"}}>{label}</div>
      <div style={{width, height, position: "relative", flex: "none"}}>
        <div style={{position: "absolute", inset: 0, borderRadius: height / 2, background: "#E7EAF2"}} />
        <div style={{position: "absolute", left: 0, top: 0, bottom: 0, width: w, borderRadius: height / 2, background: color}} />
      </div>
      <div style={{fontSize, fontWeight: 700, color: C.ink, fontVariantNumeric: "tabular-nums", minWidth: 80}}>
        {format ? format(value * g) : vi(value * g)}
      </div>
    </div>
  );
};

// Vertical bar used for the head-to-head comparisons in the results chapter.
export const VBar: React.FC<{
  value: number;
  max: number;
  at: number;
  height: number;
  width?: number;
  color: string;
  label: React.ReactNode;
  digits?: number;
  dur?: number;
  valueColor?: string;
}> = ({value, max, at, height, width = 150, color, label, digits = 2, dur = 36, valueColor = C.ink}) => {
  const frame = useCurrentFrame();
  const g = grow(frame, at, dur);
  const h = (value / max) * height * g;
  return (
    <div style={{display: "flex", flexDirection: "column", alignItems: "center", width: width + 80}}>
      <div style={{height, display: "flex", flexDirection: "column", justifyContent: "flex-end", alignItems: "center"}}>
        <div
          style={{
            fontFamily: MONO,
            fontSize: 44,
            fontWeight: 600,
            color: valueColor,
            marginBottom: 10,
            opacity: interpolate(frame, [at, at + 10], [0, 1], clamp),
            fontVariantNumeric: "tabular-nums",
          }}
        >
          {vi(value * g, digits)}
        </div>
        <div style={{width, height: Math.max(4, h), borderRadius: "16px 16px 6px 6px", background: color}} />
      </div>
      <div style={{height: 3, width: width + 60, background: C.line, borderRadius: 2}} />
      <div style={{marginTop: 14, fontSize: 24, fontWeight: 600, color: C.ink2, textAlign: "center", lineHeight: 1.3}}>{label}</div>
    </div>
  );
};

// Half-ring gauge for agreement rates.
export const Gauge: React.FC<{value: number; at: number; size?: number; color?: string; digits?: number; label: React.ReactNode}> = ({
  value,
  at,
  size = 320,
  color = C.green,
  digits = 1,
  label,
}) => {
  const frame = useCurrentFrame();
  const g = grow(frame, at, 50);
  const th = 26;
  const r = (size - th) / 2;
  const half = Math.PI * r;
  const cx = size / 2;
  const cy = size / 2;
  return (
    <div style={{width: size, textAlign: "center"}}>
      <svg width={size} height={size / 2 + th / 2 + 4} style={{overflow: "visible"}}>
        <path d={`M ${th / 2} ${cy} A ${r} ${r} 0 0 1 ${size - th / 2} ${cy}`} fill="none" stroke="#E4E7F0" strokeWidth={th} strokeLinecap="round" />
        <path
          d={`M ${th / 2} ${cy} A ${r} ${r} 0 0 1 ${size - th / 2} ${cy}`}
          fill="none"
          stroke={color}
          strokeWidth={th}
          strokeLinecap="round"
          strokeDasharray={`${half * value * g} ${half * 2}`}
          opacity={g > 0 ? 1 : 0}
        />
        <text
          x={cx}
          y={cy - 14}
          textAnchor="middle"
          fontSize={size * 0.19}
          fontWeight={800}
          fill={C.ink}
          style={{fontVariantNumeric: "tabular-nums", letterSpacing: "-0.02em"}}
        >
          {vi(value * 100 * g, digits)}%
        </text>
      </svg>
      <div style={{fontSize: 26, color: C.ink2, fontWeight: 600, marginTop: 8, lineHeight: 1.3}}>{label}</div>
    </div>
  );
};
