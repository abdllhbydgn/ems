# EMS sitesi — kalıcı çalışma kuralları

> **Her sohbette önce `HAFIZA.md`'yi oku; sohbet sonunda oraya kısa not ekle.**

Site tek dosyadır: `index.html` (GitHub Pages + Firebase/Firestore). Bu kurallar her oturumda geçerlidir.

## Soru ekleme / birleştirme / senkronizasyon (HER ZAMAN)
- Yeni bir soru, bulgu, CAP maddesi veya kontrol listesi eklerken **önce diğer tüm bölümlerde aynı soru var mı kontrol et** (CSR, İSG, Çevre, Sivil Savunma, Organik, Higg, OEKO-TEX, Inditex, M&S, Müşteri Denetim Soruları ve müşteri bulguları).
- Aynı soru varsa **birleştir**: yeni kayıt açma, mevcut soruyu bağla (`CUSTOMER_DOC_QUESTIONS` "same" alanı, `_qMergeDefs` grupları).
- Birleşik sorular **entegre ve senkronize** çalışır: durum değişikliği tüm grup üyelerine ve bağlı bulgulara yansır (`_syncMergedGroup`), genel toplamda bir kez sayılır (`_uniqueQuestions`).
- Bulgular soruya bağlanır (`_linkFindingsToQuestions`); bulgu ↔ soru durumu iki yönlü senkron.
- **MÜŞTERİLER VE DENETİMLER BAĞIMSIZDIR (kullanıcı kuralı):** Müşteri soruları (kategori `custq`, `inditex`, `ms`; `_isCustQ`) genel toplamdan, `_uniqueQuestions`/`calcMetrics`/birleştirmeden ve bölüm sayfalarından ÇIKARILMIŞTIR; aynı soru olsa bile birleştirme YOK. Her müşterinin kendi soru nesnesi vardır (`_brandSet`, `fqCust` tek müşteri); `CUSTOMER_DOC_QUESTIONS` satırları hep müşterinin kendi sorusudur (`r[6]` yalnız eski ortak sorudan durum/fotoğraf devri için, `_custSplitMigrate`). Yeni müşteri sorusu/bulgusu eklerken diğer bölümlerle eşleme yapma; yalnız aynı müşterinin soru/bulgusuyla ilişkilendir.

## Belge birleştirme kuralı (kullanıcı kuralı, HER ZAMAN)
- Yeni prosedür / talimat / form / SOP yazmadan önce **mevcut resmî belgelerle karşılaştır** (`prosedurler/` + `manifest.json`, `formlar/` + `manifest.json`, QMS `QMS_PRS_OFFICIAL`).
- **FORMLAR BİRLEŞTİRİLMEZ (kullanıcı kuralı):** Excel formları (`formlar/`, `FRM-*`) farklı amaçlıdır; konu benzese de birleştirme, mevcut Excel'i değiştirme, ikisini tek forma indirme. Yalnız **prosedür, talimat ve SOP** için birleştirme kuralı geçerlidir. Taslak form (`FRM-*`) ile mevcut Excel form yan yana kalır; gerekirse aralarına sadece "ilgili form" bağlantısı konur.
- Aynı konuda belge varsa **yeni ikinci kopya açma**: mevcut belgeyi daha kapsamlı ve kurumsal bir dille yazıp **tek belgede birleştir** (aynı kod/ad, revizyon R01…, `manifest.json` `rev` değişir).
- Prosedürler EN+AR tek .docx; imza bloğu mevcut şablondan (bkz. HAFIZA); üretim araçları: scratchpad `prolib.py`/`assemble.py` yöntemi (şablon docx + gövde yeniden yazımı). Belgelerin geçtiği yerler `prosedurler/refs.json` (Doküman Dizini bunu kullanır; belge eklenince yeniden üret).

## Veri ve fotoğraflar
- **FOTOĞRAFLARI SİLME.** Mevcut verileri ve sitenin işleyişini bozma.
- Kanıt fotoğrafı/belgesi yalnız "Tamamlandı" ve "Devam Ediyor" (bulgularda "Kapandı"/"Devam Ediyor") için zorunlu; "Başlanmadı"/"Açık" için istenmez. (Soru durumu adları: Tamamlandı / Devam Ediyor / Başlanmadı.)
- Sorulara sorumlu + elle termin: `q.owner`, `q.ownerDue` (admin ve Kişi Rehberi'nde "atama yetkisi" (`assign` bayrağı, `_qCanAssign`) verilmiş kişiler atar ve e-posta gönderir; bu kişiler yalnız sorumlu alanlarını onaysız yazar (`_ownerOnlyChange`); adresleri koda gömme, yönetici Kişi Rehberi → toplu ekle'den yapıştırır; birleşik grupta ortak, boş bulgu sorumlusuna geçer) — `openQOwnerDialog`. E-posta `q.ownerEmail`; Kişi Rehberi `openContactDirectory` (= `dailyAuditEmailPool`, tek ortak liste; e-posta adreslerini koda gömme); e-posta Outlook ile `qOwnerMail` / `qOwnerMailAll`.
- Sorular buluttaki tek `questions` belgesinde saklanır (1 MB sınırı) — soru metinlerini kısa tut, boyutu kontrol et.
- Performans Sistemi olduğu gibi kalır.
- Yetki modeli B: silme/değişiklik admin onayına, yeni kayıt doğrudan; personel silemez.

## EĞİTİM / TANITIM VİDEOSU BİTİŞ EKRANI (kullanıcı kuralı, 26.10.2026, HER ZAMAN)
- **Her eğitim ve tanıtım videosu** sahnenin ortasında bitmez; mutlaka son sahne "Thank you" bitiş ekranıdır: solda EMS logosu + "Thank you / Teşekkürler · شكراً" + "Quality starts with you" etiketi, sağda Abdullah Baydoğan iletişim kartı (ofis, fabrika, telefon, e-posta, web). Şablon: `tanitim/bitis_ekrani_sablon.js` (`CLOSE`), örnek metin: `tanitim/oryantasyon.json` son sahne (`kapanis`). Bitişte ≥ 3–4 sn sabit tutulur, kapanış cümleleri seslendirilir (EN ses, TR+AR altyazı). Bu ekran olmadan video teslim edilmez/yayınlanmaz.
- **VİDEO ÜRETİM İŞ AKIŞI (kullanıcı kuralı, 26.10.2026, HER ZAMAN):** videoyu **bir kez çek, hazır tut**. Sahne klipleri ve araçlar `tanitim/kaynak/` altında saklanır (README'ye bak); küçük metin/ses düzeltmesinde videoyu baştan çekme, **yalnız ilgili sahneyi yeniden çek**, klipleri yeniden birleştir. Yeni video çekince sahne klipleri + meta + araçlar da repoya konur (ephemeral konteynere güvenme).
- Eğitim videoları: İngilizce seslendirme, altyazı TÜRKÇE + ARAPÇA (tek video); Türkçe seslendirme yapma.

## Dil ve sunum
- **YENİLEMEDE AYNI SAYFA (kullanıcı kuralı):** her yeni sayfa/pencere açılışında `saveLastView("ad", params)` çağır ve `_applySavedView` içine `case` ekle; yenileyince kullanıcı ana sayfaya düşmemeli.
- Site 3 dilli kalmalı (TR/EN/AR). Soru metni "TR / EN" biçiminde; metin içinde " / " kullanma.
- Raporlar dönem başlığıyla başlar. Özet kartları `_pdfKpiBandHtml` (lacivert bant). Rapor başlığı her zaman `_pdfHeadHtml` (logo solda, ad ortada, sağda konu ikonu); imza tam genişlik bant (`_pdfSignatureCanvas`). Yeni rapor eklerken bunları kullan.
- **İMZA YERİ KURALI (tüm indirilen raporlar):** imza bandı raporun bittiği yerin hemen altına gelir; tam sığmayacaksa (yarım kalacaksa) bir sonraki sayfanın en üstüne, üstünde ince "EMS — Rapor devamı" satırıyla konur (`_pdfAddSignature`). Sayfa ortasına/altına itme.

## MOBİL KONTROL (kullanıcı kuralı, 24.10.2026, HER ZAMAN)
- Yaptığımız her yenilik ve düzeltme **mobilde de** kontrol edilir: Playwright ile 390 ve 360 px genişlikte (isMobile) aç, yatay taşma var mı bak (`scrollWidth` ≤ `innerWidth`), ekran görüntüsüyle göz at; sorun varsa düzelt, sonra teslim et. Kullanıcıya cevapta "mobilde de baktım" diye yaz.

## İş akışı
- Geliştirme dalı: `claude/selam-pwr5q1`. Her değişiklikte commit → push → main'e PR → PR'ı birleştir.
- **SÜRÜM (her değişiklikte ZORUNLU):** commit'ten hemen önce `index.html` sonundaki `EMS_BUILD` ve `version.json` aynı değere (İstanbul saati `YYYY-AA-GG SS:DD`) güncellenir. Komut:
  `B=$(TZ=Europe/Istanbul date +"%Y-%m-%d %H:%M"); sed -i "s/^const EMS_BUILD = \".*\";/const EMS_BUILD = \"$B\";/" index.html; printf '{"build": "%s"}\n' "$B" > version.json`
  Site en alttaki telif satırında ("© … Designer by Abdullah Baydogan" yanında) "Sürüm / Build: GG.AA.YYYY SS:DD" gösterir; yayındaki `version.json` daha yeniyse üstte "Yeni sürüm — Yenile" şeridi çıkar. Kullanıcıya cevapta yeni sürüm saatini yaz ("en altta Sürüm / Build: … görünce yeni hâldesiniz").
- Kullanıcıya Türkçe açıkla; 2–3 dakika sonra Ctrl+F5 yapmasını söyle.
- Commit/PR metinlerine model adı yazma.

## Dosya haritası (TOKEN TASARRUFU — tüm dosyayı okuma)
`index.html` ≈ 5,5 MB / 67.800 satır. **Asla tamamını okuma.** Sembolü `grep -n` ile bul, yalnız o aralığı `sed -n 'A,Bp'` ya da Read offset/limit ile oku.
Satır numaraları yaklaşıktır; düzenlemeden önce grep ile doğrula.

| ~Satır | Bölüm / sembol |
|---|---|
| 37–2360 | CSS (`<style>` blokları); 1830–1876 Firebase SDK, Chart.js, PDF kütüphane yükleyici (`LIBS`) |
| 5849–66494 | **Ana script** (tek blok) |
| 5960 | `UI_TRANSLATIONS` (TR/EN/AR arayüz metinleri); 8853 `setLanguage`; 9068 `BI_STATIC_TEXT`; 41667 `_DYN_DICT` |
| 9733 | `defaultAuditQuestions` (CSR/İSG/Çevre/Sivil Savunma/Organik/Higg… varsayılan sorular) |
| 17446 | `CUSTOMER_DOC_QUESTIONS` (müşteri denetim soruları, "same" alanı); 18137 `CUSTOMER_DOC_EXTRA_MERGES` |
| 18147 | `OEKOTEX_QUESTIONS`; 18305 `HR_QUESTIONS` |
| 18657 / 19855 | `AR_Q_TEXT` / `AR_Q_SCOPE` (soruların Arapçası) |
| 21286–29400 | Günlük iç denetim: `DAILY_AUDIT_DEPARTMENTS`, `DAILY_AUDIT_QUESTION_BANK`, `openDailyAudit*`, aylık/haftalık raporlar |
| 27202–27300 | A4 PDF sayfalama `_pdfAddCanvasA4`, `REPORT_SIGNATURE` |
| 31193 / 31235 | `NEXT_FU_AUDIT`, `GEORGE_AUDITS` |
| 31365 | `firebase.initializeApp`; 31375 `save()`; 47094 `load()`; 46497 `_transactionalMergeSave` |
| 32292–41200 | **Performans Sistemi (DOKUNMA):** `TEAM_*`, KPI/OKR, `openTeamHub` |
| 41622 | Site duyurusu; 41931 `requestApproval` (yetki modeli B); 43093 `openBackupHistory`; 43196 `openUserManagement` |
| 43616–45270 | Departman denetimi: `openDeptAudit*`, `openDepartmentsHub`, `openDepartmentChecklist` |
| 47117 / 47215 / 47264 | `DEPARTMENT_SCOPES`, `PRODUCTION_MAIN_DEPARTMENTS`, `PRODUCTION_DEPARTMENTS` |
| 49917 | `AR_DEPT_TEXT`; 50135 `canEditScope`; 50717 `VISITOR_PUBLIC_DOCS` |
| 52169–53100 | Sertifikalar (`CERT_STATUS_META`); 52591 `ABOUT_CONTENT`, `openAboutHub` |
| 53637–54500 | Eğitim videoları, prosedür arama, doküman galerisi |
| 56046–56110 | M&S kontrol listesi, marka soru seti (`BRAND_MODULE_CATS`) |
| 56107–56480 | Bulgu → soru: `_linkFindingsToQuestions`, `QUESTION_DEDUP_MERGES` |
| 56464–56600 | Soru birleştirme: `_qMergeDefs`, `_uniqueQuestions`, `_syncMergedGroup` |
| 56673–57620 | Müşteri sayfası bulguları, `openAddFindingForm`, `openCustomerPicker`, `openCustomerDashboard`, `openCustomerAudits`; 58656 `Q_TO_FINDING_STATUS` |
| ~61100–61600 | Kimyasal tüketim: `_chemicalDeptStats`, `_chemMonthlySeries` (aylık giriş/kullanım/stok), `openChemicalDeptReport` (rapor panosu `crp-*`), `_chemImportMonthlyWide` (aylık Excel: Gün 1–31 blokları), `handleChemicalExcelImport` |
| 63472–64780 | Üretim raporları panosu |
| 64835–65360 | Yönetim özeti (+PDF), ana sayfa uyarı şeridi, müşteri denetimine hazırlık, mobil hızlı denetim |
| 65359–66494 | Çevrimdışı kayıt, döviz, bulut, ekran, Excel (grafikli) |
| 66990–67734 | `EMSShell` (kabuk/menü) |

Bulut: Firestore belgeleri (`questions` tek belge, 1 MB sınırı) `save()` → `_transactionalMergeSave(docId, …)` ile yazılır.
**Soru belgeleri ikiye bölündü:** genel sorular `questions`, müşteri soruları (`_isCustQ`) `customerQuestions` belgesinde (bellekte tek `auditQuestions` dizisi; `_saveQuestionDocs`, `_qCombineCloud`, `_qDocsOf`; önce müşteri belgesi yazılır, başarılıysa eski kopyalar `_qPurgeLegacyCust` ile genel belgeden temizlenir; yazılamazsa her şey genel belgeye yazılır). Doğrudan belge işlemlerinde (`_safeArrayItemUpdate`, silme) `_qDocsOf(q)` kullan.

## Ür-Ge - Ar-Ge Departmanı (kullanıcı isteği, 17-19.10.2026)
- Adı "Ür-Ge - Ar-Ge Departmanı" (kullanıcı kararı; ürün geliştirme = Ür-Ge, araştırma ve geliştirme = Ar-Ge; her projede `kind`: urge|arge, aşamaları farklı: `URGE_STAGES` / `ARGE_STAGES`; Ar-Ge alanları: hedef, bütçe, hibe, patent, sonuç). Sol menüde Yönetim Merkezi'nin altında "Ür-Ge - Ar-Ge Departmanı" düğmesi (`nav_urge`, `openUrge`); sayfa `#urge-modal` (qa-dept-overlay), kod/CSS `<script id="urge-module">` + `<style id="urge-css">` (index.html, cert-hub-modal'ın hemen üstü / ems-scroll-top düğmesinin üstü).
- Veri: bulutta AYRI `urge` belgesi (`urgeProjects`, `urgeSamples`, `urgeTests`); fotoğraf `_saveDocFileData("urge", id, "photo"/"photo2"/"photo3")`. Yetki: Kullanıcı Yönetimi'nde "Ür-Ge" kapsamı (`DEPARTMENT_SCOPES` key `urge`, `_REC_POLICY.urge*`); giriş yapan herkes görür, kapsamı olan/ yönetici düzenler (personel değişikliği/silme onaya düşer).
- Sekmeler: Pano, Projeler (aşama: Fikir→Tasarım→Numune→Test→Müşteri Onayı→Üretime Hazır→Tamamlandı), Numuneler (tur R1,R2; Revize→Yeni Tur), Testler, Raporlar (PDF `urgeDownloadPDF`, Excel `urgeDownloadXlsx`). Ür-Ge verisi yedeğe dahildir (`_extraBackupFields` / `_restoreExtraBackupFields`).

## Kimyasal tüketim Excel'i (her ay)
- Kullanıcının aylık dosyası "Monthly Consumption" biçimidir: malzeme başına 1 satır, A–I kimlik + açılış, her gün 6 sütun (Opening, Received, To Prod., Returned, Consum., Closing). `_chemImportMonthlyWide` okur; ay/yıl başlıktan alınır; o ayın kayıtları dosyadaki son hâlle değiştirilir.
- Mantık: Tüketim = Üretime çıkış − İade; Kapanış = Açılış + Giriş − Tüketim; ay sonu stok = sonraki ay başı (tutarsızlık uyarılır).
- **Kullanıcı yeni aylık Excel verdiğinde:** dosyayı `kimyasal/` klasörüne `YYYY-AA_Baski_Kimyasal_Tuketim.xlsx` adıyla koy, `kimyasal/manifest.json`'a `{file, period, rev}` ekle (aynı ay güncellenirse `rev` değiştir). Site admin açılışında `_chemAutoImportMaybe` ile otomatik içe aktarır; işlenen dosyalar bulutta `chemExcelRevs`.
- Ay geçişi uzlaştırması `_chemReconcile`: ay başı sayım > önceki ay sonu → o ayın 1'inde giriş (`chemadj_in_*`); eksik → önceki ayın son günü kullanım (`chemadj_out_*`); sonradan eklenen malzemenin ilk stoğu giriş; ayın listesinde olmayan malzeme o ay 0 (`chemabs_*`).
- Gömülü `defaultChemicalMaterials/Records` (Ağustos–Eylül) buluta yalnız `CHEM_SEED_V` değişince bir kez yazılır; bu sabiti gereksiz değiştirme (bulut kimyasal verisini sıfırlar).
- Ana sayfa kartları, tüketim ekranı ve rapor aynı dönemi (`_chemSelectedPeriod`) kullanır; aylık seri (Ağustos→) rapor, ekran ve PDF'te gösterilir.

## Araçlar
- Bulut verisini okumak için ortam değişkeni `FIREBASE_SA_JSON` (yalnız okuma yetkili servis hesabı JSON'u) varsa Firestore'u doğrudan oku; ekran görüntüsüne güvenme.
- Kullanıcı Excel/belgeleri Google Drive'a atabilir; Drive bağlantısıyla al.
- `.claude/settings.json`: sık komutlar için kalıcı izinler.

## ÖNCE ANLAT, SONRA YAP (kullanıcı kuralı)
- **HAKKIYLA, 4x4 MÜKEMMEL YAP (kullanıcının ana kuralı):** her işi eksiksiz bitir; yarım, "sonra bakarız" bırakma. Teslimden önce kendin dene (masaüstü, mobil, 3 dil, hata yok), ekran görüntüsüyle kontrol et, bulduğun her kusuru düzelt. Kullanıcıya iş bırakma; yapılabilecek her şeyi sen yap. Yapamadığın bir şey varsa nedenini açıkça söyle.
- **HER ZAMAN ÖNCE GÖSTER:** her tasarım/ekran/rapor değişikliğinde önce örnek görsel (önce–sonra) gönder; onay gelmeden main'e alma (değişiklik dalda bekleyebilir).
- Yeni bir özellik, ayar, otomasyon, eklenti ya da kullanıcıdan bir işlem (silme, kurulum, ayar) isteyen her adımda: **önce ne yapacağını ve nedenini 2–3 kısa maddeyle anlat, kullanıcının onayını bekle, sonra yap.**
- Kullanıcıya adım adım, tek seferde tek iş ver; gerekirse ekran görüntüsü üzerinde işaretleyerek göster.
- Kısa ve net yaz; teknik terim kullanma.
- **Her işin sonunda** kullanıcının işini kolaylaştıracak en fazla 1–2 kısa öneri sun (araç, otomasyon, düzen, tasarruf); onay almadan yapma.
