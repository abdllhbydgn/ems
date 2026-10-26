module.exports=`(()=>{
if(window.ENG)return;
const st=document.createElement('style');st.textContent=\`
#fx-cur{position:fixed;left:0;top:0;z-index:2147483600;pointer-events:none;width:30px;height:30px;filter:drop-shadow(0 3px 4px rgba(0,0,0,.45))}
#fx-ring{position:fixed;z-index:2147483500;pointer-events:none;border:4px solid #E11D2E;border-radius:14px;box-shadow:0 0 0 6000px rgba(8,12,24,.36),0 0 24px 5px rgba(225,29,46,.65);opacity:0}
#fx-lab{position:fixed;z-index:2147483550;pointer-events:none;background:#E11D2E;color:#fff;font:800 20px/1.25 Arial,sans-serif;padding:9px 16px;border-radius:11px;box-shadow:0 8px 22px rgba(0,0,0,.4);opacity:0;white-space:nowrap}
#fx-rip{position:fixed;z-index:2147483580;pointer-events:none;border:4px solid #E11D2E;border-radius:50%;opacity:0}
#fx-cap{position:fixed;left:6%;right:6%;bottom:18px;z-index:2147483640;pointer-events:none;text-align:center;opacity:0}
#fx-cap div{display:block;margin-top:5px}#fx-cap span{display:inline-block;background:rgba(8,12,24,.86);color:#fff;font-weight:700;line-height:1.35;padding:6px 16px;border-radius:10px;font-family:Arial,sans-serif}
#fx-cap .tr span{font-size:21px;color:#fff}#fx-cap .ar span{font-size:23px;color:#ffe9a8}
#fx-chap{position:fixed;left:18px;bottom:128px;z-index:2147483630;pointer-events:none;background:#E11D2E;color:#fff;font:800 17px Arial,sans-serif;padding:7px 14px;border-radius:99px;box-shadow:0 6px 18px rgba(0,0,0,.35);opacity:0}
\`;document.head.appendChild(st);
const mk=(id,h)=>{const e=document.createElement('div');e.id=id;if(h)e.innerHTML=h;document.body.appendChild(e);return e};
const cur=mk('fx-cur','<svg viewBox="0 0 24 24" width="30" height="30"><path d="M3 2l7 19 3-8 8-3z" fill="#111827" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/></svg>');
const ring=mk('fx-ring'),lab=mk('fx-lab'),rip=mk('fx-rip'),cap=mk('fx-cap'),chap=mk('fx-chap');
cur.style.transform='translate(640px,500px)';
const ease=k=>k<=0?0:k>=1?1:k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2;
const lerp=(a,b,k)=>a+(b-a)*k;
function leafMatch(root,t){t=t.toLowerCase();const all=[...root.querySelectorAll('*')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0&&(e.textContent||'').toLowerCase().includes(t)});return all.filter(e=>![...e.children].some(c=>all.includes(c)))}
function find(sp){
 let els;
 if(sp.t){const roots=[...document.querySelectorAll(sp.q||'body')];els=[];roots.forEach(r=>{els=els.concat(leafMatch(r,sp.t))});}
 else els=[...document.querySelectorAll(sp.q)].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0});
 let e=els[sp.i||0];if(!e)return null;for(let k=0;k<(sp.up||0);k++)if(e.parentElement)e=e.parentElement;return e}
function scroller(e){let c=e.parentElement;while(c&&c!==document.body){const cs=getComputedStyle(c);if((cs.overflowY==='auto'||cs.overflowY==='scroll')&&c.scrollHeight>c.clientHeight+20)return c;c=c.parentElement}return document.scrollingElement}
const E=window.ENG={
 check(t){const S=E.s;if(S.idx<0||t<S.items[S.idx].start+.85||t>S.items[S.idx].end)return {ok:true,idx:-1,op:0};const r=document.getElementById('fx-ring');const x=parseFloat(r.style.left),y=parseFloat(r.style.top),w=parseFloat(r.style.width),h=parseFloat(r.style.height);const c=S.cur;const ok=c.x>=x-4&&c.x<=x+w+4&&c.y>=y-4&&c.y<=y+h+4;return {ok,c:[Math.round(c.x),Math.round(c.y)],r:[Math.round(x),Math.round(y),Math.round(w),Math.round(h)],idx:S.idx,op:r.style.opacity}},
 init(plan){E.plan=plan;E.s={idx:-1,cur:{x:640,y:500},pc:{x:640,y:500},pr:null,pa:0,items:[],scr:null,fired:{},sfired:{},scrs:[],lastR:null};
  // düzleştir
  const items=[];plan.sentences.forEach((s,k)=>{const n=(s.targets||[]).length;(s.targets||[]).forEach((tg,i)=>{items.push({start:s.start+i*(s.end-s.start)/n,end:s.start+(i+1)*(s.end-s.start)/n,sp:tg,k})})});E.s.items=items},
 render(t){
  const P=E.plan,S=E.s;let settle=false;
  // cümle başı pre
  P.sentences.forEach((s,k)=>{if(t>=s.start&&!S.sfired[k]){S.sfired[k]=1;if(s.pre){try{(new Function(s.pre))()}catch(e){}settle=true}}
   (s.pres||[]).forEach((pp,j)=>{const key='pp'+k+'_'+j;if(t>=s.start+pp.at&&!S.sfired[key]){S.sfired[key]=1;try{(new Function(pp.js))()}catch(er){}settle=true}});
   (s.scrolls||[]).forEach((sc,j)=>{const key=k+'_'+j;if(t>=s.start+(sc.at||0)&&!S.fired[key]){const el=sc.q==='win'?document.scrollingElement:document.querySelector(sc.q);if(el){S.fired[key]=1;S.scrs.push({el,from:el.scrollTop,to:sc.to,t0:s.start+(sc.at||0),dur:sc.dur||2})}}})});
  if(settle)return {settle:true};
  // aktif hedef
  let idx=-1;for(let i=0;i<S.items.length;i++)if(t>=S.items[i].start)idx=i;
  if(idx!==S.idx){S.pc={x:S.cur.x,y:S.cur.y};S.pr=S.lastR?{...S.lastR}:null;S.idx=idx;S.arr=false;
    if(idx>=0){const it=S.items[idx];const el=find(it.sp);if(el){const r=el.getBoundingClientRect();if((r.top<80||r.bottom>650)&&!S.fired['q'+idx]){const sc=scroller(el);S.scrs.push({el:sc,from:sc.scrollTop,to:Math.max(0,sc.scrollTop+r.top-200),t0:it.start,dur:.8})}}}
  }
  // sonraki hedef görünür değilse, ondan 1 sn önce kaydırmaya başla (imleç hedefe vardığında hedef yerinde olsun)
  for(let i=Math.max(0,idx+1);i<S.items.length&&i<=idx+1;i++){const nx=S.items[i];if(!S.fired['p'+i]&&t>=nx.start-1.0){S.fired['p'+i]=1;const el2=find(nx.sp);if(el2){const r2=el2.getBoundingClientRect();if(r2.top<80||r2.bottom>650){const sc2=scroller(el2);S.scrs.push({el:sc2,from:sc2.scrollTop,to:Math.max(0,sc2.scrollTop+r2.top-200),t0:Math.max(t,nx.start-1.0),dur:.85});S.fired['q'+i]=1}}}}
  // kaydırmalar
  S.scrs.forEach(a=>{const k=ease((t-a.t0)/a.dur);a.el.scrollTop=lerp(a.from,a.to,k)});
  let ringA=0,label='';
  if(idx>=0){const it=S.items[idx];const el=find(it.sp);
   if(el){const r=el.getBoundingClientRect();const pad=it.sp.pad==null?8:it.sp.pad;
     const tg={x:r.left-pad,y:r.top-pad,w:r.width+pad*2,h:r.height+pad*2};
     const cx=Math.min(r.left+Math.min(r.width*.55,160),innerWidth-30),cy=Math.min(r.top+r.height*.5,innerHeight-60);
     const mv=Math.min(.75,(it.end-it.start)*.5);const k=ease((t-it.start)/mv);
     const from=S.pr||tg;
     const rr={x:lerp(from.x,tg.x,k),y:lerp(from.y,tg.y,k),w:lerp(from.w,tg.w,k),h:lerp(from.h,tg.h,k)};
     S.cur={x:lerp(S.pc.x,cx,k),y:lerp(S.pc.y,cy,k)};
     S.lastR=tg;
     ringA=Math.min(1,(t-it.start)/.25)*(t<=it.end?1:Math.max(0,1-(t-it.end)/.3));
     ring.style.left=rr.x+'px';ring.style.top=rr.y+'px';ring.style.width=rr.w+'px';ring.style.height=rr.h+'px';
     if(it.sp.label&&t<=it.end+.1){label=it.sp.label;lab.style.left=Math.max(10,Math.min(rr.x,innerWidth-300))+'px';lab.style.top=Math.max(8,Math.min(rr.y+rr.h+16,innerHeight-190))+'px'}
     const arr=it.start+Math.min(.75,(it.end-it.start)*.5);
     if(t>=arr&&!S.fired['a'+idx]){S.fired['a'+idx]=1;if(it.sp.act==='click'){el.click();settle=true}}
     if(it.sp.type&&t>=arr){const inp=el;const n=Math.floor(Math.min(1,(t-arr)/Math.max(.4,it.end-arr-.2))*it.sp.type.length);const v=it.sp.type.slice(0,n);if(inp.value!==v){inp.value=v;inp.dispatchEvent(new Event('input',{bubbles:true}))}}
     if(it.sp.click){const q=t-arr;if(q>=0&&q<.6){rip.style.left=(S.cur.x-8-q*70)+'px';rip.style.top=(S.cur.y-8-q*70)+'px';rip.style.width=(16+q*140)+'px';rip.style.height=(16+q*140)+'px';rip.style.opacity=String(1-q/.6)}else rip.style.opacity='0'}else rip.style.opacity='0';
   }}
  else rip.style.opacity='0';
  ring.style.opacity=String(ringA);
  lab.textContent=label;lab.style.opacity=label?String(Math.min(1,ringA*1.2)):'0';
  cur.style.transform='translate('+S.cur.x+'px,'+S.cur.y+'px)';
  // altyazı
  let ci=-1;P.sentences.forEach((s,k)=>{if(t>=s.start-.05&&t<=s.end+.35)ci=k});
  if(ci>=0&&P.sentences[ci].tr!==undefined){const s=P.sentences[ci];const a=Math.min(1,(t-s.start+.05)/.2)*Math.min(1,(s.end+.35-t)/.2);cap.innerHTML=(s.tr?'<div class="tr"><span>'+s.tr+'</span></div>':'')+(s.ar?'<div class="ar" dir="rtl"><span>'+s.ar+'</span></div>':'');cap.style.opacity=String(Math.max(0,Math.min(1,a)))}else cap.style.opacity='0';
  chap.textContent=P.chapter||'';chap.style.opacity=P.chapter?String(Math.min(1,t/.5)):'0';
  // deterministik animasyonlar
  try{document.getAnimations().forEach(a=>{const ef=a.effect&&a.effect.getComputedTiming?a.effect.getComputedTiming():null;if(P.cards||(ef&&ef.iterations===Infinity)){try{a.pause();a.currentTime=t*1000}catch(e){}}})}catch(e){}
  return {settle:settle};
 }
};})();`;
