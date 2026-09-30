import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {clamp, EASE, pop, rand, sp} from "../anim";
import {Illustrative, SceneFrame} from "../components/frame";
import {Icon} from "../components/Icon";
import {Arrow, Bin, Card, Chip, Counter, Paper, Show, Stamp, TestTile, Tone} from "../components/ui";
import {C} from "../theme";
import {beats, Scene} from "../timeline";

const GRID = {x: 560, y: 290, w: 30, gap: 12};
const PH = GRID.w * 1.28;
const cell = (i: number) => ({
  x: GRID.x + (i % 10) * (GRID.w + GRID.gap),
  y: GRID.y + Math.floor(i / 10) * (PH + GRID.gap),
});
const WRONG = Array.from({length: 100}, (_, i) => i).filter((i) => rand(i * 7.3 + 1) < 0.36);
const BINS: {x: number; tone: Tone; label: string}[] = [
  {x: 1080, tone: "indigo", label: "Hộp 1"},
  {x: 1325, tone: "amber", label: "Hộp 2"},
  {x: 1570, tone: "green", label: "Hộp 3"},
];
const BIN_Y = 450;

const Teacher: React.FC<{at: number; out?: number}> = ({at, out}) => (
  <Show at={at} out={out} dy={24}>
    <div style={{position: "absolute", left: 150, top: 340, width: 300, display: "flex", flexDirection: "column", alignItems: "center", gap: 18}}>
      <div
        style={{
          width: 170,
          height: 170,
          borderRadius: 999,
          background: C.indigoSoft,
          display: "grid",
          placeItems: "center",
          boxShadow: `inset 0 0 0 3px ${C.indigo}30`,
        }}
      >
        <Icon name="cap" size={92} color={C.indigo} stroke={1.8} />
      </div>
      <div style={{fontSize: 34, fontWeight: 700}}>Cô giáo</div>
    </div>
  </Show>
);

export const Problem: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {b, at} = beats(scene);
  const gridOut = b(1) - 4;
  const gridBack = b(3) - 4;
  const redAt = b(3) + 4;
  const flyAt = at(4, "gom");
  const teachAt = at(4, "dạy");
  const gridVisible = frame < gridOut + 14 || frame >= gridBack;
  const gridOpacity =
    frame < gridBack
      ? interpolate(frame, [gridOut, gridOut + 12], [1, 0], clamp)
      : interpolate(frame, [gridBack, gridBack + 12], [0, 1], clamp);

  const scanAt = at(1, "test");
  const okAt = at(2, "đúng");
  const rowB = at(2, "trượt");
  const failAt = at(2, "sai");

  return (
    <SceneFrame scene={scene}>
      <Teacher at={b(0)} out={gridOut} />
      <Teacher at={gridBack} />

      {/* 100 submissions */}
      {gridVisible ? (
        <div style={{opacity: gridOpacity}}>
          {Array.from({length: 100}, (_, i) => {
            const {x, y} = cell(i);
            const d = (i % 10) + Math.floor(i / 10);
            const inT = frame < gridBack ? pop(frame, b(0) + 8 + d * 2.4) : 1;
            const wrongK = WRONG.indexOf(i);
            const isWrong = wrongK >= 0 && frame >= gridBack;
            const redT = isWrong ? sp(frame, redAt + wrongK * 1.3) : 0;
            // Wrong papers fly to a bin when the teacher starts grouping.
            let fx = x;
            let fy = y;
            let size = GRID.w;
            let moved = 0;
            if (isWrong) {
              const bin = wrongK % 3;
              const slot = Math.floor(wrongK / 3);
              const tx = BINS[bin].x + 28 + (slot % 4) * 42;
              const ty = BIN_Y + 70 + Math.floor(slot / 4) * 50;
              moved = interpolate(frame, [flyAt + wrongK * 1.1, flyAt + wrongK * 1.1 + 26], [0, 1], {...clamp, easing: EASE});
              fx = x + (tx - x) * moved;
              fy = y + (ty - y) * moved - Math.sin(Math.PI * moved) * 90;
              size = GRID.w + (28 - GRID.w) * moved;
            }
            return (
              <React.Fragment key={i}>
                {isWrong && moved > 0 ? (
                  <div
                    style={{
                      position: "absolute",
                      left: x,
                      top: y,
                      width: GRID.w,
                      height: PH,
                      borderRadius: 4,
                      border: `2px dashed ${C.line}`,
                      opacity: moved,
                    }}
                  />
                ) : null}
                <div
                  style={{
                    position: "absolute",
                    left: fx,
                    top: fy,
                    transform: `scale(${0.3 + 0.7 * Math.min(1, inT)})`,
                    opacity: Math.min(1, inT * 1.5),
                    zIndex: moved > 0 ? 5 : 1,
                  }}
                >
                  <Paper w={size} lines={3} tone={redT > 0.5 ? "red" : "plain"} mark={redT > 0.05 ? "x" : null} markT={redT} />
                </div>
              </React.Fragment>
            );
          })}
        </div>
      ) : null}

      {/* L0: counter */}
      <Show at={b(0) + 10} out={gridOut} dy={20}>
        <div style={{position: "absolute", left: 1130, top: 400}}>
          <Counter to={100} at={b(0) + 10} dur={50} style={{fontSize: 150, fontWeight: 800, letterSpacing: "-0.04em", lineHeight: 1}} />
          <div style={{fontSize: 38, fontWeight: 600, color: C.ink2, marginTop: 6}}>bài lập trình được nộp</div>
        </div>
      </Show>

      {/* L1–L2: the autograder */}
      <Show at={b(1)} out={b(3) - 8} dy={24}>
        <Card
          pad={0}
          radius={32}
          style={{position: "absolute", left: 300, top: 340, width: 360, height: 360, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 22}}
        >
          <div style={{position: "absolute", top: 26, width: 150, height: 12, borderRadius: 99, background: C.soft, boxShadow: `inset 0 2px 3px rgba(29,34,51,0.15)`}} />
          <div style={{width: 150, height: 150, borderRadius: 40, background: C.indigo, display: "grid", placeItems: "center", boxShadow: "0 16px 30px -14px rgba(63,81,181,0.8)"}}>
            <Icon name="bot" size={96} color="#fff" stroke={1.8} />
          </div>
          <div style={{fontSize: 32, fontWeight: 700, textAlign: "center", lineHeight: 1.2}}>
            Máy chấm
            <br />
            tự động
          </div>
        </Card>
        {/* a submission dropping into the slot */}
        {(() => {
          const t = interpolate(frame, [at(1, "thử") - 10, at(1, "thử") + 14], [0, 1], {...clamp, easing: EASE});
          return (
            <div style={{position: "absolute", left: 445, top: 210 + 150 * t, opacity: interpolate(t, [0, 0.1, 0.8, 1], [0, 1, 1, 0])}}>
              <Paper w={70} />
            </div>
          );
        })()}
      </Show>

      <Show at={at(1, "kiểm") - 4} out={b(3) - 8} dy={20}>
        <ResultRow y={380} results={[true, true, true, true]} scanAt={scanAt} stampAt={okAt} verdict="ĐÚNG" tone="green" labels />
      </Show>
      <Show at={rowB - 4} out={b(3) - 8} dy={20}>
        <ResultRow y={610} results={[true, true, false, true]} scanAt={rowB} stampAt={failAt} verdict="SAI" tone="red" />
      </Show>

      {/* L3: too many to read one by one */}
      <Show at={at(3, "không")} out={b(4) - 6} dy={16}>
        <div style={{position: "absolute", left: 1110, top: 440}}>
          <Chip tone="red" icon="timer" size={34}>
            Không đọc kịp từng bài
          </Chip>
        </div>
      </Show>

      {/* L4: group similar mistakes, teach each box once */}
      {BINS.map((bin, k) => {
        const s = sp(frame, flyAt - 20 + k * 5);
        if (s < 0.01) return null;
        return (
          <div key={bin.label} style={{position: "absolute", left: bin.x, top: BIN_Y, opacity: s, transform: `translateY(${(1 - s) * 40}px)`}}>
            <Bin label={bin.label} tone={bin.tone} w={210} h={310} />
          </div>
        );
      })}
      {BINS.map((bin, k) => {
        const s = pop(frame, teachAt + k * 7);
        if (s < 0.01) return null;
        return (
          <div
            key={`t${k}`}
            style={{position: "absolute", left: bin.x + 105, top: BIN_Y - 46, transform: `translate(-50%, -50%) scale(${0.5 + 0.5 * s})`, opacity: Math.min(1, s * 1.5)}}
          >
            <Chip tone={bin.tone} solid icon="cap" size={24}>
              Dạy 1 lần
            </Chip>
          </div>
        );
      })}
      <Illustrative x={560} y={800} at={gridBack} />
    </SceneFrame>
  );
};

const ResultRow: React.FC<{
  y: number;
  results: boolean[];
  scanAt: number;
  stampAt: number;
  verdict: string;
  tone: "green" | "red";
  labels?: boolean;
}> = ({y, results, scanAt, stampAt, verdict, tone, labels}) => {
  const frame = useCurrentFrame();
  const arrow = interpolate(frame, [stampAt - 12, stampAt - 2], [0, 1], {...clamp, easing: EASE});
  return (
    <div style={{position: "absolute", left: 0, top: 0}}>
      <div style={{position: "absolute", left: 830, top: y - 4}}>
        <Paper w={60} />
      </div>
      <div style={{position: "absolute", left: 930, top: y, display: "flex", gap: 16}}>
        {results.map((ok, i) => {
          const done = frame >= scanAt + i * 6;
          const s = pop(frame, scanAt + i * 6);
          return (
            <div key={i} style={{display: "flex", flexDirection: "column", alignItems: "center", gap: 10}}>
              <div style={{position: "relative", width: 64, height: 64}}>
                <div style={{position: "absolute", inset: 0}}>
                  <TestTile ok ghost size={64} />
                </div>
                {done ? (
                  <div style={{position: "absolute", inset: 0}}>
                    <TestTile ok={ok} size={64} t={Math.min(1, s)} />
                  </div>
                ) : null}
              </div>
              {labels ? <div style={{fontSize: 22, fontWeight: 600, color: C.ink3, whiteSpace: "nowrap"}}>test {i + 1}</div> : null}
            </div>
          );
        })}
      </div>
      <Arrow x1={1266} y1={y + 32} x2={1346} y2={y + 32} t={arrow} color={C.ink3} width={4} />
      {frame >= stampAt ? (
        <div style={{position: "absolute", left: 1372, top: y - 2}}>
          <Stamp at={stampAt} tone={tone} size={42}>
            {verdict}
          </Stamp>
        </div>
      ) : null}
    </div>
  );
};

export const problemPops = (scene: Scene) => {
  const {at} = beats(scene);
  const t = at(4, "dạy");
  return [at(2, "đúng"), at(2, "sai"), t, t + 7, t + 14];
};
