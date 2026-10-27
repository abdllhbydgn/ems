const { chromium } = require('playwright');const fs=require('fs'),vm=require('vm');
const src=fs.readFileSync(__dirname+'/../index.html','utf8');
const a=src.indexOf('const ORG_STEPS = [');const b=src.indexOf('\nORG_STEPS.forEach',a);
const ctx={};vm.createContext(ctx);vm.runInContext(src.slice(a,b).replace('const ORG_STEPS','var ORG_STEPS'),ctx);const ST=ctx.ORG_STEPS;
const gm='data:image/png;base64,'+fs.readFileSync(__dirname+'/gots_hd_1400.png').toString('base64');
const ems=/const EMS_REPORT_LOGO = "([^"]+)"/.exec(src)[1], emsW=/const EMS_REPORT_LOGO_WHITE = "([^"]+)"/.exec(src)[1];
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;');
const css=`@page{size:420mm 297mm;margin:0}*{box-sizing:border-box}body{margin:0;font-family:'Plus Jakarta Sans','Noto Sans','DejaVu Sans',Arial,sans-serif;color:#0f172a}
.pg{width:420mm;height:297mm;position:relative;overflow:hidden;background:#fff;page-break-after:always;border:14mm solid var(--c);}
.top{display:flex;align-items:center;justify-content:space-between;padding:10mm 16mm 0}.top img.g{height:44mm;border-radius:50%}.top img.e{height:30mm}
.kick{text-align:center;font-size:16pt;letter-spacing:3px;white-space:nowrap;font-weight:800;color:var(--c);margin-top:2mm}
.mid{display:flex;align-items:center;gap:18mm;padding:6mm 20mm 0}.num{flex:none;width:92mm;height:92mm;border-radius:50%;background:var(--c);color:#fff;display:grid;place-items:center;font-size:120pt;font-weight:900;box-shadow:0 0 0 6mm rgba(0,0,0,.08)}
.nm{flex:1}.tr{font-size:56pt;font-weight:900;line-height:1.08;color:var(--c)}.en{font-size:30pt;font-weight:700;margin-top:5mm;color:#334155}.ar{font-size:44pt;font-weight:800;margin-top:5mm;direction:rtl;text-align:right;color:#1e293b}
.rules{display:grid;grid-template-columns:repeat(3,1fr);gap:8mm;padding:10mm 20mm 0}.r{border:2px solid var(--c);border-radius:6mm;padding:6mm 7mm;background:var(--l);min-height:44mm}.r b{display:block;font-size:17pt;color:var(--c);margin-bottom:2mm}.r div{font-size:15pt;line-height:1.4}.r .a{direction:rtl;text-align:right;margin-top:2mm;font-size:16pt}
.bot span,.bot small{white-space:nowrap}.bot{position:absolute;left:0;right:0;bottom:0;height:24mm;background:var(--c);color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 18mm;font-size:14pt;font-weight:800;letter-spacing:.5px}
.bot small{font-weight:600;font-size:13pt;opacity:.9}`;
const colors={g:['#14532d','#ecfdf5'],b:['#1d4ed8','#eff6ff'],y:['#b45309','#fffbeb'],r:['#b91c1c','#fef2f2']};
function page(o){const [c,l]=colors[o.col||'g'];
 return `<div class="pg" style="--c:${c};--l:${l}"><div class="top"><img class="g" src="${gm}"><div style="text-align:center"><div class="kick">${esc(o.kick)}</div></div><img class="e" src="${ems}"></div>
 <div class="mid">${o.num!=null?`<div class="num">${o.num}</div>`:`<div class="num" style="font-size:96pt">${o.sym}</div>`}<div class="nm"><div class="tr">${esc(o.tr)}</div><div class="en">${esc(o.en)}</div><div class="ar">${esc(o.ar)}</div></div></div>
 <div class="rules">${o.rules.map(r=>`<div class="r"><b>${esc(r[0])}</b><div>${esc(r[1])}</div><div class="a">${esc(r[2])}</div></div>`).join('')}</div>
 <div class="bot"><span>${esc(o.foot[0])}</span><small>${esc(o.foot[1])}</small></div></div>`;}
const FOOT=['ORGANİK ÜRÜN · ORGANIC PRODUCT · منتج عضوي','EMS Eroğlu Manufacturing Studio · www.eroglumanufacturing.com'];
const TRH=['Uygulama','Practice','التطبيق'];
const pages=[];
ST.forEach((s,i)=>{const n=String(i+1).padStart(2,'0');
 const rules=s.rules.slice(0,3).map(r=>[TRH[0]+' '+(0),r[0],r[2]]);
 // heading per rule: numbered
 const rr=s.rules.slice(0,3).map((r,k)=>[String(k+1)+'. '+['Kural','Rule','القاعدة'][0]+' / Rule / القاعدة',r[0]+'\n'+r[1],r[2]]);
 pages.push({file:`${n}`,html:page({kick:'ORGANİK ÜRÜN ÜRETİM ALANI · ORGANIC PRODUCTION AREA',col:'g',num:i+1,tr:s.n[0].toLocaleUpperCase('tr'),en:s.n[1].toUpperCase(),ar:s.n[2],rules:s.rules.slice(0,3).map((r,k)=>[`${k+1}`,r[0]+' — '+r[1],r[2]]),foot:FOOT}),name:s.n[0]});});
const G=[
 {file:'A1',col:'g',sym:'✔',kick:'RENK KODU · COLOUR CODE',tr:'ORGANİK ÜRÜN ALANI',en:'ORGANIC PRODUCT AREA',ar:'مكان المنتج العضوي',rules:[['1','Yalnızca sertifikalı organik malzeme.','Only certified organic material.','خامات عضوية معتمدة بس.'],['2','Konvansiyonel malzeme girmez.','No conventional material.','ممنوع دخول أي خامات تقليدية.'],['3','Etiketli ve izlenebilir olmalıdır.','Labelled and traceable.','لازم تكون متعلّمة وتتتبّع.']]},
 {file:'A2',col:'b',sym:'■',kick:'RENK KODU · COLOUR CODE',tr:'KONVANSİYONEL ALAN',en:'CONVENTIONAL AREA',ar:'المكان التقليدي',rules:[['1','Yalnızca konvansiyonel malzeme.','Conventional material only.','خامات تقليدية بس.'],['2','Organik malzeme bırakılmaz.','Do not leave organic material here.','ما تسيبش خامات عضوية هنا.'],['3','Organik alana araç/gereç taşınmaz.','Do not carry tools to the organic area.','ما تنقلش الأدوات لمكان العضوي.']]},
 {file:'A3',col:'y',sym:'!',kick:'RENK KODU · COLOUR CODE',tr:'BEKLETME / KARANTİNA ALANI',en:'HOLDING / QUARANTINE AREA',ar:'مكان الانتظار والحجز',rules:[['1','Etiketsiz veya şüpheli malzeme burada bekler.','Unlabelled or doubtful material waits here.','الخامات اللي من غير ملصق أو مشكوك فيها بتستنى هنا.'],['2','Neden ve tarih etikete yazılır.','Reason and date are written on the tag.','السبب والتاريخ بيتكتبوا على الكارت.'],['3','Karar gelene kadar kullanılmaz.','Do not use until a decision is made.','ما تتستخدمش لحد ما يطلع القرار.']]},
 {file:'A4',col:'r',sym:'✖',kick:'RENK KODU · COLOUR CODE',tr:'UYGUN OLMAYAN / BLOKE ÜRÜNLER',en:'NON-CONFORMING / BLOCKED PRODUCTS',ar:'منتجات مش مطابقة (محجوزة)',rules:[['1','Organik olarak kullanılamaz.','Must not be used as organic.','ما تتستخدمش كعضوي.'],['2','Uygunsuzluk kaydı açılır.','A nonconformity record is opened.','بيتفتح تقرير عدم مطابقة.'],['3','Kalite onayı olmadan çıkış yapılmaz.','No release without Quality approval.','ما تطلعش من غير موافقة الجودة.']]}];
G.forEach(g=>pages.push({file:g.file,name:g.tr,html:page({kick:g.kick,col:g.col,sym:g.sym,tr:g.tr,en:g.en,ar:g.ar,rules:g.rules.map(r=>[r[0],r[1]+' — '+r[2],r[3]]),foot:FOOT})}));
(async()=>{const b=await chromium.launch();const p=await b.newPage();
 const all=[];
 for(const pg of pages){const html=`<!doctype html><meta charset="utf-8"><style>${css}</style><body>${pg.html}</body>`;
  await p.setContent(html,{waitUntil:'load'});await p.waitForTimeout(150);
  const tr={ı:'i',ğ:'g',ü:'u',ş:'s',ö:'o',ç:'c',İ:'I',Ğ:'G',Ü:'U',Ş:'S',Ö:'O',Ç:'C'};const slug=pg.name.replace(/[ığüşöçİĞÜŞÖÇ]/g,m=>tr[m]).replace(/[^A-Za-z0-9]+/g,'_').replace(/^_|_$/g,'');
  const fn=`Tabela_${pg.file}_${slug}.pdf`;
  await p.pdf({path:(process.env.OUT||__dirname+'/../organik/tabelalar/')+fn,width:'420mm',height:'297mm',printBackground:true});
  if(/^\d+$/.test(pg.file)||1)all.push(pg.html);
  if(pg.file==='05'||pg.file==='A3'){await p.screenshot({path:process.env.S+'/sign_'+pg.file+'.png',fullPage:false});}
  console.log(fn);}
 await p.setContent(`<!doctype html><meta charset="utf-8"><style>${css}</style><body>${all.join('')}</body>`,{waitUntil:'load'});
 await p.pdf({path:__dirname+'/../organik/tabelalar/Organik_Alan_Tabelalari_A3_Tumu.pdf',width:'420mm',height:'297mm',printBackground:true});
 await b.close();})();
