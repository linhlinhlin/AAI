import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {clamp, EASE, pop, rand, sp, vi} from "../anim";
import {Illustrative, SceneFrame} from "../components/frame";
import {Donut, VBar} from "../components/charts";
import {Tabs} from "../components/Tabs";
import {Card, Chip, Show} from "../components/ui";
import {C, GROUP, MONO} from "../theme";
import {beats, Scene} from "../timeline";

// Registered test-run results: research/runs/mechanism-v1.1-test/summary.md and categories.md.
const grow = (frame: number, at: number, dur = 36) => interpolate(frame, [at, at + dur], [0, 1], {...clamp, easing: EASE});

const CeilingBar: React.FC<{label: string; sub: string; value: number; ci: string; at: number; show: number; color: string; y: number}> = ({
  label,
  sub,
  value,
  ci,
  at,
  show,
  color,
  y,
}) => {
  const frame = useCurrentFrame();
  const g = grow(frame, at, 40);
  return (
    <div style={{position: "absolute", left: 150, top: y, display: "flex", alignItems: "center", gap: 30, opacity: sp(frame, show)}}>
      <div style={{width: 360, textAlign: "right"}}>
        <div style={{fontSize: 32, fontWeight: 800}}>{label}</div>
        <div style={{fontSize: 22, color: C.ink2, fontWeight: 600}}>{sub}</div>
      </div>
      <div style={{position: "relative", width: 1000, height: 64}}>
        <div style={{position: "absolute", inset: 0, borderRadius: 32, background: "repeating-linear-gradient(135deg, #F1E3E2 0 12px, #F8EEED 12px 24px)"}} />
        <div style={{position: "absolute", left: 0, top: 0, bottom: 0, width: `${value * 100 * g}%`, borderRadius: 32, background: color}} />
        <div style={{position: "absolute", left: `${value * 100 * g}%`, top: "50%", transform: "translate(16px, -50%)", fontSize: 44, fontWeight: 800, color: C.ink, fontVariantNumeric: "tabular-nums", opacity: g > 0 ? 1 : 0, whiteSpace: "nowrap"}}>
          {vi(value * 100 * g, 1)}%
        </div>
        <div style={{position: "absolute", left: 0, top: 76, fontFamily: MONO, fontSize: 19, color: C.ink3, opacity: sp(frame, at + 30), whiteSpace: "nowrap"}}>{ci}</div>
      </div>
    </div>
  );
};

// Cluster centres relative to the plot card (900 × 600 at 150, 262).
const CLUSTERS = [
  {x: 200, y: 190},
  {x: 470, y: 150},
  {x: 720, y: 270},
  {x: 290, y: 420},
  {x: 610, y: 450},
];

const Marker: React.FC<{shape: number; color: string; size: number}> = ({shape, color, size}) => {
  if (shape === 0) return <div style={{width: size, height: size, borderRadius: 99, background: color, boxShadow: "0 0 0 2px #fff"}} />;
  if (shape === 1) return <div style={{width: size * 0.9, height: size * 0.9, borderRadius: 4, background: color, boxShadow: "0 0 0 2px #fff"}} />;
  return (
    <svg width={size} height={size} viewBox="0 0 20 20" style={{overflow: "visible"}}>
      <path d="M10 1 19 18H1z" fill={color} stroke="#fff" strokeWidth={2} strokeLinejoin="round" />
    </svg>
  );
};

export const Results: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {b, at} = beats(scene);
  const active = frame < b(1) ? -1 : frame < b(3) ? 0 : frame < b(5) ? 1 : frame < b(6) ? 2 : 3;
  const r74 = at(1, "74%");
  const r51 = at(1, "51%");
  const d35 = at(2, "35%");
  const d82 = at(2, "82%");
  const aInj = at(3, "0,09");
  const aDev = at(3, "0,33");
  const aReal = at(4, "0,29");
  const aReal2 = at(4, "0,35");
  const notSure = at(4, "chưa");
  const f1 = at(5, "0,35");
  const f0 = at(5, "luật", 1);
  const embAt = b(6) + 4;
  const byProgram = at(6, "chương");
  const notByError = at(6, "lỗi");

  return (
    <SceneFrame scene={scene}>
      <Tabs labels={["Trần", "Điểm ARI", "Luật NẾU⁠–⁠THÌ", "Mô hình AI đọc code"]} active={active} at={[16, 21, 26, 31]} />

      {/* L0 */}
      <Show at={20} out={b(1) - 8} dy={16}>
        <div style={{position: "absolute", left: 0, right: 0, top: 400, display: "flex", flexDirection: "column", alignItems: "center", gap: 20}}>
          <div style={{fontSize: 64, fontWeight: 800, letterSpacing: "-0.02em"}}>4 kết quả chính</div>
          <Chip tone="green" icon="lock" size={28}>
            đo trên phần dữ liệu niêm phong, mở đúng một lần
          </Chip>
        </div>
      </Show>

      {/* L1: ceilings */}
      <Show at={b(1)} out={b(2) - 8} dy={20}>
        <div style={{position: "absolute", left: 0, right: 0, top: 268, textAlign: "center", fontSize: 28, fontWeight: 700, color: C.ink2}}>
          Chỉ nhìn kết quả test thì xếp đúng được tối đa bao nhiêu bài?
        </div>
        <CeilingBar label="Bài thật" sub="339 đáp án thật" value={0.739} ci="khoảng tin cậy 95%: 69,6% – 78,3%" at={r74} show={b(1) + 4} color={C.indigo} y={380} />
        <CeilingBar label="Bài hỏng có chủ đích" sub="3.320 bài" value={0.507} ci="khoảng tin cậy 95%: 42,9% – 58,8%" at={r51} show={b(1) + 10} color={C.violet} y={560} />
        <Show at={r51 + 40}>
          <div style={{position: "absolute", left: 540, top: 720, display: "flex", alignItems: "center", gap: 12}}>
            <div style={{width: 40, height: 22, borderRadius: 11, background: "repeating-linear-gradient(135deg, #F1E3E2 0 8px, #F8EEED 8px 16px)", boxShadow: "inset 0 0 0 1px #E9CFCD"}} />
            <div style={{fontSize: 23, fontWeight: 600, color: C.ink2}}>phần không thể xếp đúng, dù thuật toán giỏi đến đâu</div>
          </div>
        </Show>
      </Show>

      {/* L2: collisions */}
      <Show at={b(2)} out={b(3) - 8} dy={20}>
        <div style={{position: "absolute", left: 0, right: 0, top: 268, textAlign: "center", fontSize: 28, fontWeight: 700, color: C.ink2}}>
          Các cặp bài có phiếu giống hệt nhau: bao nhiêu cặp thật ra sai vì lý do khác?
        </div>
        {[
          [0.355, d35, "Bài thật", "740 trên 2.087 cặp", C.indigo, 480],
          [0.816, d82, "Bài hỏng có chủ đích", "2.367 trên 2.901 cặp", C.violet, 1100],
        ].map(([v, t, label, sub, color, x], k) => (
          <div key={label as string} style={{position: "absolute", left: x as number, top: 340, width: 340, display: "flex", flexDirection: "column", alignItems: "center", opacity: sp(frame, b(2) + 4 + k * 6)}}>
            <Donut value={v as number} at={t as number} size={320} color={color as string} digits={1} thickness={34} />
            <div style={{fontSize: 32, fontWeight: 800, marginTop: 18}}>{label as string}</div>
            <div style={{fontSize: 23, color: C.ink2, fontWeight: 600}}>{sub as string}</div>
          </div>
        ))}
      </Show>

      {/* L3–L4: ARI */}
      <Show at={b(3)} out={b(5) - 8} dy={20}>
        <Card pad={30} radius={30} style={{position: "absolute", left: 150, top: 262, width: 780, height: 610}}>
          <div style={{fontSize: 28, fontWeight: 800}}>Bài hỏng có chủ đích</div>
          <div style={{fontSize: 22, color: C.ink2, fontWeight: 600}}>dữ liệu có kiểm soát</div>
          <div style={{display: "flex", justifyContent: "center", gap: 20, marginTop: 10}}>
            <VBar value={0.093} max={0.4} at={aInj} height={300} color="#C5CAD9" label={<>Chỉ kết quả test</>} />
            <VBar value={0.328} max={0.4} at={aDev} height={300} color={C.indigo} label={<>Thêm OAV độ lệch</>} />
          </div>
          <div style={{display: "flex", flexDirection: "column", alignItems: "center", gap: 10, marginTop: 14, opacity: sp(frame, aDev + 26)}}>
            <Chip tone="green" solid icon="check" size={23}>
              Tăng rõ, gấp hơn 3 lần
            </Chip>
            <div style={{fontFamily: MONO, fontSize: 18, color: C.ink3}}>mức tăng 0,24 · khoảng tin cậy 95%: 0,14 – 0,33</div>
          </div>
        </Card>
        <Card pad={30} radius={30} style={{position: "absolute", left: 990, top: 262, width: 780, height: 610, opacity: sp(frame, aReal - 10)}}>
          <div style={{fontSize: 28, fontWeight: 800}}>Bài thật</div>
          <div style={{fontSize: 22, color: C.ink2, fontWeight: 600}}>339 đáp án thật</div>
          <div style={{display: "flex", justifyContent: "center", gap: 20, marginTop: 10}}>
            <VBar value={0.292} max={0.4} at={aReal} height={300} color="#C5CAD9" label={<>Chỉ kết quả test</>} />
            <VBar value={0.345} max={0.4} at={aReal2} height={300} color="#9FA8DA" label={<>Thêm OAV độ lệch</>} />
          </div>
          <div style={{display: "flex", flexDirection: "column", alignItems: "center", gap: 10, marginTop: 14, opacity: sp(frame, notSure)}}>
            <Chip tone="amber" solid icon="alert" size={23}>
              Có tăng, nhưng chưa đủ chắc chắn
            </Chip>
            <div style={{fontFamily: MONO, fontSize: 18, color: C.ink3}}>khoảng tin cậy 95% của mức tăng: −0,08 – 0,18</div>
          </div>
        </Card>
      </Show>

      {/* L5: IF–THEN rules on unseen problems */}
      <Show at={b(5)} out={b(6) - 8} dy={20}>
        <div style={{position: "absolute", left: 0, right: 0, top: 262, textAlign: "center"}}>
          <div style={{fontSize: 30, fontWeight: 800}}>Luật NẾU–THÌ trên bài tập mới, chưa gặp khi học</div>
          <div style={{fontSize: 23, color: C.ink2, fontWeight: 600, marginTop: 4}}>bài hỏng có chủ đích · điểm F1 (0 là tệ nhất, 1 là tốt nhất)</div>
        </div>
        {(
          [
            ["Luật từ OAV độ lệch", "ILA-2", 0.35, f1, C.indigo],
            ["Luật chỉ từ kết quả test", "ILA-2", 0.039, f0, "#C5CAD9"],
            ["Cây quyết định từ độ lệch", "CART, để so sánh", 0.402, f0 + 60, "#9FA8DA"],
          ] as const
        ).map(([label, sub, v, t, color], k) => {
          const g = grow(frame, t, 34);
          return (
            <div key={label} style={{position: "absolute", left: 150, top: 400 + k * 130, display: "flex", alignItems: "center", gap: 30, opacity: sp(frame, k < 2 ? b(5) + 4 + k * 6 : t - 8)}}>
              <div style={{width: 470, textAlign: "right"}}>
                <div style={{fontSize: 30, fontWeight: 800}}>{label}</div>
                <div style={{fontSize: 21, color: C.ink2, fontWeight: 600}}>{sub}</div>
              </div>
              <div style={{position: "relative", width: 900, height: 56}}>
                <div style={{position: "absolute", inset: 0, borderRadius: 28, background: "#E7EAF2"}} />
                <div style={{position: "absolute", left: 0, top: 0, bottom: 0, width: Math.max(56, (v / 0.5) * 900 * g), borderRadius: 28, background: color}} />
                <div style={{position: "absolute", left: Math.max(56, (v / 0.5) * 900 * g), top: "50%", transform: "translate(16px, -50%)", fontFamily: MONO, fontSize: 40, fontWeight: 600, whiteSpace: "nowrap", opacity: g > 0 ? 1 : 0}}>
                  {vi(v * g, 2)}
                </div>
              </div>
            </div>
          );
        })}
        <Show at={f0 + 40}>
          <div style={{position: "absolute", left: 650, top: 800, fontSize: 21, color: C.ink3, fontWeight: 600}}>
            Trên bài thật, luật từ độ lệch cũng nhỉnh hơn, nhưng chưa đủ chắc chắn.
          </div>
        </Show>
      </Show>

      {/* L6: code embeddings group by author, not by mistake */}
      <Show at={b(6)} dy={20}>
        <Card pad={0} radius={30} style={{position: "absolute", left: 150, top: 262, width: 900, height: 600}}>
          <div style={{position: "absolute", left: 30, top: 24, fontSize: 24, fontWeight: 700, color: C.ink2}}>Mô hình AI đọc code: bài nào gần bài nào</div>
        </Card>
        {Array.from({length: 60}, (_, i) => {
          const c = i % 5;
          const cl = CLUSTERS[c];
          const ang = rand(i * 3.3 + 1) * Math.PI * 2;
          const rad = 20 + rand(i * 5.1 + 7) * 62;
          const s = pop(frame, embAt + i * 0.6);
          const colored = frame >= byProgram - 4;
          return (
            <div key={i} style={{position: "absolute", left: 150 + cl.x + Math.cos(ang) * rad - 11, top: 262 + cl.y + Math.sin(ang) * rad * 0.8 - 11, transform: `scale(${Math.min(1, s)})`, opacity: Math.min(1, s * 1.5)}}>
              <Marker shape={Math.floor(rand(i * 9.7 + 2) * 3)} color={colored ? GROUP[c] : C.ink3} size={22} />
            </div>
          );
        })}
        <Illustrative x={180} y={826} at={embAt} />
        <div style={{position: "absolute", left: 1110, top: 280, width: 660}}>
          <div style={{fontSize: 22, fontWeight: 700, color: C.ink3, letterSpacing: "0.07em", textTransform: "uppercase", marginBottom: 14, opacity: sp(frame, byProgram)}}>Chú thích</div>
          <div style={{display: "flex", alignItems: "center", gap: 14, opacity: sp(frame, byProgram)}}>
            <div style={{display: "flex", gap: 6}}>
              {GROUP.map((g) => (
                <div key={g} style={{width: 20, height: 20, borderRadius: 99, background: g}} />
              ))}
            </div>
            <div style={{fontSize: 26, fontWeight: 700}}>màu = chương trình gốc</div>
          </div>
          <div style={{display: "flex", alignItems: "center", gap: 14, marginTop: 12, opacity: sp(frame, notByError)}}>
            <div style={{display: "flex", gap: 8, alignItems: "center"}}>
              <Marker shape={0} color={C.ink2} size={20} />
              <Marker shape={1} color={C.ink2} size={20} />
              <Marker shape={2} color={C.ink2} size={20} />
            </div>
            <div style={{fontSize: 26, fontWeight: 700}}>hình = loại lỗi</div>
          </div>
          {[
            ["Gom theo chương trình gốc", 0.719, C.indigo, byProgram + 10],
            ["Gom theo loại lỗi", -0.115, C.red, notByError + 6],
          ].map(([label, v, color, t]) => {
            const g = grow(frame, t as number, 30);
            const w = Math.abs(v as number) * 520 * g;
            return (
              <div key={label as string} style={{marginTop: 34, opacity: sp(frame, (t as number) - 6)}}>
                <div style={{fontSize: 26, fontWeight: 700, color: C.ink2}}>{label as string} · điểm ARI</div>
                <div style={{display: "flex", alignItems: "center", gap: 16, marginTop: 10}}>
                  <div style={{width: 520, height: 40, borderRadius: 20, background: "#E7EAF2", position: "relative"}}>
                    <div style={{position: "absolute", left: 0, top: 0, bottom: 0, width: Math.max(8, w), borderRadius: 20, background: color as string}} />
                  </div>
                  <div style={{fontFamily: MONO, fontSize: 36, fontWeight: 600}}>{vi((v as number) * g, 2)}</div>
                </div>
              </div>
            );
          })}
          <div style={{marginTop: 34, opacity: sp(frame, notByError + 30)}}>
            <Chip tone="red" icon="alert" size={24}>
              Gom theo người viết, không theo lỗi
            </Chip>
          </div>
        </div>
      </Show>
    </SceneFrame>
  );
};

export const resultsPops = (scene: Scene) => {
  const {at} = beats(scene);
  return [at(1, "74%") + 40, at(1, "51%") + 40, at(3, "0,33") + 36, at(4, "chưa"), at(5, "0,35") + 34];
};
