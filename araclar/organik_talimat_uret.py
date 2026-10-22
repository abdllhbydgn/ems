import zipfile,re,sys,copy,os
from xml.sax.saxutils import escape
from lxml import etree
import content as C
TPL="/home/user/ems/prosedurler/EMS.OR.TL.21.01. Organic Product Identification and Labelling Instruction.docx"
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
q=lambda t:'{%s}%s'%(W,t)
RF='<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Arial"/>'
def run(t,b=False,rtl=False):
    return '<w:r><w:rPr>%s%s%s<w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r>'%(RF,'<w:b/><w:bCs/>' if b else '','<w:rtl/>' if rtl else '',escape(t))
def para(runs,rtl=False,ind=True,num=False,spacing='80'):
    ppr='<w:pStyle w:val="ListeParagraf"/>'
    if num: ppr+='<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
    if rtl: ppr+='<w:bidi/>'
    ppr+='<w:spacing w:after="%s"/>'%('60' if num else spacing)
    if ind and not num: ppr+='<w:ind w:left="%d" w:right="%d"/>'%((0,709) if rtl else (709,0))
    ppr+='<w:jc w:val="both"/>'
    return '<w:p xmlns:w="%s"><w:pPr>%s</w:pPr>%s</w:p>'%(W,ppr,''.join(runs))
def head(t,rtl): return para([run(t,True,rtl)],rtl,spacing='60').replace('<w:spacing w:after="60"/>','<w:spacing w:before="120" w:after="60"/>')
def text(t,rtl): return para([run(t,False,rtl)],rtl)
def blank(rtl): return para([],rtl)
def bullet(lbl,t,rtl): return para([run('• ',False,rtl),run(lbl,True,rtl),run(' '+t,False,rtl)],rtl)
def li(t,rtl): return para([run(t,False,rtl)],rtl,num=True)
def build_lang(i,lang):
    s=C.STEPS[i];rtl=(lang=='ar');L=1 if lang=='en' else 2
    name={'en':C.EN_NAME[i],'ar':C.AR_NAME[i]}[lang]
    own=C.OWN[s['own']][L]
    fr=C.FREQ[s['fr']][0 if lang=='en' else 1]
    P=[]
    T=lambda en,ar: en if lang=='en' else ar
    P.append(head(T('PURPOSE','الغرض'),rtl));P.append(text(s['pu'][L],rtl));P.append(blank(rtl))
    P.append(head(T('SCOPE','النطاق'),rtl))
    P.append(text(T('This instruction applies to the %s and to every person who works in it or brings material to it, for all orders produced under GOTS or OCS.'%name,'تنطبق هذه التعليمات على %s وعلى كل شخص يعمل فيها أو يُدخل إليها مواد، وذلك في جميع الطلبيات التي تُنتج وفق GOTS أو OCS.'%name) if lang=='en' else 'التعليمات دي بتتطبق على %s وعلى كل شخص بيشتغل فيها أو بيدخّل لها مواد، في كل الأوردرات اللي بتتنتج حسب GOTS أو OCS.'%name,rtl));P.append(blank(rtl))
    P.append(head(T('RESPONSIBILITIES','المسؤوليات'),rtl))
    P.append(bullet(own+':',T('Keeps the area marked and in order, makes sure this instruction and its records are applied, and reports every problem to the OCS Coordinator.','بيحافظ على علامات المنطقة وترتيبها، وبيتأكد إن التعليمات دي وسجلاتها متطبقة، وبيبلّغ منسق OCS بأي مشكلة.'),rtl))
    P.append(bullet(T('OCS Coordinator:','منسق OCS:'),T('Approves the set-up of the area, checks the records and follows up findings and corrective actions.','بيعتمد تجهيز المنطقة، وبيراجع السجلات، وبيتابع الملاحظات والإجراءات التصحيحية.'),rtl))
    P.append(bullet(T('Quality Assurance:','ضمان الجودة:'),T('Checks the area during in-line and final inspections and in the internal audit.','بيفحص المنطقة أثناء الفحص على الخط والفحص النهائي وفي التدقيق الداخلي.'),rtl))
    P.append(bullet(T('Operators and Handlers:','المشغّلون والعمال:'),T('Work as instructed, keep organic and conventional material apart and report any doubt at once.','بيشتغلوا حسب التعليمات، وبيفصلوا المواد العضوية عن التقليدية، وبيبلّغوا فوراً عن أي شك.'),rtl))
    P.append(blank(rtl))
    P.append(head(T('DEFINITIONS','التعريفات'),rtl))
    P.append(bullet(T('Organic area:','المنطقة العضوية:'),T('A physically separated and clearly marked area used only for GOTS or OCS organic material.','منطقة مفصولة فعلياً ومعلّمة بوضوح، بتُستخدم للمواد العضوية GOTS أو OCS بس.'),rtl))
    P.append(bullet(T('Green label:','الملصق الأخضر:'),T('The internal label with order, lot and TC number carried by organic material in this area.','ملصق التمييز الداخلي اللي عليه رقم الأوردر والدفعة وشهادة TC، وبتشيله المواد العضوية في المنطقة دي.'),rtl))
    P.append(bullet(T('Conventional material:','المادة التقليدية:'),T('Any material that is not certified organic. It never enters this area.','أي مادة مش معتمدة عضوية. وما بتدخلش المنطقة دي أبداً.'),rtl))
    P.append(blank(rtl))
    P.append(head(T('INSTRUCTIONS','التعليمات'),rtl))
    P.append(head(T('1. AREA RULES','1. قواعد المنطقة'),rtl))
    for k,r in enumerate(s['rules'],1): P.append(text('1.%d. %s'%(k,r[L]),rtl))
    P.append(head(T('2. WORKFLOW','2. تسلسل العمل'),rtl))
    for k,r in enumerate(s['flow'],1): P.append(text('2.%d. %s'%(k,r[L]),rtl))
    P.append(head(T('3. CHECKS BEFORE AND DURING WORK','3. الفحوصات قبل العمل وأثناءه'),rtl))
    for k,r in enumerate(s['chk'],1): P.append(text('3.%d. %s'%(k,r[L]),rtl))
    P.append(head(T('4. PROHIBITIONS','4. المحظورات'),rtl))
    P.append(li(T('Do not mix organic and conventional material in this area, or on the same pallet, trolley, table or carton.','لا تخلط المواد العضوية والتقليدية في المنطقة دي، ولا على نفس البالتة أو العربية أو الترابيزة أو الكرتونة.'),rtl))
    P.append(li(T('Do not bring unlabelled or doubtful material into the area.','لا تدخّل مادة من غير ملصق أو مشكوك في حالتها للمنطقة.'),rtl))
    P.append(li(T('Do not remove, cover or change the area signs or the green labels.','لا تشيل ولا تغطّي ولا تغيّر لافتات المنطقة أو الملصقات الخضراء.'),rtl))
    P.append(head(T('5. IN CASE OF PROBLEM','5. في حالة وجود مشكلة'),rtl))
    P.append(text(T('5.1. If organic and conventional material are mixed, or the status of a material is doubtful, stop work, move the material to the yellow holding area and inform the OCS Coordinator immediately.','5.1. لو المواد العضوية والتقليدية اتخلطت، أو حالة مادة مشكوك فيها، وقّف الشغل، وانقل المادة لمنطقة الانتظار الصفراء، وبلّغ منسق OCS فوراً.'),rtl))
    P.append(text(T('5.2. Record the case on the Organic Nonconforming Product and Hold Notice (EMS.OR.FRM.21.23). Nonconforming product goes to the red blocked area and is never sold as organic.','5.2. سجّل الحالة في نموذج إشعار المنتج العضوي غير المطابق والحجز (EMS.OR.FRM.21.23). المنتج غير المطابق بيروح لمنطقة الحجز الحمراء وما بيتباعش على إنه عضوي أبداً.'),rtl))
    P.append(head(T('6. RELATED DOCUMENTS AND RECORDS','6. الوثائق والسجلات ذات الصلة'),rtl))
    for c,en,ar in C.CORE: P.append(li('%s. %s'%(c,en if lang=='en' else ar),rtl))
    for f in C.FORMS_AREA[i]+['21.23']:
        n=C.FORM_NAMES[f];P.append(li('EMS.OR.FRM.%s. %s'%(f,n[1] if lang=='en' else n[2]),rtl))
    P.append(blank(rtl))
    P.append(head(T('7. FEEDBACK AND MONITORING','7. المتابعة والمراجعة'),rtl))
    P.append(text(T('The %s checks the application of this instruction %s and the OCS Coordinator reviews the records every month. The instruction is reviewed at least once a year and whenever the GOTS or OCS standard, customer requirements or the area layout change.'%(own,fr),'%s بيتحقق من تطبيق التعليمات دي %s، ومنسق OCS بيراجع السجلات كل شهر. وبتتراجع التعليمات مرة في السنة على الأقل، وكمان لما بيتغير معيار GOTS أو OCS أو متطلبات العملاء أو تخطيط المنطقة.'%(own,fr)),rtl))
    return P
def build(i,outdir):
    code='EMS.OR.TL.21.%02d'%(3+i)
    en=C.EN_NAME[i]+' Instruction'; ar='تعليمات '+C.AR_NAME[i]
    zin=zipfile.ZipFile(TPL)
    out=os.path.join(outdir,'%s. %s.docx'%(code,en))
    zo=zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED)
    for it in zin.infolist():
        d=zin.read(it.filename)
        if it.filename=='word/document.xml':
            root=etree.fromstring(d);b=root.find(q('body'));kids=list(b)
            for k in kids[:103]: b.remove(k)       # gövde: 0..102 (EN+AR) silinir
            pos=0
            frag=build_lang(i,'en')+['<w:p xmlns:w="%s"><w:r><w:br w:type="page"/></w:r></w:p>'%W]+build_lang(i,'ar')
            for x in frag: b.insert(pos,etree.fromstring(x));pos+=1
            # imza görüntülerini kaldır (taslak, imzasız)
            for dr in list(root.iter(q('drawing'))):
                p=dr.getparent();p.getparent().remove(p)
            d=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
        elif it.filename=='word/header2.xml':
            root=etree.fromstring(d);ts=list(root.iter(q('t')))
            ts[0].text=en.upper();ts[1].text=ar;ts[8].text=code+'.';ts[9].text='';ts[10].text='-';ts[11].text='R0';ts[12].text='0';ts[13].text='22.10.2026'
            d=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
        zo.writestr(it,d)
    zo.close();return out,code,en
if __name__=='__main__':
    od=sys.argv[1];os.makedirs(od,exist_ok=True)
    for i in range(15): print(build(i,od))
