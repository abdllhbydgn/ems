#!/usr/bin/env python3
"""Oryantasyon eğitimi sesleri: tanitim/oryantasyon.json -> tanitim/audio3/<dil>_<sahne>_<cümle>.mp3 (edge-tts, yapay zekâ sesi; TR/EN/AR)."""
import asyncio, json, os, edge_tts
VOICES = {"tr": "tr-TR-EmelNeural", "en": "en-US-AriaNeural", "ar": "ar-EG-SalmaNeural"}
RATE = {"tr": "-4%", "en": "-2%", "ar": "-6%"}
async def main():
    sc = json.load(open("tanitim/oryantasyon.json", encoding="utf-8"))
    os.makedirs("tanitim/audio3", exist_ok=True)
    for i, s in enumerate(sc, 1):
        for k, row in enumerate(s["s"], 1):
            for L, v in VOICES.items():
                out = f"tanitim/audio3/{L}_{i:02d}_{k:02d}.mp3"
                if os.path.exists(out): continue
                for deneme in range(4):
                    try:
                        await edge_tts.Communicate(row[L].strip(), v, rate=RATE[L]).save(out)
                        print("ok", out); break
                    except Exception as e:
                        print("tekrar", out, deneme, e); await asyncio.sleep(2)
asyncio.run(main())
