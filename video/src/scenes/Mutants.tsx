import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {clamp, EASE, pop, sp} from "../anim";
import {SceneFrame} from "../components/frame";
import {HBar} from "../components/charts";
import {Icon} from "../components/Icon";
import {Card, Chip, Counter, Paper, Show} from "../components/ui";
import {C, MONO} from "../theme";
import {beats, Scene} from "../timeline";

// research/runs/mechanism-bench-v1.1/stats.json
const REAL: [string, number][] = [
  ["Văn bản in ra", 180],
  ["Biểu thức tính toán", 30],
  ["Thiếu bước", 29],
  ["Điều kiện rẽ nhánh", 19],
  ["Luồng điều khiển", 18],
  ["Biên vòng lặp", 17],
  ["Đặc tả định dạng in", 13],
  ["Thừa bước", 9],
  ["Khởi tạo", 8],
  ["Vị trí câu lệnh", 7],
  ["Đọc dữ liệu", 6],
  ["Kiểu số, chia nguyên", 3],
];
const INJECTED: [string, number][] = [
  ["Văn bản in ra", 637],
  ["Thiếu bước", 502],
  ["Thừa bước", 458],
  ["Biên vòng lặp", 449],
  ["Khởi tạo", 365],
  ["Biểu thức tính toán", 347],
  ["Vị trí câu lệnh", 326],
  ["Điều kiện rẽ nhánh", 194],
  ["Đặc tả định dạng in", 42],
];
const OPERATORS = [
  "bỏ xuống dòng",
  "xóa một lệnh",
  "lặp lại một lệnh",
  "đổi giá trị khởi tạo",
  "đổi phép tính",
  "đưa lệnh in vào vòng lặp",
  "đổi < và <= ở vòng lặp",
  "đổi điểm bắt đầu vòng lặp",
  "đổi < và <= ở if",
  "đổi && và ||",
  "đưa lệnh vào vòng lặp",
  "đổi chữ hoa, thường",
  "đổi số chữ số thập phân",
];

const Cup: React.FC<{lift: number}> = ({lift}) => (
  <svg width="200" height="190" viewBox="0 0 200 190" style={{overflow: "visible", transform: `translateY(${-lift * 120}px) rotate(${lift * -8}deg)`}}>
    <defs>
      <linearGradient id="cup" x1="0" x2="1">
        <stop offset="0" stopColor="#5C6BC0" />
        <stop offset="1" stopColor="#3949AB" />
      </linearGradient>
    </defs>
    <path d="M40 10 h120 l30 170 h-180z" fill="url(#cup)" />
    <rect x="4" y="170" width="192" height="20" rx="10" fill="#303F9F" />
    <path d="M62 30 l-16 120" stroke="rgba(255,255,255,0.35)" strokeWidth="10" strokeLinecap="round" />
  </svg>
);

export const Mutants: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {b, at} = beats(scene);
  const halfAt = at(0, "nửa");
  const hitAt = at(1, "hỏng");
  const hammer = interpolate(frame, [hitAt - 14, hitAt, hitAt + 10], [-50, 8, -20], {...clamp, easing: EASE});
  const broken = frame >= hitAt;

  // L2: hide and seek
  const cover = interpolate(frame, [b(2) + 16, b(2) + 34], [1, 0], {...clamp, easing: EASE});
  const seekAt = at(2, "thám");
  const foundAt = at(2, "tìm");
  const stopAt = Math.max(foundAt + 12, seekAt + 42);
  const leg = (stopAt - seekAt) / 3;
  const glassX = interpolate(frame, [seekAt, seekAt + leg, seekAt + 2 * leg, stopAt], [420, 1280, 640, 960], {...clamp, easing: EASE});
  const reveal = sp(frame, stopAt + 4);

  return (
    <SceneFrame scene={scene}>
      {/* L0: real labels are lopsided */}
      <Show at={b(0)} out={b(1) - 8} dy={20}>
        <div style={{position: "absolute", left: 0, right: 0, top: 268, textAlign: "center", fontSize: 28, fontWeight: 700, color: C.ink2}}>
          339 đáp án thật, chia theo loại lỗi
        </div>
        <div style={{position: "absolute", left: 200, top: 326, display: "flex", flexDirection: "column", gap: 10}}>
          {REAL.map(([name, n], k) => (
            <HBar
              key={name}
              label={name}
              value={n}
              max={180}
              at={b(0) + 6 + k * 3}
              width={760}
              height={24}
              labelWidth={290}
              fontSize={23}
              color={k === 0 ? C.amber : "#9FA8DA"}
            />
          ))}
        </div>
        {(() => {
          const s = pop(frame, halfAt);
          return s > 0.01 ? (
            <div style={{position: "absolute", left: 1390, top: 314, transform: `scale(${0.6 + 0.4 * s})`, opacity: Math.min(1, s * 1.5), transformOrigin: "left center"}}>
              <Chip tone="amber" solid size={30}>
                53%: hơn một nửa
              </Chip>
            </div>
          ) : null;
        })()}
      </Show>

      {/* L1: break correct programs on purpose, one spot each */}
      <Show at={b(1)} out={b(2) - 8} dy={20}>
        <div style={{position: "absolute", left: 150, top: 330, width: 340, display: "flex", flexDirection: "column", alignItems: "center"}}>
          <div style={{position: "relative", width: 160, height: 190}}>
            {[2, 1, 0].map((k) => (
              <div key={k} style={{position: "absolute", left: k * 14, top: k * 10}}>
                <Paper w={130} lines={5} tone="green" mark={k === 0 ? "check" : null} />
              </div>
            ))}
          </div>
          <Counter to={964} at={at(1, "964") - 6} dur={30} style={{fontSize: 88, fontWeight: 800, color: C.green, letterSpacing: "-0.03em", marginTop: 26}} />
          <div style={{fontSize: 28, fontWeight: 700, color: C.ink2}}>bài đúng làm gốc</div>
        </div>
        <Card pad={30} radius={26} style={{position: "absolute", left: 560, top: 380, width: 600}}>
          <div style={{fontSize: 20, fontWeight: 700, letterSpacing: "0.07em", textTransform: "uppercase", color: C.ink3, marginBottom: 14}}>
            {broken ? "Sau khi làm hỏng" : "Bài đúng"}
          </div>
          <div style={{fontFamily: MONO, fontSize: 32, padding: "12px 16px", borderRadius: 14, background: broken ? C.redSoft : C.greenSoft}}>
            for (i = 1; i{" "}
            <span style={{background: broken ? "#F4B9B4" : "transparent", borderRadius: 6, padding: "0 4px", color: broken ? "#A8322C" : C.ink}}>{broken ? "<" : "<="}</span>{" "}
            n; i++)
          </div>
          <div style={{marginTop: 18, height: 44}}>
            <Show at={at(1, "chỗ")}>
              <Chip tone="red" icon="alert" size={24}>
                Chỉ hỏng đúng một chỗ
              </Chip>
            </Show>
          </div>
        </Card>
        <div style={{position: "absolute", left: 1050, top: 300, transform: `rotate(${hammer}deg)`, transformOrigin: "80% 80%", opacity: sp(frame, hitAt - 24) * interpolate(frame, [hitAt + 30, hitAt + 44], [1, 0], clamp)}}>
          <Icon name="hammer" size={110} color={C.ink} stroke={1.8} />
        </div>
        <div style={{position: "absolute", left: 1230, top: 300, width: 560}}>
          <div style={{fontSize: 22, fontWeight: 700, letterSpacing: "0.07em", textTransform: "uppercase", color: C.ink3, marginBottom: 16, opacity: sp(frame, at(1, "kiểu") - 6)}}>
            13 kiểu làm hỏng biết trước
          </div>
          <div style={{display: "flex", flexWrap: "wrap", gap: 10}}>
            {OPERATORS.map((op, k) => {
              const s = pop(frame, at(1, "kiểu") + k * 2.5);
              return (
                <div key={op} style={{transform: `scale(${0.6 + 0.4 * Math.min(1, s)})`, opacity: Math.min(1, s * 1.5)}}>
                  <Chip tone="indigo" size={21}>
                    {op}
                  </Chip>
                </div>
              );
            })}
          </div>
        </div>
      </Show>

      {/* L2: hide an object, see if the detective finds it */}
      <Show at={b(2)} out={b(3) - 8} dy={20}>
        {[640, 960, 1280].map((x, k) => {
          const hidden = k === 1;
          const lift = hidden ? Math.max(cover, reveal) : 0;
          return (
            <div key={x} style={{position: "absolute", left: x - 100, top: 420}}>
              {hidden ? (
                <div style={{position: "absolute", left: 50, top: 80, opacity: Math.max(cover, reveal)}}>
                  <div style={{width: 100, height: 100, borderRadius: 24, background: C.amberSoft, display: "grid", placeItems: "center", boxShadow: `inset 0 0 0 3px ${C.amber}66`}}>
                    <Icon name="gift" size={60} color={C.amber} />
                  </div>
                </div>
              ) : null}
              <Cup lift={lift} />
            </div>
          );
        })}
        <div style={{position: "absolute", left: 300, top: 630, width: 1320, height: 10, borderRadius: 5, background: C.line}} />
        {frame >= seekAt - 4 ? (
          <div style={{position: "absolute", left: glassX - 50, top: 300, opacity: sp(frame, seekAt - 4)}}>
            <Icon name="search" size={100} color={C.ink} stroke={2.2} />
          </div>
        ) : null}
        {(() => {
          const s = pop(frame, stopAt + 10);
          return s > 0.01 ? (
            <div style={{position: "absolute", left: 960, top: 700, transform: `translateX(-50%) scale(${0.6 + 0.4 * s})`, opacity: Math.min(1, s * 1.5)}}>
              <Chip tone="green" solid icon="check" size={30}>
                Biết trước đáp án, nên chấm được thám tử
              </Chip>
            </div>
          ) : null;
        })()}
      </Show>

      {/* L3: 3,320 mutants with a certain answer */}
      <Show at={b(3) - 2} dy={20}>
        <Card pad={36} radius={28} style={{position: "absolute", left: 170, top: 300, width: 700}}>
          {(
            [
              ["4.350", "bài hỏng được tạo", C.ink, b(3) + 4],
              ["− 722", "vẫn đúng mọi test: không tính", C.ink3, b(3) + 14],
              ["− 308", "cảnh báo hoặc lỗi biên dịch: bỏ", C.ink3, b(3) + 24],
            ] as const
          ).map(([n, label, color, t]) => (
            <div key={label} style={{display: "flex", alignItems: "baseline", gap: 18, marginBottom: 12, opacity: sp(frame, t)}}>
              <div style={{fontFamily: MONO, fontSize: 36, fontWeight: 600, color, width: 150, textAlign: "right"}}>{n}</div>
              <div style={{fontSize: 27, color: C.ink2, fontWeight: 600}}>{label}</div>
            </div>
          ))}
          <div style={{height: 2, background: C.soft, margin: "18px 0"}} />
          <div style={{display: "flex", alignItems: "baseline", gap: 18}}>
            <Counter to={3320} at={at(3, "3.320") - 4} dur={36} style={{fontSize: 96, fontWeight: 800, color: C.green, letterSpacing: "-0.03em"}} />
            <div style={{fontSize: 30, fontWeight: 700}}>bài hỏng dùng được</div>
          </div>
          <div style={{marginTop: 16, opacity: sp(frame, at(3, "đáp"))}}>
            <Chip tone="green" icon="check" size={24}>
              Bài nào cũng biết chắc hỏng ở đâu
            </Chip>
          </div>
        </Card>
        <div style={{position: "absolute", left: 960, top: 300}}>
          <div style={{fontSize: 24, fontWeight: 700, color: C.ink2, marginBottom: 16, opacity: sp(frame, b(3) + 10)}}>9 loại lỗi, đều nhau hơn nhiều</div>
          <div style={{display: "flex", flexDirection: "column", gap: 9}}>
            {INJECTED.map(([name, n], k) => (
              <HBar key={name} label={name} value={n} max={637} at={b(3) + 14 + k * 3} width={420} height={22} labelWidth={260} fontSize={21} color="#7986CB" />
            ))}
          </div>
        </div>
      </Show>
    </SceneFrame>
  );
};

export const mutantsPops = (scene: Scene) => {
  const {at} = beats(scene);
  const seek = at(2, "thám");
  const stop = Math.max(at(2, "tìm") + 12, seek + 42);
  return [at(0, "nửa"), at(1, "hỏng"), stop + 10, at(3, "3.320") + 30];
};
