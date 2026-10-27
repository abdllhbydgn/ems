#!/usr/bin/env python3
"""Organik tabela / asma tabela / araba etiketi / plaka / refakat kartı PDF'lerindeki GOTS logosunu HD (vektörden çizilmiş) sürümle değiştirir.
Yerleşim, boyut ve sayfa düzeni AYNI kalır (yalnız görselin pikselleri değişir). İdempotent: yeni görsel zaten varsa dokunmaz.
- 408x412 görsel (etrafında saydam boşluk) → araclar/gots_hd_canvas.png (aynı boşluk oranı)
- 200x200 görsel (daire kenardan kenara) → araclar/gots_hd_kare.png
Kullanım: python3 araclar/organik_logo_hd.py   (sonra araclar/organik_zip.py ile ZIP'i yeniden üret, index.html ORG_ZIP_V'yi artır)"""
import glob, os, sys, pymupdf
sys.path.insert(0, os.path.dirname(__file__))
from organik_logo_boyut import logo_kinds
HERE = os.path.dirname(os.path.abspath(__file__))
CANVAS = os.path.join(HERE, "gots_hd_canvas.png"); SQ = os.path.join(HERE, "gots_hd_kare.png")
def main(root="organik/tabelalar"):
    n_files = n_imgs = 0
    for f in sorted(glob.glob(root + "/**/*.pdf", recursive=True)):
        doc = pymupdf.open(f); done = set(); changed = 0
        for page in doc:
            for name, (kind, xref) in logo_kinds(doc, page).items():
                if kind != "gots" or xref in done: continue
                info = doc.extract_image(xref); w, h = info["width"], info["height"]
                if (w, h) == (408, 412): src = CANVAS
                elif (w, h) == (200, 200): src = SQ
                else: continue  # zaten HD veya bilinmeyen / already HD or unknown
                page.replace_image(xref, filename=src); done.add(xref); changed += 1
        if changed:
            tmp = f + ".tmp"; doc.save(tmp, garbage=3, deflate=True); doc.close(); os.replace(tmp, f)
            n_files += 1; n_imgs += changed
        else: doc.close()
    print("güncellenen PDF:", n_files, "görsel:", n_imgs)
if __name__ == "__main__": main()
