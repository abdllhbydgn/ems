#!/usr/bin/env python3
"""Organik tabela / araba etiketi / plaka / refakat kartı PDF'lerinde GOTS (organik) logosunu EMS logosu büyüklüğüne getirir.
Kural (kullanıcı, 26.10.2026): organik logo BÜYÜYECEK (hiçbir yerde küçülmez), tabela alanı/sayfa düzeni aynı kalır; logo en az EMS logosu kadar büyük olur.
GÖRÜNEN GOTS çapı = max(şimdiki görünen çap, EMS logosunun görünen YÜKSEKLİĞİ); merkez sabit. (GOTS görselinin etrafında saydam boşluk olabilir; bu yüzden görünen daire ölçülür.)
EMS logosu olmayan sayfalarda (araba plakaları) referans: araba tabelasındaki EMS logosu yüksekliği (REF_PT).
Kullanım: python3 araclar/organik_logo_boyut.py  (organik/tabelalar/**/*.pdf yerinde güncellenir; ikinci çalıştırmada değişmez)"""
import glob, re, sys, io, pymupdf
from PIL import Image
import numpy as np
def visible_frac(doc, xref):
    """Görselin görünen (saydam/beyaz olmayan) alanının genişlik/yükseklik oranı."""
    i = doc.extract_image(xref); im = Image.open(io.BytesIO(i["image"])).convert("RGBA")
    if i.get("smask"):
        m = Image.open(io.BytesIO(doc.extract_image(i["smask"])["image"])).convert("L"); im.putalpha(m)
    a = np.array(im); ok = (a[..., 3] > 20) & (a[..., :3].sum(axis=2) < 740)
    ys, xs = np.where(ok)
    if not len(xs): return 1.0, 1.0
    return (xs.max() - xs.min() + 1) / a.shape[1], (ys.max() - ys.min() + 1) / a.shape[0]
REF_PT = 50.0
def logo_kinds(doc, page):
    res = doc.xref_get_key(page.xref, "Resources/XObject")[1]
    names = {}
    for n, x in re.findall(r"/(\w+)\s+(\d+)\s+0\s+R", res):
        try:
            im = doc.extract_image(int(x))
        except Exception:
            continue
        if not im or im["width"] < 100: continue
        r = im["width"] / im["height"]
        names[n] = ("gots" if 0.9 < r < 1.1 else "ems" if r > 1.15 else "other", int(x))
    return names
def fix(path):
    doc = pymupdf.open(path); changed = 0
    for page in doc:
        kinds = logo_kinds(doc, page)
        if not kinds: continue
        info = {}
        for im in page.get_image_info(xrefs=True):
            info.setdefault(im["xref"], []).append(im["bbox"])
        ems_h = [(b[3] - b[1]) * visible_frac(doc, x)[1] for n, (k, x) in kinds.items() if k == "ems" for b in info.get(x, [])]
        target_vis = max(ems_h) if ems_h else REF_PT
        cs = page.get_contents()
        for cx in cs:
            s = doc.xref_stream(cx).decode("latin1"); out = s; occ = {}
            pat = re.compile(r"([-\d.]+) 0 0 ([-\d.]+) ([-\d.]+) ([-\d.]+) cm(\s[^Q]*?)/(\w+) Do")
            def sub(m):
                nonlocal changed
                a, d, e, f = (float(m.group(i)) for i in (1, 2, 3, 4)); name = m.group(6)
                if name not in kinds or kinds[name][0] != "gots": return m.group(0)
                k = occ.setdefault(name, 0); occ[name] += 1
                bbs = info.get(kinds[name][1], []); 
                if k >= len(bbs): return m.group(0)
                bw = bbs[k][2] - bbs[k][0]; bh = bbs[k][3] - bbs[k][1]
                fw = visible_frac(doc, kinds[name][1])[0]; cur_vis = bw * fw
                if target_vis <= cur_vis + 0.6: return m.group(0)  # yalnız büyüt / grow only
                target = target_vis / fw  # yeni görsel genişliği (pt)
                na = abs(a) * target / bw; nd = d * target / bh
                ne = e + (a - na) / 2; nf = f + d / 2 - nd / 2
                changed += 1
                return "%.5f 0 0 %.5f %.5f %.5f cm%s/%s Do" % (na if a > 0 else -na, nd, ne, nf, m.group(5), name)
            out = pat.sub(sub, s)
            if out != s: doc.update_stream(cx, out.encode("latin1"))
    if changed: doc.saveIncr() if False else doc.save(path + ".tmp", garbage=3, deflate=True); 
    return doc, changed
if __name__ == "__main__":
    import os
    for f in sorted(glob.glob("organik/tabelalar/**/*.pdf", recursive=True)):
        if "Kirik_Igne" in f: continue
        d, n = fix(f); d.close()
        if n:
            os.replace(f + ".tmp", f); print("güncellendi", n, f)
        else: print("değişmedi", f)
