import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {clamp, EASE, pop, sp} from "../anim";
import {SceneFrame} from "../components/frame";
import {Icon, IconName} from "../components/Icon";
import {Card, Chip, Show, TestTile, Tone, TONE} from "../components/ui";
import {C, FONT as FONT_BODY, MONO} from "../theme";
import {beats, Scene} from "../timeline";

const TILES: {title: string; need: string; got: React.ReactNode; tone: Tone}[] = [
  {title: "Thiếu xuống dòng?", need: "00:01:00↵", got: "00:01:00", tone: "amber"},
  {title: "Số đúng, viết khác?", need: "00:01:00", got: "0:1:0", tone: "violet"},
  {title: "Số lệch một?", need: "15", got: "14", tone: "red"},
  {title: "Không in gì cả?", need: "42", got: <span style={{color: C.ink3, fontFamily: FONT_BODY}}>(trống)</span>, tone: "indigo"},
];

// The nine per-test descriptors of the deviation OAV (misconceptions-prototype, agg:*).
const DESCRIPTORS = [
  "Đạt hay trượt?",
  "Số dòng có khớp?",
  "Thiếu xuống dòng cuối?",
  "Chỉ khác khoảng trắng?",
  "Các con số ra sao?",
  "Phần chữ ra sao?",
  "Khác từ chỗ nào?",
  "Bị cụt hay thừa?",
  "Trùng đáp án test khác?",
];

const ABC: {name: string; chip: string; tone: Tone}[] = [
  {name: "Bài A", chip: "xuống dòng cuối: thiếu", tone: "amber"},
  {name: "Bài B", chip: "con số: chỉ khác cách viết", tone: "violet"},
  {name: "Bài C", chip: "con số: khác hẳn", tone: "indigo"},
];

export const Deviation: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {b, at} = beats(scene);
  const bulb = pop(frame, 16);
  const newAt = at(1, "hãy");
  const extraAt = at(1, "thế");
  const tileAt = [at(2, "thiếu"), at(2, "số", 0), at(2, "số", 1), at(2, "hay")];
  const oavAt = at(3, "oav");
  const benefits: [IconName, string, number][] = [
    ["cpu", "Máy tự tính được", at(3, "máy")],
    ["hand", "Không cần ai chấm tay", at(3, "chấm")],
    ["globe", "Dùng chung cho mọi bài tập", at(3, "dùng")],
  ];
  const splitAt = at(4, "khác");
  const devAt = at(4, "phiếu");
  const split = interpolate(frame, [splitAt, splitAt + 26], [0, 1], {...clamp, easing: EASE});

  return (
    <SceneFrame scene={scene}>
      {/* L0: the idea */}
      <Show at={4} out={b(1) - 8}>
        <div style={{position: "absolute", left: 960, top: 470, transform: "translate(-50%, -50%)"}}>
          <div
            style={{
              position: "absolute",
              left: "50%",
              top: "50%",
              width: 520,
              height: 520,
              transform: "translate(-50%, -50%)",
              borderRadius: 999,
              background: "radial-gradient(circle, rgba(227,155,47,0.35) 0%, rgba(227,155,47,0) 65%)",
              opacity: bulb,
            }}
          />
          <svg width="420" height="420" viewBox="-210 -210 420 420" style={{position: "absolute", left: "50%", top: "50%", transform: `translate(-50%, -50%) rotate(${frame * 0.4}deg)`, opacity: bulb}}>
            {Array.from({length: 12}, (_, k) => {
              const a = (k / 12) * Math.PI * 2;
              const len = 26 + 10 * Math.sin(frame / 8 + k);
              return <line key={k} x1={Math.cos(a) * 160} y1={Math.sin(a) * 160} x2={Math.cos(a) * (160 + len)} y2={Math.sin(a) * (160 + len)} stroke={C.amber} strokeWidth={8} strokeLinecap="round" />;
            })}
          </svg>
          <div style={{width: 240, height: 240, borderRadius: 999, background: "#fff", boxShadow: "0 24px 60px -24px rgba(227,155,47,0.9)", display: "grid", placeItems: "center", transform: `scale(${bulb})`, position: "relative"}}>
            <Icon name="bulb" size={130} color={C.amber} stroke={1.8} />
          </div>
        </div>
        <div style={{position: "absolute", left: 0, right: 0, top: 690, display: "flex", justifyContent: "center", opacity: sp(frame, 34)}}>
          <Chip tone="amber" solid size={32}>
            Ý tưởng chính
          </Chip>
        </div>
      </Show>

      {/* L1: record how the output is wrong */}
      <Show at={b(1)} out={b(2) - 8} dy={20}>
        <Card pad={34} radius={28} style={{position: "absolute", left: 170, top: 330, width: 560, height: 300}}>
          <div style={{fontSize: 21, fontWeight: 700, letterSpacing: "0.07em", textTransform: "uppercase", color: C.ink3}}>Cách cũ: chỉ ghi</div>
          <div style={{display: "flex", alignItems: "center", gap: 22, marginTop: 34}}>
            <div style={{fontSize: 34, fontWeight: 700}}>Test 1</div>
            <Chip tone="red" icon="x" size={28}>
              trượt
            </Chip>
          </div>
          <div style={{fontSize: 26, color: C.ink3, fontWeight: 600, marginTop: 34}}>…sai thế nào thì không biết</div>
        </Card>
        {(() => {
          const s = sp(frame, newAt - 4);
          const x = pop(frame, extraAt);
          return (
            <Card
              pad={34}
              radius={28}
              style={{
                position: "absolute",
                left: 800,
                top: 330,
                width: 950,
                height: 300,
                opacity: s,
                transform: `translateX(${(1 - s) * 60}px)`,
                boxShadow: `0 0 0 3px ${C.indigo}, 0 24px 50px -24px rgba(29,34,51,0.45)`,
              }}
            >
              <div style={{fontSize: 21, fontWeight: 700, letterSpacing: "0.07em", textTransform: "uppercase", color: C.indigo}}>Cách mới: ghi thêm</div>
              <div style={{display: "flex", alignItems: "center", gap: 22, marginTop: 34}}>
                <div style={{fontSize: 34, fontWeight: 700}}>Test 1</div>
                <Chip tone="red" icon="x" size={28}>
                  trượt
                </Chip>
                <div style={{fontSize: 40, fontWeight: 800, color: C.indigo, opacity: Math.min(1, x * 1.5)}}>+</div>
                <div style={{transform: `scale(${0.6 + 0.4 * x})`, opacity: Math.min(1, x * 1.5), transformOrigin: "left center"}}>
                  <Chip tone="amber" solid size={28} icon="search">
                    output sai thế nào
                  </Chip>
                </div>
              </div>
              <div style={{fontSize: 26, color: C.ink2, fontWeight: 600, marginTop: 34, opacity: sp(frame, extraAt + 16)}}>
                ví dụ: <span style={{color: C.ink, fontWeight: 700}}>“thiếu xuống dòng ở cuối”</span>
              </div>
            </Card>
          );
        })()}
      </Show>

      {/* L2: four kinds of deviation */}
      <Show at={b(2) - 2} out={b(3) - 8} dy={20}>
        {TILES.map((t, k) => {
          const s = pop(frame, tileAt[k]);
          return (
            <Card
              key={t.title}
              pad={30}
              radius={28}
              style={{
                position: "absolute",
                left: 160 + k * 405,
                top: 340,
                width: 380,
                height: 300,
                opacity: Math.min(1, s * 1.5),
                transform: `translateY(${(1 - Math.min(1, s)) * 40}px)`,
                boxShadow: `inset 0 4px 0 ${TONE[t.tone].solid}, 0 20px 40px -24px rgba(29,34,51,0.45)`,
              }}
            >
              <div style={{fontSize: 30, fontWeight: 800, lineHeight: 1.2, height: 76}}>{t.title}</div>
              {[
                ["Cần in", t.need, C.greenSoft],
                ["Đã in", t.got, C.redSoft],
              ].map(([label, v, bg]) => (
                <div key={label as string} style={{display: "flex", alignItems: "center", gap: 14, marginTop: 14}}>
                  <div style={{fontSize: 21, fontWeight: 700, color: C.ink3, width: 80, flex: "none"}}>{label}</div>
                  <div style={{fontFamily: MONO, fontSize: 30, fontWeight: 600, background: bg as string, borderRadius: 12, padding: "6px 14px", whiteSpace: "nowrap"}}>{v}</div>
                </div>
              ))}
            </Card>
          );
        })}
      </Show>

      {/* L3: the deviation OAV */}
      <Show at={b(3) - 2} out={b(4) - 8} dy={20}>
        <div style={{position: "absolute", left: 0, right: 0, top: 232, textAlign: "center", opacity: sp(frame, oavAt - 4)}}>
          <span style={{fontSize: 64, fontWeight: 800, color: C.indigo, letterSpacing: "-0.02em"}}>OAV độ lệch</span>
        </div>
        <Card pad={30} radius={28} style={{position: "absolute", left: 170, top: 350, width: 980}}>
          <div style={{fontSize: 26, fontWeight: 700, color: C.ink2, marginBottom: 20}}>Với mỗi test, máy tự trả lời 9 câu hỏi nhỏ:</div>
          <div style={{display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 14}}>
            {DESCRIPTORS.map((d, k) => {
              const s = pop(frame, oavAt + 8 + k * 3);
              return (
                <div
                  key={d}
                  style={{
                    height: 76,
                    borderRadius: 16,
                    background: C.indigoSoft,
                    display: "flex",
                    alignItems: "center",
                    gap: 12,
                    padding: "0 18px",
                    fontSize: 24,
                    fontWeight: 700,
                    color: C.indigoDeep,
                    opacity: Math.min(1, s * 1.5),
                    transform: `scale(${0.7 + 0.3 * Math.min(1, s)})`,
                  }}
                >
                  <span style={{fontFamily: MONO, fontSize: 20, color: C.indigo, opacity: 0.7}}>{k + 1}</span>
                  {d}
                </div>
              );
            })}
          </div>
        </Card>
        <div style={{position: "absolute", left: 1210, top: 380, display: "flex", flexDirection: "column", gap: 30}}>
          {benefits.map(([icon, text, t]) => {
            const s = sp(frame, t);
            return (
              <div key={text} style={{display: "flex", alignItems: "center", gap: 20, opacity: s, transform: `translateX(${(1 - s) * 40}px)`}}>
                <div style={{width: 80, height: 80, borderRadius: 24, background: C.greenSoft, display: "grid", placeItems: "center", flex: "none"}}>
                  <Icon name={icon} size={42} color={C.green} />
                </div>
                <div style={{fontSize: 31, fontWeight: 700, lineHeight: 1.25, maxWidth: 420}}>{text}</div>
              </div>
            );
          })}
        </div>
      </Show>

      {/* L4: A, B and C now separate */}
      <Show at={b(4)} dy={20}>
        {ABC.map((it, k) => {
          const x = 730 + (k - 1) * 560 * split + (1 - split) * (k - 1) * 18;
          const y = 350 + (1 - split) * (k - 1) * 14;
          const dev = pop(frame, devAt + k * 5);
          return (
            <Card
              key={it.name}
              pad={28}
              radius={26}
              style={{
                position: "absolute",
                left: x,
                top: y,
                width: 460,
                zIndex: 3 - Math.abs(k - 1),
                boxShadow: split > 0.5 ? `0 0 0 3px ${TONE[it.tone].solid}, 0 24px 50px -24px rgba(29,34,51,0.45)` : undefined,
              }}
            >
              <div style={{display: "flex", alignItems: "center", justifyContent: "space-between"}}>
                <div style={{fontSize: 34, fontWeight: 800}}>{it.name}</div>
                <div style={{display: "flex", gap: 8}}>
                  {[0, 1, 2, 3].map((i) => (
                    <TestTile key={i} ok={false} size={40} />
                  ))}
                </div>
              </div>
              <div style={{height: 2, background: C.soft, margin: "20px 0"}} />
              <div style={{height: 50, display: "flex", alignItems: "center"}}>
                {dev > 0.01 ? (
                  <div style={{transform: `scale(${0.6 + 0.4 * dev})`, opacity: Math.min(1, dev * 1.5), transformOrigin: "left center"}}>
                    <Chip tone={it.tone} size={25}>
                      {it.chip}
                    </Chip>
                  </div>
                ) : (
                  <div style={{fontSize: 24, color: C.ink3, fontWeight: 600}}>độ lệch: ?</div>
                )}
              </div>
            </Card>
          );
        })}
        {(() => {
          const s = pop(frame, at(4, "tách"));
          return s > 0.01 ? (
            <div style={{position: "absolute", left: 960, top: 680, transform: `translateX(-50%) scale(${0.6 + 0.4 * s})`, opacity: Math.min(1, s * 1.5)}}>
              <Chip tone="green" solid icon="split" size={32}>
                Ba phiếu khác nhau: tách ra được!
              </Chip>
            </div>
          ) : null;
        })()}
      </Show>
    </SceneFrame>
  );
};

export const deviationPops = (scene: Scene) => {
  const {at} = beats(scene);
  return [16, at(1, "thế"), at(2, "thiếu"), at(2, "số", 0), at(2, "số", 1), at(2, "hay"), at(4, "tách")];
};
