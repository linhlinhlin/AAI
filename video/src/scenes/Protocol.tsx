import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {clamp, EASE, pop, sp} from "../anim";
import {SceneFrame} from "../components/frame";
import {Icon} from "../components/Icon";
import {Arrow, Card, Chip, Show, Stamp, Tone, TONE} from "../components/ui";
import {C, MONO} from "../theme";
import {beats, Scene} from "../timeline";

// research/splits/cpack-v3.json: split by student, 70/15/15 target.
const JARS: {name: string; n: string; share: number; tone: Tone; note: string}[] = [
  {name: "Để học", n: "6.088 bài", share: 0.707, tone: "indigo", note: "máy học luật, học từ vựng"},
  {name: "Để thử", n: "1.569 bài", share: 0.182, tone: "amber", note: "chỉnh đúng một thông số"},
  {name: "Niêm phong", n: "950 bài", share: 0.11, tone: "green", note: "chỉ mở một lần, ở cuối"},
];

// research/protocol-mechanism-v1.json: registration and amendments (UTC, 30/09/2026).
const EVENTS: {time: string; name: string; note: string; tone: Tone}[] = [
  {time: "12:06", name: "Đăng ký", note: "giả thuyết, cách đo", tone: "indigo"},
  {time: "12:17", name: "A1 – A4", note: "làm rõ giả thuyết và đơn vị dữ liệu", tone: "neutral"},
  {time: "12:30", name: "A5", note: "loại bài chạy không ổn định", tone: "neutral"},
  {time: "12:50", name: "A6", note: "sửa bộ phân loại nhãn", tone: "neutral"},
  {time: "13:02", name: "A7", note: "chốt hệ số phạt ILA-2 = 1,0", tone: "neutral"},
  {time: "sau A7", name: "Mở niêm phong", note: "chạy đúng một lần", tone: "green"},
];

const Jar: React.FC<{fill: number; tone: Tone; t: number; locked: boolean; open: number}> = ({fill, tone, t, locked, open}) => {
  const h = 280;
  const level = (h - 40) * fill * t;
  return (
    <div style={{position: "relative", width: 220, height: h + 50}}>
      {/* lid */}
      <div
        style={{
          position: "absolute",
          left: 30,
          top: -open * 40,
          width: 160,
          height: 30,
          borderRadius: 10,
          background: C.ink2,
          transform: `rotate(${-open * 18}deg)`,
          transformOrigin: "0% 100%",
        }}
      />
      <div
        style={{
          position: "absolute",
          left: 0,
          top: 36,
          width: 220,
          height: h,
          borderRadius: "30px 30px 40px 40px",
          background: "rgba(255,255,255,0.75)",
          boxShadow: `inset 0 0 0 4px ${C.line}, 0 20px 40px -24px rgba(29,34,51,0.45)`,
          overflow: "hidden",
        }}
      >
        <div style={{position: "absolute", left: 0, right: 0, bottom: 0, height: level, background: `linear-gradient(180deg, ${TONE[tone].solid}CC, ${TONE[tone].solid})`}} />
        <div style={{position: "absolute", left: 22, top: 20, width: 20, height: h - 60, borderRadius: 10, background: "rgba(255,255,255,0.55)"}} />
      </div>
      {locked ? (
        <div style={{position: "absolute", left: 110, top: 130, transform: "translate(-50%, -50%)", width: 84, height: 84, borderRadius: 99, background: "#fff", boxShadow: "0 10px 24px -10px rgba(29,34,51,0.5)", display: "grid", placeItems: "center"}}>
          <Icon name={open > 0.5 ? "unlock" : "lock"} size={44} color={open > 0.5 ? C.green : C.ink} />
        </div>
      ) : null}
    </div>
  );
};

export const Protocol: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {b, at} = beats(scene);
  const seeAt = at(0, "xem");
  const rows = [at(1, "giả"), at(1, "cách"), at(1, "thắng"), at(1, "thua")];
  const stampAt = at(1, "đăng");
  const jarAt = [at(2, "học"), at(2, "thử"), at(2, "niêm")];
  const onceAt = at(3, "lần");
  const openAt = at(3, "cuối");
  const open = sp(frame, openAt, 14);
  const focus = interpolate(frame, [b(3), b(3) + 16], [0, 1], {...clamp, easing: EASE});

  return (
    <SceneFrame scene={scene}>
      {/* L0: rules first, results second */}
      <Show at={b(0)} out={b(1) - 8} dy={20}>
        {(
          [
            ["book", "1 · Viết luật chơi", "trước", 380, b(0) + 4, "indigo"],
            ["eye", "2 · Rồi mới xem kết quả", "sau", 1060, seeAt, "green"],
          ] as const
        ).map(([icon, title, when, x, t, tone]) => {
          const s = pop(frame, t);
          return (
            <Card
              key={title}
              pad={36}
              radius={30}
              style={{position: "absolute", left: x, top: 340, width: 480, display: "flex", flexDirection: "column", alignItems: "center", gap: 18, opacity: Math.min(1, s * 1.5), transform: `scale(${0.7 + 0.3 * Math.min(1, s)})`}}
            >
              <div style={{width: 110, height: 110, borderRadius: 32, background: TONE[tone].bg, display: "grid", placeItems: "center"}}>
                <Icon name={icon} size={60} color={TONE[tone].solid} />
              </div>
              <div style={{fontSize: 34, fontWeight: 800, textAlign: "center"}}>{title}</div>
              <Chip tone={tone} size={24}>
                {when}
              </Chip>
            </Card>
          );
        })}
        <Arrow x1={880} y1={470} x2={1040} y2={470} t={interpolate(frame, [seeAt - 10, seeAt], [0, 1], clamp)} color={C.ink3} width={5} />
        <Show at={at(0, "lừa") - 4}>
          <div style={{position: "absolute", left: 0, right: 0, top: 700, display: "flex", justifyContent: "center"}}>
            <Chip tone="indigo" icon="shield" size={28}>
              Để không tự lừa mình
            </Chip>
          </div>
        </Show>
      </Show>

      {/* L1: the registered protocol */}
      <Show at={b(1)} out={b(2) - 8} dy={20}>
        <Card pad={40} radius={30} style={{position: "absolute", left: 440, top: 280, width: 1040}}>
          <div style={{display: "flex", alignItems: "center", gap: 18}}>
            <div style={{width: 64, height: 64, borderRadius: 18, background: C.indigoSoft, display: "grid", placeItems: "center"}}>
              <Icon name="clipboard" size={36} color={C.indigo} />
            </div>
            <div>
              <div style={{fontSize: 34, fontWeight: 800}}>Luật chơi viết sẵn</div>
              <div style={{fontSize: 22, color: C.ink2, fontWeight: 500}}>giao thức nghiên cứu, viết trước khi có kết quả</div>
            </div>
          </div>
          <div style={{height: 2, background: C.soft, margin: "22px 0 8px"}} />
          {[
            ["Giả thuyết", "H1 đến H5"],
            ["Cách đo", "trần, ARI, điểm F1"],
            ["Thế nào là thắng", "khoảng tin cậy 95% nằm hẳn trên 0"],
            ["Thế nào là thua", "khoảng tin cậy chạm hoặc dưới 0"],
          ].map(([k, v], i) => {
            const s = sp(frame, rows[i]);
            return (
              <div key={k} style={{display: "flex", alignItems: "center", gap: 18, height: 78, opacity: s, transform: `translateX(${(1 - s) * 30}px)`}}>
                <div style={{width: 40, height: 40, borderRadius: 99, background: C.green, display: "grid", placeItems: "center", flex: "none"}}>
                  <Icon name="check" size={24} color="#fff" stroke={3} />
                </div>
                <div style={{fontSize: 30, fontWeight: 800, width: 260, flex: "none"}}>{k}</div>
                <div style={{fontSize: 28, color: C.ink2, fontWeight: 600}}>{v}</div>
              </div>
            );
          })}
        </Card>
        {frame >= stampAt ? (
          <div style={{position: "absolute", left: 1150, top: 262}}>
            <Stamp at={stampAt} tone="indigo" size={40} rotate={-8}>
              ĐĂNG KÝ TRƯỚC
            </Stamp>
            <div style={{fontFamily: MONO, fontSize: 20, color: C.indigo, marginTop: 14, marginLeft: 20, opacity: sp(frame, stampAt + 10)}}>30/09/2026 · 12:06 UTC</div>
          </div>
        ) : null}
      </Show>

      {/* L2–L3: three jars, one sealed */}
      <Show at={b(2) - 2} out={b(4) - 8} dy={20}>
        {JARS.map((j, k) => {
          const s = pop(frame, b(2) + 4 + k * 5);
          const fill = sp(frame, jarAt[k] + 4, 200, 30);
          const named = sp(frame, jarAt[k] - 4);
          const dim = k < 2 ? 1 - 0.6 * focus : 1;
          const grow = k === 2 ? 1 + 0.08 * focus : 1;
          return (
            <div
              key={j.name}
              style={{
                position: "absolute",
                left: 450 + k * 400,
                top: 280,
                width: 220,
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                opacity: Math.min(1, s * 1.5) * dim,
                transform: `scale(${(0.7 + 0.3 * Math.min(1, s)) * grow})`,
              }}
            >
              <Jar fill={j.share / 0.707 * 0.9} tone={j.tone} t={fill} locked={k === 2} open={k === 2 ? open : 0} />
              <div style={{fontSize: 32, fontWeight: 800, marginTop: 16, whiteSpace: "nowrap", opacity: named}}>{j.name}</div>
              <div style={{fontSize: 24, color: C.ink2, fontWeight: 600, whiteSpace: "nowrap", opacity: named}}>
                {j.n} · {Math.round(j.share * 100)}%
              </div>
            </div>
          );
        })}
        <Show at={jarAt[2] + 20} out={b(3) - 4}>
          <div style={{position: "absolute", left: 0, right: 0, top: 760, display: "flex", justifyContent: "center"}}>
            <Chip tone="neutral" icon="users" size={26}>
              Chia theo sinh viên: mỗi bạn chỉ nằm ở một phần
            </Chip>
          </div>
        </Show>
        {(() => {
          const s = pop(frame, onceAt);
          return s > 0.01 ? (
            <div style={{position: "absolute", left: 1510, top: 360, transform: `scale(${0.6 + 0.4 * s})`, opacity: Math.min(1, s * 1.5), transformOrigin: "left center"}}>
              <Chip tone="green" solid size={30}>
                Chỉ mở 1 lần
              </Chip>
              <div style={{fontSize: 24, color: C.ink2, fontWeight: 600, marginTop: 14, maxWidth: 300, lineHeight: 1.35}}>ở cuối cùng, với cấu hình đã chốt</div>
            </div>
          ) : null;
        })()}
      </Show>

      {/* L4: every change is dated */}
      <Show at={b(4) - 2} dy={20}>
        <div style={{position: "absolute", left: 250, top: 536, width: 1420, height: 6, borderRadius: 3, background: C.line}} />
        {EVENTS.map((e, k) => {
          const x = 250 + k * 284;
          const s = pop(frame, b(4) + 6 + k * 9);
          const t = TONE[e.tone];
          return (
            <div key={e.name} style={{position: "absolute", left: x, top: 380, width: 260, transform: "translateX(-50%)", display: "flex", flexDirection: "column", alignItems: "center", opacity: Math.min(1, s * 1.5)}}>
              <div style={{fontFamily: MONO, fontSize: 24, fontWeight: 600, color: e.tone === "neutral" ? C.ink2 : t.solid, height: 34}}>{e.time}</div>
              <div style={{fontSize: 28, fontWeight: 800, height: 44, whiteSpace: "nowrap"}}>{e.name}</div>
              <div
                style={{
                  width: 64,
                  height: 64,
                  borderRadius: 99,
                  background: e.tone === "neutral" ? "#fff" : t.solid,
                  boxShadow: e.tone === "neutral" ? `inset 0 0 0 4px ${C.ink3}, 0 0 0 8px ${C.bg}` : `0 0 0 8px ${C.bg}`,
                  display: "grid",
                  placeItems: "center",
                  marginTop: 32,
                  transform: `scale(${0.5 + 0.5 * Math.min(1, s)})`,
                }}
              >
                <Icon name={k === 0 ? "clipboard" : k === EVENTS.length - 1 ? "unlock" : "calendar"} size={32} color={e.tone === "neutral" ? C.ink2 : "#fff"} />
              </div>
              <div style={{fontSize: 22, color: C.ink2, fontWeight: 600, textAlign: "center", marginTop: 16, lineHeight: 1.3}}>{e.note}</div>
            </div>
          );
        })}
        <Show at={at(4, "kiểm")}>
          <div style={{position: "absolute", left: 0, right: 0, top: 270, display: "flex", justifyContent: "center", gap: 20}}>
            <Chip tone="indigo" icon="calendar" size={26}>
              30/09/2026, giờ UTC · mọi sửa đổi đều trước khi mở niêm phong
            </Chip>
          </div>
        </Show>
        <Show at={at(4, "kiểm") + 14}>
          <div style={{position: "absolute", left: 0, right: 0, top: 790, display: "flex", justifyContent: "center"}}>
            <Chip tone="neutral" icon="key" size={24}>
              Mỗi tệp dữ liệu và giao thức đều ghi mã SHA-256 để ai cũng đối chiếu được
            </Chip>
          </div>
        </Show>
      </Show>
    </SceneFrame>
  );
};

export const protocolPops = (scene: Scene) => {
  const {at} = beats(scene);
  return [at(0, "xem"), at(1, "đăng"), at(2, "học"), at(2, "thử"), at(2, "niêm"), at(3, "cuối")];
};
