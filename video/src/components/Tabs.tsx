import React from "react";
import {useCurrentFrame} from "remotion";
import {sp} from "../anim";
import {C} from "../theme";

// A row of numbered pills; the active one is filled. Used to show where the narration is.
export const Tabs: React.FC<{labels: string[]; active: number; at: number[]; top?: number}> = ({labels, active, at, top = 172}) => {
  const frame = useCurrentFrame();
  return (
    <div style={{position: "absolute", left: 0, right: 0, top, display: "flex", justifyContent: "center", alignItems: "center", gap: 14}}>
      {labels.map((label, i) => {
        const s = sp(frame, at[i]);
        const on = active === i;
        return (
          <div
            key={label}
            style={{
              display: "flex",
              alignItems: "center",
              gap: 12,
              padding: "10px 22px 10px 10px",
              borderRadius: 999,
              background: on ? C.indigo : "#fff",
              color: on ? "#fff" : C.ink2,
              boxShadow: on ? "0 10px 24px -12px rgba(63,81,181,0.8)" : `0 0 0 1px ${C.line}`,
              fontSize: 25,
              fontWeight: 700,
              opacity: s,
              transform: `translateY(${(1 - s) * 20}px) scale(${on ? 1.04 : 1})`,
              whiteSpace: "nowrap",
            }}
          >
            <div
              style={{
                width: 34,
                height: 34,
                borderRadius: 99,
                display: "grid",
                placeItems: "center",
                background: on ? "rgba(255,255,255,0.22)" : C.soft,
                fontSize: 19,
              }}
            >
              {i + 1}
            </div>
            {label}
          </div>
        );
      })}
    </div>
  );
};
