import React from "react";
import {Composition} from "remotion";
import {Explainer} from "./Explainer";
import timeline from "./timeline.json";

export const RemotionRoot: React.FC = () => (
  <Composition
    id="Explainer"
    component={Explainer}
    durationInFrames={timeline.total}
    fps={timeline.fps}
    width={timeline.width}
    height={timeline.height}
  />
);
