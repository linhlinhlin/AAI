import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {clamp, EASE, pop, sp} from "../anim";
import {SceneFrame} from "../components/frame";
import {Icon, IconName} from "../components/Icon";
import {Card, Chip, Show} from "../components/ui";
import {C, MONO} from "../theme";
import {beats, Scene} from "../timeline";

const Line: React.FC<{at: number; lead: string; main: string; color: string; strike?: number; dim?: number; underline?: number}> = ({
  at,
  lead,
  main,
  color,
  strike = 0,
  dim = 0,
  underline = 0,
}) => {
  const frame = useCurrentFrame();
  const s = sp(frame, at);
  return (
    <div style={{display: "flex", alignItems: "baseline", justifyContent: "center", gap: 26, opacity: s * (1 - 0.55 * dim), transform: `translateY(${(1 - s) * 40}px)`}}>
      <div style={{fontSize: 46, fontWeight: 700, color: C.ink2}}>{lead}</div>
      <div style={{position: "relative", fontSize: 92, fontWeight: 800, letterSpacing: "-0.03em", color}}>
        {main}
        {strike > 0 ? <div style={{position: "absolute", left: -6, top: "54%", height: 10, width: `${strike * 103}%`, borderRadius: 5, background: C.red}} /> : null}
        {underline > 0 ? (
          <div style={{position: "absolute", left: 0, bottom: -4, height: 18, width: `${underline * 100}%`, borderRadius: 9, background: C.amber, opacity: 0.45, zIndex: -1}} />
        ) : null}
      </div>
    </div>
  );
};

export const Conclusion: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {b, at} = beats(scene);
  const askAt = at(1, "hãy");
  const strike = interpolate(frame, [askAt - 6, askAt + 8], [0, 1], {...clamp, easing: EASE});
  const underline = interpolate(frame, [at(1, "thế") - 4, at(1, "thế") + 16], [0, 1], {...clamp, easing: EASE});
  return (
    <SceneFrame scene={scene}>
      <Show at={b(0) + 2} dy={16}>
        <div style={{position: "absolute", left: 0, right: 0, top: 262, display: "flex", justifyContent: "center"}}>
          <Chip tone="amber" solid icon="bulb" size={30}>
            Bài học lớn nhất
          </Chip>
        </div>
      </Show>
      <div style={{position: "absolute", left: 0, right: 0, top: 370, display: "flex", flexDirection: "column", gap: 40}}>
        <Line at={b(1) + 2} lead="Đừng chỉ hỏi" main="bài có sai không?" color={C.ink} strike={strike} dim={strike} />
        <Line at={askAt} lead="Hãy hỏi" main="output sai thế nào?" color={C.indigo} underline={underline} />
      </div>
      <Show at={b(2)} dy={20}>
        <div style={{position: "absolute", left: 0, right: 0, top: 690, display: "flex", justifyContent: "center", alignItems: "center", gap: 18}}>
          <div style={{width: 64, height: 64, borderRadius: 20, background: C.indigo, display: "grid", placeItems: "center"}}>
            <Icon name="bot" size={38} color="#fff" />
          </div>
          <div style={{fontSize: 34, fontWeight: 700}}>Cải tiến rẻ nhất: dùng output máy chấm đã có sẵn</div>
        </div>
        <div style={{position: "absolute", left: 0, right: 0, top: 780, display: "flex", justifyContent: "center", gap: 18}}>
          {["Không cần thêm dữ liệu", "Không cần chấm tay"].map((t, k) => (
            <div key={t} style={{opacity: sp(frame, at(2, "sẵn") + k * 8), transform: `translateY(${(1 - sp(frame, at(2, "sẵn") + k * 8)) * 14}px)`}}>
              <Chip tone="green" icon="check" size={26}>
                {t}
              </Chip>
            </div>
          ))}
        </div>
      </Show>
    </SceneFrame>
  );
};

export const conclusionPops = (scene: Scene) => {
  const {at} = beats(scene);
  return [at(1, "hãy")];
};

export const Limits: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {b, at} = beats(scene);
  const limits: [IconName, string, string, number][] = [
    ["school", "Mới có 1 khóa học", "C-Pack-IPAs", at(2, "khóa")],
    ["code", "Mới có 1 ngôn ngữ", "ngôn ngữ C", at(2, "ngôn")],
    ["bot", "Nhãn mới được AI kiểm tra", "chưa có người chấm độc lập", at(2, "ai")],
  ];
  const next: [IconName, string, number][] = [
    ["users", "Nhờ hai thầy cô chấm lại nhãn", at(3, "hai")],
    ["globe", "Thử ở khóa học khác", at(3, "thử")],
    ["school", "Dùng ứng dụng trong lớp học thật", at(3, "dùng")],
  ];
  return (
    <SceneFrame scene={scene}>
      <Show at={b(0)} out={b(1) - 8} dy={16}>
        <div style={{position: "absolute", left: 0, right: 0, top: 380, display: "flex", flexDirection: "column", alignItems: "center", gap: 26}}>
          <div style={{width: 150, height: 150, borderRadius: 44, background: C.amberSoft, display: "grid", placeItems: "center", transform: `scale(${pop(frame, b(0) + 4)})`}}>
            <Icon name="alert" size={84} color={C.amber} />
          </div>
          <div style={{fontSize: 44, fontWeight: 800, opacity: sp(frame, b(0) + 10)}}>Thành thật về giới hạn</div>
        </div>
      </Show>

      {/* L1: what the labels do and do not say */}
      <Show at={b(1)} out={b(2) - 8} dy={20}>
        <Card pad={36} radius={30} style={{position: "absolute", left: 250, top: 300, width: 660, height: 360}}>
          <Chip tone="green" icon="check" size={26}>
            Đáp án cho biết
          </Chip>
          <div style={{fontSize: 34, fontWeight: 800, marginTop: 20}}>chương trình đã đổi gì</div>
          <div style={{fontFamily: MONO, fontSize: 26, marginTop: 26, borderRadius: 14, overflow: "hidden", boxShadow: `inset 0 0 0 1px ${C.line}`}}>
            <div style={{background: C.redSoft, padding: "6px 18px"}}>− for (i = 1; i &lt; n; i++)</div>
            <div style={{background: C.greenSoft, padding: "6px 18px"}}>+ for (i = 1; i &lt;= n; i++)</div>
          </div>
        </Card>
        <Card pad={36} radius={30} style={{position: "absolute", left: 1010, top: 300, width: 660, height: 360, opacity: sp(frame, at(1, "chưa"))}}>
          <Chip tone="red" icon="x" size={26}>
            Chưa cho biết
          </Chip>
          <div style={{fontSize: 34, fontWeight: 800, marginTop: 20}}>bạn ấy nghĩ gì trong đầu</div>
          <div style={{display: "flex", alignItems: "center", gap: 24, marginTop: 26}}>
            <div style={{width: 110, height: 110, borderRadius: 32, background: C.violetSoft, display: "grid", placeItems: "center"}}>
              <Icon name="brain" size={64} color={C.violet} />
            </div>
            <div style={{fontSize: 80, fontWeight: 800, color: C.violet, transform: `rotate(${Math.sin(frame / 7) * 6}deg)`}}>?</div>
          </div>
        </Card>
      </Show>

      {/* L2–L3: limits, then next steps */}
      <Show at={b(2)} dy={20}>
        <div style={{position: "absolute", left: 0, right: 0, top: 262, display: "flex", justifyContent: "center", gap: 24}}>
          {limits.map(([icon, title, sub, t]) => {
            const s = pop(frame, t);
            const dim = frame >= b(3) ? 1 - 0.35 * sp(frame, b(3)) : 1;
            return (
              <Card key={title} pad={26} radius={24} style={{width: 510, display: "flex", alignItems: "center", gap: 20, opacity: Math.min(1, s * 1.5) * dim, transform: `translateY(${(1 - Math.min(1, s)) * 30}px)`}}>
                <div style={{width: 72, height: 72, borderRadius: 22, background: C.amberSoft, display: "grid", placeItems: "center", flex: "none"}}>
                  <Icon name={icon} size={40} color={C.amber} />
                </div>
                <div>
                  <div style={{fontSize: 27, fontWeight: 800, lineHeight: 1.2}}>{title}</div>
                  <div style={{fontSize: 22, color: C.ink2, fontWeight: 600, marginTop: 4}}>{sub}</div>
                </div>
              </Card>
            );
          })}
        </div>
      </Show>
      <Show at={b(3)} dy={24}>
        <Card pad={34} radius={30} style={{position: "absolute", left: 460, top: 480, width: 1000}}>
          <div style={{fontSize: 22, fontWeight: 700, letterSpacing: "0.07em", textTransform: "uppercase", color: C.indigo, marginBottom: 10}}>Việc tiếp theo</div>
          {next.map(([icon, text, t]) => {
            const s = sp(frame, t);
            return (
              <div key={text} style={{display: "flex", alignItems: "center", gap: 22, height: 84, borderTop: `1px solid ${C.soft}`, opacity: s, transform: `translateX(${(1 - s) * 30}px)`}}>
                <div style={{width: 40, height: 40, borderRadius: 12, boxShadow: `inset 0 0 0 3px ${C.line}`, flex: "none"}} />
                <Icon name={icon} size={38} color={C.indigo} />
                <div style={{fontSize: 32, fontWeight: 700}}>{text}</div>
              </div>
            );
          })}
        </Card>
      </Show>
    </SceneFrame>
  );
};

export const Outro: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const s = pop(frame, 18);
  return (
    <SceneFrame scene={scene} push={0.02}>
      <div style={{position: "absolute", left: 0, right: 0, top: 250, display: "flex", flexDirection: "column", alignItems: "center"}}>
        <div style={{fontSize: 24, fontWeight: 700, letterSpacing: "0.14em", textTransform: "uppercase", color: C.indigo, opacity: sp(frame, 10)}}>Nghiên cứu AAI · Đề tài 5</div>
        <div style={{fontSize: 130, fontWeight: 800, letterSpacing: "-0.04em", marginTop: 14, transform: `scale(${0.7 + 0.3 * s})`, opacity: Math.min(1, s * 1.5)}}>Cảm ơn bạn!</div>
        <div style={{display: "flex", flexDirection: "column", alignItems: "center", gap: 10, marginTop: 50, fontSize: 24, color: C.ink2, fontWeight: 500, opacity: sp(frame, 50)}}>
          <div>Dữ liệu: C-Pack-IPAs, đã ẩn danh</div>
          <div>Giọng đọc tổng hợp: Microsoft vi-VN-HoaiMy</div>
          <div>Hình động dựng bằng Remotion</div>
        </div>
      </div>
    </SceneFrame>
  );
};
