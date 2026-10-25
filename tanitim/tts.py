#!/usr/bin/env python3
"""Tanıtım videosu sesleri: tanitim/script.json -> tanitim/audio/<dil>_<sahne>.mp3 (edge-tts, yapay zekâ sesi).
GitHub Actions'ta çalışır (.github/workflows/tanitim-ses.yml); sandbox'tan Bing TTS engelli."""
import asyncio, json, os, edge_tts
VOICES = {"tr": "tr-TR-EmelNeural", "en": "en-US-AriaNeural", "ar": "ar-EG-SalmaNeural"}
RATE = {"tr": "-4%", "en": "-4%", "ar": "-6%"}
async def main():
    sc = json.load(open("tanitim/script.json", encoding="utf-8"))
    os.makedirs("tanitim/audio", exist_ok=True)
    for s in sc:
        for lang, voice in VOICES.items():
            out = f"tanitim/audio/{lang}_{s['n']:02d}.mp3"
            if os.path.exists(out): continue
            await edge_tts.Communicate(s[lang], voice, rate=RATE[lang]).save(out)
            print("ok", out)
asyncio.run(main())
