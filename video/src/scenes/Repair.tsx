import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {clamp, EASE, pop, sp} from "../anim";
import {Illustrative, SceneFrame} from "../components/frame";
import {Icon} from "../components/Icon";
import {Arrow, Card, Chip, Counter, Paper, Show, Tone, TONE} from "../components/ui";
import {C, MONO} from "../theme";
import {beats, Scene} from "../timeline";

type DiffLine = {text: string; kind: " " | "+" | "-"; hunk?: "A" | "B" | "C"};
const DIFF: DiffLine[] = [
  {text: "int n, i, s = 0;", kind: " "},
  {text: "// tong tu 1 den n", kind: "+", hunk: "A"},
  {text: 'scanf("%d", &n);', kind: " "},
  {text: "for (i = 1; i < n; i++)", kind: "-", hunk: "B"},
  {text: "for (i = 1; i <= n; i++)", kind: "+", hunk: "B"},
  {text: "    s += i;", kind: "-", hunk: "C"},
  {text: "    s = s + i;", kind: "+", hunk: "C"},
  {text: 'printf("%d\\n", s);', kind: " "},
];
const LINE_H = 50;
const DIFF_TOP = 372;
const HUNK_Y: Record<"A" | "B" | "C", number> = {A: DIFF_TOP + LINE_H * 1, B: DIFF_TOP + LINE_H * 3, C: DIFF_TOP + LINE_H * 5};
const HUNK_ROWS: Record<"A" | "B" | "C", number> = {A: 1, B: 2, C: 2};

const CATEGORIES: [string, string][] = [
  ["Biên vòng lặp", "for · while"],
  ["Điều kiện rẽ nhánh", "if · switch"],
  ["Khởi tạo", "x = 0"],
  ["Biểu thức tính toán", "+ − × ÷"],
  ["Kiểu số, chia nguyên", "int · float"],
  ["Đặc tả định dạng in", "%02d · %.2f"],
  ["Văn bản in ra", '"chữ" · \\n'],
  ["Đọc dữ liệu", "scanf"],
  ["Vị trí câu lệnh", "{ … }"],
  ["Thiếu bước", "+ một lệnh"],
  ["Thừa bước", "− một lệnh"],
  ["Luồng điều khiển", "break · return"],
];

const BRICKS: Tone[] = ["indigo", "amber", "green", "violet", "red", "indigo"];

const Brick: React.FC<{tone: Tone; w: number}> = ({tone, w}) => (
  <div style={{position: "relative", width: w, height: 58}}>
    {[0, 1, 2, 3].map((k) => (
      <div
        key={k}
        style={{
          position: "absolute",
          top: -12,
          left: 22 + k * ((w - 44 - 34) / 3),
          width: 34,
          height: 14,
          borderRadius: "7px 7px 2px 2px",
          background: TONE[tone].solid,
          filter: "brightness(1.08)",
        }}
      />
    ))}
    <div
      style={{
        position: "absolute",
        inset: 0,
        borderRadius: 10,
        background: TONE[tone].solid,
        boxShadow: "inset 0 -8px 0 rgba(0,0,0,0.12), 0 6px 14px -8px rgba(29,34,51,0.5)",
      }}
    />
  </div>
);

export const Repair: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {b, at} = beats(scene);

  // L5: delta debugging steps
  const T1 = b(5) + 12;
  const T2 = T1 + 52;
  const T3 = T2 + 52;
  const done = T3 + 50;
  const removedA = interpolate(frame, [T1 + 26, T1 + 40], [0, 1], clamp);
  const removedC = interpolate(frame, [T2 + 26, T2 + 40], [0, 1], clamp);
  const flashB = frame >= T3 && frame < T3 + 44 ? 1 : 0;
  const hunkLabels = at(4, "nhiều");
  const irrelevant = at(4, "chẳng");

  // L6: Lego
  const legoIn = b(6) + 2;
  const fixAt = at(6, "đặt");
  const fixT = sp(frame, fixAt, 16);
  const scanT = interpolate(frame, [at(6, "tìm"), fixAt - 6], [0, 1], {...clamp, easing: EASE});

  // L7: twelve categories
  const flyAt = at(7, "xếp");
  const flyT = interpolate(frame, [flyAt, flyAt + 30], [0, 1], {...clamp, easing: EASE});

  return (
    <SceneFrame scene={scene}>
      {/* L0: we need an answer key */}
      <Show at={b(0)} out={b(1) - 8} dy={20}>
        {[0, 1, 2].map((k) => (
          <div key={k} style={{position: "absolute", left: 190 + k * 215, top: 380}}>
            <div
              style={{
                width: 190,
                height: 230,
                borderRadius: 24,
                background: `linear-gradient(180deg, ${TONE[(["indigo", "amber", "green"] as Tone[])[k]].bg}, #fff)`,
                boxShadow: `inset 0 0 0 2px ${TONE[(["indigo", "amber", "green"] as Tone[])[k]].solid}40`,
                display: "flex",
                flexWrap: "wrap",
                alignContent: "flex-start",
                gap: 12,
                padding: "62px 24px 0",
              }}
            >
              {[0, 1, 2, 3].map((i) => (
                <Paper key={i} w={56} lines={3} tone="red" />
              ))}
            </div>
            <div style={{position: "absolute", left: 95, top: 14, transform: "translateX(-50%)", fontSize: 22, fontWeight: 700, color: C.ink2}}>
              Hộp {k + 1}
            </div>
          </div>
        ))}
        <Arrow x1={850} y1={500} x2={960} y2={500} t={interpolate(frame, [at(0, "đáp") - 10, at(0, "đáp")], [0, 1], clamp)} color={C.ink3} width={4} />
        <Card pad={34} radius={28} style={{position: "absolute", left: 1000, top: 318, width: 640, opacity: sp(frame, at(0, "đáp") - 4)}}>
          <div style={{display: "flex", alignItems: "center", gap: 18}}>
            <div style={{width: 64, height: 64, borderRadius: 18, background: C.amberSoft, display: "grid", placeItems: "center"}}>
              <Icon name="key" size={36} color={C.amber} />
            </div>
            <div>
              <div style={{fontSize: 34, fontWeight: 800}}>Đáp án</div>
              <div style={{fontSize: 23, color: C.ink2, fontWeight: 500}}>Mỗi bài sai vì lý do gì?</div>
            </div>
          </div>
          {[1, 2, 3].map((n, k) => (
            <div key={n} style={{display: "flex", alignItems: "center", gap: 18, marginTop: 20, opacity: sp(frame, at(0, "mỗi") + k * 6)}}>
              <Paper w={40} lines={3} tone="red" />
              <div style={{fontSize: 30, fontWeight: 700, width: 110}}>Bài {n}</div>
              <Icon name="arrowRight" size={30} color={C.ink3} />
              <Chip tone="amber" size={26} icon="help">
                lý do?
              </Chip>
            </div>
          ))}
        </Card>
      </Show>

      {/* L1: marking by hand is slow and error-prone */}
      <Show at={b(1)} out={b(2) - 8} dy={20}>
        {Array.from({length: 22}, (_, i) => {
          const s = sp(frame, b(1) + 2 + i * 2.2);
          return (
            <div
              key={i}
              style={{
                position: "absolute",
                left: 620 + ((i * 37) % 11) - 5,
                top: 740 - i * 20 - (1 - s) * 60,
                opacity: s,
                transform: `rotate(${((i * 53) % 9) - 4}deg)`,
              }}
            >
              <div style={{width: 220, height: 34, borderRadius: 8, background: "#fff", boxShadow: `0 0 0 1px ${C.line}, 0 4px 10px -6px rgba(29,34,51,0.3)`}} />
            </div>
          );
        })}
        <div style={{position: "absolute", left: 1000, top: 330}}>
          <div style={{fontSize: 46, fontWeight: 800}}>Chấm tay từng bài?</div>
          <div style={{fontSize: 30, color: C.ink2, fontWeight: 500, marginTop: 8}}>hàng nghìn bài sai</div>
          <div style={{display: "flex", flexDirection: "column", gap: 18, marginTop: 34, alignItems: "flex-start"}}>
            {[
              ["timer", "Quá mệt", at(1, "mệt")],
              ["alert", "Dễ nhầm", at(1, "nhầm")],
            ].map(([icon, text, t]) => {
              const s = pop(frame, t as number);
              return (
                <div key={text as string} style={{transform: `scale(${0.6 + 0.4 * s})`, opacity: Math.min(1, s * 1.5), transformOrigin: "left center"}}>
                  <Chip tone="red" icon={icon as "timer"} size={34}>
                    {text}
                  </Chip>
                </div>
              );
            })}
          </div>
        </div>
      </Show>

      {/* L2: students resubmit a correct version soon after */}
      <Show at={b(2)} out={b(3) - 8} dy={20}>
        <Show at={at(2, "mẹo")}>
          <div style={{position: "absolute", left: 0, right: 0, top: 248, display: "flex", justifyContent: "center"}}>
            <Chip tone="indigo" icon="sparkles" size={30}>
              Mẹo của nhóm
            </Chip>
          </div>
        </Show>
        <div style={{position: "absolute", left: 240, top: 598, width: 1440, height: 6, borderRadius: 3, background: C.line}} />
        <div style={{position: "absolute", left: 1640, top: 586}}>
          <Icon name="chevronRight" size={30} color={C.ink3} />
        </div>
        {[0, 1, 2, 3].map((k) => {
          const ok = k === 3;
          const t = ok ? at(2, "đúng") : b(2) + 8 + k * 8;
          const s = pop(frame, t);
          const x = 420 + k * 340;
          return (
            <div key={k} style={{position: "absolute", left: x, top: 400, transform: "translateX(-50%)", display: "flex", flexDirection: "column", alignItems: "center", opacity: Math.min(1, s * 1.5)}}>
              <div style={{transform: `scale(${0.6 + 0.4 * s})`}}>
                <Paper w={96} lines={5} tone={ok ? "green" : "red"} mark={ok ? "check" : "x"} />
              </div>
              <div style={{width: 22, height: 22, borderRadius: 99, background: ok ? C.green : C.red, marginTop: 38, boxShadow: "0 0 0 6px #fff"}} />
              <div style={{fontSize: 26, fontWeight: 700, color: C.ink2, marginTop: 14}}>Lần {k + 1}</div>
            </div>
          );
        })}
        {(() => {
          const s = sp(frame, at(2, "sau"));
          return (
            <div style={{position: "absolute", left: 1080 - 40, top: 360, width: 420, opacity: s}}>
              <div style={{height: 22, borderRadius: "14px 14px 0 0", border: `4px solid ${C.amber}`, borderBottom: "none", clipPath: `inset(0 ${100 - 100 * s}% 0 0)`}} />
              <div style={{position: "absolute", left: "50%", top: -58, transform: "translateX(-50%)"}}>
                <Chip tone="amber" solid size={26}>
                  cặp sai → đúng
                </Chip>
              </div>
            </div>
          );
        })()}
      </Show>

      {/* L3–L5: the diff and the search for the smallest repair */}
      <Show at={b(3)} out={b(6) - 8} dy={20}>
        <Card pad={0} radius={28} style={{position: "absolute", left: 170, top: 286, width: 860, height: 520, overflow: "hidden"}}>
          <div style={{display: "flex", alignItems: "center", gap: 14, padding: "22px 30px", borderBottom: `1px solid ${C.soft}`}}>
            <Chip tone="red" size={22}>
              Lần 3 · sai
            </Chip>
            <Icon name="arrowRight" size={26} color={C.ink3} />
            <Chip tone="green" size={22}>
              Lần 4 · đúng
            </Chip>
            <div style={{marginLeft: "auto", fontSize: 22, color: C.ink3, fontWeight: 600}}>những gì bạn ấy đã sửa</div>
          </div>
        </Card>
        {DIFF.map((l, i) => {
          const y = DIFF_TOP + i * LINE_H;
          const s = interpolate(frame, [b(3) + 6 + i * 4, b(3) + 16 + i * 4], [0, 1], clamp);
          const gone = l.hunk === "A" ? removedA : l.hunk === "C" ? removedC : 0;
          const flash = l.hunk === "B" ? flashB : 0;
          const bg = l.kind === "+" ? C.greenSoft : l.kind === "-" ? C.redSoft : "transparent";
          return (
            <div
              key={i}
              style={{
                position: "absolute",
                left: 170,
                top: y,
                width: 860,
                height: LINE_H,
                display: "flex",
                alignItems: "center",
                gap: 18,
                padding: "0 30px",
                fontFamily: MONO,
                fontSize: 28,
                background: flash ? "#F7D5D2" : bg,
                opacity: s * (1 - 0.75 * gone),
                clipPath: `inset(0 ${100 - 100 * s}% 0 0)`,
              }}
            >
              <span style={{width: 18, color: l.kind === "+" ? C.green : l.kind === "-" ? C.red : C.ink3}}>{l.kind === "-" ? "−" : l.kind}</span>
              <span style={{whiteSpace: "pre", textDecoration: gone > 0.5 ? "line-through" : "none", color: C.ink}}>{l.text}</span>
              {l.hunk && DIFF.findIndex((d) => d.hunk === l.hunk) === i ? (
                <span
                  style={{
                    marginLeft: "auto",
                    width: 36,
                    height: 36,
                    borderRadius: 10,
                    background: l.hunk === "B" ? C.indigo : C.ink3,
                    color: "#fff",
                    display: "grid",
                    placeItems: "center",
                    fontFamily: MONO,
                    fontSize: 20,
                    opacity: sp(frame, at(3, "sửa")),
                  }}
                >
                  {l.hunk}
                </span>
              ) : null}
            </div>
          );
        })}
        {/* hunk labels (L4) */}
        {(
          [
            ["A", "Thêm ghi chú", 0],
            ["B", "Sửa điều kiện vòng lặp", 1],
            ["C", "Viết lại, cùng nghĩa", 2],
          ] as const
        ).map(([h, text, k]) => {
          const s = sp(frame, hunkLabels + k * 8);
          const gray = h !== "B" && frame >= irrelevant ? sp(frame, irrelevant + k * 4) : 0;
          const out = interpolate(frame, [b(5) - 8, b(5)], [1, 0], clamp);
          const y = HUNK_Y[h] + (HUNK_ROWS[h] * LINE_H) / 2;
          return (
            <div key={h} style={{position: "absolute", left: 1060, top: y, transform: `translateY(-50%) translateX(${(1 - s) * -20}px)`, opacity: s * out, display: "flex", alignItems: "center", gap: 14}}>
              <div style={{width: 14, height: 3, background: C.line}} />
              <Chip tone={h === "B" ? "indigo" : "neutral"} size={26}>
                {text}
              </Chip>
              {gray > 0.01 ? (
                <div style={{opacity: gray, fontSize: 24, fontWeight: 700, color: C.ink3, whiteSpace: "nowrap"}}>chẳng liên quan</div>
              ) : null}
            </div>
          );
        })}
        {/* the search (L5) */}
        <Show at={b(5) - 2}>
          <Card pad={30} radius={28} style={{position: "absolute", left: 1070, top: 286, width: 680, height: 520}}>
            <div style={{fontSize: 22, fontWeight: 700, letterSpacing: "0.07em", textTransform: "uppercase", color: C.ink3, marginBottom: 12}}>
              Máy thử bỏ từng chỗ sửa
            </div>
            {(
              [
                ["A", T1, true],
                ["C", T2, true],
                ["B", T3, false],
              ] as const
            ).map(([h, t, ok]) => {
              const s = sp(frame, t - 6);
              const running = frame >= t && frame < t + 24;
              const res = pop(frame, t + 24);
              return (
                <div key={h} style={{display: "flex", alignItems: "center", gap: 14, height: 88, borderBottom: `1px solid ${C.soft}`, opacity: s}}>
                  <div style={{fontSize: 28, fontWeight: 700, width: 104}}>Bỏ {h}</div>
                  <div style={{width: 42, height: 42, display: "grid", placeItems: "center", transform: running ? `rotate(${(frame - t) * -18}deg)` : undefined}}>
                    <Icon name="replay" size={32} color={running ? C.indigo : C.ink3} />
                  </div>
                  <div style={{fontSize: 24, color: C.ink2, fontWeight: 600, width: 104, whiteSpace: "nowrap"}}>chạy lại</div>
                  {res > 0.01 ? (
                    <div style={{display: "flex", alignItems: "center", gap: 10, transform: `scale(${0.6 + 0.4 * res})`, opacity: Math.min(1, res * 1.5), transformOrigin: "left center"}}>
                      <Chip tone={ok ? "green" : "red"} icon={ok ? "check" : "x"} size={24} solid>
                        {ok ? "vẫn đúng" : "sai"}
                      </Chip>
                      <div style={{fontSize: 24, fontWeight: 700, color: ok ? C.ink3 : C.indigo, whiteSpace: "nowrap"}}>{ok ? "→ bỏ luôn" : "→ giữ lại"}</div>
                    </div>
                  ) : null}
                </div>
              );
            })}
            {(() => {
              const s = pop(frame, done);
              return s > 0.01 ? (
                <div
                  style={{
                    marginTop: 26,
                    padding: "18px 22px",
                    borderRadius: 18,
                    background: C.indigoSoft,
                    boxShadow: `inset 0 0 0 2px ${C.indigo}55`,
                    transform: `scale(${0.7 + 0.3 * s})`,
                    opacity: Math.min(1, s * 1.5),
                  }}
                >
                  <div style={{fontSize: 22, fontWeight: 700, color: C.indigoDeep, marginBottom: 6}}>Chỗ sửa nhỏ nhất</div>
                  <div style={{fontFamily: MONO, fontSize: 26}}>
                    i &lt; n <span style={{color: C.ink3}}>→</span> i &lt;= n
                  </div>
                </div>
              ) : null;
            })()}
          </Card>
        </Show>
      </Show>

      {/* L6: Lego tower */}
      <Show at={legoIn} out={b(7) - 8} dy={20}>
        <Show at={at(6, "delta")}>
          <div style={{position: "absolute", left: 0, right: 0, top: 248, display: "flex", justifyContent: "center"}}>
            <Chip tone="indigo" solid size={32} icon="search">
              Delta debugging
            </Chip>
          </div>
        </Show>
        <div style={{position: "absolute", left: 470, top: 0}}>
          {BRICKS.map((tone, k) => {
            const y = 760 - (k + 1) * 64;
            const s = sp(frame, legoIn + k * 5);
            const misplaced = k === 2;
            const off = misplaced ? 76 * (1 - fixT) : 0;
            const rot = misplaced ? 7 * (1 - fixT) : 0;
            const lean = k > 2 ? 5 * (1 - fixT) : 0;
            return (
              <div
                key={k}
                style={{
                  position: "absolute",
                  left: off + (k > 2 ? (k - 2) * 26 * (1 - fixT) : 0),
                  top: y - (1 - s) * 80,
                  opacity: s,
                  transform: `rotate(${rot + lean}deg)`,
                  transformOrigin: "0% 100%",
                }}
              >
                <Brick tone={tone} w={260} />
              </div>
            );
          })}
          <div style={{position: "absolute", left: -40, top: 760, width: 340, height: 12, borderRadius: 6, background: C.line}} />
          {scanT > 0 && scanT < 1 ? (
            <div style={{position: "absolute", left: 300, top: 360 + scanT * (760 - 3 * 64 - 360 + 10), transform: "translateY(-50%)"}}>
              <Icon name="search" size={64} color={C.ink} stroke={2.2} />
            </div>
          ) : null}
          {(() => {
            const s = pop(frame, at(6, "vững"));
            return s > 0.01 ? (
              <div style={{position: "absolute", left: 130, top: 292, transform: `translate(-50%, 0) scale(${0.6 + 0.4 * s})`, opacity: Math.min(1, s * 1.5)}}>
                <Chip tone="green" solid icon="check" size={30}>
                  Đứng vững!
                </Chip>
              </div>
            ) : null;
          })()}
        </div>
        <div style={{position: "absolute", left: 930, top: 390, display: "flex", flexDirection: "column", gap: 28}}>
          {[
            ["Viên Lego", "một chỗ sửa", at(6, "lego")],
            ["Tháp đứng vững", "bài chạy đúng mọi test", at(6, "vững") - 10],
            ["Tìm đúng viên", "chỗ sửa ít nhất mà bài vẫn đúng", fixAt],
          ].map(([a, bb, t]) => {
            const s = sp(frame, t as number);
            return (
              <div key={a as string} style={{display: "flex", alignItems: "center", gap: 18, opacity: s, transform: `translateX(${(1 - s) * 30}px)`}}>
                <div style={{fontSize: 32, fontWeight: 800, width: 260}}>{a}</div>
                <div style={{fontSize: 30, color: C.indigo, fontWeight: 700}}>=</div>
                <div style={{fontSize: 30, color: C.ink2, fontWeight: 600}}>{bb}</div>
              </div>
            );
          })}
        </div>
      </Show>

      {/* L7: twelve kinds of mistakes */}
      <Show at={b(7) - 2} out={b(8) - 8} dy={20}>
        {CATEGORIES.map(([name, hint], k) => {
          const col = k % 4;
          const row = Math.floor(k / 4);
          const s = pop(frame, b(7) + 2 + k * 2.5);
          const lit = k === 0 && flyT >= 1;
          return (
            <div
              key={name}
              style={{
                position: "absolute",
                left: 330 + col * 320,
                top: 318 + row * 152,
                width: 300,
                height: 136,
                borderRadius: 22,
                background: lit ? C.indigo : "#fff",
                color: lit ? "#fff" : C.ink,
                boxShadow: lit ? "0 16px 34px -16px rgba(63,81,181,0.9)" : `0 0 0 1px ${C.line}, 0 10px 24px -18px rgba(29,34,51,0.4)`,
                padding: "18px 22px",
                display: "flex",
                flexDirection: "column",
                justifyContent: "space-between",
                opacity: Math.min(1, s * 1.5),
                transform: `scale(${(0.7 + 0.3 * Math.min(1, s)) * (lit ? 1.04 : 1)})`,
              }}
            >
              <div style={{fontSize: 27, fontWeight: 700, lineHeight: 1.2}}>{name}</div>
              <div style={{fontFamily: MONO, fontSize: 19, color: lit ? "rgba(255,255,255,0.8)" : C.ink3}}>{hint}</div>
            </div>
          );
        })}
        {flyT > 0 && flyT < 1 ? (
          <div
            style={{
              position: "absolute",
              left: 960 + (480 - 960) * flyT,
              top: 250 + (386 - 250) * flyT - Math.sin(Math.PI * flyT) * 60,
              transform: `translate(-50%, -50%) scale(${1 - 0.4 * flyT})`,
              padding: "12px 22px",
              borderRadius: 16,
              background: "#fff",
              boxShadow: `0 0 0 2px ${C.indigo}, 0 14px 30px -14px rgba(29,34,51,0.5)`,
              fontFamily: MONO,
              fontSize: 26,
              whiteSpace: "nowrap",
            }}
          >
            i &lt; n → i &lt;= n
          </div>
        ) : null}
        <Show at={b(7) + 4}>
          <div style={{position: "absolute", left: 0, right: 0, top: 250, textAlign: "center", fontSize: 28, fontWeight: 700, color: C.ink2, opacity: flyT > 0 ? 1 - flyT : 1}}>
            12 loại lỗi
          </div>
        </Show>
      </Show>

      {/* L8: 339 verified answers */}
      <Show at={b(8) - 2} dy={20}>
        {(
          [
            [750, "lần sửa bài", "sai → đúng", b(8) + 2, "neutral"],
            [746, "cặp chạy lại khớp", "kiểm chứng tự động", b(8) + 18, "indigo"],
            [339, "đáp án một loại lỗi", "dùng để chấm cách gom", at(8, "339"), "green"],
          ] as const
        ).map(([n, label, sub, t, tone], k) => {
          const s = pop(frame, t);
          const x = 240 + k * 520;
          return (
            <React.Fragment key={label}>
              {k > 0 ? <Arrow x1={x - 92} y1={480} x2={x - 18} y2={480} t={interpolate(frame, [t - 10, t], [0, 1], clamp)} color={C.ink3} width={5} /> : null}
              <Card
                pad={34}
                radius={28}
                style={{
                  position: "absolute",
                  left: x,
                  top: 360,
                  width: 420,
                  opacity: Math.min(1, s * 1.5),
                  transform: `scale(${0.7 + 0.3 * Math.min(1, s)})`,
                  boxShadow: tone === "green" ? `0 0 0 3px ${C.green}, 0 24px 50px -24px rgba(29,34,51,0.45)` : undefined,
                }}
              >
                <Counter to={n} at={t} dur={30} style={{fontSize: 96, fontWeight: 800, letterSpacing: "-0.03em", color: TONE[tone].solid === C.ink3 ? C.ink : TONE[tone].solid}} />
                <div style={{fontSize: 30, fontWeight: 700, marginTop: 4}}>{label}</div>
                <div style={{fontSize: 24, color: C.ink2, fontWeight: 500, marginTop: 4}}>{sub}</div>
              </Card>
            </React.Fragment>
          );
        })}
        <div style={{position: "absolute", left: 0, right: 0, top: 660, display: "flex", justifyContent: "center", gap: 24}}>
          <Show at={at(8, "kiểm")}>
            <Chip tone="green" icon="replay" size={28}>
              Cái nào cũng chạy lại để kiểm chứng
            </Chip>
          </Show>
          <Show at={at(8, "kiểm") + 16}>
            <Chip tone="neutral" size={28}>
              406 ca sửa nhiều loại lỗi cùng lúc: để riêng
            </Chip>
          </Show>
        </div>
      </Show>
      <Illustrative x={170} y={818} at={b(3)} text={frame < b(6) - 8 ? "Minh họa" : ""} />
    </SceneFrame>
  );
};

export const repairPops = (scene: Scene) => {
  const {b, at} = beats(scene);
  const T1 = b(5) + 12;
  return [at(2, "đúng"), T1 + 24, T1 + 76, T1 + 128, T1 + 154, at(6, "vững"), at(7, "xếp") + 30, at(8, "339")];
};
