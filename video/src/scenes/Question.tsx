import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {clamp, EASE, pop, sp} from "../anim";
import {SceneFrame} from "../components/frame";
import {Icon, IconName} from "../components/Icon";
import {Card, Chip, Paper, Show, TestTile, Tone, TONE} from "../components/ui";
import {C} from "../theme";
import {beats, Scene} from "../timeline";

const EqualSign: React.FC<{t: number}> = ({t}) => (
  <svg width="64" height="64" viewBox="0 0 64 64" style={{transform: `scale(${0.4 + 0.6 * t})`, opacity: Math.min(1, t * 1.5)}}>
    <rect x="10" y="20" width="44" height="7" rx="3.5" fill={C.red} />
    <rect x="10" y="37" width="44" height="7" rx="3.5" fill={C.red} />
  </svg>
);

// A small, friendly cake that did not turn out well.
const Cake: React.FC<{t: number; frame: number; seed: number}> = ({t, frame, seed}) => {
  const puff = (k: number) => {
    const p = ((frame + seed * 13 + k * 22) % 66) / 66;
    return {transform: `translate(${Math.sin(p * 6 + k) * 6}px, ${-p * 46}px) scale(${0.6 + p * 0.8})`, opacity: (1 - p) * 0.7 * t};
  };
  return (
    <svg width="220" height="190" viewBox="-110 -130 220 190" style={{overflow: "visible", transform: `scale(${0.6 + 0.4 * t})`, opacity: Math.min(1, t * 1.5)}}>
      {[0, 1, 2].map((k) => (
        <g key={k} style={puff(k)}>
          <circle cx={-26 + k * 24} cy={-96} r={11} fill="#C9CEDC" />
        </g>
      ))}
      <ellipse cx="0" cy="44" rx="100" ry="14" fill="#DDE1EB" />
      <rect x="-78" y="-38" width="156" height="80" rx="18" fill="#EFCB8E" />
      <rect x="-78" y="2" width="156" height="10" fill="#E2B775" />
      <path d="M-78 -20 q0 -26 26 -26 h104 q26 0 26 26 v6 q-10 10 -20 0 q-10 16 -22 0 q-12 14 -24 0 q-12 16 -24 0 q-12 12 -22 0 q-12 14 -22 0 q-10 8 -22 -4z" fill="#F6BFCB" />
      <rect x="-5" y="-78" width="10" height="34" rx="4" fill="#9FA8DA" />
      <circle cx="-22" cy="16" r="5" fill={C.ink} />
      <circle cx="22" cy="16" r="5" fill={C.ink} />
      <path d="M-14 34 q14 -10 28 0" fill="none" stroke={C.ink} strokeWidth="4.5" strokeLinecap="round" />
    </svg>
  );
};

const CAKES: {reason: string; icon: IconName; tone: Tone; fix: string}[] = [
  {reason: "Quên cho đường", icon: "cube", tone: "amber", fix: "Nhớ cân đường"},
  {reason: "Nướng quá lửa", icon: "flame", tone: "red", fix: "Hạ nhỏ lửa"},
  {reason: "Lấy nhầm muối", icon: "salt", tone: "violet", fix: "Đọc nhãn lọ"},
];

export const Question: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {b, at} = beats(scene);
  const qIn = pop(frame, 16);
  const toMid = interpolate(frame, [b(1) - 4, b(1) + 18], [0, 1], {...clamp, easing: EASE});
  const qOut = interpolate(frame, [b(2) - 8, b(2) + 4], [1, 0], clamp);
  const qSize = 240 - 130 * toMid;
  const qY = 500 + 160 * toMid;
  const sameAt = at(1, "cùng");
  const whyAt = at(1, "lý");
  const reasonAt = [at(3, "quên"), at(3, "nướng"), at(3, "lấy")];
  const badAt = at(4, "dở");
  const diffAt = at(4, "khác");
  const fixAt = at(4, "cách");

  return (
    <SceneFrame scene={scene}>
      {/* The big question mark */}
      {qOut > 0.01 ? (
        <div style={{position: "absolute", left: 960, top: qY, transform: "translate(-50%, -50%)", opacity: qOut}}>
          {[0, 1].map((k) => {
            const p = ((frame - 16 + k * 30) % 60) / 60;
            return frame > 16 ? (
              <div
                key={k}
                style={{
                  position: "absolute",
                  left: "50%",
                  top: "50%",
                  width: qSize,
                  height: qSize,
                  borderRadius: 999,
                  border: `3px solid ${C.indigo}`,
                  transform: `translate(-50%, -50%) scale(${1 + p * 0.6})`,
                  opacity: (1 - p) * 0.35 * (1 - toMid),
                }}
              />
            ) : null;
          })}
          <div
            style={{
              width: qSize,
              height: qSize,
              borderRadius: 999,
              background: C.indigo,
              color: "#fff",
              display: "grid",
              placeItems: "center",
              fontSize: qSize * 0.6,
              fontWeight: 800,
              transform: `scale(${qIn})`,
              boxShadow: "0 24px 50px -20px rgba(63,81,181,0.8)",
            }}
          >
            ?
          </div>
        </div>
      ) : null}

      {/* Two submissions, same failed tests */}
      <Show at={b(1)} out={b(2) - 8} dy={24}>
        {[0, 1].map((k) => (
          <Card key={k} pad={30} radius={28} style={{position: "absolute", left: k === 0 ? 330 : 1210, top: 320, width: 380, display: "flex", flexDirection: "column", alignItems: "center", gap: 22}}>
            <div style={{display: "flex", alignItems: "center", gap: 18}}>
              <Paper w={54} lines={4} />
              <div style={{fontSize: 34, fontWeight: 800}}>Bài {k + 1}</div>
            </div>
            <div style={{display: "flex", gap: 12}}>
              {[false, true, false, true].map((ok, i) => (
                <TestTile key={i} ok={ok} size={56} t={Math.min(1, pop(frame, b(1) + 10 + i * 4 + k * 3))} />
              ))}
            </div>
          </Card>
        ))}
        <div style={{position: "absolute", left: 960, top: 454, transform: "translate(-50%, -50%)", display: "flex", flexDirection: "column", alignItems: "center"}}>
          <EqualSign t={pop(frame, sameAt)} />
          <div style={{opacity: sp(frame, sameAt + 4), fontSize: 26, fontWeight: 700, color: C.ink2, whiteSpace: "nowrap", marginTop: 4}}>cùng test trượt</div>
        </div>
        {[0, 1].map((k) => {
          const s = pop(frame, whyAt + k * 6);
          return (
            <div key={`w${k}`} style={{position: "absolute", left: k === 0 ? 520 : 1400, top: 634, transform: `translate(-50%, 0) scale(${0.6 + 0.4 * s})`, opacity: Math.min(1, s * 1.5)}}>
              <Chip tone="amber" size={30} icon="help">
                Lý do {k === 0 ? "A" : "B"}?
              </Chip>
            </div>
          );
        })}
      </Show>

      {/* Three cakes, three reasons */}
      {CAKES.map((cake, k) => {
        const x = 480 + k * 480;
        const s = sp(frame, b(2) + 4 + k * 8);
        if (s < 0.01) return null;
        const r = pop(frame, reasonAt[k]);
        const bad = pop(frame, badAt + k * 4);
        const pulse = 1 + 0.08 * Math.sin(Math.PI * interpolate(frame, [diffAt + k * 5, diffAt + k * 5 + 14], [0, 1], clamp));
        const fix = pop(frame, fixAt + k * 7);
        return (
          <React.Fragment key={k}>
            <Card pad={0} radius={30} style={{position: "absolute", left: x - 190, top: 290, width: 380, height: 270, display: "grid", placeItems: "center", opacity: s, transform: `translateY(${(1 - s) * 30}px)`}}>
              <div style={{marginTop: 30}}>
                <Cake t={Math.min(1, pop(frame, b(2) + 8 + k * 8))} frame={frame} seed={k} />
              </div>
              {bad > 0.01 ? (
                <div style={{position: "absolute", right: 18, top: 18, transform: `scale(${bad})`}}>
                  <Chip tone="red" solid icon="x" size={24}>
                    Dở
                  </Chip>
                </div>
              ) : null}
            </Card>
            {r > 0.01 ? (
              <div style={{position: "absolute", left: x, top: 590, transform: `translateX(-50%) scale(${(0.6 + 0.4 * r) * pulse})`, opacity: Math.min(1, r * 1.5)}}>
                <Chip tone={cake.tone} icon={cake.icon} size={30}>
                  {cake.reason}
                </Chip>
              </div>
            ) : null}
            {fix > 0.01 ? (
              <div
                style={{
                  position: "absolute",
                  left: x,
                  top: 682,
                  transform: `translateX(-50%) translateY(${(1 - fix) * 20}px)`,
                  opacity: Math.min(1, fix * 1.5),
                  display: "flex",
                  alignItems: "center",
                  gap: 12,
                  padding: "14px 24px",
                  borderRadius: 18,
                  background: "#fff",
                  boxShadow: `0 0 0 2px ${TONE[cake.tone].solid}55, 0 12px 26px -16px rgba(29,34,51,0.5)`,
                  fontSize: 28,
                  fontWeight: 700,
                  whiteSpace: "nowrap",
                }}
              >
                <Icon name="bulb" size={30} color={TONE[cake.tone].solid} />
                {cake.fix}
              </div>
            ) : null}
          </React.Fragment>
        );
      })}
    </SceneFrame>
  );
};

export const questionPops = (scene: Scene) => {
  const {b, at} = beats(scene);
  return [16, b(2) + 8, b(2) + 16, b(2) + 24, at(3, "quên"), at(3, "nướng"), at(3, "lấy"), at(4, "dở"), at(4, "cách")];
};
