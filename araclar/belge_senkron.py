#!/usr/bin/env python3
"""Tüm resmî prosedür / talimat / politika (Word) ve form (Excel/Word) belgelerini birbirine bağlar ve eşitler (kullanıcı kuralı, 27.10.2026).
1) Her belgenin metninden belge kodlarını (EMS.XX.PRO|POL|TL|FRM|SOP.NN.NN) okur.
2) prosedurler/refs.json = {belge: [atıf yaptığı belgeler]} dosyasını yeniden kurar (mevcut atıflar korunur, yeni bulunanlar eklenir; var olmayan kodlar eklenmez).
3) Tutarlılık denetimi: manifest kodu ↔ dosya adı ↔ Word başlık kodu, eksik/ölü dosya, yinelenen kod, atıf yapılan ama bulunmayan kodlar.
Çıktı: refs.json + belge_senkron_rapor.json (araclar/) — site Doküman Dizini refs.json'ı okur.
Kullanım: python3 araclar/belge_senkron.py [--yaz]   (--yaz verilmezse yalnız rapor)"""
import json, re, os, sys, glob, zipfile
import docx, openpyxl
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CODE = re.compile(r"EMS\.[A-ZÜİÖÇŞĞ]{2,3}\.(?:PRO|POL|TL|FRM|SOP|RPR|KRT)\.\d{2}\.\d{2}")
J = lambda p: json.load(open(os.path.join(ROOT, p), encoding="utf-8"))
norm = lambda c: c.rstrip(".")
def docx_text(path):
    d = docx.Document(path); out = [p.text for p in d.paragraphs]
    for t in d.tables:
        for r in t.rows:
            for c in r.cells: out.append(c.text)
    for s in d.sections:
        for t in s.header.tables:
            for r in t.rows:
                for c in r.cells: out.append(c.text)
    return "\n".join(out)
def xlsx_text(path):
    out = []
    try:
        wb = openpyxl.load_workbook(path, read_only=False)
        for ws in wb:
            for row in ws.iter_rows():
                for c in row:
                    if isinstance(c.value, str): out.append(c.value)
    except Exception: pass
    return "\n".join(out)
def main(write=False):
    pm, fm = J("prosedurler/manifest.json"), J("formlar/manifest.json")
    inv = {}; problems = []
    for x in pm:
        c = norm(x["code"])
        if c in inv: problems.append(["yinelenen kod", c])
        inv[c] = ("prosedurler/" + x["file"], x)
        p = os.path.join(ROOT, "prosedurler", x["file"])
        if not os.path.exists(p): problems.append(["dosya yok (prosedür)", x["file"]])
        elif not x["file"].startswith(c): problems.append(["dosya adı kodla başlamıyor", x["file"]])
    for x in fm:
        m = re.search(r"EMS\.[A-ZÜİÖÇŞĞ]{2,3}\.(?:FRM|RPR|KRT)\.\d{2}\.\d{2}", x.get("name", ""))
        c = m.group(0) if m else None
        p = os.path.join(ROOT, "formlar", x["file"])
        if not os.path.exists(p): problems.append(["dosya yok (form)", x["file"]]); continue
        if c:
            if c in inv: problems.append(["yinelenen kod", c, x["file"]])
            inv[c] = ("formlar/" + x["file"], x)
        else: problems.append(["form adında kod yok", x["file"]])
    # TR manifest
    for x in J("prosedurler_tr/manifest.json"):
        if not os.path.exists(os.path.join(ROOT, "prosedurler_tr", x["file"])): problems.append(["dosya yok (TR)", x["file"]])
        if norm(x["code"]) not in inv: problems.append(["TR belgenin resmî karşılığı yok", x["code"]])
    # Site (QMS) eşleme tabloları: eski kod → resmî kod; hedefler var mı
    site = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read(); mapped = set()
    for nm in ("QMS_PRS_OFFICIAL", "QMS_TLM_OFFICIAL", "QMS_FRM_NEW"):
        i = site.index("const " + nm + " ="); j = site.index("};", i)
        for k, v in re.findall(r'"([^"]+)"\s*:\s*"([^"]+)"', site[i:j + 2]):
            if norm(v) in inv: mapped.add(norm(v))
            else: problems.append(["site eşlemesi: resmî belge yok", nm, k, v])
    refs0 = J("prosedurler/refs.json"); refs = {k: list(v) for k, v in refs0.items()}
    dangling = {}; added = 0
    for c, (path, x) in sorted(inv.items()):
        fp = os.path.join(ROOT, path)
        try: txt = docx_text(fp) if fp.endswith(".docx") else xlsx_text(fp) if fp.endswith(".xlsx") else ""
        except Exception as e: problems.append(["okunamadı", path, str(e)[:60]]); continue
        if c in inv and fp.endswith(".docx") and not x.get("file", "").startswith("N/A"):
            h = docx.Document(fp).sections[0].header
            hc = " ".join(p.text for t in h.tables for r in t.rows for cell in r.cells for p in cell.paragraphs)
            if fp.startswith(os.path.join(ROOT, "prosedurler")) and c.split(".")[0] == "EMS" and c not in hc.replace(" ", ""):
                problems.append(["Word başlığında kod farklı/yok", c])
        found = sorted({norm(t) for t in CODE.findall(txt)} - {c})
        for t in found:
            if t in inv:
                lst = refs.setdefault(c, [])
                if t not in lst: lst.append(t); added += 1
            else: dangling.setdefault(c, []).append(t)
    for k in refs:
        refs[k] = sorted(set(refs[k]), key=lambda z: z)
    # Aile kuralı: hiçbir belgeyle bağlı olmayan belgeyi aynı bölüm ve numara grubundaki (EMS.XX.*.NN.*) belgelerle bağlar:
    # prosedür/talimat/form → aynı gruptaki politika(lar)ı; politika → aynı gruptaki prosedür/talimatları; politika yoksa aynı gruptaki ilk prosedürü.
    fam = {}
    for c in inv:
        m = re.match(r"(EMS\.[^.]+)\.([A-Z]{2,3})\.(\d{2})\.(\d{2})$", c)
        if m: fam.setdefault((m.group(1), m.group(3)), []).append((m.group(2), c))
    def linked(c, cited_now): return c in cited_now or bool(refs.get(c))
    cited_now = {t for v in refs.values() for t in v} | set(mapped)
    famadd = 0
    for c in sorted(inv):
        if linked(c, cited_now): continue
        m = re.match(r"(EMS\.[^.]+)\.([A-Z]{2,3})\.(\d{2})\.(\d{2})$", c)
        if not m: continue
        peers = [x for x in fam.get((m.group(1), m.group(3)), []) if x[1] != c]
        pol = [x[1] for x in peers if x[0] == "POL"][:3]; pro = [x[1] for x in peers if x[0] in ("PRO", "TL")][:3]
        if m.group(2) == "POL":
            for t in pro[:12] or []:
                lst = refs.setdefault(t, [])
                if c not in lst: lst.append(c); famadd += 1
        else:
            for t in (pol or pro[:2]):
                lst = refs.setdefault(c, [])
                if t not in lst: lst.append(t); famadd += 1
        cited_now = {t for v in refs.values() for t in v} | set(mapped)
    for k in refs: refs[k] = sorted(set(refs[k]))
    cited = {t for v in refs.values() for t in v}
    orphans = sorted(c for c in inv if c not in cited and c not in mapped and c not in refs)
    rep = {"belge_sayisi": len(inv), "yeni_atif": added, "aile_baglantisi": famadd, "sorunlar": problems, "bulunmayan_atiflar": {k: sorted(set(v)) for k, v in dangling.items()}, "hicbir_belgeyle_bagli_olmayan": orphans}
    json.dump(rep, open(os.path.join(ROOT, "araclar", "belge_senkron_rapor.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if write:
        json.dump(refs, open(os.path.join(ROOT, "prosedurler", "refs.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("belge:", len(inv), "· yeni atıf:", added, "· aile bağlantısı:", famadd, "· sorun:", len(problems), "· bulunmayan atıf yapan belge:", len(dangling), "· bağsız belge:", len(orphans))
    return rep
if __name__ == "__main__": main("--yaz" in sys.argv)
