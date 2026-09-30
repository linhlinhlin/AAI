import React from "react";
import {Img, interpolate, staticFile, useCurrentFrame} from "remotion";
import {clamp, EASE, pop, sp} from "../anim";
import {SceneFrame} from "../components/frame";
import {Icon} from "../components/Icon";
import {Chip} from "../components/ui";
import {C, MONO} from "../theme";
import {beats, Scene} from "../timeline";
import layout from "../app_layout.json";

// Screenshots of AAI Lab (scripts/capture_app.py): 1224×1000 CSS px captured at 2×, with the
// boxes of the parts the camera visits in app_layout.json.
const SHOT = {w: layout.clip.width, h: layout.clip.height};
const WIN = {x: 330, y: 206, w: 1260, h: 664, bar: 46};
const VIEW = {w: WIN.w, h: WIN.h - WIN.bar};

type Cam = {cx: number; cy: number; z: number};
type Rect = [number, number, number, number];
type Key = {t: number; dur: number; cam: Cam; spot?: Rect; note?: string};

const around = (pad: number, ...boxes: number[][]): Rect => {
  const x0 = Math.min(...boxes.map((r) => r[0]));
  const y0 = Math.min(...boxes.map((r) => r[1]));
  const x1 = Math.max(...boxes.map((r) => r[0] + r[2]));
  const y1 = Math.max(...boxes.map((r) => r[1] + r[3]));
  return [x0 - pad, y0 - pad, x1 - x0 + 2 * pad, y1 - y0 + 2 * pad];
};
const MAX = layout.lab_max;
const MIXED = layout.lab_mixed;

const lerpCam = (a: Cam, b: Cam, t: number): Cam => ({cx: a.cx + (b.cx - a.cx) * t, cy: a.cy + (b.cy - a.cy) * t, z: a.z + (b.z - a.z) * t});

const camera = (keys: Key[], frame: number) => {
  let cam = keys[0].cam;
  let spot: Rect | undefined;
  let spotT = 0;
  let note: string | undefined;
  let noteT = 0;
  for (let i = 1; i < keys.length; i++) {
    const k = keys[i];
    if (frame < k.t) break;
    const t = interpolate(frame, [k.t, k.t + k.dur], [0, 1], {...clamp, easing: EASE});
    cam = lerpCam(cam, k.cam, t);
    spot = k.spot;
    spotT = k.spot ? interpolate(frame, [k.t + k.dur * 0.6, k.t + k.dur + 8], [0, 1], clamp) : 0;
    note = k.note;
    noteT = k.note ? interpolate(frame, [k.t + k.dur * 0.5, k.t + k.dur + 6], [0, 1], clamp) : 0;
  }
  return {cam, spot, spotT, note, noteT};
};

const toView = (cam: Cam, x: number, y: number) => ({x: (x - cam.cx) * cam.z + VIEW.w / 2, y: (y - cam.cy) * cam.z + VIEW.h / 2});

export const Tool: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {b, at} = beats(scene);
  const winIn = sp(frame, 4);
  const swap = interpolate(frame, [b(3) - 4, b(3) + 8], [0, 1], clamp);
  const clickAt = at(4, "đúng");

  const keys: Key[] = [
    {t: 0, dur: 0, cam: {cx: 612, cy: 300, z: 1.03}},
    {t: 24, dur: 160, cam: {cx: 612, cy: 402, z: 1.03}, note: "Chạy ngay trên máy của giáo viên"},
    {t: b(1) - 4, dur: 28, cam: {cx: 430, cy: 350, z: 1.5}, spot: around(0, MAX.tabs), note: "Bài sai của cả lớp, gom thành từng nhóm"},
    {t: at(1, "bằng") - 6, dur: 28, cam: {cx: 790, cy: 560, z: 1.55}, spot: around(10, MAX.bars, MAX.rule), note: "Bằng chứng chung + một luật NẾU–THÌ"},
    {t: b(2) - 4, dur: 26, cam: {cx: 789, cy: 300, z: 1.55}, spot: around(10, MAX.title, MAX.hypothesis), note: "Chỉ đưa giả thuyết khi luật đúng với ít nhất nửa nhóm"},
    {t: b(3) - 4, dur: 26, cam: {cx: 612, cy: 392, z: 1.08}, spot: around(10, MIXED.mixed), note: "Nhóm có nhiều lý do: ứng dụng nói thẳng"},
    {t: b(4) - 4, dur: 28, cam: {cx: 948, cy: 224, z: 2.25}, spot: around(8, MIXED.verdict), note: "Giáo viên quyết định cuối cùng"},
  ];
  const {cam, spot, spotT, note, noteT} = camera(keys, frame);

  // Cursor for the verdict click.
  const target = toView(cam, 1030, 221);
  const cursorT = interpolate(frame, [b(4) + 18, clickAt - 2], [0, 1], {...clamp, easing: EASE});
  const cursor = {x: VIEW.w * 0.78 + (target.x - VIEW.w * 0.78) * cursorT, y: VIEW.h * 0.92 + (target.y - VIEW.h * 0.92) * cursorT};
  const clicked = frame >= clickAt;
  const ring = interpolate(frame, [clickAt, clickAt + 16], [0, 1], clamp);

  const spotView = spot ? {a: toView(cam, spot[0], spot[1]), b: toView(cam, spot[0] + spot[2], spot[1] + spot[3])} : null;
  const badge = toView(cam, 112, 380);

  return (
    <SceneFrame scene={scene} push={0}>
      {/* browser window */}
      <div
        style={{
          position: "absolute",
          left: WIN.x,
          top: WIN.y,
          width: WIN.w,
          height: WIN.h,
          borderRadius: 22,
          overflow: "hidden",
          background: "#fff",
          boxShadow: "0 0 0 1px rgba(29,34,51,0.08), 0 40px 80px -36px rgba(29,34,51,0.55)",
          opacity: winIn,
          transform: `translateY(${(1 - winIn) * 60}px) scale(${0.96 + 0.04 * winIn})`,
        }}
      >
        <div style={{height: WIN.bar, background: "#F0F2F7", display: "flex", alignItems: "center", gap: 10, padding: "0 18px", borderBottom: "1px solid #E1E5EE"}}>
          {["#EC6A5E", "#F4BF4F", "#61C554"].map((c) => (
            <div key={c} style={{width: 13, height: 13, borderRadius: 99, background: c}} />
          ))}
          <div style={{marginLeft: 20, flex: 1, height: 28, borderRadius: 8, background: "#fff", display: "flex", alignItems: "center", gap: 10, padding: "0 14px", fontFamily: MONO, fontSize: 16, color: C.ink2}}>
            <Icon name="lock" size={15} color={C.ink3} />
            127.0.0.1:8770 · AAI Lab
          </div>
        </div>
        <div style={{position: "relative", width: VIEW.w, height: VIEW.h, overflow: "hidden", background: "#F6F7FB"}}>
          <div
            style={{
              position: "absolute",
              left: 0,
              top: 0,
              width: SHOT.w,
              height: SHOT.h,
              transformOrigin: "0 0",
              transform: `translate(${VIEW.w / 2 - cam.cx * cam.z}px, ${VIEW.h / 2 - cam.cy * cam.z}px) scale(${cam.z})`,
            }}
          >
            <Img src={staticFile("img/lab_max.png")} style={{position: "absolute", inset: 0, width: SHOT.w, height: SHOT.h, opacity: 1 - swap}} />
            <Img src={staticFile("img/lab_mixed.png")} style={{position: "absolute", inset: 0, width: SHOT.w, height: SHOT.h, opacity: swap}} />
            {/* the teacher's verdict after the click */}
            {clicked ? (
              <>
                <div style={{position: "absolute", left: 896, top: 203, width: 90, height: 34, borderRadius: 8, background: "#EBEDF3"}}>
                  <div style={{fontSize: 13.5, color: C.ink3, textAlign: "center", lineHeight: "34px"}}>Chưa xem</div>
                </div>
                <div
                  style={{
                    position: "absolute",
                    left: 990,
                    top: 203,
                    width: 82,
                    height: 34,
                    borderRadius: 8,
                    background: "#fff",
                    boxShadow: "0 1px 3px rgba(29,34,51,0.2)",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    gap: 4,
                    color: C.green,
                    fontWeight: 700,
                    fontSize: 13.5,
                    transform: `scale(${0.9 + 0.1 * pop(frame, clickAt)})`,
                  }}
                >
                  <Icon name="check" size={13} color={C.green} stroke={3} />
                  Đúng
                </div>
              </>
            ) : null}
          </div>
          {/* spotlight */}
          {spotView && spotT > 0 ? (
            <div
              style={{
                position: "absolute",
                left: spotView.a.x,
                top: spotView.a.y,
                width: spotView.b.x - spotView.a.x,
                height: spotView.b.y - spotView.a.y,
                borderRadius: 18,
                boxShadow: `0 0 0 3px ${C.indigo}, 0 0 0 3000px rgba(24,28,43,${0.32 * spotT})`,
                opacity: spotT,
              }}
            />
          ) : null}
          {/* the mixed badge in the group list */}
          {frame >= b(3) + 20 && frame < b(4) - 4 ? (
            <div
              style={{
                position: "absolute",
                left: badge.x - 80,
                top: badge.y - 26,
                width: 160,
                height: 52,
                borderRadius: 999,
                boxShadow: `0 0 0 ${3 + 3 * Math.sin(frame / 5)}px ${C.amber}`,
                opacity: sp(frame, b(3) + 20),
              }}
            />
          ) : null}
          {/* cursor */}
          {frame >= b(4) + 14 ? (
            <div style={{position: "absolute", left: cursor.x, top: cursor.y, opacity: sp(frame, b(4) + 14)}}>
              {clicked ? (
                <div style={{position: "absolute", left: -30, top: -30, width: 60, height: 60, borderRadius: 99, border: `4px solid ${C.green}`, transform: `scale(${0.4 + ring})`, opacity: 1 - ring}} />
              ) : null}
              <svg width="40" height="40" viewBox="0 0 24 24" style={{position: "absolute", left: -4, top: -3, transform: `scale(${frame >= clickAt && frame < clickAt + 5 ? 0.85 : 1})`}}>
                <path d="M4.04 4.66a.5.5 0 0 1 .62-.62l16 5.5a.5.5 0 0 1-.05.96l-6.12 1.37a2 2 0 0 0-1.52 1.52l-1.37 6.12a.5.5 0 0 1-.96.05z" fill={C.ink} stroke="#fff" strokeWidth={1.6} strokeLinejoin="round" />
              </svg>
            </div>
          ) : null}
          {/* note */}
          {note && noteT > 0 ? (
            <div style={{position: "absolute", left: 24, bottom: 22, opacity: noteT, transform: `translateY(${(1 - noteT) * 14}px)`}}>
              <Chip tone="ink" size={27}>
                {note}
              </Chip>
            </div>
          ) : null}
        </div>
      </div>

    </SceneFrame>
  );
};

export const toolPops = (scene: Scene) => {
  const {at} = beats(scene);
  return [at(4, "đúng")];
};
