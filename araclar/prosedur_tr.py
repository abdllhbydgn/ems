#!/usr/bin/env python3
"""Resmî EN+AR prosedür/talimat Word belgesinden TÜRKÇE sürüm üretir (resmî dosyaya dokunulmaz).
Kullanım:
  python3 prosedur_tr.py extract <docx> <json>     # İngilizce paragrafları (run run) JSON'a çıkarır
  python3 prosedur_tr.py build <docx> <json> <out> # JSON'daki Türkçe metinle yeni docx üretir
JSON: {"title_en": "...", "title_tr": "...", "paras": [[run1, run2...], ...]}  (boş paragraf = [])
Türkçe paragraf sayısı İngilizce ile aynı olmalı (aynı sıra); Arapça kısım atılır."""
import sys, json, re, zipfile, io, copy
from lxml import etree
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
q = lambda t: "{%s}%s" % (W, t)
AR = re.compile(r"[؀-ۿ]")

def _body(z):
    r = etree.fromstring(z.read("word/document.xml"))
    return r, r.find(q("body"))

def _ptext(p):
    return "".join(t.text or "" for t in p.iter(q("t")))

def _en_paras(body):
    """İngilizce paragraflar: gövdenin başından ilk Arapça paragrafa kadar."""
    out = []
    for el in body:
        if etree.QName(el).localname != "p":
            break
        if AR.search(_ptext(el)):
            break
        out.append(el)
    return out

def _runs_t(p):
    return [t for t in p.iter(q("t"))]

def extract(docx, js):
    z = zipfile.ZipFile(docx)
    r, body = _body(z)
    paras = [[t.text or "" for t in _runs_t(p)] for p in _en_paras(body)]
    h2 = etree.fromstring(z.read("word/header2.xml"))
    ts = [t.text or "" for t in h2.iter(q("t"))]
    json.dump({"title_en": ts[0], "title_tr": "", "paras": paras}, open(js, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

def build(docx, js, out):
    d = json.load(open(js, encoding="utf-8"))
    zin = zipfile.ZipFile(docx)
    r, body = _body(zin)
    en = _en_paras(body)
    assert len(en) == len(d["paras"]), "paragraf sayısı farklı %d != %d" % (len(en), len(d["paras"]))
    for p, runs in zip(en, d["paras"]):
        ts = _runs_t(p)
        assert len(ts) == len(runs), "run sayısı farklı: %r" % _ptext(p)[:60]
        for t, s in zip(ts, runs):
            t.text = s
            t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    # Arapça kısmı at: ilk Arapça paragraftan son Arapça paragrafa kadar
    kids = list(body)
    ar_idx = [i for i, el in enumerate(kids) if etree.QName(el).localname == "p" and AR.search(_ptext(el))]
    if ar_idx:
        for el in kids[ar_idx[0]:ar_idx[-1] + 1]:
            body.remove(el)
    note = d.get("note")
    if note:  # çeviri notu: "ONAYLAYANLAR" satırının hemen üstüne, yoksa gövdenin sonuna
        P = etree.SubElement(body, q("p")); body.remove(P)
        ppr = etree.SubElement(P, q("pPr")); jc = etree.SubElement(ppr, q("jc")); jc.set(q("val"), "center")
        rr = etree.SubElement(P, q("r")); rp = etree.SubElement(rr, q("rPr"))
        etree.SubElement(rp, q("i")); sz = etree.SubElement(rp, q("sz")); sz.set(q("val"), "16")
        co = etree.SubElement(rp, q("color")); co.set(q("val"), "666666")
        tt = etree.SubElement(rr, q("t")); tt.text = note
        tgt = [el for el in body if etree.QName(el).localname == "p" and "ONAYLAYANLAR" in _ptext(el).upper()]
        if tgt: tgt[0].addprevious(P)
        else:
            sp = body.find(q("sectPr"))
            (sp.addprevious(P) if sp is not None else body.append(P))
    xml = etree.tostring(r, xml_declaration=True, encoding="UTF-8", standalone=True)
    h2 = etree.fromstring(zin.read("word/header2.xml"))
    ts = [t for t in h2.iter(q("t"))]
    ts[0].text = d["title_tr"]
    if len(ts) > 1 and AR.search(ts[1].text or ""):
        ts[1].text = d["title_en"]
    hxml = etree.tostring(h2, xml_declaration=True, encoding="UTF-8", standalone=True)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zo:
        for i in zin.infolist():
            data = zin.read(i.filename)
            if i.filename == "word/document.xml": data = xml
            elif i.filename == "word/header2.xml": data = hxml
            zo.writestr(i, data)
    open(out, "wb").write(buf.getvalue())

if __name__ == "__main__":
    c = sys.argv[1]
    if c == "extract": extract(sys.argv[2], sys.argv[3])
    elif c == "build": build(sys.argv[2], sys.argv[3], sys.argv[4])
