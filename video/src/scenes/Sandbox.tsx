import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {clamp, EASE, pop, sp} from "../anim";
import {SceneFrame} from "../components/frame";
import {Gauge} from "../components/charts";
import {Icon, IconName} from "../components/Icon";
import {Arrow, Card, Chip, Counter, Paper, Show, Stamp} from "../components/ui";
import {C} from "../theme";
import {beats, Scene} from "../timeline";

const ROOM = {x: 540, y: 292, w: 660, h: 480};

export const Sandbox: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {b, at} = beats(scene);
  const nAt = at(0, "8.607");
  const roomIn = sp(frame, b(1));
  const rules: [IconName, string, number][] = [
    ["wifiOff", "Không có mạng", at(1, "mạng")],
    ["shield", "Không có quyền đặc biệt", at(1, "quyền")],
    ["timer", "Có đồng hồ bấm giờ", at(1, "đồng")],
  ];
  const keyAt = b(2) + 2;
  const peekAt = at(2, "nhìn");

  return (
    <SceneFrame scene={scene}>
      {/* L0: replay everything */}
      <Show at={b(0)} out={b(1) - 8} dy={20}>
        <div style={{position: "absolute", left: 0, right: 0, top: 300, display: "flex", flexDirection: "column", alignItems: "center"}}>
          <div style={{display: "flex", alignItems: "center", gap: 34}}>
            <div style={{width: 120, height: 120, borderRadius: 36, background: C.indigoSoft, display: "grid", placeItems: "center"}}>
              <div style={{transform: `rotate(${-frame * 6}deg)`}}>
                <Icon name="replay" size={70} color={C.indigo} />
              </div>
            </div>
            <Counter to={8607} at={nAt - 6} dur={50} style={{fontSize: 170, fontWeight: 800, letterSpacing: "-0.04em", lineHeight: 1}} />
          </div>
          <div style={{fontSize: 38, fontWeight: 700, color: C.ink2, marginTop: 14, opacity: sp(frame, nAt)}}>bài nộp được chạy lại từ đầu</div>
          <div style={{display: "flex", gap: 18, marginTop: 34}}>
            {["246 sinh viên", "25 bài tập", "106 test"].map((t, k) => (
              <div key={t} style={{opacity: sp(frame, nAt + 16 + k * 6), transform: `translateY(${(1 - sp(frame, nAt + 16 + k * 6)) * 16}px)`}}>
                <Chip tone="neutral" size={28}>
                  {t}
                </Chip>
              </div>
            ))}
          </div>
        </div>
      </Show>

      {/* L1–L2: the sealed room */}
      <Show at={b(1)} out={b(3) - 8} dy={0}>
        <div
          style={{
            position: "absolute",
            left: ROOM.x,
            top: ROOM.y,
            width: ROOM.w,
            height: ROOM.h,
            borderRadius: 40,
            background: "linear-gradient(140deg, rgba(255,255,255,0.92), rgba(230,233,248,0.75))",
            boxShadow: `inset 0 0 0 4px ${C.indigo}55, inset 0 0 60px rgba(63,81,181,0.12), 0 30px 60px -30px rgba(29,34,51,0.45)`,
            transform: `scale(${0.85 + 0.15 * roomIn})`,
            opacity: roomIn,
          }}
        >
          <div style={{position: "absolute", left: 30, top: 26, display: "flex", alignItems: "center", gap: 14}}>
            <div style={{width: 52, height: 52, borderRadius: 16, background: C.indigo, display: "grid", placeItems: "center"}}>
              <Icon name="box" size={30} color="#fff" />
            </div>
            <div>
              <div style={{fontSize: 30, fontWeight: 800}}>Phòng kín Docker</div>
              <div style={{fontSize: 21, color: C.ink2, fontWeight: 500}}>mỗi bài một phòng riêng</div>
            </div>
          </div>
          {/* glass sheen */}
          <div style={{position: "absolute", right: 40, top: 30, width: 110, height: 300, borderRadius: 60, background: "linear-gradient(180deg, rgba(255,255,255,0.8), rgba(255,255,255,0))", transform: "rotate(18deg)", opacity: 0.6}} />
          <div style={{position: "absolute", left: "50%", top: 150, transform: "translateX(-50%)", display: "flex", flexDirection: "column", alignItems: "center", gap: 18}}>
            <div style={{position: "relative"}}>
              <Paper w={130} lines={6} />
              <div style={{position: "absolute", right: -30, bottom: -18, width: 64, height: 64, borderRadius: 99, background: "#fff", boxShadow: "0 6px 16px -6px rgba(29,34,51,0.4)", display: "grid", placeItems: "center"}}>
                <div style={{transform: `rotate(${-frame * 8}deg)`}}>
                  <Icon name="replay" size={36} color={C.indigo} />
                </div>
              </div>
            </div>
            <div style={{fontSize: 26, fontWeight: 700, color: C.ink2}}>bài của sinh viên đang chạy</div>
          </div>
          {(() => {
            const s = pop(frame, peekAt);
            return s > 0.01 ? (
              <div style={{position: "absolute", left: 30, bottom: 28, transform: `scale(${0.6 + 0.4 * s})`, opacity: Math.min(1, s * 1.5), transformOrigin: "left bottom"}}>
                <Chip tone="red" icon="eyeOff" size={26}>
                  Không nhìn trộm được đáp án
                </Chip>
              </div>
            ) : null;
          })()}
        </div>
        {/* rules of the room */}
        <div style={{position: "absolute", left: 1260, top: 330, display: "flex", flexDirection: "column", gap: 26}}>
          {rules.map(([icon, text, t]) => {
            const s = sp(frame, t);
            return (
              <div key={text} style={{display: "flex", alignItems: "center", gap: 20, opacity: s, transform: `translateX(${(1 - s) * 40}px)`}}>
                <div style={{width: 76, height: 76, borderRadius: 22, background: "#fff", boxShadow: `0 0 0 1px ${C.line}, 0 10px 24px -14px rgba(29,34,51,0.4)`, display: "grid", placeItems: "center"}}>
                  <Icon name={icon} size={40} color={C.indigo} />
                </div>
                <div style={{fontSize: 32, fontWeight: 700, maxWidth: 400, lineHeight: 1.2}}>{text}</div>
              </div>
            );
          })}
        </div>
        {/* the answer key stays outside */}
        {(() => {
          const s = sp(frame, keyAt);
          return (
            <>
              <Card pad={28} radius={26} style={{position: "absolute", left: 130, top: 430, width: 330, opacity: s, transform: `translateX(${(1 - s) * -40}px)`}}>
                <div style={{display: "flex", alignItems: "center", gap: 14}}>
                  <div style={{width: 58, height: 58, borderRadius: 18, background: C.amberSoft, display: "grid", placeItems: "center"}}>
                    <Icon name="key" size={32} color={C.amber} />
                  </div>
                  <div style={{fontSize: 32, fontWeight: 800}}>Đáp án</div>
                  <div style={{marginLeft: "auto"}}>
                    <Icon name="lock" size={30} color={C.ink2} />
                  </div>
                </div>
                <div style={{fontSize: 23, color: C.ink2, fontWeight: 500, marginTop: 12, lineHeight: 1.35}}>giữ ở ngoài phòng, chỉ dùng để so kết quả</div>
              </Card>
              <Arrow x1={560} y1={600} x2={478} y2={600} t={interpolate(frame, [at(2, "ngoài"), at(2, "ngoài") + 14], [0, 1], {...clamp, easing: EASE})} color={C.ink3} width={4} dashed />
            </>
          );
        })()}
      </Show>

      {/* L3: agreement with the original grader */}
      <Show at={b(3) - 2} dy={20}>
        <div style={{position: "absolute", left: 0, right: 0, top: 310, display: "flex", justifyContent: "center", gap: 170}}>
          <div style={{display: "flex", flexDirection: "column", alignItems: "center"}}>
            <Gauge value={0.9842} at={at(3, "98,4%") - 4} size={420} digits={1} label="khớp máy chấm năm xưa" />
            <div style={{fontSize: 22, color: C.ink3, fontWeight: 600, marginTop: 6, opacity: sp(frame, at(3, "98,4%") + 20)}}>trên 28.081 ô kết quả test</div>
          </div>
          <div style={{display: "flex", flexDirection: "column", alignItems: "center"}}>
            <Gauge value={0.9968} at={at(3, "99,7%") - 4} size={420} digits={1} color={C.indigo} label="khớp khi chạy lại lần hai" />
            <div style={{fontSize: 22, color: C.ink3, fontWeight: 600, marginTop: 6, opacity: sp(frame, at(3, "99,7%") + 20)}}>56 bài chạy không ổn định: loại ra</div>
          </div>
        </div>
      </Show>
      {frame >= at(4, "đáng") ? (
        <div style={{position: "absolute", left: 960, top: 690, transform: "translateX(-50%)"}}>
          <Stamp at={at(4, "đáng")} tone="green" size={44} rotate={-4}>
            DỮ LIỆU ĐÁNG TIN
          </Stamp>
        </div>
      ) : null}
    </SceneFrame>
  );
};

export const sandboxPops = (scene: Scene) => {
  const {at} = beats(scene);
  return [at(1, "mạng"), at(1, "quyền"), at(1, "đồng"), at(2, "nhìn"), at(4, "đáng")];
};
