#!/usr/bin/env python3
"""EMS.İK.PRO.01.23 Gizlilik Sözleşmesi (Confidentiality Agreement) — resmî EN+AR Word + Türkçe Word üretir.
Şablon: mevcut İK prosedürü (EMS.İK.PRO.01.16) — başlık tablosu, imza bloğu ve paragraf biçimleri aynen korunur; gövde yeniden yazılır.
Çıktı: prosedurler/EMS.İK.PRO.01.23. Confidentiality Agreement Procedure.docx  ve  prosedurler_tr/aynı ad.docx (+ manifest/refs güncellemesi: araclar/ik_gizlilik_kayit.py değil, bu dosyanın sonu).
Kullanım: python3 araclar/ik_gizlilik_uret.py   (idempotent: her çalıştırmada dosyaları yeniden yazar)"""
import copy, json, os, re, sys, docx
from docx.oxml.ns import qn
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
TPL = os.path.join(ROOT, "prosedurler", "EMS.İK.PRO.01.16. Personnel Files and Records Procedure.docx")
CODE = "EMS.İK.PRO.01.23."
NAME_EN = "Confidentiality Agreement Procedure"
FILE = "EMS.İK.PRO.01.23. Confidentiality Agreement Procedure.docx"
TITLE_EN, TITLE_AR, TITLE_TR = "CONFIDENTIALITY AGREEMENT PROCEDURE", "إجراء اتفاقية السرية", "GİZLİLİK SÖZLEŞMESİ PROSEDÜRÜ"

# (tür, EN, AR, TR)  tür: H başlık · B gövde · E boş · RB etiketli madde (3 parça) · SH alt başlık · CL madde · BU madde işaretli
I = []
def H(en, ar, tr): I.append(("H", en, ar, tr))
def B(en, ar, tr): I.append(("B", en, ar, tr))
def E(): I.append(("E", "", "", ""))
def RB(en, ar, tr): I.append(("RB", en, ar, tr))   # her biri (etiket, metin)
def SH(en, ar, tr): I.append(("SH", en, ar, tr))
def CL(en, ar, tr): I.append(("CL", en, ar, tr))
def BU(en, ar, tr): I.append(("BU", en, ar, tr))

H("PURPOSE", "الغرض", "AMAÇ")
B("This procedure and the attached agreement define how EMS Eroğlu Manufacturing Studio (EMS) protects its own confidential information and the confidential information entrusted to it by customers, suppliers and employees. It sets the confidentiality commitment that every employee, trainee, temporary worker, contractor and consultant signs before gaining access to such information.",
  "يحدد هذا الإجراء والاتفاقية المرفقة به كيف تحمي EMS Eroğlu Manufacturing Studio (EMS) معلوماتها السرية والمعلومات السرية التي يأتمنها عليها العملاء والموردون والعاملون. ويضع التزام السرية الذي يوقعه كل موظف ومتدرب وعامل مؤقت ومقاول ومستشار قبل أن يُتاح له الاطلاع على هذه المعلومات.",
  "Bu prosedür ve ekindeki sözleşme, EMS Eroğlu Manufacturing Studio'nun (EMS) kendi gizli bilgilerini ve müşterilerin, tedarikçilerin ve çalışanların kendisine emanet ettiği gizli bilgileri nasıl koruduğunu belirler. Bu bilgilere erişmeden önce her çalışanın, stajyerin, geçici işçinin, yüklenicinin ve danışmanın imzaladığı gizlilik taahhüdünü düzenler.")
E()
H("SCOPE", "النطاق", "KAPSAM")
B("This procedure applies to all EMS employees (permanent, fixed-term and temporary), trainees, labour-agency workers, subcontractors, consultants and any other person who has access to EMS confidential information, in all departments and locations, during the relationship and after it ends.",
  "يسري هذا الإجراء على جميع موظفي EMS (الدائمين ومحددي المدة والمؤقتين) والمتدربين وعمال شركات التوظيف والمقاولين من الباطن والمستشارين وأي شخص آخر يطلع على المعلومات السرية لـ EMS، في جميع الأقسام والمواقع، أثناء العلاقة وبعد انتهائها.",
  "Bu prosedür; tüm EMS çalışanlarını (belirsiz süreli, belirli süreli ve geçici), stajyerleri, işgücü ajansı çalışanlarını, alt yüklenicileri, danışmanları ve EMS'nin gizli bilgilerine erişimi olan diğer herkesi, tüm bölümlerde ve tüm yerlerde, ilişki süresince ve sona erdikten sonra kapsar.")
E()
H("RESPONSIBILITIES", "المسؤوليات", "SORUMLULUKLAR")
RB(("• ", "HR Manager:", " Owns this procedure, makes sure the agreement is signed before the first working day or before access is given, keeps the signed copies in the personnel file and follows up departures."),
   ("• ", "مدير الموارد البشرية:", " يملك هذا الإجراء، ويتأكد من توقيع الاتفاقية قبل أول يوم عمل أو قبل إتاحة الاطلاع، ويحتفظ بالنسخ الموقعة في ملف الموظف ويتابع حالات الانتهاء."),
   ("• ", "İK Müdürü:", " Bu prosedürün sahibidir; sözleşmenin ilk iş gününden veya erişim verilmeden önce imzalanmasını sağlar, imzalı nüshaları personel dosyasında saklar ve ayrılışları takip eder."))
RB(("• ", "Department Managers:", " Decide who needs access to confidential information, tell their staff which information is confidential and report any breach."),
   ("• ", "مديرو الأقسام:", " يحددون من يحتاج إلى الاطلاع على المعلومات السرية، ويبلغون فريقهم بما هو سري، ويبلغون عن أي مخالفة."),
   ("• ", "Bölüm Müdürleri:", " Gizli bilgiye kimin erişmesi gerektiğine karar verir, ekibine hangi bilginin gizli olduğunu bildirir ve her ihlali raporlar."))
RB(("• ", "Information Technology:", " Applies access rights and password rules (EMS.BG.PRO.15.01.) and removes access on the last working day."),
   ("• ", "تكنولوجيا المعلومات:", " تطبق صلاحيات الوصول وقواعد كلمات المرور (EMS.BG.PRO.15.01.) وتلغي الصلاحيات في آخر يوم عمل."),
   ("• ", "Bilgi Teknolojileri:", " Erişim yetkilerini ve şifre kurallarını (EMS.BG.PRO.15.01.) uygular ve son iş gününde erişimi kaldırır."))
RB(("• ", "Purchasing and Merchandising:", " Make sure suppliers, subcontractors and agents sign a confidentiality undertaking before samples, designs or specifications are shared."),
   ("• ", "المشتريات والمرشندايزنج:", " يتأكدون من توقيع الموردين والمقاولين من الباطن والوكلاء تعهد السرية قبل مشاركة العينات أو التصميمات أو المواصفات."),
   ("• ", "Satın Alma ve Merchandising:", " Numune, tasarım veya şartname paylaşılmadan önce tedarikçilerin, alt yüklenicilerin ve acentelerin gizlilik taahhüdü imzalamasını sağlar."))
RB(("• ", "Security and Administrative Affairs:", " Apply the visitor rules (EMS.İD.PRO.03.02.), including the ban on photographs in restricted areas."),
   ("• ", "الأمن والشؤون الإدارية:", " يطبقان قواعد الزوار (EMS.İD.PRO.03.02.) بما فيها منع التصوير في المناطق المحظورة."),
   ("• ", "Güvenlik ve İdari İşler:", " Yasak alanlarda fotoğraf çekme yasağı dahil ziyaretçi kurallarını (EMS.İD.PRO.03.02.) uygular."))
RB(("• ", "Employees and other signatories:", " Read and sign the agreement, protect confidential information and report any loss or leak at once."),
   ("• ", "الموظفون وسائر الموقعين:", " يقرؤون الاتفاقية ويوقعونها ويحمون المعلومات السرية ويبلغون فورًا عن أي فقد أو تسريب."),
   ("• ", "Çalışanlar ve diğer imza sahipleri:", " Sözleşmeyi okur ve imzalar, gizli bilgiyi korur ve her kayıp veya sızıntıyı derhal bildirir."))
E()
H("DEFINITIONS", "التعريفات", "TANIMLAR")
RB(("• ", "Confidential Information:", " Any information that is not public and that EMS or its customers, suppliers or employees treat as private, in any form (written, electronic, oral, sample, image or product)."),
   ("• ", "المعلومات السرية:", " أي معلومات غير معلنة تعتبرها EMS أو عملاؤها أو مورّدوها أو موظفوها خاصة، بأي شكل (مكتوب أو إلكتروني أو شفهي أو عينة أو صورة أو منتج)."),
   ("• ", "Gizli Bilgi:", " Kamuya açık olmayan ve EMS'nin veya müşterilerinin, tedarikçilerinin ya da çalışanlarının özel kabul ettiği, her biçimdeki (yazılı, elektronik, sözlü, numune, görüntü veya ürün) bilgidir."))
RB(("• ", "Customer Information:", " Orders, designs, tech packs, patterns, samples, prices, brand and audit information and any specification of EMS customers."),
   ("• ", "معلومات العميل:", " الطلبيات والتصميمات والمواصفات الفنية والباترونات والعينات والأسعار ومعلومات العلامة التجارية والتدقيق وأي مواصفات خاصة بعملاء EMS."),
   ("• ", "Müşteri Bilgisi:", " EMS müşterilerinin siparişleri, tasarımları, teknik föyleri, kalıpları, numuneleri, fiyatları, marka ve denetim bilgileri ile her türlü şartnamesidir."))
RB(("• ", "Personal Data:", " Information about an identified or identifiable person, protected as in EMS.BG.POL.15.01. and the applicable data protection law."),
   ("• ", "البيانات الشخصية:", " معلومات عن شخص محدد الهوية أو يمكن تحديد هويته، وتُحمى وفق EMS.BG.POL.15.01. وقانون حماية البيانات المعمول به."),
   ("• ", "Kişisel Veri:", " Kimliği belirli veya belirlenebilir bir kişiye ilişkin bilgidir; EMS.BG.POL.15.01. ve yürürlükteki veri koruma mevzuatı uyarınca korunur."))
RB(("• ", "Signatory:", " The person who signs the Confidentiality Agreement and receives confidential information."),
   ("• ", "الموقّع:", " الشخص الذي يوقع اتفاقية السرية ويطلع على المعلومات السرية."),
   ("• ", "İmza Sahibi:", " Gizlilik Sözleşmesi'ni imzalayan ve gizli bilgiye erişen kişidir."))
E()
H("MAIN AND SUB PROCESSES", "العمليات الرئيسية والفرعية", "ANA VE ALT SÜREÇLER")
SH("1. WHO SIGNS AND WHEN", "1. من يوقع ومتى", "1. KİM, NE ZAMAN İMZALAR")
CL("1.1. Every new employee signs the Confidentiality Agreement (Annex 1) on the first working day, together with the employment contract and before getting access to systems, samples or customer information.",
   "1.1. يوقع كل موظف جديد اتفاقية السرية (الملحق 1) في أول يوم عمل مع عقد العمل، وقبل أن يُتاح له الاطلاع على الأنظمة أو العينات أو معلومات العملاء.",
   "1.1. Her yeni çalışan, Gizlilik Sözleşmesi'ni (Ek 1) ilk iş gününde, iş sözleşmesiyle birlikte ve sistemlere, numunelere veya müşteri bilgisine erişmeden önce imzalar.")
CL("1.2. Existing employees sign it at the first review after this procedure is issued; HR keeps a list and follows up unsigned copies.",
   "1.2. يوقعها الموظفون الحاليون عند أول مراجعة بعد صدور هذا الإجراء؛ وتحتفظ الموارد البشرية بقائمة وتتابع النسخ غير الموقعة.",
   "1.2. Mevcut çalışanlar, bu prosedür yayımlandıktan sonraki ilk değerlendirmede imzalar; İK bir liste tutar ve imzalanmayan nüshaları takip eder.")
CL("1.3. Labour-agency workers, subcontractors, consultants, trainees and temporary workers sign before access is given. Suppliers and agents sign a confidentiality undertaking in the same form or in their contract.",
   "1.3. يوقع عمال شركات التوظيف والمقاولون من الباطن والمستشارون والمتدربون والعمال المؤقتون قبل إتاحة الاطلاع. ويوقع الموردون والوكلاء تعهد سرية بالصيغة نفسها أو ضمن عقدهم.",
   "1.3. İşgücü ajansı çalışanları, alt yükleniciler, danışmanlar, stajyerler ve geçici işçiler erişim verilmeden önce imzalar. Tedarikçiler ve acenteler aynı formda veya sözleşmelerinde bir gizlilik taahhüdü imzalar.")
CL("1.4. The signed original is kept in the personnel file (EMS.İK.PRO.01.16.) and a copy is given to the signatory.",
   "1.4. يُحفظ الأصل الموقع في ملف الموظف (EMS.İK.PRO.01.16.) وتُعطى نسخة للموقّع.",
   "1.4. İmzalı asıl nüsha personel dosyasında (EMS.İK.PRO.01.16.) saklanır; bir kopyası imza sahibine verilir.")
E()
SH("2. WHAT IS CONFIDENTIAL", "2. ما هو سري", "2. GİZLİ OLAN BİLGİLER")
CL("2.1. Customer information: orders, designs, tech packs, patterns, samples, trims, prices, forecasts, brand rules and audit reports.",
   "2.1. معلومات العملاء: الطلبيات والتصميمات والمواصفات الفنية والباترونات والعينات والاكسسوارات والأسعار والتوقعات وقواعد العلامات التجارية وتقارير التدقيق.",
   "2.1. Müşteri bilgileri: siparişler, tasarımlar, teknik föyler, kalıplar, numuneler, aksesuarlar, fiyatlar, tahminler, marka kuralları ve denetim raporları.")
CL("2.2. Commercial and financial information: costs, price lists, margins, supplier terms, wages and payroll, business plans, and customer and supplier lists.",
   "2.2. المعلومات التجارية والمالية: التكاليف وقوائم الأسعار وهوامش الربح وشروط الموردين والأجور والرواتب وخطط العمل وقوائم العملاء والموردين.",
   "2.2. Ticari ve mali bilgiler: maliyetler, fiyat listeleri, kâr marjları, tedarikçi şartları, ücret ve bordro, iş planları, müşteri ve tedarikçi listeleri.")
CL("2.3. Technical and production information: dye recipes and formulas, process settings, machine programs, quality methods, know-how, product development and R&D work.",
   "2.3. المعلومات الفنية والإنتاجية: وصفات الصباغة وتركيباتها وإعدادات العمليات وبرامج الماكينات وأساليب الجودة والخبرة الفنية وأعمال تطوير المنتجات والبحث والتطوير.",
   "2.3. Teknik ve üretim bilgileri: boya reçeteleri ve formülleri, proses ayarları, makine programları, kalite yöntemleri, bilgi birikimi (know-how), ürün geliştirme ve Ar-Ge çalışmaları.")
CL("2.4. Employee and personal data: personnel files, health records, wages, disciplinary and grievance records, and data of workers and visitors.",
   "2.4. بيانات الموظفين والبيانات الشخصية: ملفات الموظفين والسجلات الصحية والأجور وسجلات الجزاءات والشكاوى وبيانات العمال والزوار.",
   "2.4. Çalışan ve kişisel veriler: personel dosyaları, sağlık kayıtları, ücretler, disiplin ve şikâyet kayıtları, işçi ve ziyaretçi verileri.")
CL("2.5. Information system data: passwords, access codes, network details, systems, files and e-mails.",
   "2.5. بيانات أنظمة المعلومات: كلمات المرور ورموز الدخول وتفاصيل الشبكة والأنظمة والملفات والبريد الإلكتروني.",
   "2.5. Bilgi sistemi verileri: şifreler, erişim kodları, ağ bilgileri, sistemler, dosyalar ve e-postalar.")
CL("2.6. Any information marked \"Confidential\" and any information that a reasonable person would regard as confidential.",
   "2.6. أي معلومات مكتوب عليها «سري» وأي معلومات يعتبرها الشخص العادي سرية.",
   "2.6. \"Gizli\" olarak işaretlenmiş her bilgi ve makul bir kişinin gizli sayacağı her bilgi.")
E()
SH("3. OBLIGATIONS OF THE SIGNATORY", "3. التزامات الموقّع", "3. İMZA SAHİBİNİN YÜKÜMLÜLÜKLERİ")
CL("3.1. Use confidential information only for EMS work and only as far as needed for the task.",
   "3.1. يستخدم المعلومات السرية لعمل EMS فقط وبالقدر اللازم للمهمة.",
   "3.1. Gizli bilgiyi yalnızca EMS işi için ve görevin gerektirdiği ölçüde kullanır.")
CL("3.2. Do not disclose it to anyone inside or outside EMS who does not need it, including family, friends, other employers, competitors, the media and social networks.",
   "3.2. لا يفصح عنها لأي شخص داخل EMS أو خارجها لا يحتاج إليها، بمن فيهم الأسرة والأصدقاء وأصحاب العمل الآخرون والمنافسون ووسائل الإعلام وشبكات التواصل الاجتماعي.",
   "3.2. Aile, arkadaşlar, diğer işverenler, rakipler, medya ve sosyal ağlar dahil, EMS içinde veya dışında buna ihtiyacı olmayan kimseye açıklamaz.")
CL("3.3. Do not copy, photograph, record, forward by personal e-mail or messaging applications, or take it out of EMS (paper, USB, phone, cloud) without the written approval of the Department Manager.",
   "3.3. لا ينسخها ولا يصورها ولا يسجلها ولا يرسلها عبر البريد الشخصي أو تطبيقات المراسلة ولا يخرجها من EMS (ورقًا أو USB أو هاتفًا أو سحابة) دون موافقة كتابية من مدير القسم.",
   "3.3. Bölüm Müdürü'nün yazılı onayı olmadan kopyalamaz, fotoğraflamaz, kaydetmez, kişisel e-posta veya mesajlaşma uygulamalarıyla iletmez, EMS dışına (kâğıt, USB, telefon, bulut) çıkarmaz.")
CL("3.4. Keep documents, samples and screens out of sight of unauthorised persons, lock documents away and log out of systems.",
   "3.4. يُبقي المستندات والعينات والشاشات بعيدًا عن أنظار غير المصرح لهم، ويؤمّن المستندات ويسجل الخروج من الأنظمة.",
   "3.4. Belgeleri, numuneleri ve ekranları yetkisiz kişilerin görüşünden uzak tutar, belgeleri kilit altına alır ve sistemlerden çıkış yapar.")
CL("3.5. Do not use confidential information for personal benefit or for another business, and do not use EMS information for a competitor.",
   "3.5. لا يستخدم المعلومات السرية لمصلحة شخصية أو لعمل آخر، ولا يستخدم معلومات EMS لصالح منافس.",
   "3.5. Gizli bilgiyi kişisel çıkar veya başka bir iş için kullanmaz ve EMS bilgilerini bir rakip lehine kullanmaz.")
CL("3.6. Report any loss, leak, theft or suspected breach immediately to the Department Manager or HR.",
   "3.6. يبلغ فورًا مدير القسم أو الموارد البشرية عن أي فقد أو تسريب أو سرقة أو اشتباه في مخالفة.",
   "3.6. Her kayıp, sızıntı, hırsızlık veya ihlal şüphesini derhal Bölüm Müdürü'ne veya İK'ya bildirir.")
CL("3.7. Where a customer contract or audit requires a stricter rule, the stricter rule applies.",
   "3.7. إذا اشترط عقد عميل أو تدقيق قاعدة أشد، تُطبق القاعدة الأشد.",
   "3.7. Bir müşteri sözleşmesi veya denetimi daha sıkı bir kural gerektiriyorsa, daha sıkı kural uygulanır.")
E()
SH("4. EXCEPTIONS", "4. الاستثناءات", "4. İSTİSNALAR")
CL("4.1. The duty does not apply to information that becomes public without a breach of this agreement, that the signatory lawfully knew before joining EMS, or that is lawfully received from a third party without restriction.",
   "4.1. لا ينطبق الالتزام على المعلومات التي تصبح علنية دون مخالفة لهذه الاتفاقية، أو التي كان الموقّع يعلمها بصورة مشروعة قبل انضمامه إلى EMS، أو التي يتلقاها بصورة مشروعة من طرف ثالث دون قيود.",
   "4.1. Yükümlülük; bu sözleşmenin ihlali olmaksızın kamuya açık hale gelen, imza sahibinin EMS'ye katılmadan önce hukuka uygun biçimde bildiği veya üçüncü bir taraftan kısıtlama olmaksızın hukuka uygun biçimde edindiği bilgiler için geçerli değildir.")
CL("4.2. Disclosure required by law, a court or a public authority is allowed to the extent required, after informing HR unless the law prohibits it.",
   "4.2. يجوز الإفصاح الذي يوجبه القانون أو المحكمة أو جهة رسمية بالقدر المطلوب، بعد إبلاغ الموارد البشرية ما لم يمنع القانون ذلك.",
   "4.2. Kanunun, mahkemenin veya bir resmî makamın gerektirdiği açıklama, kanun yasaklamadıkça İK'ya bilgi verildikten sonra gerektiği ölçüde yapılabilir.")
CL("4.3. Nothing in this procedure prevents an employee from raising a complaint through the EMS channels (EMS.İK.PRO.01.20.), from reporting a legal violation to the competent authority, or from speaking in confidence with social auditors.",
   "4.3. لا يمنع هذا الإجراء الموظف من تقديم شكوى عبر قنوات EMS (EMS.İK.PRO.01.20.) أو من الإبلاغ عن مخالفة قانونية للجهة المختصة أو من التحدث بسرية مع المدققين الاجتماعيين.",
   "4.3. Bu prosedür, çalışanın EMS kanallarından (EMS.İK.PRO.01.20.) şikâyet iletmesini, bir hukuka aykırılığı yetkili makama bildirmesini veya sosyal denetçilerle gizlilik içinde görüşmesini engellemez.")
E()
SH("5. DURATION", "5. المدة", "5. SÜRE")
CL("5.1. The duty starts when access starts, continues throughout the employment or contract and remains in force for five (5) years after it ends. For trade secrets, personal data and customer information it continues for as long as the information remains confidential.",
   "5.1. يبدأ الالتزام عند بدء الاطلاع، ويستمر طوال مدة العمل أو العقد، ويظل ساريًا لمدة خمس (5) سنوات بعد انتهائه. وبالنسبة للأسرار التجارية والبيانات الشخصية ومعلومات العملاء يستمر ما دامت المعلومات سرية.",
   "5.1. Yükümlülük erişimle başlar, çalışma veya sözleşme süresince devam eder ve sona ermesinden sonra beş (5) yıl daha geçerliliğini korur. Ticari sırlar, kişisel veriler ve müşteri bilgileri için bilgi gizli kaldığı sürece devam eder.")
E()
SH("6. RETURN OF MATERIALS AND EXIT", "6. إعادة المواد والانتهاء", "6. MALZEMELERİN İADESİ VE AYRILIŞ")
CL("6.1. On the last working day, or earlier on request, the signatory returns all documents, samples, files, badges, keys, devices and copies, and IT removes the access.",
   "6.1. في آخر يوم عمل، أو قبله عند الطلب، يعيد الموقّع جميع المستندات والعينات والملفات والبطاقات والمفاتيح والأجهزة والنسخ، وتلغي تكنولوجيا المعلومات الصلاحيات.",
   "6.1. Son iş gününde veya talep halinde daha önce, imza sahibi tüm belgeleri, numuneleri, dosyaları, kartları, anahtarları, cihazları ve kopyaları iade eder; Bilgi Teknolojileri erişimi kaldırır.")
CL("6.2. The signatory deletes confidential information held on personal devices or accounts and confirms this in writing in the exit clearance.",
   "6.2. يحذف الموقّع المعلومات السرية المحفوظة على أجهزته أو حساباته الشخصية ويؤكد ذلك كتابيًا في إخلاء الطرف.",
   "6.2. İmza sahibi kişisel cihaz veya hesaplarındaki gizli bilgiyi siler ve bunu ilişik kesme belgesinde yazılı olarak teyit eder.")
E()
SH("7. BREACH AND CONSEQUENCES", "7. المخالفة وآثارها", "7. İHLAL VE SONUÇLARI")
CL("7.1. A breach is handled under the Disciplinary Assessment and Implementation Procedure (EMS.İK.PRO.01.04.) and the Code of Ethics and Business Conduct Policy (EMS.İK.POL.01.02.). Serious breaches may lead to termination as allowed by applicable labour law.",
   "7.1. تُعالج المخالفة وفق إجراء التقييم والتطبيق التأديبي (EMS.İK.PRO.01.04.) وسياسة الأخلاقيات وسلوك العمل (EMS.İK.POL.01.02.). وقد تؤدي المخالفات الجسيمة إلى إنهاء الخدمة بالقدر الذي يسمح به قانون العمل المعمول به.",
   "7.1. İhlal, Disiplin Değerlendirme ve Uygulama Prosedürü (EMS.İK.PRO.01.04.) ve Etik ve İş Davranış Kuralları Politikası (EMS.İK.POL.01.02.) uyarınca ele alınır. Ağır ihlaller, yürürlükteki iş hukukunun izin verdiği ölçüde iş sözleşmesinin feshine yol açabilir.")
CL("7.2. EMS may also claim compensation for any damage and take legal action to stop the breach, as allowed by applicable law.",
   "7.2. ولـ EMS أيضًا أن تطالب بالتعويض عن أي ضرر وأن تتخذ الإجراءات القانونية لوقف المخالفة، وفق ما يسمح به القانون المعمول به.",
   "7.2. EMS ayrıca, yürürlükteki hukukun izin verdiği ölçüde, her türlü zarar için tazminat talep edebilir ve ihlali durdurmak için yasal yollara başvurabilir.")
CL("7.3. Breaches that involve personal data or customer information are reported through EMS.BG.PRO.15.02. and to the customer where required.",
   "7.3. تُبلَّغ المخالفات التي تمس البيانات الشخصية أو معلومات العملاء عبر EMS.BG.PRO.15.02. وإلى العميل عند اللزوم.",
   "7.3. Kişisel veri veya müşteri bilgisini ilgilendiren ihlaller EMS.BG.PRO.15.02. uyarınca ve gerektiğinde müşteriye bildirilir.")
E()
SH("8. TRAINING AND MONITORING", "8. التدريب والمتابعة", "8. EĞİTİM VE İZLEME")
CL("8.1. HR explains the agreement at induction and repeats a reminder in the annual training (EMS.İK.PRO.01.14. and the training plan).",
   "8.1. تشرح الموارد البشرية الاتفاقية في التعريف بالعمل وتكرر التذكير بها في التدريب السنوي.",
   "8.1. İK, sözleşmeyi işe başlangıç eğitiminde açıklar ve yıllık eğitimde hatırlatmayı tekrarlar.")
CL("8.2. The HR Manager reviews this procedure every year and reports, in the management review: the percentage of signed agreements (target 100%), the number of breaches reported and the number closed.",
   "8.2. يراجع مدير الموارد البشرية هذا الإجراء سنويًا ويرفع في مراجعة الإدارة: نسبة الاتفاقيات الموقعة (الهدف 100%) وعدد المخالفات المبلغ عنها وعدد ما أُغلق منها.",
   "8.2. İK Müdürü bu prosedürü her yıl gözden geçirir ve yönetim gözden geçirmesinde şunları raporlar: imzalanan sözleşme oranı (hedef %100), bildirilen ihlal sayısı ve kapatılan ihlal sayısı.")
E()
SH("9. RELATED DOCUMENTS AND RECORDS", "9. الوثائق والسجلات ذات الصلة", "9. İLGİLİ DOKÜMAN VE KAYITLAR")
BU("Signed Confidentiality Agreements (Annex 1)", "اتفاقيات السرية الموقعة (الملحق 1)", "İmzalı Gizlilik Sözleşmeleri (Ek 1)")
BU("EMS.İK.POL.01.02. Code of Ethics and Business Conduct Policy", "EMS.İK.POL.01.02. سياسة الأخلاقيات وسلوك العمل", "EMS.İK.POL.01.02. Etik ve İş Davranış Kuralları Politikası")
BU("EMS.İK.PRO.01.04. Disciplinary Assessment and Implementation Procedure", "EMS.İK.PRO.01.04. إجراء التقييم والتطبيق التأديبي", "EMS.İK.PRO.01.04. Disiplin Değerlendirme ve Uygulama Prosedürü")
BU("EMS.İK.PRO.01.16. Personnel Files and Records Procedure", "EMS.İK.PRO.01.16. إجراء ملفات وسجلات الموظفين", "EMS.İK.PRO.01.16. Personel Dosyaları ve Kayıtları Prosedürü")
BU("EMS.İK.PRO.01.20. Grievance and Complaints Mechanism Procedure", "EMS.İK.PRO.01.20. إجراء آلية الشكاوى والتظلمات", "EMS.İK.PRO.01.20. Şikâyet ve İtiraz Mekanizması Prosedürü")
BU("EMS.BG.POL.15.01. Information Security and Data Protection Policy", "EMS.BG.POL.15.01. سياسة أمن المعلومات وحماية البيانات", "EMS.BG.POL.15.01. Bilgi Güvenliği ve Veri Koruma Politikası")
BU("EMS.BG.PRO.15.01. Access Control and Password Procedure", "EMS.BG.PRO.15.01. إجراء التحكم في الوصول وكلمات المرور", "EMS.BG.PRO.15.01. Erişim Kontrolü ve Şifre Prosedürü")
BU("EMS.BG.PRO.15.02. Data Backup and Information Security Incident Procedure", "EMS.BG.PRO.15.02. إجراء النسخ الاحتياطي وحوادث أمن المعلومات", "EMS.BG.PRO.15.02. Veri Yedekleme ve Bilgi Güvenliği Olay Prosedürü")
BU("EMS.BG.TL.15.01. Acceptable Use of IT Resources Instruction", "EMS.BG.TL.15.01. تعليمات الاستخدام المقبول لموارد تكنولوجيا المعلومات", "EMS.BG.TL.15.01. BT Kaynaklarının Kabul Edilebilir Kullanımı Talimatı")
BU("EMS.İD.PRO.03.02. Visitor and Subcontractor Vehicle Entry and Exit Procedure", "EMS.İD.PRO.03.02. إجراء دخول وخروج الزوار ومركبات المقاولين", "EMS.İD.PRO.03.02. Ziyaretçi ve Alt Yüklenici Araç Giriş Çıkış Prosedürü")
E()
H("ANNEX 1 – CONFIDENTIALITY AGREEMENT", "الملحق 1 – اتفاقية السرية", "EK 1 – GİZLİLİK SÖZLEŞMESİ")
B("I, the undersigned, who works for or is engaged by EMS Eroğlu Manufacturing Studio, declare that I have read and understood this procedure and I agree:",
  "أقر أنا الموقع أدناه، العامل لدى EMS Eroğlu Manufacturing Studio أو المتعاقد معها، بأنني قرأت هذا الإجراء وفهمته، وأوافق على ما يلي:",
  "EMS Eroğlu Manufacturing Studio nezdinde çalışan veya onunla sözleşmeli olan ben, aşağıda imzası bulunan kişi, bu prosedürü okuduğumu ve anladığımı beyan eder ve şunları kabul ederim:")
CL("(1) to keep all confidential information secret and to use it only for EMS work;",
   "(1) أن أحافظ على سرية جميع المعلومات السرية وألا أستخدمها إلا في عمل EMS؛",
   "(1) Tüm gizli bilgileri gizli tutacağımı ve yalnızca EMS işi için kullanacağımı;")
CL("(2) not to disclose, copy, photograph, record, send or take confidential information out of EMS without written approval;",
   "(2) ألا أفصح عن المعلومات السرية أو أنسخها أو أصورها أو أسجلها أو أرسلها أو أخرجها من EMS دون موافقة كتابية؛",
   "(2) Yazılı onay olmadan gizli bilgiyi açıklamayacağımı, kopyalamayacağımı, fotoğraflamayacağımı, kaydetmeyeceğimi, göndermeyeceğimi veya EMS dışına çıkarmayacağımı;")
CL("(3) to return all materials on request or when my work ends and to delete confidential information from my personal devices;",
   "(3) أن أعيد جميع المواد عند الطلب أو عند انتهاء عملي وأن أحذف المعلومات السرية من أجهزتي الشخصية؛",
   "(3) Talep halinde veya işim sona erdiğinde tüm malzemeleri iade edeceğimi ve gizli bilgileri kişisel cihazlarımdan sileceğimi;")
CL("(4) that these duties continue for five (5) years after my work ends and, for trade secrets, personal data and customer information, for as long as they remain confidential;",
   "(4) أن هذه الالتزامات تستمر خمس (5) سنوات بعد انتهاء عملي، وبالنسبة للأسرار التجارية والبيانات الشخصية ومعلومات العملاء ما دامت سرية؛",
   "(4) Bu yükümlülüklerin işim sona erdikten sonra beş (5) yıl, ticari sırlar, kişisel veriler ve müşteri bilgileri için ise gizli kaldıkları sürece devam edeceğini;")
CL("(5) that a breach may lead to disciplinary action, termination and a claim for damages under applicable law.",
   "(5) أن المخالفة قد تؤدي إلى إجراء تأديبي وإنهاء الخدمة والمطالبة بالتعويض وفق القانون المعمول به.",
   "(5) İhlalin, yürürlükteki hukuk uyarınca disiplin işlemine, fesihe ve tazminat talebine yol açabileceğini.")
B("This agreement does not limit my right to raise a grievance or to report a legal violation to the competent authority.",
  "لا تحد هذه الاتفاقية من حقي في تقديم شكوى أو الإبلاغ عن مخالفة قانونية للجهة المختصة.",
  "Bu sözleşme, şikâyet iletme veya bir hukuka aykırılığı yetkili makama bildirme hakkımı sınırlamaz.")
E()
B("Name and Surname: ______________________   National ID No.: ________________",
  "الاسم الكامل: ______________________   الرقم القومي: ________________",
  "Ad Soyad: ______________________   Kimlik No: ________________")
B("Department / Position: ____________________   Date: ____ / ____ / ______",
  "القسم / الوظيفة: ____________________   التاريخ: ____ / ____ / ______",
  "Bölüm / Görev: ____________________   Tarih: ____ / ____ / ______")
B("Signature: ____________________   EMS Representative (HR): ____________________",
  "التوقيع: ____________________   ممثل EMS (الموارد البشرية): ____________________",
  "İmza: ____________________   EMS Temsilcisi (İK): ____________________")
E()
H("FEEDBACK AND MONITORING", "التغذية الراجعة والمتابعة", "GERİ BİLDİRİM VE İZLEME")
B("This procedure is reviewed every year by the HR Manager. Audit findings, breaches and employee feedback are evaluated, and the procedure and Annex 1 are updated when needed.",
  "يراجع مدير الموارد البشرية هذا الإجراء سنويًا. وتُقيَّم نتائج التدقيق والمخالفات وملاحظات الموظفين، ويُحدَّث الإجراء والملحق 1 عند الحاجة.",
  "Bu prosedür her yıl İK Müdürü tarafından gözden geçirilir. Denetim bulguları, ihlaller ve çalışan geri bildirimleri değerlendirilir; gerektiğinde prosedür ve Ek 1 güncellenir.")

# ---- belge üretimi ----
def clone(ex, runs, rpr_from=None):
    """Örnek paragrafı kopyalar; run sayısını örnekteki run sayısına göre ayarlar; metinleri yazar."""
    p = copy.deepcopy(ex)
    rs = p.findall(qn("w:r"))
    if isinstance(runs, str): runs = [runs]
    while len(rs) > len(runs):
        p.remove(rs[-1]); rs = p.findall(qn("w:r"))
    for r, t in zip(rs, runs):
        ts = r.findall(qn("w:t"))
        for x in ts[1:]: r.remove(x)
        if ts: ts[0].text = t; ts[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    return p

def build_official():
    d = docx.Document(TPL); body = d.element.body
    P = [p._p for p in d.paragraphs]
    en = dict(H=P[0], B=P[1], E=P[2], RB=P[7], SH=P[19], CL=P[20], BU=P[21])
    ar = dict(H=P[66], B=P[64], E=P[65], RB=P[70], SH=P[82], CL=P[83], BU=P[84])
    anchor = P[126]               # "…" boş paragraf (imza öncesi); gövde bundan önce eklenir
    for p in P[:126]: body.remove(p)
    def seq(lang, ex, idx):
        out = []
        for it in I:
            k = it[0]; t = it[idx]
            if k == "E": out.append(clone(ex["E"], [])); continue
            runs = list(t) if isinstance(t, tuple) else [t]
            out.append(clone(ex[k], runs))
        return out
    arel = seq("ar", ar, 2)
    first = clone(P[63], [I[0][2]])      # Arapça bölümün ilk başlığı (sayfa başı özelliği olan örnek)
    arel[0] = first
    for el in seq("en", en, 1) + arel: anchor.addprevious(el)
    # başlık tablosu
    h = d.sections[0].header
    def sub(old, new):
        for t in h.tables:
            for r in t.rows:
                for c in r.cells:
                    for p in c.paragraphs:
                        for ru in p.runs:
                            if ru.text == old: ru.text = new
    sub("PERSONNEL FILES AND RECORDS PROCEDURE", TITLE_EN); sub("إجراء ملفات وسجلات الموظفين", TITLE_AR); sub("EMS.İK.PRO.01.16.", CODE)
    for t in h.tables:
        for r in t.rows:
            for c in r.cells:
                for p in c.paragraphs:
                    rs = p.runs
                    if len(rs) == 2 and rs[0].text == "0" and rs[1].text == "2.10.2026": rs[0].text = "2"; rs[1].text = "7.10.2026"
    out = os.path.join(ROOT, "prosedurler", FILE); d.save(out); return out

def build_tr(official):
    d = docx.Document(official); body = d.element.body
    P = [p._p for p in d.paragraphs]
    n_en = len(I)
    for p in P[n_en:n_en * 2]: body.remove(p)          # Arapça kısım atılır
    for p, it in zip(P[:n_en], I):
        t = it[3]; runs = list(t) if isinstance(t, tuple) else [t]
        rs = p.findall(qn("w:r"))
        if it[0] == "E": continue
        for r, x in zip(rs, runs):
            ts = r.findall(qn("w:t"))
            if ts: ts[0].text = x; ts[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    h = d.sections[0].header
    for t in h.tables:
        for r in t.rows:
            for c in r.cells:
                for p in c.paragraphs:
                    for ru in p.runs:
                        if ru.text == TITLE_EN: ru.text = TITLE_TR
                        if ru.text == TITLE_AR: ru.text = ""
    out = os.path.join(ROOT, "prosedurler_tr", FILE); d.save(out); return out

def register():
    pm = os.path.join(ROOT, "prosedurler", "manifest.json"); m = json.load(open(pm, encoding="utf-8"))
    m = [x for x in m if x.get("code") != CODE]
    m.append({"folder": "İK Politikaları", "code": CODE, "name": CODE + " " + NAME_EN, "file": FILE, "rev": "gizlilik-2026-10-27"})
    json.dump(m, open(pm, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    tm = os.path.join(ROOT, "prosedurler_tr", "manifest.json"); t = json.load(open(tm, encoding="utf-8"))
    t = [x for x in t if x.get("code") != CODE]
    t.append({"code": CODE, "file": FILE, "tr": "Gizlilik Sözleşmesi Prosedürü", "rev": "tr-1"})
    json.dump(t, open(tm, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    rp = os.path.join(ROOT, "prosedurler", "refs.json"); refs = json.load(open(rp, encoding="utf-8"))
    own = re.sub(r"\.$", "", CODE)
    text = "\n".join(" ".join(x[1:4]) if isinstance(x[1], str) else "" for x in I)
    for ref in sorted(set(re.findall(r"EMS\.[A-ZÜİÖÇŞĞ]+\.(?:PRO|POL|TL)\.\d+\.\d+", text))):
        if ref == own: continue
        refs.setdefault(ref, [])
        if own not in refs[ref]: refs[ref].append(own)
    refs.setdefault(own, [])
    json.dump(refs, open(rp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    o = build_official(); t = build_tr(o); register(); print(o); print(t)
