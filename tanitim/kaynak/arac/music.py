import numpy as np, wave, sys
SR=44100;DUR=float(sys.argv[1]) if len(sys.argv)>1 else 480
BPM=112;beat=60/BPM
rng=np.random.default_rng(7)
N=int(DUR*SR);L=np.zeros(N);Rr=np.zeros(N)
def add(buf,start,sig,gain=1.0):
    i=int(start*SR);j=min(N,i+len(sig))
    if i<N: buf[i:j]+=sig[:j-i]*gain
def env(n,a,r):
    e=np.ones(n);ai=int(a*SR);ri=int(r*SR)
    if ai>0:e[:ai]=np.linspace(0,1,ai)
    if ri>0:e[-ri:]=np.linspace(1,0,ri)
    return e
def note(f,d,kind='pluck'):
    n=int(d*SR);t=np.arange(n)/SR
    if kind=='pad':
        s=sum(np.sin(2*np.pi*f*(1+k*0.004)*t+k) for k in range(3))/3+0.3*np.sin(2*np.pi*f*2*t)
        return s*env(n,0.6,0.8)
    if kind=='bass':
        s=np.sin(2*np.pi*f*t)+0.4*np.sin(2*np.pi*2*f*t)
        return s*np.exp(-t*3.0)*env(n,0.005,0.05)
    s=np.sign(np.sin(2*np.pi*f*t))*0.25+np.sin(2*np.pi*f*t)*0.6+0.2*np.sin(2*np.pi*2*f*t)
    return s*np.exp(-t*7)*env(n,0.003,0.03)
def kick():
    n=int(0.25*SR);t=np.arange(n)/SR;f=120*np.exp(-t*22)+45
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*14)
def hat():
    n=int(0.05*SR);return rng.standard_normal(n)*np.exp(-np.arange(n)/SR*90)
def clap():
    n=int(0.18*SR);return rng.standard_normal(n)*np.exp(-np.arange(n)/SR*28)
# Am - F - C - G (her akor 4 vuruş)
prog=[(220.0,[220.0,261.63,329.63]),(174.61,[174.61,220.0,261.63]),(261.63,[261.63,329.63,392.0]),(196.0,[196.0,246.94,293.66])]
bars=int(DUR/(beat*4))+1
for b in range(bars):
    t0=b*beat*4
    root,chord=prog[b%4]
    # sahne yoğunluğu: yavaş yükselen enerji (8 ölçülük döngü)
    phase=(b%16)
    # pad
    for f in chord: add(L,t0,note(f/2,beat*4,'pad'),0.05);add(Rr,t0,note(f/2*1.003,beat*4,'pad'),0.05)
    # bas
    for q in range(4):
        add(L,t0+q*beat,note(root/2,beat*0.9,'bass'),0.20);add(Rr,t0+q*beat,note(root/2,beat*0.9,'bass'),0.20)
    # arpej (8'likler)
    if phase>=2:
        pat=[0,1,2,1,2,1,0,1]
        for q in range(8):
            f=chord[pat[q]]*2
            pan=0.5+0.4*np.sin(q+b)
            add(L,t0+q*beat/2,note(f,beat*0.5),0.07*(1-pan));add(Rr,t0+q*beat/2,note(f,beat*0.5),0.07*pan)
    # vuruş
    if phase>=4:
        for q in range(4): add(L,t0+q*beat,kick(),0.34);add(Rr,t0+q*beat,kick(),0.34)
        for q in range(8): add(L,t0+q*beat/2+beat/4,hat(),0.05);add(Rr,t0+q*beat/2+beat/4,hat(),0.05)
        for q in (1,3): add(L,t0+q*beat,clap(),0.07);add(Rr,t0+q*beat,clap(),0.07)
# giriş-çıkış yumuşatma
fade=int(3*SR);L[:fade]*=np.linspace(0,1,fade);Rr[:fade]*=np.linspace(0,1,fade);L[-fade*2:]*=np.linspace(1,0,fade*2);Rr[-fade*2:]*=np.linspace(1,0,fade*2)
m=max(abs(L).max(),abs(Rr).max());L/=m;Rr/=m
out=(np.stack([L,Rr],1)*0.85*32767).astype(np.int16)
w=wave.open('music.wav','wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes(out.tobytes());w.close()
print('ok')
