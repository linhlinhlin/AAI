import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {clamp, pop, sp} from "../anim";
import {SceneFrame} from "../components/frame";
import {Icon} from "../components/Icon";
import {Arrow, Card, Chip, Counter, Show, TestTile, Tone, TONE} from "../components/ui";
import {C, FONT, MONO} from "../theme";
import {beats, Scene} from "../timeline";

type Seg = {text: string; mark?: "amber" | "red" | "violet" | "indigo"};
type Item = {
  name: string;
  printed: Seg[];
  expected: Seg[];
  newline?: boolean;
  del: Seg[];
  add: Seg[];
  tag: string;
  tone: Tone;
  category: string;
};

// lab02-ex09 in C-Pack-IPAs: three submissions with the same four failed tests
// (paper/data/motivating_example.json).
const ITEMS: Item[] = [
  {
    name: "Bài A",
    printed: [{text: "00:01:00"}],
    expected: [{text: "00:01:00"}],
    newline: true,
    del: [{text: 'printf("%02d:%02d:%02d", …);'}],
    add: [{text: 'printf("%02d:%02d:%02d'}, {text: "\\n", mark: "amber"}, {text: '", …);'}],
    tag: "Quên xuống dòng",
    tone: "amber",
    category: "Văn bản in ra",
  },
  {
    name: "Bài B",
    printed: [{text: "0:1:0"}],
    expected: [{text: "0", mark: "violet"}, {text: "0:"}, {text: "0", mark: "violet"}, {text: "1:"}, {text: "0", mark: "violet"}, {text: "0"}],
    del: [{text: 'printf("%d:%d:%d\\n", h,m,s);'}],
    add: [{text: 'printf("%'}, {text: "02", mark: "violet"}, {text: "d:%"}, {text: "02", mark: "violet"}, {text: "d:%"}, {text: "02", mark: "violet"}, {text: 'd\\n", h,m,s);'}],
    tag: "Thiếu số 0 đứng trước",
    tone: "violet",
    category: "Định dạng in",
  },
  {
    name: "Bài C",
    printed: [{text: "60", mark: "red"}, {text: ":00:00"}],
    expected: [{text: "00:01:00"}],
    del: [{text: "horas = n / 60 * 60;"}],
    add: [{text: "horas = n / "}, {text: "(", mark: "indigo"}, {text: "60 * 60"}, {text: ")", mark: "indigo"}, {text: ";"}],
    tag: "Thiếu cặp ngoặc",
    tone: "indigo",
    category: "Biểu thức tính toán",
  },
];

const MARK: Record<string, string> = {amber: C.amberSoft, red: C.redSoft, violet: C.violetSoft, indigo: C.indigoSoft};
const MARK_FG: Record<string, string> = {amber: "#95600F", red: "#A8322C", violet: "#5A3DAE", indigo: C.indigoDeep};

const Segs: React.FC<{segs: Seg[]; lit: number}> = ({segs, lit}) => (
  <>
    {segs.map((s, i) => (
      <span
        key={i}
        style={
          s.mark
            ? {
                background: lit > 0 ? MARK[s.mark] : "transparent",
                color: lit > 0 ? MARK_FG[s.mark] : undefined,
                borderRadius: 6,
                boxShadow: lit > 0 ? `0 0 0 ${2 * lit}px ${MARK_FG[s.mark]}55` : undefined,
              }
            : undefined
        }
      >
        {s.text}
      </span>
    ))}
  </>
);

const Field: React.FC<{label: string; children: React.ReactNode}> = ({label, children}) => (
  <div>
    <div style={{fontSize: 19, fontWeight: 700, letterSpacing: "0.07em", textTransform: "uppercase", color: C.ink3, marginBottom: 6}}>{label}</div>
    <div
      style={{
        height: 60,
        borderRadius: 14,
        background: C.soft,
        display: "flex",
        alignItems: "center",
        padding: "0 18px",
        fontFamily: MONO,
        fontSize: 34,
        fontWeight: 600,
        gap: 6,
      }}
    >
      {children}
    </div>
  </div>
);

const EqualSign: React.FC<{not?: boolean; t: number; color: string}> = ({not, t, color}) => (
  <svg width="64" height="64" viewBox="0 0 64 64" style={{transform: `scale(${0.4 + 0.6 * t})`, opacity: Math.min(1, t * 1.5)}}>
    <rect x="10" y="20" width="44" height="7" rx="3.5" fill={color} />
    <rect x="10" y="37" width="44" height="7" rx="3.5" fill={color} />
    {not ? <rect x="29" y="6" width="7" height="52" rx="3.5" fill={color} transform="rotate(30 32 32)" /> : null}
  </svg>
);

export const Example: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {b, at} = beats(scene);
  const n89 = at(2, "89");
  const n78 = at(2, "78");
  const cardsAt = at(2, "tấm");
  const focusAt = [b(3), b(4), b(5)];
  const allAt = b(6);
  const sameAt = at(6, "cùng");
  const diffAt = at(6, "khác");

  return (
    <SceneFrame scene={scene}>
      {/* L0: real data */}
      <Show at={b(0) + 4} out={b(1) - 8} dy={24}>
        <Card pad={40} radius={30} style={{position: "absolute", left: 460, top: 300, width: 1000, display: "flex", gap: 34, alignItems: "center"}}>
          <div style={{width: 150, height: 150, borderRadius: 40, background: C.greenSoft, display: "grid", placeItems: "center", flex: "none"}}>
            <Icon name="users" size={82} color={C.green} />
          </div>
          <div>
            <Chip tone="green" icon="check" size={24}>
              Dữ liệu thật, đã ẩn danh
            </Chip>
            <div style={{fontSize: 56, fontWeight: 800, marginTop: 14, letterSpacing: "-0.02em"}}>C-Pack-IPAs</div>
            <div style={{fontSize: 27, color: C.ink2, marginTop: 4, fontWeight: 500}}>bài nộp thật của một khóa học lập trình C</div>
          </div>
        </Card>
        <div style={{position: "absolute", left: 0, right: 0, top: 574, display: "flex", justifyContent: "center", gap: 26}}>
          {(
            [
              [8607, "bài nộp"],
              [246, "sinh viên"],
              [25, "bài tập"],
            ] as const
          ).map(([n, label], k) => {
            const s = pop(frame, b(0) + 16 + k * 7);
            return (
              <Card key={label} pad={26} radius={24} style={{width: 316, textAlign: "center", opacity: Math.min(1, s * 1.5), transform: `translateY(${(1 - Math.min(1, s)) * 30}px)`}}>
                <Counter to={n} at={b(0) + 16 + k * 7} dur={36} style={{fontSize: 60, fontWeight: 800, letterSpacing: "-0.03em", color: C.ink}} />
                <div style={{fontSize: 26, color: C.ink2, fontWeight: 600}}>{label}</div>
              </Card>
            );
          })}
        </div>
      </Show>

      {/* L1: the task */}
      <Show at={b(1)} out={b(2) - 6} dy={24}>
        <Card pad={44} radius={30} style={{position: "absolute", left: 420, top: 290, width: 1080}}>
          <div style={{display: "flex", justifyContent: "space-between", alignItems: "center"}}>
            <div style={{fontSize: 20, fontWeight: 700, letterSpacing: "0.08em", textTransform: "uppercase", color: C.ink3}}>Đề bài · lab02-ex09</div>
            <Chip tone="neutral" size={22}>
              4 test
            </Chip>
          </div>
          <div style={{fontSize: 40, fontWeight: 800, marginTop: 10}}>Đổi số giây thành giờ : phút : giây</div>
          <div style={{display: "flex", alignItems: "center", gap: 40, marginTop: 40}}>
            {[
              ["60", "giây", at(1, "60"), C.soft],
              ["00:01:00", "giờ:phút:giây", at(1, "00:01:00"), C.greenSoft],
            ].map(([v, l, t, bg], i) => {
              const s = pop(frame, t as number);
              return (
                <React.Fragment key={i}>
                  {i === 1 ? (
                    <div style={{width: 90, height: 40, position: "relative"}}>
                      <Arrow x1={0} y1={20} x2={86} y2={20} t={interpolate(frame, [(t as number) - 10, t as number], [0, 1], clamp)} color={C.ink3} width={5} />
                    </div>
                  ) : null}
                  <div style={{display: "flex", flexDirection: "column", alignItems: "center", gap: 10, opacity: Math.min(1, s * 1.5), transform: `scale(${0.7 + 0.3 * s})`}}>
                    <div style={{fontFamily: MONO, fontSize: 76, fontWeight: 600, padding: "10px 34px", borderRadius: 22, background: bg as string}}>{v}</div>
                    <div style={{fontSize: 24, color: C.ink2, fontWeight: 600}}>{l}</div>
                  </div>
                </React.Fragment>
              );
            })}
          </div>
        </Card>
      </Show>

      {/* L2: 89 wrong, 78 with the same record */}
      <Show at={n89 - 6} out={cardsAt - 10} dy={20}>
        <div style={{position: "absolute", left: 300, top: 330, display: "grid", gridTemplateColumns: "repeat(13, 34px)", gap: 8}}>
          {Array.from({length: 89}, (_, i) => {
            const s = pop(frame, n89 + i * 0.3);
            const all = i < 78 && frame >= n78 + i * 0.35;
            return (
              <div
                key={i}
                style={{
                  width: 34,
                  height: 34,
                  borderRadius: 9,
                  background: all ? C.red : C.redSoft,
                  opacity: Math.min(1, s * 1.5),
                  transform: `scale(${0.5 + 0.5 * Math.min(1, s)})`,
                  display: "grid",
                  placeItems: "center",
                }}
              >
                {all ? <Icon name="x" size={18} color="#fff" stroke={3} /> : null}
              </div>
            );
          })}
        </div>
        <div style={{position: "absolute", left: 960, top: 320}}>
          <div style={{display: "flex", alignItems: "baseline", gap: 18}}>
            <Counter to={89} at={n89} dur={24} style={{fontSize: 110, fontWeight: 800, color: C.ink, letterSpacing: "-0.03em"}} />
            <div style={{fontSize: 34, fontWeight: 700, color: C.ink2}}>bài sai</div>
          </div>
          <div style={{display: "flex", alignItems: "baseline", gap: 18, opacity: sp(frame, n78)}}>
            <Counter to={78} at={n78} dur={24} style={{fontSize: 110, fontWeight: 800, color: C.red, letterSpacing: "-0.03em"}} />
            <div style={{fontSize: 34, fontWeight: 700, color: C.ink2}}>trượt cả 4 test</div>
          </div>
          <div style={{display: "flex", gap: 10, marginTop: 12, opacity: sp(frame, n78 + 8)}}>
            {[0, 1, 2, 3].map((i) => (
              <TestTile key={i} ok={false} size={48} />
            ))}
          </div>
        </div>
      </Show>

      {/* L2–L6: three cards with one record and three different fixes */}
      {ITEMS.map((it, k) => {
        const x = 215 + k * 520;
        const s = pop(frame, cardsAt + k * 6);
        if (s < 0.01) return null;
        const focus = frame >= focusAt[k] - 4;
        const reveal = sp(frame, focusAt[k]);
        const isFocus = frame >= focusAt[k] - 4 && frame < (focusAt[k + 1] ?? allAt) - 4;
        const anyFocus = frame >= focusAt[0] - 4 && frame < allAt - 4;
        const dim = anyFocus && !isFocus ? 0.5 : 1;
        const lift = isFocus ? sp(frame, focusAt[k] - 4) : 0;
        const lit = frame >= focusAt[k] + 12 ? 1 : 0;
        const tag = pop(frame, focusAt[k] + 30);
        const cat = pop(frame, diffAt + k * 6);
        return (
          <Card
            key={it.name}
            pad={26}
            radius={28}
            style={{
              position: "absolute",
              left: x,
              top: 296,
              width: 450,
              height: 452,
              opacity: Math.min(1, s * 1.5) * dim,
              transform: `translateY(${(1 - Math.min(1, s)) * 40 - lift * 8}px) scale(${1 + 0.02 * lift})`,
              boxShadow: isFocus ? `0 0 0 3px ${TONE[it.tone].solid}, 0 24px 50px -24px rgba(29,34,51,0.45)` : undefined,
              display: "flex",
              flexDirection: "column",
              gap: 14,
            }}
          >
            <div style={{display: "flex", alignItems: "center", justifyContent: "space-between"}}>
              <div style={{fontSize: 34, fontWeight: 800}}>{it.name}</div>
              <div style={{display: "flex", gap: 7}}>
                {[0, 1, 2, 3].map((i) => (
                  <TestTile key={i} ok={false} size={36} />
                ))}
              </div>
            </div>
            <div style={{opacity: focus ? reveal : 0, display: "flex", flexDirection: "column", gap: 12}}>
              <Field label="Chương trình in ra">
                <Segs segs={it.printed} lit={lit} />
              </Field>
              <Field label="Đáp án đúng">
                <Segs segs={it.expected} lit={lit} />
                {it.newline ? (
                  <span
                    style={{
                      display: "inline-grid",
                      placeItems: "center",
                      width: 40,
                      height: 40,
                      borderRadius: 8,
                      background: lit ? C.amberSoft : "transparent",
                      boxShadow: lit ? `0 0 0 2px ${MARK_FG.amber}55` : undefined,
                    }}
                  >
                    <Icon name="enter" size={26} color={lit ? MARK_FG.amber : C.ink3} stroke={2.6} />
                  </span>
                ) : null}
              </Field>
              <div style={{fontFamily: MONO, fontSize: 16, lineHeight: 1.75, borderRadius: 12, overflow: "hidden", boxShadow: `inset 0 0 0 1px ${C.line}`}}>
                <div style={{background: C.redSoft, padding: "2px 12px", whiteSpace: "pre", color: C.ink}}>
                  <span style={{color: C.red}}>− </span>
                  {it.del.map((sg) => sg.text).join("")}
                </div>
                <div style={{background: C.greenSoft, padding: "2px 12px", whiteSpace: "pre", color: C.ink}}>
                  <span style={{color: C.green}}>+ </span>
                  <Segs segs={it.add} lit={lit} />
                </div>
              </div>
            </div>
            <div style={{marginTop: "auto", display: "flex", justifyContent: "center", height: 46}}>
              {cat > 0.01 ? (
                <div style={{transform: `scale(${0.6 + 0.4 * cat})`, opacity: Math.min(1, cat * 1.5)}}>
                  <Chip tone={it.tone} solid size={24}>
                    {it.category}
                  </Chip>
                </div>
              ) : tag > 0.01 ? (
                <div style={{transform: `scale(${0.6 + 0.4 * tag})`, opacity: Math.min(1, tag * 1.5)}}>
                  <Chip tone={it.tone} size={24}>
                    {it.tag}
                  </Chip>
                </div>
              ) : null}
            </div>
          </Card>
        );
      })}

      {/* L6: same record, different mistakes */}
      {[0, 1].map((k) => (
        <React.Fragment key={k}>
          <div style={{position: "absolute", left: 700 + k * 520, top: 318, transform: "translateX(-50%)"}}>
            <EqualSign t={pop(frame, sameAt + k * 5)} color={C.red} />
          </div>
          <div style={{position: "absolute", left: 700 + k * 520, top: 668, transform: "translateX(-50%)"}}>
            <EqualSign not t={pop(frame, diffAt + 10 + k * 5)} color={C.indigo} />
          </div>
        </React.Fragment>
      ))}
      <Show at={sameAt} dy={10}>
        <div style={{position: "absolute", left: 0, right: 0, top: 772, textAlign: "center", fontFamily: FONT, fontSize: 30, fontWeight: 700}}>
          <span style={{color: C.red}}>Cùng một tấm phiếu</span>
          <span style={{color: C.ink3}}> · </span>
          <span style={{color: C.indigo, opacity: sp(frame, diffAt)}}>ba loại lỗi khác nhau</span>
        </div>
      </Show>
    </SceneFrame>
  );
};

export const examplePops = (scene: Scene) => {
  const {b, at} = beats(scene);
  return [at(1, "00:01:00"), at(2, "78"), at(2, "tấm"), b(3) + 30, b(4) + 30, b(5) + 30, at(6, "khác")];
};
