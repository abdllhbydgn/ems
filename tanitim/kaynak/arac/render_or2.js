const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs=require('fs'),cp=require('child_process');
const ENGJS=require('./eng.js');
const SC=JSON.parse(fs.readFileSync('/home/user/ems/tanitim/oryantasyon.json','utf8'));
const logo='data:image/png;base64,'+fs.readFileSync('logo.png').toString('base64');
const FPS=25,LEAD=0.9,GAP=0.5,TAIL=1.0;
const dur=f=>parseFloat(cp.execSync(`ffprobe -v error -show_entries format=duration -of csv=p=0 ${f}`).toString());
function plan(L,i){
  const s=SC[i];let t=LEAD;
  const sentences=s.s.map((row,k)=>{const d=dur(`/home/user/ems/tanitim/audio3/${L}_${String(i+1).padStart(2,'0')}_${String(k+1).padStart(2,'0')}.mp3`);const o={start:t,end:t+d,show:row.show,targets:[]};o.tr=row.tr;o.ar=row.ar;t+=d+GAP;return o});
  return {sentences,total:t-GAP+TAIL,chapter:'',cards:true};
}
const HL=(a,b)=>`@keyframes hl_${a.toString().replace('.','_')}{0%{opacity:0}6%{opacity:1}94%{opacity:1}100%{opacity:0}}`;
function slide(L,i,P){
  const s=SC[i],rtl=L==='ar';const n=s.bullets.length;
  // her kutu için ilk gösterim ve vurgu aralıkları
  const first={},hls={};P.sentences.forEach((sn,k)=>{(sn.show||[]).forEach(b=>{if(first[b]==null)first[b]=sn.start;(hls[b]=hls[b]||[]).push([sn.start,sn.end])})});
  let css='',cards='';
  s.bullets.forEach((b,idx)=>{
    const t0=first[idx]!=null?first[idx]:P.total+5;
    let ov='';(hls[idx]||[]).forEach((h,j)=>{const nm=`h${idx}_${j}`;css+=`@keyframes ${nm}{0%{opacity:0}8%{opacity:1}92%{opacity:1}100%{opacity:0}}`;ov+=`<div class="ov" style="animation:${nm} ${(h[1]-h[0]+0.2).toFixed(2)}s ${(h[0]-0.1).toFixed(2)}s both"></div>`});
    cards+=`<div class="card" style="animation:pop .6s ${t0.toFixed(2)}s both"><div class="ic">${b.icon}</div><div class="tx">${b[L]}</div>${ov}</div>`;
  });
  const cols=n<=3?n:n===4?2:3;
  return `<style>*{box-sizing:border-box;margin:0}#fx-cur,#fx-ring,#fx-lab,#fx-rip,#fx-chap{display:none!important}html{overflow:hidden;width:1280px;height:720px}body{width:1280px;height:720px;font-family:'DejaVu Sans',Arial,sans-serif;overflow:hidden;background:linear-gradient(135deg,#fff 0%,#eef2f7 100%);position:relative}
.bar{position:absolute;left:0;top:0;height:8px;background:#E11D2E;animation:w 1.2s ease-out both;width:100%;transform-origin:${rtl?'right':'left'}}@keyframes w{from{transform:scaleX(0)}to{transform:none}}
.b1,.b2{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(225,29,46,.10),rgba(225,29,46,0));animation:fl 9s ease-in-out infinite}.b1{width:520px;height:520px;${rtl?'left':'right'}:-120px;top:-140px}.b2{width:420px;height:420px;${rtl?'right':'left'}:-100px;bottom:-160px;animation-delay:-4s;background:radial-gradient(circle,rgba(15,42,92,.10),rgba(15,42,92,0))}@keyframes fl{0%,100%{transform:translateY(0)}50%{transform:translateY(24px)}}
.head{position:absolute;top:28px;left:48px;right:48px;display:flex;align-items:center;justify-content:space-between}.head img{height:54px;animation:u .8s .1s both}.num{direction:ltr;font-size:18px;font-weight:800;color:#fff;background:#0f2a5c;padding:7px 16px;border-radius:99px;animation:u .8s .2s both}
.ttl{position:absolute;top:112px;left:48px;right:48px;display:flex;align-items:center;gap:22px;animation:u .9s .3s both}.big{width:104px;height:104px;border-radius:26px;background:#fff;box-shadow:0 12px 34px rgba(15,23,42,.14);border-bottom:6px solid #E11D2E;display:grid;place-items:center;font-size:58px;flex:none}.ttl h1{font-size:${L==='ar'?54:50}px;font-weight:800;color:#0f172a;line-height:1.15}
.grid{position:absolute;top:262px;left:48px;right:48px;display:grid;grid-template-columns:repeat(${cols},1fr);gap:20px}
.card{position:relative;background:#fff;border-radius:20px;padding:22px 24px;display:flex;align-items:center;gap:18px;box-shadow:0 10px 30px rgba(15,23,42,.10);border-${rtl?'right':'left'}:7px solid #0f2a5c;min-height:112px;opacity:0}
.ic{font-size:44px;flex:none}.tx{font-size:${L==='ar'?27:25}px;font-weight:700;color:#0f172a;line-height:1.3}
.ov{position:absolute;inset:-5px;border:5px solid #E11D2E;border-radius:24px;box-shadow:0 0 26px rgba(225,29,46,.45);opacity:0;pointer-events:none}
@keyframes pop{from{opacity:0;transform:translateY(34px) scale(.92)}to{opacity:1;transform:none}}@keyframes u{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}${css}</style>
<div class="bar"></div><div class="b1"></div><div class="b2"></div>
<div class="head"><img src="${logo}"><div class="num">${String(i+1).padStart(2,'0')} / ${String(SC.length).padStart(2,'0')}</div></div>
<div class="ttl"><div class="big">${s.icon}</div><h1>${s.title[L]}</h1></div><div class="grid">${cards}</div>`;
}
async function renderScene(b,L,i){
  const P=plan(L,i);const n=String(i+1).padStart(2,'0');const dir=`orf/en2/${n}`;
  if(fs.existsSync(dir+'/meta.json')){console.log('skip',L,n);return}
  fs.mkdirSync(dir,{recursive:true});
  const ctx=await b.newContext({viewport:{width:1280,height:720},deviceScaleFactor:1.5});const p=await ctx.newPage();
  await p.setContent(`<html dir="${L==='ar'?'rtl':'ltr'}"><body>`+'</body></html>');
  await p.setContent(slide(L,i,P));
  if(L==='ar')await p.evaluate(()=>{document.documentElement.dir='rtl';document.body.dir='rtl'});
  await p.evaluate(ENGJS);await p.evaluate(pl=>window.ENG.init(pl),P);
  const N=Math.ceil(P.total*FPS);
  for(let f=0;f<N;f++){
    await p.evaluate(t=>window.ENG.render(t),f/FPS);
    await p.screenshot({path:`${dir}/${String(f).padStart(5,'0')}.jpg`,type:'jpeg',quality:90});
  }
  await ctx.close();
  fs.writeFileSync(`${dir}/meta.json`,JSON.stringify({frames:N,total:P.total,starts:P.sentences.map(x=>[x.start,x.end])}));
  console.log('scene',L,n,N);
}
(async()=>{
  const L=process.argv[2];const only=process.argv[3]?process.argv[3].split(',').map(Number):SC.map((_,i)=>i+1);const maxN=0;
  const b=await chromium.launch();
  for(const n of only){try{await renderScene(b,L,n-1)}catch(e){console.log('FAIL',L,n,e.message)}}
  await b.close();
})();
