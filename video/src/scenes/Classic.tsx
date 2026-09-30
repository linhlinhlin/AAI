import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {clamp, EASE, pop, rand, sp} from "../anim";
import {Illustrative, SceneFrame} from "../components/frame";
import {Icon} from "../components/Icon";
import {Arrow, Card, Chip, Paper, Show, TestTile, TONE, Tone} from "../components/ui";
import {C, MONO} from "../theme";
import {beats, Scene} from "../timeline";

const STEPS = ["Ghi phiếu OAV", "Gom nhóm · K-means", "Viết luật · ILA"];

export const StepBar: React.FC<{active: number; at: number[]}> = ({active, at}) => {
  const frame = useCurrentFrame();
  return (
    <div style={{position: "absolute", left: 0, right: 0, top: 172, display: "flex", justifyContent: "center", alignItems: "center", gap: 14}}>
      {STEPS.map((label, i) => {
        const s = sp(frame, at[i]);
        const on = active === i;
        return (
          <React.Fragment key={label}>
            {i > 0 ? (
              <div style={{opacity: s}}>
                <Icon name="chevronRight" size={30} color={C.ink3} />
              </div>
            ) : null}
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: 12,
                padding: "10px 22px 10px 10px",
                borderRadius: 999,
                background: on ? C.indigo : "#fff",
                color: on ? "#fff" : C.ink2,
                boxShadow: on ? "0 10px 24px -12px rgba(63,81,181,0.8)" : `0 0 0 1px ${C.line}`,
                fontSize: 26,
                fontWeight: 700,
                opacity: s,
                transform: `translateY(${(1 - s) * 20}px) scale(${on ? 1.04 : 1})`,
              }}
            >
              <div
                style={{
                  width: 36,
                  height: 36,
                  borderRadius: 99,
                  display: "grid",
                  placeItems: "center",
                  background: on ? "rgba(255,255,255,0.22)" : C.soft,
                  fontSize: 20,
                }}
              >
                {i + 1}
              </div>
              {label}
            </div>
          </React.Fragment>
        );
      })}
    </div>
  );
};

type Sig = boolean[];
const CLUSTERS: {sig: Sig; tone: Tone; cx: number}[] = [
  {sig: [true, false, true], tone: "indigo", cx: 520},
  {sig: [false, false, true], tone: "amber", cx: 960},
  {sig: [false, true, false], tone: "green", cx: 1400},
];
const CY = 580;
const CARDS = Array.from({length: 18}, (_, i) => {
  const c = i % 3;
  const slot = Math.floor(i / 3);
  return {
    c,
    sx: 260 + rand(i * 3.1 + 2) * 1320,
    sy: 310 + rand(i * 5.7 + 9) * 470,
    tx: CLUSTERS[c].cx + (slot % 2 === 0 ? -82 : 82),
    ty: CY - 70 + Math.floor(slot / 2) * 84,
  };
});

const MiniCard: React.FC<{sig: Sig; tone?: Tone | null}> = ({sig, tone}) => (
  <div
    style={{
      width: 150,
      height: 64,
      borderRadius: 16,
      background: "#fff",
      boxShadow: tone ? `0 0 0 3px ${TONE[tone].solid}, 0 8px 18px -10px rgba(29,34,51,0.35)` : `0 0 0 1px ${C.line}, 0 8px 18px -10px rgba(29,34,51,0.3)`,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      gap: 8,
    }}
  >
    {sig.map((ok, k) => (
      <TestTile key={k} ok={ok} size={32} />
    ))}
  </div>
);

const ValueChip: React.FC<{ok: boolean}> = ({ok}) => (
  <Chip tone={ok ? "green" : "red"} icon={ok ? "check" : "x"} size={26}>
    {ok ? "đạt" : "trượt"}
  </Chip>
);

export const Classic: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {b, at} = beats(scene);
  const active = frame < b(1) ? -1 : frame < b(3) ? 0 : frame < b(4) ? 1 : 2;
  const rowsAt = [at(1, "test", 0), at(1, "test", 1), at(1, "test", 2)];
  const oav = [at(2, "đối"), at(2, "thuộc"), at(2, "giá")];
  const kAt = at(3, "k-means");
  const gomAt = at(3, "gom");
  const binAt = at(3, "hộp");
  const ruleIf = at(4, "nếu");
  const ruleThen = at(4, "thì");
  const shift = interpolate(frame, [b(4), b(4) + 24], [0, 1], {...clamp, easing: EASE});
  const glow = sp(frame, ruleThen + 8);
  const ring = (k: number, color: string) => {
    const s = sp(frame, oav[k]);
    return {boxShadow: `0 0 0 ${3 * s}px ${color}`, background: `${color}${s > 0.05 ? "10" : "00"}`, borderRadius: 14};
  };

  return (
    <SceneFrame scene={scene}>
      <StepBar active={active} at={[20, 28, 36]} />

      {/* Overview of the three steps */}
      <Show at={18} out={b(1) - 10} dy={10}>
        <div style={{position: "absolute", left: 0, right: 0, top: 350, display: "flex", justifyContent: "center", gap: 44}}>
          {(
            [
              ["file", "Ghi phiếu", "Mỗi bài thành một tấm phiếu", "indigo"],
              ["layers", "Gom nhóm", "Phiếu giống nhau vào chung hộp", "amber"],
              ["book", "Viết luật", "Mỗi hộp có một luật NẾU⁠–⁠THÌ", "green"],
            ] as const
          ).map(([icon, title, desc, tone], i) => {
            const s = pop(frame, 22 + i * 10);
            return (
              <Card
                key={title}
                pad={34}
                radius={28}
                style={{width: 450, display: "flex", flexDirection: "column", alignItems: "center", gap: 20, textAlign: "center", textWrap: "balance", opacity: Math.min(1, s * 1.5), transform: `translateY(${(1 - s) * 40}px)`}}
              >
                <div style={{width: 116, height: 116, borderRadius: 32, background: TONE[tone].bg, display: "grid", placeItems: "center"}}>
                  <Icon name={icon} size={62} color={TONE[tone].solid} />
                </div>
                <div style={{fontSize: 38, fontWeight: 800}}>
                  {i + 1}. {title}
                </div>
                <div style={{fontSize: 28, color: C.ink2, fontWeight: 500, lineHeight: 1.4}}>{desc}</div>
              </Card>
            );
          })}
        </div>
      </Show>

      {/* Step 1: one submission becomes one record */}
      <Show at={b(1)} out={b(3) - 10} dy={20}>
        <div style={{position: "absolute", left: 250, top: 430}}>
          <Paper w={130} lines={6} />
          <div style={{fontSize: 26, fontWeight: 600, color: C.ink2, marginTop: 18, textAlign: "center"}}>Bài nộp</div>
        </div>
        <Arrow x1={420} y1={520} x2={560} y2={520} t={interpolate(frame, [at(1, "ghi") - 4, at(1, "ghi") + 12], [0, 1], clamp)} color={C.indigo} width={4} />
        <Card pad={34} radius={28} style={{position: "absolute", left: 600, top: 300, width: 700, height: 470}}>
          <div style={{display: "flex", alignItems: "center", justifyContent: "space-between", padding: "8px 12px", ...ring(0, C.indigo)}}>
            <div style={{fontSize: 34, fontWeight: 800}}>Bài của bạn An</div>
            <Show at={oav[0]}>
              <Chip tone="indigo" size={22}>
                O · Đối tượng
              </Chip>
            </Show>
          </div>
          <div style={{height: 2, background: C.soft, margin: "18px 0 14px"}} />
          <div style={{display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16}}>
            <div style={{padding: "6px 12px 12px", ...ring(1, C.violet)}}>
              <div style={{height: 40, marginBottom: 6}}>
                <Show at={oav[1]}>
                  <Chip tone="violet" size={22}>
                    A · Thuộc tính
                  </Chip>
                </Show>
              </div>
              {["Test 1", "Test 2", "Test 3"].map((t, k) => (
                <div key={t} style={{height: 72, display: "flex", alignItems: "center", fontSize: 32, fontWeight: 600, opacity: sp(frame, rowsAt[k] - 2)}}>
                  {t}
                </div>
              ))}
            </div>
            <div style={{padding: "6px 12px 12px", ...ring(2, C.amber)}}>
              <div style={{height: 40, marginBottom: 6}}>
                <Show at={oav[2]}>
                  <Chip tone="amber" size={22}>
                    V · Giá trị
                  </Chip>
                </Show>
              </div>
              {[false, true, false].map((ok, k) => {
                const s = pop(frame, rowsAt[k] + 4);
                return (
                  <div key={k} style={{height: 72, display: "flex", alignItems: "center", opacity: Math.min(1, s * 1.5), transform: `scale(${0.6 + 0.4 * s})`, transformOrigin: "left center"}}>
                    <ValueChip ok={ok} />
                  </div>
                );
              })}
            </div>
          </div>
        </Card>
      </Show>

      {/* Step 1b: the name of the record */}
      <Show at={at(2, "oav")} out={b(3) - 10} dy={20}>
        <div style={{position: "absolute", left: 1370, top: 330}}>
          <div style={{fontSize: 120, fontWeight: 800, letterSpacing: "-0.03em", color: C.indigo, lineHeight: 1}}>OAV</div>
          {[
            ["O", "Đối tượng", C.indigo],
            ["A", "Thuộc tính", C.violet],
            ["V", "Giá trị", C.amber],
          ].map(([l, t, col], k) => {
            const s = sp(frame, oav[k]);
            return (
              <div key={l} style={{display: "flex", alignItems: "center", gap: 16, marginTop: 20, opacity: 0.25 + 0.75 * s}}>
                <div style={{width: 48, height: 48, borderRadius: 14, background: col, color: "#fff", display: "grid", placeItems: "center", fontFamily: MONO, fontSize: 26, fontWeight: 600}}>
                  {l}
                </div>
                <div style={{fontSize: 32, fontWeight: 700}}>{t}</div>
              </div>
            );
          })}
        </div>
      </Show>

      {/* Step 2: K-means */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          transformOrigin: "960px 580px",
          transform: `translateX(${-270 * shift}px) scale(${1 - 0.2 * shift})`,
        }}
      >
        {CLUSTERS.map((cl, c) => {
          const s = sp(frame, binAt + c * 5);
          if (s < 0.01) return null;
          return (
            <div
              key={c}
              style={{
                position: "absolute",
                left: cl.cx - 200,
                top: CY - 165,
                width: 400,
                height: 370,
                borderRadius: 30,
                background: `linear-gradient(180deg, ${TONE[cl.tone].bg}, rgba(255,255,255,0.6))`,
                boxShadow: `inset 0 0 0 2px ${TONE[cl.tone].solid}50${c === 2 ? `, 0 0 0 ${10 * glow}px ${TONE[cl.tone].solid}40` : ""}`,
                opacity: s,
                transform: `scale(${0.92 + 0.08 * s})`,
              }}
            >
              <div style={{position: "absolute", top: 14, width: "100%", textAlign: "center", fontSize: 24, fontWeight: 700, color: TONE[cl.tone].fg}}>
                Hộp {c + 1}
              </div>
            </div>
          );
        })}
        {frame >= b(3) - 4
          ? CARDS.map((card, i) => {
              const inT = pop(frame, b(3) + 4 + i * 1.6);
              const move = interpolate(frame, [gomAt + i * 1.2, gomAt + i * 1.2 + 34], [0, 1], {...clamp, easing: EASE});
              const x = card.sx + (card.tx - card.sx) * move;
              const y = card.sy + (card.ty - card.sy) * move;
              const assigned = frame >= gomAt - 6 + i * 0.6;
              return (
                <div
                  key={i}
                  style={{position: "absolute", left: x - 75, top: y - 32, opacity: Math.min(1, inT * 1.5), transform: `scale(${0.5 + 0.5 * Math.min(1, inT)})`}}
                >
                  <MiniCard sig={CLUSTERS[card.c].sig} tone={assigned ? CLUSTERS[card.c].tone : null} />
                </div>
              );
            })
          : null}
        {CLUSTERS.map((cl, c) => {
          const s = pop(frame, kAt + c * 5);
          if (s < 0.01) return null;
          const move = interpolate(frame, [gomAt, gomAt + 40], [0, 1], {...clamp, easing: EASE});
          const sx = [820, 1300, 600][c];
          const sy = [360, 700, 740][c];
          const x = sx + (cl.cx - sx) * move;
          const y = sy + (CY - 230 - sy) * move;
          const fade = interpolate(frame, [binAt, binAt + 12], [1, 0], clamp);
          return (
            <div
              key={`k${c}`}
              style={{
                position: "absolute",
                left: x - 26,
                top: y - 26,
                width: 52,
                height: 52,
                borderRadius: 99,
                background: TONE[cl.tone].solid,
                boxShadow: `0 0 0 8px ${TONE[cl.tone].solid}33, 0 8px 16px -6px rgba(29,34,51,0.4)`,
                display: "grid",
                placeItems: "center",
                transform: `scale(${s})`,
                opacity: fade,
              }}
            >
              <div style={{width: 16, height: 16, borderRadius: 99, background: "#fff"}} />
            </div>
          );
        })}
        <Show at={kAt} out={binAt} dy={10}>
          <div style={{position: "absolute", left: 0, right: 0, top: 262, textAlign: "center", fontSize: 24, fontWeight: 600, color: C.ink2}}>
            Mỗi chấm màu là tâm của một nhóm; phiếu nào gần tâm nào thì về nhóm đó
          </div>
        </Show>
      </div>

      {/* Step 3: an IF–THEN rule */}
      <Show at={at(4, "luật")} dy={24}>
        <Card pad={34} radius={28} style={{position: "absolute", left: 1240, top: 360, width: 540}}>
          <div style={{fontSize: 20, fontWeight: 700, letterSpacing: "0.08em", textTransform: "uppercase", color: C.ink3, marginBottom: 18}}>
            Luật do ILA viết ra
          </div>
          {[
            ["NẾU", "trượt test 3", ruleIf],
            ["THÌ", "có thể sai ở vòng lặp", ruleThen],
          ].map(([k, v, t]) => {
            const s = sp(frame, t as number);
            return (
              <div key={k as string} style={{display: "flex", alignItems: "baseline", gap: 18, margin: "10px 0", opacity: 0.15 + 0.85 * s}}>
                <div style={{fontFamily: MONO, fontWeight: 600, fontSize: 30, color: C.indigo, width: 70}}>{k}</div>
                <div style={{fontSize: 34, fontWeight: 700, clipPath: `inset(0 ${100 - 100 * s}% 0 0)`}}>{v}</div>
              </div>
            );
          })}
        </Card>
      </Show>
      <Illustrative x={1240} y={820} at={b(3)} />
    </SceneFrame>
  );
};

export const classicPops = (scene: Scene) => {
  const {at} = beats(scene);
  return [at(1, "test", 0) + 4, at(1, "test", 1) + 4, at(1, "test", 2) + 4, at(3, "k-means"), at(4, "nếu"), at(4, "thì")];
};
