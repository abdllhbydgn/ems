#!/usr/bin/env python3
"""Tanıtım videosu v4: tanitim/script2.json -> tanitim/audio2/en_<sahne>_<cümle>.mp3 (yalnız İngilizce anlatım, yapay zekâ sesi).
GitHub Actions'ta çalışır; sandbox'tan Bing TTS engelli."""
import asyncio, json, os, edge_tts
VOICE, RATE = "en-US-AriaNeural", "+0%"
async def main():
    sc = json.load(open("tanitim/script2.json", encoding="utf-8"))
    os.makedirs("tanitim/audio2", exist_ok=True)
    for i, s in enumerate(sc, 1):
        for k, row in enumerate(s["s"], 1):
            out = f"tanitim/audio2/en_{i:02d}_{k:02d}.mp3"
            if os.path.exists(out): continue
            await edge_tts.Communicate(row["en"], VOICE, rate=RATE).save(out)
            print("ok", out)
asyncio.run(main())
