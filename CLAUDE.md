# EMS sitesi — kalıcı çalışma kuralları

> **Her sohbette önce `HAFIZA.md`'yi oku; sohbet sonunda oraya kısa not ekle.**

Site tek dosyadır: `index.html` (GitHub Pages + Firebase/Firestore). Bu kurallar her oturumda geçerlidir.

## Soru ekleme / birleştirme / senkronizasyon (HER ZAMAN)
- Yeni bir soru, bulgu, CAP maddesi veya kontrol listesi eklerken **önce diğer tüm bölümlerde aynı soru var mı kontrol et** (CSR, İSG, Çevre, Sivil Savunma, Organik, Higg, OEKO-TEX, Inditex, M&S, Müşteri Denetim Soruları ve müşteri bulguları).
- Aynı soru varsa **birleştir**: yeni kayıt açma, mevcut soruyu bağla (`CUSTOMER_DOC_QUESTIONS` "same" alanı, `_qMergeDefs` grupları).
- Birleşik sorular **entegre ve senkronize** çalışır: durum değişikliği tüm grup üyelerine ve bağlı bulgulara yansır (`_syncMergedGroup`), genel toplamda bir kez sayılır (`_uniqueQuestions`).
- Bulgular soruya bağlanır (`_linkFindingsToQuestions`); bulgu ↔ soru durumu iki yönlü senkron.

## Veri ve fotoğraflar
- **FOTOĞRAFLARI SİLME.** Mevcut verileri ve sitenin işleyişini bozma.
- Her durum değişikliği için en az 1 kanıt fotoğrafı/belgesi zorunlu (her yönde, "Yapılmadı"/"Açık" dahil).
- Sorular buluttaki tek `questions` belgesinde saklanır (1 MB sınırı) — soru metinlerini kısa tut, boyutu kontrol et.
- Performans Sistemi olduğu gibi kalır.
- Yetki modeli B: silme/değişiklik admin onayına, yeni kayıt doğrudan; personel silemez.

## Dil ve sunum
- Site 3 dilli kalmalı (TR/EN/AR). Soru metni "TR / EN" biçiminde; metin içinde " / " kullanma.
- Raporlar dönem başlığıyla başlar.

## İş akışı
- Geliştirme dalı: `claude/selam-pwr5q1`. Her değişiklikte commit → push → main'e PR → PR'ı birleştir.
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
- Yeni bir özellik, ayar, otomasyon, eklenti ya da kullanıcıdan bir işlem (silme, kurulum, ayar) isteyen her adımda: **önce ne yapacağını ve nedenini 2–3 kısa maddeyle anlat, kullanıcının onayını bekle, sonra yap.**
- Kullanıcıya adım adım, tek seferde tek iş ver; gerekirse ekran görüntüsü üzerinde işaretleyerek göster.
- Kısa ve net yaz; teknik terim kullanma.
- **Her işin sonunda** kullanıcının işini kolaylaştıracak en fazla 1–2 kısa öneri sun (araç, otomasyon, düzen, tasarruf); onay almadan yapma.
