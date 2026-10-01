import {loadFont} from "@remotion/google-fonts/BeVietnamPro";
import {loadFont as loadMono} from "@remotion/google-fonts/JetBrainsMono";

const body = loadFont("normal", {weights: ["400", "500", "600", "700", "800"], subsets: ["vietnamese", "latin"]});
const mono = loadMono("normal", {weights: ["400", "600"], subsets: ["latin"]});

export const FONT = body.fontFamily;
export const MONO = mono.fontFamily;

// The palette of AAI Lab: cool neutrals, one indigo, status colours only for outcomes.
export const C = {
  bg: "#F4F5FA",
  ink: "#1D2233",
  ink2: "#555D72",
  ink3: "#8A91A4",
  line: "#DADEE9",
  panel: "#FFFFFF",
  soft: "#EEF0F6",
  indigo: "#3F51B5",
  indigoDeep: "#2B3990",
  indigoSoft: "#E6E9F8",
  red: "#D0463F",
  redSoft: "#FBE3E1",
  green: "#2A9A7E",
  greenSoft: "#DCF2EA",
  amber: "#E39B2F",
  amberSoft: "#FCEFD7",
  violet: "#7B5BD3",
  violetSoft: "#EEE8FB",
};

export const GROUP = [C.indigo, C.amber, C.green, C.violet, C.red];

export const shadow = "0 1px 2px rgba(29,34,51,0.06), 0 12px 32px -10px rgba(29,34,51,0.18)";
export const ring = `0 0 0 1px rgba(29,34,51,0.07)`;
