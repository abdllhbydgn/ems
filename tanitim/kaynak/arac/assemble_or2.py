import json,subprocess,sys,os,numpy as np,wave
V='/tmp/claude-0/-home-user/5d050a5c-9efe-5868-b7c0-331c83134422/scratchpad/v4/'
SC=json.load(open('/home/user/ems/tanitim/oryantasyon.json'));XF=0.4;SR=44100
L='en'
def run(c):
    r=subprocess.run(c,capture_output=True,text=True)
    if r.returncode: print(' '.join(c)[:300],r.stderr[-800:]);sys.exit(1)
n=len(SC);metas=[json.load(open(V+f'orf/en2/{i:02d}/meta.json')) for i in range(1,n+1)]
os.makedirs(V+f'orc/en2',exist_ok=True)
for i,m in enumerate(metas,1):
    out=V+f'orc/en2/{i:02d}.mp4'
    if os.path.exists(out) and os.path.getmtime(out)>os.path.getmtime(V+f'orf/en2/{i:02d}/meta.json'): continue
    run(['ffmpeg','-y','-framerate','25','-i',V+f'orf/en2/{i:02d}/%05d.jpg','-c:v','libx264','-preset','veryfast','-crf','21','-g','50','-pix_fmt','yuv420p','-vf','scale=1920:1080:flags=lanczos',out])
ins=[];fc=[];lens=[m['frames']/25 for m in metas]
for i in range(n): ins+=['-i',V+f'orc/en2/{i+1:02d}.mp4']
prev='[0:v]';cum=lens[0]
for i in range(1,n):
    o=cum-XF;out=f'[x{i}]';fc.append(f"{prev}[{i}:v]xfade=transition=fade:duration={XF}:offset={o:.3f}{out}");prev=out;cum=o+lens[i]
run(['ffmpeg','-y']+ins+['-filter_complex',';'.join(fc),'-map',prev,'-c:v','libx264','-preset','veryfast','-crf','22','-g','50','-pix_fmt','yuv420p',V+f'orf_en2_silent.mp4'])
starts=[];t=0
for m in metas: starts.append(t);t+=m['frames']/25-XF
total=t+XF
N=int((total+1)*SR);narr=np.zeros(N,dtype=np.float32)
def pcm(f):
    r=subprocess.run(['ffmpeg','-v','error','-i',f,'-f','f32le','-ac','1','-ar',str(SR),'-'],capture_output=True);return np.frombuffer(r.stdout,dtype=np.float32)
for i,m in enumerate(metas):
    for k,(a,b) in enumerate(m['starts']):
        x=pcm(f'/home/user/ems/tanitim/audio3/{L}_{i+1:02d}_{k+1:02d}.mp3');p=int((starts[i]+a)*SR);narr[p:p+len(x)]+=x
mus=wave.open(V+'music.wav');mm=np.frombuffer(mus.readframes(mus.getnframes()),dtype=np.int16).reshape(-1,2).astype(np.float32)/32768;mus.close()
if len(mm)<N: mm=np.tile(mm,(N//len(mm)+1,1))
mm=mm[:N]
env=np.abs(narr);k=int(0.25*SR);env=np.convolve(env,np.ones(k)/k,mode='same');act=(env>0.012).astype(np.float32)
k2=int(0.5*SR);act=np.convolve(act,np.hanning(k2)/np.hanning(k2).sum(),mode='same');act=np.clip(act*1.6,0,1)
duck=1-0.78*act;g_m=0.42
Lc=narr+mm[:,0]*g_m*duck;Rc=narr+mm[:,1]*g_m*duck
peak=max(abs(Lc).max(),abs(Rc).max());g=0.92/peak if peak>0.92 else 1
out=(np.stack([Lc,Rc],1)*g*32767).astype(np.int16)
w=wave.open(V+f'orf_en2_mix.wav','wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes(out.tobytes());w.close()
run(['ffmpeg','-y','-i',V+f'orf_en2_silent.mp4','-i',V+f'orf_en2_mix.wav','-c:v','libx264','-preset','medium','-crf','27','-maxrate','3000k','-bufsize','6000k','-g','50','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',V+f'oryantasyon_en2.mp4'])
print('hazır',L,round(total,1))
