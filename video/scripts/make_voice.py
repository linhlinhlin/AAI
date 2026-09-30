"""Narration for the explainer: one neural-TTS clip per line, and the timeline Remotion reads.

For every line of script.json this writes public/voice/<scene>_<n>.mp3 (from `say`, or `show`
when no spoken form is given), measures it with ffprobe, keeps the word timings, and writes
src/timeline.json with every scene's and line's start frame. Clips whose text did not change
are reused. Also writes a quiet synthesized music bed and two sound effects.

Run from video/:  python scripts/make_voice.py
"""

import asyncio
import hashlib
import json
import math
import subprocess
import wave
from pathlib import Path

import edge_tts
import numpy as np

HERE = Path(__file__).resolve().parents[1]
VOICE = HERE / "public" / "voice"
LEAD, GAP, TAIL = 0.55, 0.4, 0.9  # seconds of silence before, between and after lines
SPECIAL = {"intro": (2.2, 1.2), "outro": (0.8, 3.0), "conclusion": (0.8, 1.6)}  # (lead, tail)


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                          str(path)], capture_output=True, text=True, check=True).stdout
    return float(out.strip())


async def synthesize(text, voice, rate, path, semaphore):
    stamp = path.with_suffix(".json")
    key = hashlib.sha256(f"v2|{voice}|{rate}|{text}".encode()).hexdigest()
    if path.exists() and stamp.exists() and json.loads(stamp.read_text(encoding="utf-8")).get("key") == key:
        return json.loads(stamp.read_text(encoding="utf-8"))["words"]
    async with semaphore:
        words, audio = [], bytearray()
        attempts = 16
        for attempt in range(attempts):
            # The service drops some requests at random. Word timings are needed for the captions,
            # so sentence boundaries are only the last resort.
            boundary = "WordBoundary" if attempt < attempts - 2 else "SentenceBoundary"
            try:
                communicate = edge_tts.Communicate(text, voice, rate=rate, boundary=boundary)
                words, audio = [], bytearray()
                async for chunk in communicate.stream():
                    if chunk["type"] == "audio":
                        audio += chunk["data"]
                    elif chunk["type"] == "WordBoundary":
                        words.append([round(chunk["offset"] / 1e7, 3),
                                      round((chunk["offset"] + chunk["duration"]) / 1e7, 3), chunk["text"]])
                break
            except Exception:  # the service drops requests at random: wait and retry
                if attempt == attempts - 1:
                    raise
                await asyncio.sleep(min(20.0, 2.0 * (attempt + 1)))
    path.write_bytes(bytes(audio))
    stamp.write_text(json.dumps({"key": key, "words": words}), encoding="utf-8")
    return words


def write_wav(path, samples, rate=48000):
    samples = np.clip(samples, -1, 1)
    data = (samples * 32767).astype("<i2")
    with wave.open(str(path), "wb") as out:
        out.setnchannels(2 if samples.ndim == 2 else 1)
        out.setsampwidth(2)
        out.setframerate(rate)
        out.writeframes(data.tobytes())


def music_bed(path, rate=48000):
    """A 32 s seamless loop of soft pad chords (Cmaj7, Am7, Fmaj7, G6), generated here."""
    chords = [[261.63, 329.63, 392.0, 493.88], [220.0, 261.63, 329.63, 392.0],
              [174.61, 220.0, 261.63, 329.63], [196.0, 246.94, 293.66, 329.63]]
    seconds = 8.0
    n = int(seconds * rate)
    t = np.arange(n) / rate
    fade = np.minimum(1, np.minimum(t / 2.2, (seconds - t) / 2.2)) ** 2
    left, right = [], []
    for chord in chords:
        l_part = np.zeros(n)
        r_part = np.zeros(n)
        for i, f in enumerate(chord):
            for detune, weight in ((-0.6, 0.5), (0.6, 0.5)):
                phase = 2 * np.pi * (f + detune) * t
                tone = 0.7 * np.sin(phase) + 0.2 * np.sin(2 * phase) + 0.08 * np.sin(3 * phase)
                pan = 0.35 + 0.3 * (i / 3)
                l_part += weight * tone * (1 - pan)
                r_part += weight * tone * pan
        bass = 0.35 * np.sin(2 * np.pi * chord[0] / 2 * t)
        left.append((l_part + bass) * fade)
        right.append((r_part + bass) * fade)
    stereo = np.stack([np.concatenate(left), np.concatenate(right)], axis=1)
    kernel = np.ones(24) / 24  # gentle low-pass
    for c in range(2):
        stereo[:, c] = np.convolve(stereo[:, c], kernel, mode="same")
    stereo /= np.abs(stereo).max()
    write_wav(path, 0.6 * stereo, rate)


def effects(folder, rate=48000):
    rng = np.random.default_rng(7)
    n = int(0.55 * rate)
    t = np.arange(n) / rate
    noise = rng.standard_normal(n)
    sweep = np.zeros(n)
    width = np.linspace(40, 6, n).astype(int)  # the sound brightens as the smoothing window narrows
    cumulative = np.cumsum(np.insert(noise, 0, 0))
    for i in range(n):
        w = max(2, width[i])
        lo = max(0, i - w)
        sweep[i] = (cumulative[i] - cumulative[lo]) / (i - lo if i > lo else 1)
    envelope = np.sin(np.pi * np.minimum(1, t / 0.55)) ** 2
    whoosh = sweep * envelope
    write_wav(folder / "whoosh.wav", 0.5 * whoosh / np.abs(whoosh).max(), rate)
    m = int(0.18 * rate)
    t = np.arange(m) / rate
    pop = np.sin(2 * np.pi * (880 - 400 * t / 0.18) * t) * np.exp(-t * 28)
    write_wav(folder / "pop.wav", 0.5 * pop / np.abs(pop).max(), rate)


async def main():
    script = json.loads((HERE / "script.json").read_text(encoding="utf-8"))
    fps = script["fps"]
    VOICE.mkdir(parents=True, exist_ok=True)
    semaphore = asyncio.Semaphore(2)
    jobs = []
    for scene in script["scenes"]:
        for n, line in enumerate(scene["lines"], start=1):
            path = VOICE / f"{scene['id']}_{n:02d}.mp3"
            jobs.append(synthesize(line.get("say", line["show"]), script["voice"], script["rate"], path, semaphore))
    all_words = await asyncio.gather(*jobs)
    timeline, cursor, k, chapter = [], 0, 0, 0
    for index, scene in enumerate(script["scenes"]):
        lead, tail = SPECIAL.get(scene["id"], (LEAD, TAIL))
        at = lead
        lines = []
        for n, line in enumerate(scene["lines"], start=1):
            path = VOICE / f"{scene['id']}_{n:02d}.mp3"
            seconds = duration(path)
            lines.append({"file": f"voice/{path.name}", "from": math.floor(at * fps),
                          "frames": math.ceil(seconds * fps), "show": line["show"], "words": all_words[k]})
            k += 1
            at += seconds + GAP
        frames = math.ceil((at - GAP + tail) * fps)
        if scene["chapter"]:
            chapter += 1
        timeline.append({"id": scene["id"], "chapter": scene["chapter"], "number": chapter if scene["chapter"] else 0,
                         "index": index, "from": cursor, "frames": frames, "lines": lines})
        cursor += frames
    (HERE / "src" / "timeline.json").write_text(json.dumps(
        {"fps": fps, "width": 1920, "height": 1080, "total": cursor, "chapters": chapter, "scenes": timeline},
        ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    audio = HERE / "public" / "audio"
    audio.mkdir(parents=True, exist_ok=True)
    if not (audio / "music.wav").exists():
        music_bed(audio / "music.wav")
    effects(audio)
    print(f"{len(timeline)} scenes, {cursor} frames = {cursor / fps / 60:.1f} min")


if __name__ == "__main__":
    asyncio.run(main())
