#!/usr/bin/env python3
"""Organik sayfasındaki 'Tümünü indir' bağlantısının ZIP'ini üretir: organik/Organik_Tabelalar_ve_Kartlar_Tumu.zip
Tabela / etiket / plaka / refakat kartı PDF'leri değişince yeniden çalıştırın (önce araclar/organik_logo_boyut.py)."""
import zipfile, glob, os
T = "organik/tabelalar"
groups = [
 ("1_Alan_Tabelalari_A3", sorted(glob.glob(T + "/Tabela_*.pdf")) + [T + "/Organik_Alan_Tabelalari_A3_Tumu.pdf"]),
 ("2_Asma_Tabelalar_100x40cm", sorted(glob.glob(T + "/asma/*.pdf"))),
 ("3_Araba_Tabelalari_A4", sorted(glob.glob(T + "/araba/Araba_Tabela_*.pdf"))),
 ("4_Araba_Aski_Etiketleri_A5", sorted(glob.glob(T + "/araba/Araba_Etiketi_*.pdf"))),
 ("5_Araba_Plakalari_01-30", [T + "/araba/Araba_Plakalari_01-30.pdf"]),
 ("6_Refakat_Karti", [T + "/araba/Organik_Urun_Refakat_Karti.pdf"]),
 ("7_Ilgili_Formlar_Excel", sorted(glob.glob("formlar/16. Organik Üretim/EMS.OR.FRM.21.24*.xlsx") + glob.glob("formlar/16. Organik Üretim/EMS.OR.FRM.21.25*.xlsx"))),
]
out = "organik/Organik_Tabelalar_ve_Kartlar_Tumu.zip"
readme = ["EMS ORGANİK — TABELA, ETİKET, PLAKA VE REFAKAT KARTI SETİ", "", "Tüm dosyalar baskıya hazırdır. Organik (GOTS) logosu her yerde EMS logosu büyüklüğündedir.", ""]
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for g, files in groups:
        readme.append(g.replace("_", " ") + " (" + str(len(files)) + " dosya)")
        for f in files:
            if os.path.exists(f): z.write(f, g + "/" + os.path.basename(f))
    z.writestr("OKU_BENI.txt", "\n".join(readme) + "\n")
print(out, round(os.path.getsize(out) / 1048576, 1), "MB")
