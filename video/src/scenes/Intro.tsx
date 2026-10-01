import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {clamp, EASE, pop, sp, tween} from "../anim";
import {SceneFrame} from "../components/frame";
import {Card, Chip, TestTile, Tone} from "../components/ui";
import {C} from "../theme";
import {beats, Scene} from "../timeline";

const REASONS: {text: string; tone: Tone}[] = [
  {text: "Quên xuống dòng", tone: "amber"},
  {text: "Thiếu số 0", tone: "violet"},
  {text: "Thiếu dấu ngoặc", tone: "indigo"},
];

const TitleLine: React.FC<{at: number; children: React.ReactNode; size: number}> = ({at, children, size}) => {
  const frame = useCurrentFrame();
  const s = sp(frame, at);
  return (
    <div style={{overflow: "hidden", paddingBottom: size * 0.12}}>
      <div style={{transform: `translateY(${(1 - s) * size * 1.2}px)`, fontSize: size, fontWeight: 800, letterSpacing: "-0.03em", lineHeight: 1.08}}>
        {children}
      </div>
    </div>
  );
};

export const Intro: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {b, at} = beats(scene);
  const split = b(1);
  const chipsAt = at(1, "cách");
  const rowOut = interpolate(frame, [split, split + 14], [1, 0], {...clamp, easing: EASE});
  const rowY = tween(frame, 36, 30, 540, 700);
  const rowScale = tween(frame, 36, 30, 1.25, 1);
  const underline = interpolate(frame, [104, 134], [0, 1], {...clamp, easing: EASE});

  return (
    <SceneFrame scene={scene} push={0.03}>
      {/* Title block */}
      <div style={{position: "absolute", left: 0, right: 0, top: 210, display: "flex", flexDirection: "column", alignItems: "center"}}>
        <div
          style={{
            fontSize: 24,
            fontWeight: 700,
            letterSpacing: "0.14em",
            textTransform: "uppercase",
            color: C.indigo,
            opacity: sp(frame, 46),
            transform: `translateY(${(1 - sp(frame, 46)) * 16}px)`,
            marginBottom: 18,
          }}
        >
          Nghiên cứu AAI · Đề tài 5
        </div>
        <TitleLine at={58} size={104}>
          Cùng sai,
        </TitleLine>
        <TitleLine at={74} size={104}>
          nhưng sai{" "}
          <span style={{color: C.indigo, position: "relative", display: "inline-block"}}>
            vì sao?
            <svg
              width="420"
              height="30"
              viewBox="0 0 420 30"
              style={{position: "absolute", left: 0, bottom: -18, width: "100%", overflow: "visible"}}
            >
              <path
                d="M4 18 C 90 6, 180 26, 260 14 S 380 8, 416 16"
                fill="none"
                stroke={C.amber}
                strokeWidth={9}
                strokeLinecap="round"
                pathLength={100}
                strokeDasharray={100}
                strokeDashoffset={100 * (1 - underline)}
              />
            </svg>
          </span>
        </TitleLine>
      </div>

      {/* One row of four failed tests... */}
      {rowOut > 0.01 ? (
        <div
          style={{
            position: "absolute",
            left: 960,
            top: rowY,
            transform: `translate(-50%, -50%) scale(${rowScale * (0.85 + 0.15 * rowOut)})`,
            display: "flex",
            gap: 20,
            opacity: rowOut,
          }}
        >
          {[0, 1, 2, 3].map((i) => (
            <TestTile key={i} ok={false} size={88} t={Math.min(1, pop(frame, 6 + i * 6))} />
          ))}
        </div>
      ) : null}

      {/* ...splits into three identical rows with three different reasons. */}
      {[0, 1, 2].map((k) => {
        const s = sp(frame, split + 2, 18);
        const x = 960 + (k - 1) * 440 * s;
        const chip = pop(frame, chipsAt + k * 9);
        return (
          <div
            key={k}
            style={{
              position: "absolute",
              left: x,
              top: 700,
              transform: "translate(-50%, -50%)",
              opacity: interpolate(frame, [split, split + 10], [0, 1], clamp),
            }}
          >
            <Card pad={26} radius={26} style={{display: "flex", flexDirection: "column", alignItems: "center", gap: 20, width: 340}}>
              <div style={{display: "flex", gap: 12}}>
                {[0, 1, 2, 3].map((i) => (
                  <TestTile key={i} ok={false} size={56} />
                ))}
              </div>
              <div style={{height: 50, display: "grid", placeItems: "center"}}>
                {chip > 0.01 ? (
                  <div style={{transform: `scale(${0.6 + 0.4 * chip})`, opacity: Math.min(1, chip * 1.6)}}>
                    <Chip tone={REASONS[k].tone} size={26}>
                      {REASONS[k].text}
                    </Chip>
                  </div>
                ) : (
                  <div style={{fontSize: 34, fontWeight: 800, color: C.ink3}}>?</div>
                )}
              </div>
            </Card>
          </div>
        );
      })}
    </SceneFrame>
  );
};

export const introPops = (scene: Scene) => {
  const {at} = beats(scene);
  return [6, 12, 18, 24, at(1, "cách")];
};
