# Video üretim kaynağı (oryantasyon)

Kural (kullanıcı, 26.10.2026): videoyu **bir kez çek, hazır tut**. Küçük metin/ses düzeltmesinde baştan çekme; yalnız ilgili sahneyi yenile.

- `sahneler/NN.mp4` = çekilmiş sahne klipleri (İngilizce ses sahneye göre, TR+AR altyazı gömülü değil: altyazı karelerin içinde); `NN.meta.json` = kare sayısı ve cümle zamanları.
- `arac/` = `render_or2.js` (slayt sahneleri, Playwright, kare kare), `render_close.js` (Thank you bitiş ekranı), `eng.js` (imleç/altyazı motoru), `assemble_or2.py` (klipleri birleştirir + ses + müzik), `music.py` (müziği üretir), `logo.png`.
- Ses: `tanitim/audio3/en_<sahne>_<cümle>.mp3` (GitHub Actions `tanitim-ses.yml`, edge-tts; sandbox'tan üretilemez).

## Tek sahneyi yenileme
1. `tanitim/oryantasyon.json` içinde ilgili sahnenin metnini düzelt; yeni sesi üret (workflow main'e push ile çalışır).
2. Çalışma klasörüne geri yükle: `sahneler/NN.mp4` → `orc/en2/NN.mp4`, `sahneler/NN.meta.json` → `orf/en2/NN/meta.json`.
3. Yalnız o sahneyi sil ve yeniden çek: `rm -r orf/en2/NN` → `node render_or2.js en NN` (bitiş ekranı için `node render_close.js`).
4. `python3 assemble_or2.py x` yalnız değişen klibi yeniden kodlar, diğerlerini kullanır; çıktı `oryantasyon_en2.mp4` → `tanitim/EMS_Oryantasyon_Yeni_Baslayan.mp4`.
5. Her videonun son sahnesi "Thank you" bitiş ekranıdır (bkz. `../bitis_ekrani_sablon.js`).
