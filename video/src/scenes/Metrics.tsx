import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {clamp, EASE, pop, rand, sp} from "../anim";
import {Illustrative, SceneFrame} from "../components/frame";
import {Icon} from "../components/Icon";
import {Tabs} from "../components/Tabs";
import {Card, Chip, Paper, Show, TestTile, TONE} from "../components/ui";
import {C, GROUP, MONO} from "../theme";
import {beats, Scene} from "../timeline";

const Dots: React.FC<{sorted: boolean; t: number}> = ({sorted, t}) => (
  <div style={{position: "relative", width: 300, height: 170}}>
    {Array.from({length: 15}, (_, i) => {
      const g = i % 3;
      const x = sorted ? 40 + g * 100 + (Math.floor(i / 3) % 3) * 16 - 16 : 20 + rand(i * 4.1 + 3) * 250;
      const y = sorted ? 50 + Math.floor(i / 9) * 30 + (Math.floor(i / 3) % 2) * 26 : 20 + rand(i * 7.9 + 1) * 120;
      return (
        <div
          key={i}
          style={{
            position: "absolute",
            left: x,
            top: y,
            width: 26,
            height: 26,
            borderRadius: 99,
            background: GROUP[g],
            opacity: t,
            transform: `scale(${t})`,
            boxShadow: "0 0 0 3px #fff",
          }}
        />
      );
    })}
  </div>
);

export const Metrics: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {b, at} = beats(scene);
  const active = frame < b(1) ? -1 : frame < b(3) ? 0 : frame < b(4) ? 1 : 2;
  const stuckAt = at(1, "không");
  const ceilAt = b(2) + 6;
  const zeroAt = at(3, "0");
  const oneAt = at(3, "1");
  const marker = interpolate(frame, [zeroAt, oneAt + 10], [0, 1], {...clamp, easing: EASE});
  const fairAt = at(4, "công");
  const tilt = interpolate(frame, [b(4) + 20, b(4) + 40, fairAt, fairAt + 24], [0, 9, 9, 0], {...clamp, easing: EASE});

  return (
    <SceneFrame scene={scene}>
      <Tabs labels={["Trần khả phân biệt", "Điểm ARI", "Điểm F1"]} active={active} at={[16, 22, 28]} />

      {/* L0: the three measures */}
      <Show at={14} out={b(1) - 8} dy={10}>
        <div style={{position: "absolute", left: 0, right: 0, top: 330, display: "flex", justifyContent: "center", gap: 44}}>
          {(
            [
              ["gauge", "Trần", "tối đa xếp đúng được bao nhiêu", "indigo"],
              ["layers", "ARI", "cách gom giống đáp án tới đâu", "amber"],
              ["scale", "F1", "luật NẾU⁠–⁠THÌ đoán đúng tới đâu", "green"],
            ] as const
          ).map(([icon, title, desc, tone], i) => {
            const s = pop(frame, 20 + i * 8);
            return (
              <Card key={title} pad={34} radius={28} style={{width: 440, display: "flex", flexDirection: "column", alignItems: "center", gap: 18, textAlign: "center", opacity: Math.min(1, s * 1.5), transform: `translateY(${(1 - s) * 40}px)`}}>
                <div style={{width: 110, height: 110, borderRadius: 32, background: TONE[tone].bg, display: "grid", placeItems: "center"}}>
                  <Icon name={icon} size={60} color={TONE[tone].solid} />
                </div>
                <div style={{fontSize: 40, fontWeight: 800}}>{title}</div>
                <div style={{fontSize: 27, color: C.ink2, fontWeight: 500, lineHeight: 1.35, textWrap: "balance"}}>{desc}</div>
              </Card>
            );
          })}
        </div>
      </Show>

      {/* L1–L2: the identifiability ceiling */}
      <Show at={b(1)} out={b(3) - 8} dy={20}>
        {[
          ["Bài A", "thật ra: quên xuống dòng", "amber"],
          ["Bài B", "thật ra: thiếu số 0", "violet"],
        ].map(([name, why, tone], k) => (
          <Card key={name} pad={28} radius={26} style={{position: "absolute", left: k === 0 ? 400 : 1100, top: 300, width: 420}}>
            <div style={{display: "flex", alignItems: "center", justifyContent: "space-between"}}>
              <div style={{fontSize: 32, fontWeight: 800}}>{name}</div>
              <div style={{display: "flex", gap: 8}}>
                {[0, 1, 2, 3].map((i) => (
                  <TestTile key={i} ok={false} size={38} />
                ))}
              </div>
            </div>
            <div style={{marginTop: 22, display: "flex", alignItems: "center", gap: 10, opacity: 0.55}}>
              <Icon name="eyeOff" size={26} color={C.ink3} />
              <Chip tone={tone as "amber"} size={22}>
                {why}
              </Chip>
            </div>
          </Card>
        ))}
        <div style={{position: "absolute", left: 960, top: 300, transform: "translateX(-50%)", display: "flex", flexDirection: "column", alignItems: "center", gap: 8}}>
          <div style={{width: 120, height: 120, borderRadius: 99, background: "#fff", boxShadow: `0 0 0 1px ${C.line}, 0 16px 34px -18px rgba(29,34,51,0.5)`, display: "grid", placeItems: "center", transform: `rotate(${Math.sin(frame / 6) * 8}deg)`}}>
            <Icon name="search" size={64} color={C.ink} />
          </div>
          <div style={{fontSize: 22, fontWeight: 700, color: C.ink2}}>thám tử giỏi nhất</div>
        </div>
        {(() => {
          const s = pop(frame, stuckAt);
          return s > 0.01 ? (
            <div style={{position: "absolute", left: 960, top: 490, transform: `translateX(-50%) scale(${0.6 + 0.4 * s})`, opacity: Math.min(1, s * 1.5)}}>
              <Chip tone="red" solid icon="x" size={28}>
                Phiếu giống hệt: không thể tách
              </Chip>
            </div>
          ) : null;
        })()}
        {/* the ceiling bar */}
        <Show at={ceilAt - 4}>
          <div style={{position: "absolute", left: 400, top: 610, width: 1120}}>
            <div style={{display: "flex", justifyContent: "space-between", fontSize: 24, fontWeight: 700, color: C.ink2, marginBottom: 12}}>
              <span>Tỷ lệ bài có thể xếp đúng</span>
              <span style={{fontFamily: MONO, color: C.ink3}}>100%</span>
            </div>
            <div style={{position: "relative", height: 46, borderRadius: 23, background: "repeating-linear-gradient(135deg, #F1E3E2 0 12px, #F8EEED 12px 24px)"}}>
              <div style={{position: "absolute", left: 0, top: 0, bottom: 0, width: `${70 * interpolate(frame, [ceilAt, ceilAt + 30], [0, 1], {...clamp, easing: EASE})}%`, borderRadius: 23, background: C.indigo}} />
              <div style={{position: "absolute", left: "70%", top: -18, bottom: -18, width: 5, borderRadius: 3, background: C.ink, opacity: sp(frame, ceilAt + 24)}} />
            </div>
            <div style={{position: "relative", height: 60}}>
              <div style={{position: "absolute", left: "70%", top: 22, transform: "translateX(-50%)", opacity: sp(frame, ceilAt + 26), whiteSpace: "nowrap"}}>
                <Chip tone="ink" size={24}>
                  Trần: tối đa làm được
                </Chip>
              </div>
              <div style={{position: "absolute", right: 0, top: 28, fontSize: 22, fontWeight: 700, color: "#A8322C", opacity: sp(frame, ceilAt + 34)}}>không thể vượt</div>
            </div>
          </div>
          <Illustrative x={400} y={790} at={ceilAt} />
        </Show>
      </Show>

      {/* L3: ARI from coin toss to perfect */}
      <Show at={b(3) - 2} out={b(4) - 8} dy={20}>
        <div style={{position: "absolute", left: 360, top: 450, width: 1200}}>
          <div style={{position: "relative", height: 18, borderRadius: 9, background: `linear-gradient(90deg, #D5D9E4, ${C.indigo})`}}>
            {[0, 0.25, 0.5, 0.75, 1].map((v) => (
              <div key={v} style={{position: "absolute", left: `${v * 100}%`, top: 30, transform: "translateX(-50%)", fontFamily: MONO, fontSize: 24, color: C.ink3}}>
                {String(v).replace(".", ",")}
              </div>
            ))}
            <div
              style={{
                position: "absolute",
                left: `${marker * 100}%`,
                top: "50%",
                width: 50,
                height: 50,
                borderRadius: 99,
                background: "#fff",
                boxShadow: `0 0 0 6px ${C.indigo}, 0 10px 20px -8px rgba(29,34,51,0.5)`,
                transform: "translate(-50%, -50%)",
                opacity: sp(frame, zeroAt - 6),
              }}
            />
          </div>
        </div>
        {[
          ["coins", "0 = xếp hú họa", "như tung đồng xu", 200, zeroAt, false],
          ["trophy", "1 = xếp hoàn hảo", "khớp hệt đáp án", 1330, oneAt, true],
        ].map(([icon, title, sub, x, t, sorted]) => {
          const s = sp(frame, t as number);
          return (
            <div key={title as string} style={{position: "absolute", left: x as number, top: 540, width: 390, display: "flex", flexDirection: "column", alignItems: "center", opacity: s, transform: `translateY(${(1 - s) * 30}px)`}}>
              <div style={{display: "flex", alignItems: "center", gap: 14}}>
                <Icon name={icon as "coins"} size={44} color={sorted ? C.amber : C.ink2} />
                <div style={{fontSize: 32, fontWeight: 800, whiteSpace: "nowrap"}}>{title as string}</div>
              </div>
              <div style={{fontSize: 24, color: C.ink2, fontWeight: 600, marginTop: 4}}>{sub as string}</div>
              <Dots sorted={sorted as boolean} t={s} />
            </div>
          );
        })}
        <div style={{position: "absolute", left: 0, right: 0, top: 300, textAlign: "center", fontSize: 28, fontWeight: 700, color: C.ink2, opacity: sp(frame, b(3) + 4)}}>
          ARI so cách gom của máy với đáp án thật
        </div>
      </Show>

      {/* L4: macro-F1 treats rare mistakes fairly */}
      <Show at={b(4) - 2} dy={20}>
        <div style={{position: "absolute", left: 0, right: 0, top: 262, display: "flex", justifyContent: "center"}}>
          <Chip tone="green" size={26}>
            F1 trung bình theo từng loại lỗi (macro-F1)
          </Chip>
        </div>
        <div style={{position: "absolute", left: 960, top: 340, width: 0, height: 0}}>
          <div style={{position: "absolute", left: -8, top: 20, width: 16, height: 380, borderRadius: 8, background: C.ink2}} />
          <div style={{position: "absolute", left: -90, top: 390, width: 180, height: 22, borderRadius: 11, background: C.ink2}} />
          <div style={{position: "absolute", left: 0, top: 30, transform: `rotate(${-tilt}deg)`, transformOrigin: "0 0"}}>
            <div style={{position: "absolute", left: -420, top: -8, width: 840, height: 16, borderRadius: 8, background: C.ink}} />
            {[
              [-420, "Văn bản in ra", "180 bài", 18, "amber"],
              [420, "Kiểu số, chia nguyên", "3 bài", 3, "violet"],
            ].map(([x, name, n, count, tone]) => (
              <div key={name as string} style={{position: "absolute", left: x as number, top: 0, transform: `rotate(${tilt}deg)`, transformOrigin: "0 0"}}>
                <div style={{position: "absolute", left: -2, top: 0, width: 4, height: 70, background: C.ink3}} />
                <div
                  style={{
                    position: "absolute",
                    left: -170,
                    top: 70,
                    width: 340,
                    padding: "16px 18px 18px",
                    borderRadius: 24,
                    background: "#fff",
                    boxShadow: `0 0 0 2px ${TONE[tone as "amber"].solid}66, 0 16px 34px -20px rgba(29,34,51,0.5)`,
                  }}
                >
                  <div style={{display: "flex", flexWrap: "wrap", gap: 6, justifyContent: "center", minHeight: 96, alignContent: "center"}}>
                    {Array.from({length: count as number}, (_, i) => (
                      <Paper key={i} w={30} lines={2} tone={tone as "amber"} />
                    ))}
                  </div>
                  <div style={{fontSize: 25, fontWeight: 800, textAlign: "center", marginTop: 10}}>{name as string}</div>
                  <div style={{fontSize: 21, color: C.ink2, fontWeight: 600, textAlign: "center"}}>{n as string} · tính một phần ngang nhau</div>
                </div>
              </div>
            ))}
          </div>
        </div>
        {(() => {
          const s = pop(frame, at(4, "hiếm") + 6);
          return s > 0.01 ? (
            <div style={{position: "absolute", left: 960, top: 790, transform: `translateX(-50%) scale(${0.6 + 0.4 * s})`, opacity: Math.min(1, s * 1.5)}}>
              <Chip tone="green" solid icon="scale" size={26}>
                Loại lỗi hiếm cũng được tính công bằng
              </Chip>
            </div>
          ) : null;
        })()}
      </Show>
    </SceneFrame>
  );
};

export const metricsPops = (scene: Scene) => {
  const {at} = beats(scene);
  return [at(1, "không"), at(3, "1") + 10, at(4, "công") + 20];
};
