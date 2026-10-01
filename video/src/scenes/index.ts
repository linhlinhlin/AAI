import React from "react";
import {Scene} from "../timeline";
import {Classic, classicPops} from "./Classic";
import {Deviation, deviationPops} from "./Deviation";
import {Conclusion, conclusionPops, Limits, Outro} from "./Ending";
import {Example, examplePops} from "./Example";
import {Intro, introPops} from "./Intro";
import {Metrics, metricsPops} from "./Metrics";
import {Mutants, mutantsPops} from "./Mutants";
import {Problem, problemPops} from "./Problem";
import {Protocol, protocolPops} from "./Protocol";
import {Question, questionPops} from "./Question";
import {Repair, repairPops} from "./Repair";
import {Results, resultsPops} from "./Results";
import {Sandbox, sandboxPops} from "./Sandbox";
import {Tool, toolPops} from "./Tool";

type Entry = {component: React.FC<{scene: Scene}>; pops?: (scene: Scene) => number[]};

export const SCENES: Record<string, Entry> = {
  intro: {component: Intro, pops: introPops},
  problem: {component: Problem, pops: problemPops},
  classic: {component: Classic, pops: classicPops},
  question: {component: Question, pops: questionPops},
  example: {component: Example, pops: examplePops},
  repair: {component: Repair, pops: repairPops},
  sandbox: {component: Sandbox, pops: sandboxPops},
  mutants: {component: Mutants, pops: mutantsPops},
  deviation: {component: Deviation, pops: deviationPops},
  protocol: {component: Protocol, pops: protocolPops},
  metrics: {component: Metrics, pops: metricsPops},
  results: {component: Results, pops: resultsPops},
  tool: {component: Tool, pops: toolPops},
  conclusion: {component: Conclusion, pops: conclusionPops},
  limits: {component: Limits},
  outro: {component: Outro},
};
