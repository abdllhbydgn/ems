const { chromium } = require('playwright');const fs=require('fs'),vm=require('vm');
const src=fs.readFileSync(__dirname+'/../index.html','utf8');
const a=src.indexOf('const ORG_STEPS = [');const b=src.indexOf('\nORG_STEPS.forEach',a);
const ctx={};vm.createContext(ctx);vm.runInContext(src.slice(a,b).replace('const ORG_STEPS','var ORG_STEPS'),ctx);const ST=ctx.ORG_STEPS;
const gm='data:image/png;base64,'+fs.readFileSync(__dirname+'/gots_hd_1400.png').toString('base64');
const emsC=/const EMS_REPORT_LOGO = "([^"]+)"/.exec(src)[1];
const emsW=/const EMS_REPORT_LOGO_WHITE = "([^"]+)"/.exec(src)[1];
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;');
const css=`@page{size:1000mm 400mm;margin:0}*{box-sizing:border-box}html,body{margin:0}body{font-family:'Plus Jakarta Sans','Noto Sans','DejaVu Sans',Arial,sans-serif}
.sg{width:1000mm;height:400mm;position:relative;overflow:hidden;background:linear-gradient(135deg,var(--c1),var(--c2));color:#fff;page-break-after:always}
.sg:before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(115deg,rgba(255,255,255,.04) 0 3mm,transparent 3mm 18mm)}
.fr{position:absolute;inset:14mm;border:5mm solid #fff;border-radius:22mm}
.in{position:absolute;inset:34mm 46mm 34mm 46mm;display:flex;align-items:center;gap:36mm}
.lf{flex:none;display:flex;flex-direction:column;align-items:center;gap:40mm}
.gl{width:132mm;height:132mm}.gl img{width:132mm;height:132mm;display:block}
.no{width:100mm;height:100mm;border-radius:50%;background:#fff;color:var(--c1);font-size:150pt;line-height:1;font-weight:900;display:grid;place-items:center;padding:0;letter-spacing:-2mm}
.tx{flex:1;min-width:0}.tr{font-size:104pt;font-weight:900;line-height:1.05;letter-spacing:.5px}.ln{height:3mm;background:rgba(255,255,255,.7);border-radius:2mm;margin:9mm 0}
.en{font-size:56pt;font-weight:700;opacity:.95}.ar{font-size:88pt;font-weight:800;direction:rtl;text-align:right;margin-top:8mm}
.rt{flex:none;display:flex;flex-direction:column;align-items:center;gap:12mm}.ic{width:150mm;height:150mm;border-radius:30mm;background:#fff;display:grid;place-items:center;padding:18mm}.ic img{width:100%;height:100%;object-fit:contain;display:block}
.em{height:34mm}
.ft{position:absolute;left:0;right:0;bottom:20mm;text-align:center;font-size:17pt;letter-spacing:6px;font-weight:700;opacity:.92}`;
const COL={g:['#14532d','#1d7a45'],b:['#1d4ed8','#2563eb'],y:['#a16207','#ca8a04'],r:['#991b1b','#dc2626']};
function sign(o){const [c1,c2]=COL[o.col||'g'];return `<div class="sg" style="--c1:${c1};--c2:${c2}"><div class="fr"></div><div class="in"><div class="lf"><div class="gl"><img src="${gm}"></div>${o.no!=null?`<div class="no">${o.no}</div>`:''}</div><div class="tx"><div class="tr">${esc(o.tr)}</div><div class="ln"></div><div class="en">${esc(o.en)}</div><div class="ar">${esc(o.ar)}</div></div><div class="rt"><div class="ic"><img src="${emsC}"></div></div></div><div class="ft">ORGANİK ÜRÜN · ORGANIC PRODUCT · منتج عضوي</div></div>`;}
const items=ST.map((s,i)=>({file:String(i+1).padStart(2,'0'),html:sign({col:'g',no:i+1,tr:s.n[0].toLocaleUpperCase('tr'),en:s.n[1].toUpperCase(),ar:s.n[2],ic:s.ic}),name:s.n[0]}));
const GEN=[['A1','g','🟢','ORGANİK ÜRÜN ALANI','ORGANIC PRODUCT AREA','مكان المنتج العضوي'],['A2','b','🔵','KONVANSİYONEL ALAN','CONVENTIONAL AREA','المكان التقليدي'],['A3','y','🟡','BEKLETME / KARANTİNA ALANI','HOLDING / QUARANTINE AREA','مكان الانتظار والحجز'],['A4','r','🔴','UYGUN OLMAYAN / BLOKE ÜRÜNLER','NON-CONFORMING / BLOCKED PRODUCTS','منتجات مش مطابقة (محجوزة)']];
GEN.forEach(g=>items.push({file:g[0],name:g[3],html:sign({col:g[1],ic:g[2],tr:g[3],en:g[4],ar:g[5]})}));
(async()=>{const br=await chromium.launch();const p=await br.newPage();
 const tr={ı:'i',ğ:'g',ü:'u',ş:'s',ö:'o',ç:'c',İ:'I',Ğ:'G',Ü:'U',Ş:'S',Ö:'O',Ç:'C'};
 const OUT=(process.env.OUT||__dirname+'/../organik/tabelalar/asma/');
 for(const it of items){
  await p.setContent(`<!doctype html><meta charset="utf-8"><style>${css}</style><body>${it.html}</body>`,{waitUntil:'load'});await p.waitForTimeout(200);
  const slug=it.name.replace(/[ığüşöçİĞÜŞÖÇ]/g,m=>tr[m]).replace(/[^A-Za-z0-9]+/g,'_').replace(/^_|_$/g,'');
  const fn=`Asma_${it.file}_${slug}.pdf`;await p.pdf({path:OUT+fn,width:'1000mm',height:'400mm',printBackground:true});console.log(fn);}
 await p.setContent(`<!doctype html><meta charset="utf-8"><style>${css}</style><body>${items.map(x=>x.html).join('')}</body>`,{waitUntil:'load'});
 await p.pdf({path:OUT+'Asma_Tabelalar_Tumu_100x40cm.pdf',width:'1000mm',height:'400mm',printBackground:true});
 await br.close();})();
