# HAFIZA — sohbetler arası defter

Her sohbet başında oku. Sohbet sonunda en üste 3–5 satırlık not ekle (tarih, ne yapıldı, karar, bekleyen).
Kısa tut: en fazla ~60 satır. Eski kayıtları tek satırlık özete indir.

## Kullanıcı hakkında
- Abdullah Baydoğan (abdllhbydgn@gmail.com). Türkçe, kısa ve sade cevap ister; teknik terim sevmez.
- Kural: her işin sonunda işini kolaylaştıracak en fazla 1–2 kısa öneri sun (araç, otomasyon, kısayol, düzen); onay almadan yapma.
- Kural: önce anlat, onay al, sonra yap. Adım adım, tek seferde tek iş; gerekirse ekran görüntüsünü işaretleyip göster.
- Token tasarrufu: yeni iş = yeni sohbet; basit işler Sonnet.

## Kalıcı düzenler
- Aylık kimyasal Excel: kullanıcı Drive "EMS Excel" klasörüne atar (id 16WSQV8I0Zsva86vxM4ZHxcW0mZ6g36XT) → ems/kimyasal/ + manifest (CLAUDE.md'de ayrıntı).
- Takvim: her ayın 1'i 09:00 "Excel'i klasöre at" hatırlatması.
- Rutin "EMS aylık bakım" (trig_01HqMkBTdsu7Hm44aSWK7mXd): her ayın 2'si 07:47, Excel + 3 site kontrolü, küçük hataları düzeltir.
- Firebase eklentisi ve servis hesabı anahtarı bu bulut ortamında KULLANILAMIYOR — tekrar önerme. Bulut verisi için ekran görüntüsü iste.
- Eklentiler kurulu: firebase, MetaFloor (bulutta etkisiz).

## Bekleyen öneriler (kullanıcı henüz karar vermedi)
- (10 Ekim karar: yönetime kimyasal özet e-postası YAPILMAYACAK; kullanıcı kendisi gönderir. Tekrar önerme.)
- Denetim/sertifika tarihlerini kullanıcıdan alıp Takvim'e 30 gün önceden uyarıyla ekleme.

## Günlük
- 2026-10-10: 'Yapay zekâ izlerinden arındırma' (tasarım sadeleştirme) KONUSU BEKLİYOR. Kullanıcı ZİYARETÇİ SAYFASINA (view-visitor-home) DOKUNULMASIN dedi; asıl hedef 'Genel Durum' (view-dashboard, giriş sonrası ana sayfa). Önizleme gösterildi (renkli gradyan/pastel kartlar → düz beyaz kart + ince lacivert üst çizgi, tek lacivert halka, çizgi simgeler, sol menü tek renk, uyarı şeridi sade); uygulama onayı BEKLENİYOR ('Genel Durumu uygula' denirse). Sırası: Genel Durum → pop-up/raporlar → diğer sayfalar. Teknik temizlik: commit'lere model adı yazma (kullanıcı kuralı; ben ihlal etmiştim); CLAUDE.md/HAFIZA.md görünürlüğü.
- 2026-10-10: Pop-up maddeleri kurumsal dille yeniden yazıldı (TR/EN/AR) + 4 yeni madde (KKD, elektrik panoları, ilk yardım dolapları, içme suyu/yemekhane hijyeni) = 13 madde. ANN_FIXED.ver=2: eski kayıtlı sürüm varsa yeni varsayılan kullanılır. Öneri listesinden kalan 4 madde (tahliye planı, yangın sistemi/tatbikat, makine koruyucu, eğitim-kaza kayıtları): kullanıcı 'şimdilik gerek yok' dedi — tekrar önerme.
- 2026-10-10: Pop-up boyutu kullanıcının ekran görüntüsündeki gibi: genişlik 85vw (max 1640px), yükseklik 88vh; telefonda 94vw/otomatik.
- 2026-10-10: Pop-up'taki 'Bugünün Yapılacakları' başlığı 'Bugünkü Program' (EN: Today's Schedule, AR: برنامج اليوم) olarak değiştirildi.
- 2026-10-10: Pop-up dil hatası: sitenin DOM çeviricisi (_alTextNodes/_AL_SKIP_SEL) pop-up içeriğini site diline geri çeviriyordu → pop-up kabına translate="no" + lang özniteliği (büyük harf İ sorunu), yapılacaklar _annDyn ile pop-up diline çevrilir. Pop-up açılışta site dilinde açılır (currentLang).
- 2026-10-10: Ana sayfadaki pop-up ve 📢 düğmesi YALNIZ bilgilendirme sayfasını açar (düzenle/aktif düğmeleri kaldırıldı). Düzenleme: Yönetim Merkezi → İçerik → 'Bilgilendirme Pop-up'ını Düzenle' + Yönetim Özeti başlığındaki 📢 düğmesi (yalnız admin). 'Yönetim özeti' ifadesi Yönetim Merkezi/Özeti diye yorumlandı.
- 2026-10-10: Bilgilendirme pop-up'ı TEK ekrana bağlandı: eski ayrı düzenleyici (site-announcement-editor-modal) kaldırıldı; openSiteAnnouncementEditor/FAB/Yönetim Merkezi 'Duyuru' hepsi openAnnFixedEditor (ann-fx-modal). Pop-up düzeni: üstte konu kutuları, ALTTA duyuru metni + bugünün yapılacakları (çip) + düzenle çubuğu; sayfaya sığar; açılış dili = site dili (currentLang), başlık/butonlar pt3.
- 2026-10-10 (yayınlandı): Pop-up sabit mesajı konulara göre gruplu; admin '✏️ Düzenle' ile üst yazıyı, konuları, maddeleri, simgeleri ve renkleri değiştirir/ekler/siler/sıralar (openAnnFixedEditor → siteAnnouncement.fixed; boş/değişen EN-AR otomatik çevrilir; varsayılan ANN_FIXED).
- 2026-10-10: Önemli Bilgilendirme pop-up'ının altına SABİT yönetici mesajı (ANN_FIXED, 9 ikonlu aksiyon maddesi, TR/EN/AR) eklendi; pop-up artık her girişte açılır, süre 45 sn. ÖNİZLEME gösterildi, kullanıcı onayı bekleniyor (dalda, main'e ALINMADI).
- 2026-10-10: Yönetim Merkezi 'Yapılacaklar' → Önemli Bilgilendirme pop-up'ında 'Bugünkü Program' (yalnız giriş yapmış personel+admin görür, ziyaretçi görmez). İş başına 👁️ ile gizlenebilir; tamamlanan kalkar. Kopya siteAnnouncement.todos (_todoPublish).
- 2026-10-10: Sertifika uyarısı 60 → 30 güne indirildi (_FX_CERT_WARN_DAYS). Takvim'e sertifika hatırlatması EKLENMEYECEK (kullanıcı: uyarı sitede olsun). Tarihi boş 8 sertifika: BSCI, SA8000, ZDHC, FAMA, U.S. Cotton, Sivil Savunma, ISO/IEC 17025, Higg FEM — kullanıcı sitede girecek.
- 2026-10-07: Tüm raporlarda ortak başlık _pdfHeadHtml (logo sol, ad orta, sağda konu ikonu, renkler _PDF_TOPIC_COLORS) + tam genişlik imza bandı (_pdfSignatureCanvas 3 sütun). Ekran görüntüsü raporları _reportBannerHtml da aynı. Performans Sistemi raporu değişmedi.
- 2026-10-07: Ziyaretçi/hakkımızda bölüm sayfaları, kalite sayfası, üretim bölüm/kategori ve sertifika sayfalarında önce önceki bölümün fotoğrafı görünüyordu → açılışta eski fotoğraf temizlenir, geç gelen eski yükleme yok sayılır.
- 2026-10-07: Sorumlusu olan maddeye admin kanıt yükleyince 'Bu kanıtla madde tamamlandı mı?' penceresi (_qAfterEvidence): Evet → Tamamlandı + teşekkür; Hayır → Devam Ediyor; 'Durumu değiştirme'.
- 2026-10-07: Tamamlanan maddelerde sorumlu düğmesi yerine '✅ Tamamlayan: Ad · tarih — Teşekkürler! 🙏' (q.completedBy/completedAt; sorumlu yoksa durumu değiştiren kullanıcı).
- 2026-10-07: Rehber birleştirme düzeltildi: otomatik birleştirme YALNIZ aynı e-posta; aynı ad farklı e-posta silinmez, 'olası tekrar' olarak gösterilir; 'Harici Alıcı' gibi genel etiketler ad olarak karşılaştırılmaz.
- 2026-10-07: Kişi Rehberi tekrar önleme: aynı e-posta → eklenmez, eksik bilgi tamamlanır; aynı ad (Türkçe harf/büyük-küçük farkı yok sayılır) farklı e-posta → eklenmez, ön izlemede gösterilir, istenirse e-posta güncellenir; '🧹 Tekrarları birleştir' düğmesi.
- 2026-10-07: Sürüm yazısı sol alttaki kutudan alındı, en alttaki telif satırına (Designer by … yanına) 'Sürüm / Build: …' olarak kondu.
- 2026-10-07: Site bilgilendirmesi (duyuru penceresi) artık ziyaretçiye gösterilmiyor; VISITOR_PUBLIC_DOCS ve firestore.rules'tan siteAnnouncement çıkarıldı. firestore.rules Firebase Console'da yayınlandı (kullanıcı, 07.10).
- 2026-10-07: Sürüm sistemi: sol altta 'Sürüm: …' + version.json ile 'Yeni sürüm — Yenile' şeridi; her değişiklikte EMS_BUILD + version.json güncellenir (CLAUDE.md kuralı). Sebep: kullanıcı önbellek yüzünden eski sayfayı görüyordu (soru listesi No sütunu düzeltmesi).
- 2026-10-07: Toplu e-posta konu satırı = arama kelimesi/konu + madde sayısı. Uzun listeler Outlook bağlantı sınırına (≈1900 karakter) sığmadığı için .eml dosyası (X-Unsent, HTML tablo: soru/bölüm/kapsam/durum/termin) iner; açınca Outlook'ta hazır taslak.
- 2026-10-07: Soru listesinde çoklu seçim (satır kutusu + 'Listedekilerin tümünü seç') → alttaki şeritten toplu sorumlu ata / seçilenlere e-posta (_qSel, openQOwnerDialog(0)).
- 2026-10-07: Kişi Rehberi (Yönetim → 📇; ortak liste = dailyAuditEmailPool, bulutta dailyAuditRecords belgesi; toplu yapıştır: Outlook/Excel). Sorumlu atarken e-posta otomatik; ✉️ E-posta (tek madde) + sorumluya göre süzünce 'açık maddelerini gönder' (Outlook açılır, uzun liste panoya). Kullanıcı toplu e-posta listesi verecek → rehbere yapıştırması söylenecek.
- 2026-10-07: Arama yapılınca birleşik sorular ayrı ayrı sayılıp toplam şişiyordu (ör. 1920) — düzeltildi: KPI ve liste her zaman grubu 1 kez sayar, arama grubun tüm kopyalarında yapılır. Sorumlu düğmesi belirgin (mor/lacivert/kırmızı).
- 2026-10-07: Soru listesi penceresinde arama kutusu hep açık (Tüm Sorular + Tamamlandı/Devam/Başlanmadı listeleri; sorumlu adıyla da arar). "Yapılmadı" → "Başlanmadı" (sertifika "Başvuru Yapılmadı" ve günlük iç denetim metni değişmedi).
- 2026-10-07: Sorulara sorumlu + elle termin eklendi (👤 çip, admin atar, listeden/serbest, bölüme toplu atama, sorumluya göre süzme, termini geçen uyarısı). Fotoğraf zorunluluğu yalnız Tamamlandı/Devam Ediyor (bulgu: Kapandı/Devam Ediyor). İç denetimler (günlük/departman OK-NOK) değişmedi.
- 2026-10-07: "Silinen soru geri geliyor" sebebi: birleşik grupta yalnız görünen kopya siliniyordu. deleteModalItem artık grubun tüm üyelerini kalıcı siler (bölümleri listeleyip onay sorar; bulgu/fotoğraf kalır). Silme yalnız admin; personel talep gönderir.
- 2026-10-07: Prosedürlerdeki ZIP indirme kutusu kaldırıldı. Baskı: en çok kullanılan 2 malzeme stok < 3 ton uyarısı eklendi (_chemTopStockAlert; şerit, yönetim özeti, kimyasal ekranı, rapor, PDF). Gmail/otomatik rutin İSTEMİYOR (rutin silindi). E-posta iş adresinden (abdullah.baydogan@eroglums.com, Outlook) gider: uyarı kutusundaki "Mahmut Bey'e e-posta hazırla" düğmesi (_chemTopStockMail) PDF raporu indirir + Outlook'u hazır metinle açar; kullanıcı PDF'i ekleyip Gönder'e basar.
- 2026-10-06: Prosedürler İng+Ar, 3 imzalı (225 belge). Kimyasal rapor panosu yenilendi; aylık Giriş/Kullanım/Stok kurgusu (Ağu–Eyl–Eki), ay geçişi uzlaştırması, her açılışta veri ezilmesi kaldırıldı, Ekim Excel'i kimyasal/'a kondu. Sızan Firebase anahtarları silindi (No keys). Hafıza defteri açıldı.
- 2026-10-06 (2. sohbet): Bugün iş yok; sadece hafıza okundu. Bekleyen iki öneri (yönetim e-postası, takvim uyarıları) hâlâ karar bekliyor.

- 2026-10-07 16:23: Rapor imza bandı büyütüldü; tablo raporlarında satır/fotoğraf kesilmesi giderildi (ölçülü sayfalama, _pdfFitChunks); müşteriler sütunu genişletildi; rapor başlığı büyütüldü; yeni EMS logosu (GitHub "EMS LOGO.png", beyaz zemin) EMS_REPORT_LOGO olarak gömüldü.
- 2026-10-07 16:28: Tüm raporlar kontrol edildi. Kimyasal tüketim raporu malzeme tablosu ölçülü sayfalamaya geçti (_pdfFitRowPages). Tek sayfalık sabit tasarımlı raporlarda (yönetici, kimyasal, üretim; size "lg") başlık önceki ölçüde bırakıldı, taşma olmasın diye.
- 2026-10-07 16:34: Rapor indirme hızlandı: büyük fotoğraflar rapor kopyasında gösterim boyutuna küçültülür (_pdfShrinkImages, _h2cRun içinde); sayfa bölme ölçümü fotoğrafsız hafif kopya ile (_pdfLiteHtml) ve az denemeyle (_pdfFitChunks tahminle başlar).
- 2026-10-07 16:43: Rapor özet kartları lacivert kurumsal banda çevrildi (_pdfKpiBandHtml / _pdfKpiBandStd; tablo raporu + 4 bölüm/departman raporu). Tablo raporu sütun başlıkları aynı lacivert, beyaz yazı. Yeni raporda özet için bunları kullan.
- 2026-10-07 17:00: Genel Rapor (exportReportPDF) yeni tasarım taslağı: Malzeme Detayları sayfası kaldırıldı, lacivert kabuk ve alt şerit, çizgi ikonlar (GR_ICONS), lacivert kartlar, KPI sayfası _pdfKpiBandStd ve taşma düzeltmesi. Kullanıcı onayı bekleniyor, main dalına alınmadı.
- 2026-10-07 17:05: Genel Rapor ikinci taslak: lacivert kapak (EMS_REPORT_LOGO_WHITE), içindekiler, sayfa numaraları (__GRPG__), çok dilimli halka (donutSvg), müşteri sıralaması ve bulgu kartları yenilendi, lacivert kapanış sayfası. Onay bekleniyor, main dalına alınmadı.
- 2026-10-07 17:09: Genel Rapor yeni tasarımı yayına alındı. Sol menüde Yönetim bölümü Eğitim Videoları altına taşındı, açılır-kapanır grup oldu (#admin-nav-group, durum localStorage emsAdminNavOpen).
- 2026-10-07 17:16: Genel Rapor kapağında beyaz logo beyaz kutu olarak çıkıyordu (_pdfShrinkImages saydam PNG'yi beyaz zemine JPEG yapıyordu). Saydam resimler artık PNG ve saydam kalıyor.
- 2026-10-07 17:18: Sol menü alt sırası: video (side-nav-stats-widget) → Yönetim grubu (#admin-nav-group) → Son yedek kartı (#side-backup-info, en altta; yaşı renkli etiket, tıklayınca Yedekleme Geçmişi).
- 2026-10-07 17:27: KURAL (CLAUDE.md): imza raporun bittiği yerin hemen altına; sığmazsa sonraki sayfanın en üstüne 'EMS — Rapor devamı' satırıyla (_pdfAddSignature). Tüm indirilen raporlar.
- 2026-10-07 17:36: TASLAK (onay bekliyor, main dalına alınmadı): Yönetim Özeti v2 (.mg-v2: çizgi ikonlar _MG_ICONS, hızlı geçiş sekmeleri, lacivert tablo başlıkları, denetim+sertifika yan yana); sol alt: İletişim butonu 'Yöneticiye Mesaj At', Bağlantıyı Kopyala yalnız admin, avatar Ekibimiz fotoğrafı (_sideAvatarRefresh). CLAUDE.md: HER ZAMAN ÖNCE GÖSTER kuralı.
- 2026-10-07 17:37: Yönetim Özeti v2 ve sol alt kullanıcı alanı onaylandı, yayına alındı.
- 2026-10-07 17:44: Genel kontrol (güvenlik/senkron/3 dil/mobil): soru→bulgu durum değişikliği artık bulguları da buluta yazar (_saveCustomerAuditsOnly; changeQ, _qSetStatus, _qsRun); Yönetim Özeti tekil soru sayar (_uniqueQuestions); modül toplu sorumlu atama birleşik kopyaları atlamaz; Kişi Rehberi bulut yazımı tek işlemde (_dirCloudApply); tamamlayan kaydı bulgu yollarında da güncellenir; rehber/soru e-posta işlemlerine admin kontrolü; .eml To: satırı temizlenir; kimyasal uyarı alıcısı rehberden (CHEM_STOCK_MAIL_NAME), gömülü e-posta kaldırıldı; mobil sekmeler yana kayar. 3 dil: eksik çeviri yok.
- 2026-10-07 21:15: TASLAK (onay bekliyor): Yönetim Özeti PDF yeniden yazıldı (_mgReportHtml: akıcı A4 belge, _pdfHeadHtml + _pdfKpiBandHtml + numaralı bölümler, _pdfAddCanvasA4 ile satır arası kesim). Ekranda Denetim Puanları tablo yerine puan satırları (_mgScoreRowsHtml), denetçi e-postası ada çevrilir (_mgPersonName); yan yana düzen kaldırıldı.
- 2026-10-07 21:25: Yönetim Özeti yeni PDF raporu ve Denetim Puanları satırları onaylandı, yayına alındı.
- 2026-10-07 21:28: TASLAK (onay bekliyor): kullanıcı kendi fotoğrafını sol alttaki rozete tıklayıp yükler (_sideAvatarPick/_sideAvatarFileChange, bulutta ems_csr_files useravatar_thumb_<uid>); öncelik kendi fotoğrafı, yoksa Ekibimiz fotoğrafı, yoksa baş harfler.
- 2026-10-07 21:37: Kullanıcı fotoğrafı (sol alt rozet, kendi fotoğrafını yükleme) onaylandı, yayına alındı.
- 2026-10-07 21:52: Bulut kuralları sıkılaştırıldı (firestore.rules; kullanıcı Firebase konsoluna yapıştıracak): ems_csr silme yalnız admin, admin belgeleri (siteAnnouncement, aboutCardPhotos, prodManualOverrides, *Archive_*) yalnız admin; ems_csr_files personel silemez (yalnız kendi useravatar), admin dosyalarına yazamaz, useravatar yalnız kendi uid; users: kullanıcı kendi mustChangePassword=false yapabilir (şifre ekranı döngü hatası). Kodda artık parça silme hatası kaydı bozmaz. Eski kurallar: scratchpad/firestore.rules.eski. NOT: siteyi tüm dizileri yeniden yazdığı için 'dizi kısalamaz' kuralı KONULMAMALI.
- 2026-10-07 22:17: Şifre değiştirme: şifre değiştikten sonra users belgesine mustChangePassword yazımı başarısız olursa (admin'in users kaydı yok) artık 'değiştirilemedi' hatası gösterilmez; admin için bu yazım atlanır.
- 2026-10-08 17:15: KULLANICI KURALI (CLAUDE.md'ye yazıldı): her işi hakkıyla, 4x4 mükemmel yap; teslimden önce kendin dene ve düzelt, kullanıcıya iş bırakma. (Aynı gün EFA Hazır Giyim sitesi güzel.net için bağımsız paket olarak hazırlandı; repo dışında, scratchpad/efa_site.)
- 2026-10-08 20:55: EFA Hazır Giyim sitesi (efahazirgiyim.com, güzel.net cPanel) yayına alındı: eski WordPress dosyaları silindi, yeni statik site + PHP yönetim paneli (/yonetim, kullanıcı admin, ilk girişte şifre değişimi) + teklif.php (e-posta + panelde Gelen Teklifler) yüklendi. Kaynak ve derleme betikleri scratchpad'deydi (repo dışında); indirme için 'efa-site-paketi' dalı açıldı. Açık kalanlar: WordPress veritabanı silinmedi, haftalık yedek ayarlanmadı, form e-postası canlıda denenmedi.
- 2026-10-08 21:20: EFA kapanış: site canlıda kontrol edildi, panel şifresi kullanıcı tarafından değiştirildi, teklif formu e-postası ve panel kaydı çalışıyor, WordPress/SitePad veritabanları ve kullanıcıları silindi, zip silindi. Yedek: JetBackup 5 haftalık (artımlı, mt-nas4) zaten açık. 'efa-site-paketi' dalı kullanıcı isteğiyle kalıyor.
- 2026-10-08 21:40: TASLAK (onay bekliyor): Yönetim Merkezi (openAdminHub, .ahub-*): sol menüde tek kırmızı düğme (#admin-hub-badge = onay+kullanıcı rozeti toplamı, _adminHubBadgeSync), eski yönetim öğeleri gizli tutuldu (rozet kimlikleri çalışsın diye), duyuru yüzen düğmesi gizlendi (merkezde 'Site Duyurusu'). Kutucuklar mevcut işlevleri aynen çağırır (ADMIN_HUB_ACTIONS). 2. aşama: Site İçeriği (ekran yazıları, Hakkımızda, menü, rapor bilgileri, değişiklik geçmişi).
- 2026-10-09 00:27: Yönetim Merkezi v2 (TASLAK): içerik alanında sayfa gibi açılır (class modal-overlay, #admin-hub-modal z 10049; araçlar 10050 üstünde açılır, kapanınca merkeze dönülür), büyük kutucuklar + çizgi SVG ikonlar (_AHUB_ICON), PIN kilidi (ADMIN_HUB_PIN_HASH = sha256('EMS-HUB|PIN'), oturumda bir kez, 5 hatada 5 dk kilit; gerçek koruma yönetici girişi). Günlük bulut yedeği düzeltildi: yalnız kayıtta tetikleniyordu ve 1 MB'ı aşınca sessizce atlanıyordu → artık admin açıkken 5 dk'da bir kontrol, veriler tam yüklenmeden yazmaz, büyükse ems_csr_snapshots/{gün}/parts/{n} parçalarına bölünür (chunked=n, qTotal/qCompliant özet), geri yükleme parçaları birleştirir.
- 2026-10-09 00:43: TASLAK — Yönetim Merkezi tam ekran (odak modu ems-focus + inline z-index 20390; araçlar 20400 üstte; ahub-on) ve SİTE İÇERİĞİ modülü: ems_csr/siteContent {t, about, menu, report, log}; _applySiteContent (UI_TRANSLATIONS üzerine yazar, ABOUT_CONTENT gövdeleri, REPORT_SIGNATURE, menü gizleme .sc-hidden _applyMenuVisibility applyRolePermissions'ta), alt sayfalar adminHubGo('texts'|'about'|'menu'|'report'|'log'), Hakkımızda contenteditable + _scSanitizeHtml, geçmiş 120 kayıt + geri al + tümünü sıfırla. firestore.rules: siteContent ziyaretçi okur, personel yazamaz (kullanıcı konsolda yayımlamalı). VISITOR_PUBLIC_DOCS'a siteContent eklendi.
- 2026-10-09 00:49: Ekran Yazıları listesi yalnız sitede kullanılan yazıları gösterir (_scUsedKeys: betiklerde ≥2 geçiş ya da DOM data-i18n/attr); 77 kullanılmayan eski yazı (ör. visitor_video_placeholder 'EMS Tanıtım Videosu Yakında') gizlendi.
- 2026-10-09 00:51: TASLAK — Yönetim Merkezi başlığına gezinme: Geri/İleri (_ahubHist/_ahubIdx, adminHubBack/Fwd), merkez ana sayfası (adminHubHome, ızgara ikon), site Anasayfa (adminHubSiteHome → closeAdminHub + goHome), Alt+←/→ (RTL'de ters), alt başlıkta konum (Yönetim Merkezi › sayfa).
- 2026-10-09 01:01: TASLAK — Merkezden açılan araçlara (onaylar, kullanıcılar, kişi rehberi, duyuru, yedek geçmişi, gelir-gider) aynı başlık şeridi: #ahub-toolbar (geri/ileri/merkez/Anasayfa/kilit/kapat), AHUB_TOOLS, _ahubAttachTool/_ahubDetachTool, geçmişte 'tool:<key>' kayıtları; araç kendi X'iyle kapanınca şerit kalkar.
- 2026-10-09 01:09: TASLAK — Menü Düzeni genişletildi: sıra okları (bölüm içinde), 'Bölüm' seçimi (öğe başka bölüme taşınır), simge seçici (kabuğun çizgi simgeleri window.EMS_NAV_ICONS), bölüm başlıklarının TR/EN/AR adları. Bulut: siteContent.navLayout {bölümKey:[navKey]} ve siteContent.icons {navKey: simge}; _navCapture/_navComputed/_applyNavLayout/_applyNavIcons; geçmişte 'layout'/'icon' kayıtları geri alınabilir; 'Menü sırasını ilk hâline döndür' düğmesi.
- 2026-10-09 01:19: TASLAK — Yönetim Merkezi'ne sol menü (merkezin kendi renk/simgeleriyle; .ahub-side, _ahubSideHtml, _ahubLayout). Ana ekran kutucukları korundu, artık AHUB_MENU/AHUB_ITEMS tanımından çiziliyor. Merkez menüsünün adı/sırası/bölümü/simgesi Menü Düzeni → 'Yönetim Merkezi menüsü' sekmesinden (_scMenuTab='hub') değişir; bulut siteContent.hub {names, secNames, icons ('n:' = sol menü simge seti), layout}; geçmişte 'hub' kaydı geri alınabilir. 900px altında merkez sol menüsü gizli (kutucuklar yeterli).
- 2026-10-09 01:21: Sarı bilgilendirme (duyuru) yüzen düğmesi #announcement-admin-fab GERİ GETİRİLDİ (Yönetim Merkezi kurulurken sormadan gizlenmişti). KULLANICI KURALI: mevcut düğme/özellik/bölüm, kullanıcıya SORMADAN kaldırılmaz, gizlenmez, yeri değiştirilmez.
- 2026-10-09 01:32: TASLAK — YALNIZ Yönetim Merkezi'nde: merkezden açılan araçlar (onaylar, kullanıcılar, kişi rehberi, duyuru, yedek geçmişi, gelir-gider) açılır pencere değil, sağ tarafta sayfa gibi (.ahub-pane; _ahubPlaceTool: üst = merkez başlığı altı, yan = sol menü kenarı, RTL'de ters). _ahubView = 'tool:<key>'; sol menü işaretli, alt başlıkta adı. Ayrı araç şeridi (#ahub-toolbar) artık gösterilmiyor (merkez başlığı yeterli). Aracın kendi X'i → Genel Bakış. Kilit/kapat/anasayfa aracı da kapatır. Site alt bilgisi (footer) merkez bölümlerine taşınmaz (placeFooter skip ahub-pane). Merkez dışından açılan araçlar eskisi gibi.
- 2026-10-09 15:46: TASLAK — (1) Merkezden açılan bölümlerdeki 'sol üstten sağa açılma' efekti kaldırıldı (.modal-overlay transition: all .3s → .ahub-pane ve #admin-hub-modal'da transition:none). (2) Genel Bakış: 4 özet kartı büyük (2x2, .ahub-stats-big) + yanında Yapılacaklar kartı (#ahub-todo): gün gün liste (‹ Bugün ›), ekle/işaretle/sil, önceki günlerden tamamlanmamışlar bugünde kırmızı görünür; bulut ems_private/adminTodo {items:[{id,text,day,done,doneAt,createdAt}]} (yalnız admin), yerel önbellek ems_admin_todo. Genel Bakış'taki kutucuklar kaldırıldı (sol menü yeterli); telefonda sol menü Genel Bakış'ta kartların altında liste olarak görünür.
- 2026-10-09 15:57: TASLAK — Genel Bakış yeniden tasarlandı (.ahd): karşılama şeridi (ad, tarih, özet), 4 durum kartı (tıklanınca ilgili bölüm), 'Site durumu' 8 kart (_ahdSiteHtml: Yönetim Özeti ile aynı hesaplar — genel uyum, açık bulgu, termini geçen, sertifika uyarısı, iç/departman denetim ort., kritik kimyasal stok, bugünkü denetimler; tıklanınca merkez kapanır ve sayfa açılır ahubOpenSite), son değişiklikler, sağda boydan Yapılacaklar. Footer 'Arapça Öğren' logosu yeni logoyla (SVG, lacivert daire + turuncu piramit + mavi ses dalgaları) değiştirildi.
- 2026-10-10: Departman denetimi yetkisi: üretim ana bölümleri (iplik, orgu, boyahane, baski, nakis, konfeksiyon) Kullanıcı Yönetimi'nde kişi bazlı yetki; alt bölüm ana bölüm yetkisine bağlı (_prodMainOf). Yetkisiz bölüm kartında kilit rozeti.
- 2026-10-10: Kullanıcı Yönetimi yeni tasarım: solda isim listesi, sağda seçilen kişinin yetkileri (üretim bölümleri + genel), 'Onayla ve Kaydet'. Firestore değişikliği yok (users/{uid}.departments).
- 2026-10-10: Kullanıcı Yönetimi: görev/unvan Performans Sistemi (teamDb, e-posta eşleşmesi) üzerinden okunur, yoksa admin elle yazar (users/{uid}.jobTitle). Genel yetkiler 4 konu grubuna ayrıldı; alt bölümler kutu içinde açılır.
- 2026-10-10: Kullanıcı Yönetimi: isim listesi kaydırma konumu korunur; fotoğraflar Performans Sistemi'nden (team_member thumb) e-posta eşleşmesiyle gelir.
- 2026-10-10: Sade/kurumsal tasarım yayında (html.ems-sade, index.html başındaki <style id=ems-sade-css>; üretici betik scratchpad'de, değişiklikte CSS bloğunu elle düzenle). Muaf: pop-up, yönetim özeti, yönetim merkezi, indirilen raporlar (_h2c onclone sınıfı kaldırır). Geri dönüş: Yönetim Merkezi → Site Tasarımı (bulut ems_csr/siteContent.uiDesign) veya ?tasarim=eski.
- 2026-10-10: Antrasit (#2E3135) renk düzeni yayında; ev (anasayfa) düğmeleri, yukarı ok, aç/kapa düğmesi, altın şeritler kırmızı (#C1272D). Üretici betik scratchpad'de; antrasit/kırmızı kuralları index.html'de #ems-sade-css ve #ems-up-red bloklarında.
- 2026-10-10: Lacivert/indigo → renk değişkenleriyle antrasit (--navy) ve kırmızı (--primary, --navy-bg); muaf alanlarda değişkenler eski değerine döndürülür. Düğmeler kırmızı, yazılar antrasit. Sağ başlık boşluğu için silik süs önerildi (onay bekliyor).
- 2026-10-10: Doğru EMS logoları (siyah/beyaz, gölgesiz) kullanıcıdan alındı ve yerleştirildi (yan menü/giriş/qa overlay=beyaz; footer/rapor/grup şeridi/köşe=siyah). Logo gölgeleri ve parlama animasyonu kaldırıldı. Kırmızı daha canlı: --red #E11D2E (sade modda), koyu zeminde #FF3B47.
- 2026-10-10: Başlık bandının sağına silik kumaş dokusu deseni (A, html.ems-sade .dept-banner::after; masaüstü, tıklanmaz).
- 2026-10-10: Genel tarama (12 kombinasyon: 3 dil × masaüstü/mobil × yeni/klasik + 624 düğme + roller) yapıldı. Düzeltilenler: kart başlıkları dar ekranda kesiliyordu (sarılıyor), tasarım anahtarı siteContent'e taşındı (ziyaretçi okur, yalnız admin yazar; Firestore kuralı değişikliği gerekmez), çeviri servisi ağ hatasında 5 ardışık hatada 2 dk durur, footer kopyalarında yinelenen id temizlendi.
- 2026-10-10: Yükleme kuralı (yetki modeli B netleşti): boş yuvaya yükleme doğrudan; DOLU yuvaya yükleme (değiştirme) kayıtlı kullanıcı için yönetici onayına gider, eski dosya onaylanana kadar yerinde kalır (soru kanıtı, bulgu, doküman, sertifika; _uploadNeedsNoApproval). Sertifikada dolu yuvaya Office dosyası yüklemek kayıtlı kullanıcıya kapalı. 'Ara' düğmesi kırmızı.
- 2026-10-10: ACİL DÜZELTME: renk değişkeni dönüşümü '#1A3660'+alfa (ör. #1A36601c) tanımlarını bozmuş, Hakkımızda/Sertifikalar tam sayfa pencerelerinin arka planı kaybolmuştu → alfa'lı hex'ler geri döndürüldü. Performans Sistemi (#team-hub-modal, #team-page-root) yeni tasarımdan muaf (DOKUNMA kuralı). Gelecek renk dönüşümlerinde: hex+alfa'yı ve görsel kontrolü (saydam overlay, ikon-yazı çakışması) unutma.
- 2026-10-10: Sayfa tipi pencerelerde açılış animasyonları kapatıldı (arkadaki anasayfa 0,2-0,4 sn görünüyordu); sayfa ilk karede tam görünür.
- 2026-10-12: 'CSR & Sürdürülebilirlik' etiketleri 'CSR & Compliance' yapıldı (menü, başlık, kartlar, rapor adları; karşılama sloganı hariç). Modül sayfalarındaki (CSR, İSG, Çevre, Sertifika vb.) üst KPI kutuları İç Denetimler tarzı halka kartlara çevrildi (openDetailModal). Prosedürler klasör halkası = belge sayısı / en kalabalık klasör (renderLegalFolderGrid) — kullanıcıya açıklandı; halkadan vazgeçme kararı bekleniyor.
- 2026-10-12: Müşteriler kartlarında logo/fotoğraf eklenemiyordu: yeni tasarımda görünmez Sil düğmesi (sol üst) Fotoğraf düğmesinin üstüne biniyordu. Sil düğmesi sağ üste alındı, üzerine gelince görünür. U.S. Polo dahil denendi.
- 2026-10-12: Prosedürler klasör kartları halkasız (büyük ikon, '6 klasör · 48 belge' özeti; .legal-folder-big). Müşteri Denetimine Hazırlık: 5 büyük halka kart (Sertifika Uyarısı kutusu kaldırıldı). Müşteri kartlarında dikdörtgen logo kutusu 112x64 (object-fit:contain). 'CAP ayrı, belge adedi' isteği netleşecek.
- 2026-10-12: Belge galerileri (Şirket Profili, Üst Yönetim, Kalite, Eğitim Videoları) Hakkımızda tarzı büyük kartlar (.dgc-grid CSS).
- 2026-10-12: Hazırlık sayfasından Sertifika Durumu listesi kaldırıldı. Müşteri denetim panosu yeniden tasarımı örnek olarak gösterildi, onay bekliyor (renk: duruma göre mi antrasit mi).
- 2026-10-12: Müşteri denetim panosu üst kutuları halka kart + büyük bölüm kartları (renderCustomerTopDashboard). Prosedürler belge adedi etiketi büyütüldü. EMS Form Arşivi Prosedürler tasarımına çevrildi (link kartları; tıklama linki yeni sekmede açar; düzenle/sil/toplu ekle aynen). Toplu ekle paneli artık varsayılan kapalı.
- 2026-10-12: EMS Form Arşivi klasörlü yapıya geçti (Prosedürler mantığı): klasör kartları, klasör içinde form kartları (dosya türü önizlemesi, link görünmez), arama, klasör ekle/düzenle/sil; klasör, formsDocs öğelerinde 'folder' alanı ve isFolder kayıtlarıyla saklanır; ilk açılışta form adı sonundaki (Bölüm) ifadesinden otomatik klasörlenir. Sol menüden Yönetim Özeti kaldırıldı (ana sayfada var).
- 2026-10-12: EMS Form Arşivi artık Prosedürler ile AYNI motor: store 'forms' (klasör: formsDocs=[{id,name,documents:[{videoLink,link}]}]), _isFolderStore/_folderRoot, openProceduresLibrary→openDocumentLibrary('forms'); form kartı tıklanınca videoLink'i açar, Yükle ile önizleme fotoğrafı/PDF/Office yüklenir; eski düz liste ilk açılışta ad sonundaki (Bölüm)'e göre klasörlere taşınır (_migrateFormsToFolders).
- 2026-10-12: Form Arşivi veri düzeltmesi: yeni bulut alanı formsFolderDocs (formsFolders); eski düz liste formsDocs ve önceki denemeden kalan kayıtlar dokunulmadan kaynak olarak kullanılır, çiftler adı/linke göre tekilleştirilir, Prosedürler'deki klasör adlarıyla (24) kategorize edilir (_setupFormsFolders, _formTargetName). Sol menüye 'Kalite Yönetim Sistemi' (openQmsPage, içerik sonra). Kart tasarımı v2 ile birlikte yayında.
- 2026-10-12: Ana sayfa tüm özet kartları (genel+üretim+kimyasal) aynı boyut 112px ve aynı düzen; rakam yazı tipi 900→800 (site fontu 400-800 yükler, 900 yapay kalın görünüyordu); mobil düzeltmeleri.
- 2026-10-12: Bölüm kartları 5 sütun (özet/üretim/kimyasal kartlarıyla aynı genişlik ve aralık); halka sağ üstte; bölüm kartları hover açık kalır (madde işaretleri dot+box-shadow).
- 2026-10-12: Kalite Yönetim Sistemi menü butonu Denetime Hazırlık'ın altına taşındı.
- 2026-10-12: TÜM kartlar 256px (bölüm kartı yüksekliği) aynı; üst 5 Genel Durum kartı bölüm kartı tasarımında (_renderTopDonutCards, .top-donut); hover koyu dolgu+parlama efekti KORUNDU (yanlışlıkla kaldırmıştım, kullanıcıya sormadan); Yönetim Özeti uyarı şeridi 'GENEL DURUM' başlığının üstüne taşındı.
- 2026-10-12: Genel Uyum Oranı detay sayfası (renderComplianceBars) ana sayfa bölüm kartı tasarımında (donut3+liste); üretim/kimyasal kart rakamları 21px; Üretim menüsü adları '… Raporları'; durum renkleri tüm sitede (Tamamlandı yeşil #15803D, Devam turuncu #EA580C, Başlanmadı/Açık kırmızı #DC2626; .status-sel + option).
- 2026-10-12: Kart tasarımı tüm sayfalarda ana sayfa diliyle: İç Denetimler, Departman raporları/alt bölümler, Departman Denetim Kayıtları, Müşteriler (logo kutusu + halka + liste), Prosedürler/Form Arşivi klasör kartları (başlık satırı + büyük adet, hover görünür), üretim/kimyasal kart halkası bölüm kartlarıyla aynı. Yardımcılar: _pgLegend/_pgDonut/_donut1Svg/_donut3Svg. Departman Denetimleri ana sayfasındaki fotoğraflı kartlar fotoğraf korunsun diye dönüştürülmedi.
- 2026-10-12: Üretim/kimyasal kartlarında hover'da halka/yüzde/rakam beyaz görünür (koyu zeminde kayboluyordu).
- 2026-10-12: Modül sayfaları (İSG/Çevre/CSR/Sertifika… openDetailModal) üst 5 kutu ana sayfa üst kartlarıyla aynı tasarım (donut + liste, .modal-donut-row).
- 2026-10-13: PERFORMANS: MutationObserver yalnız eklenen eleman düğümlerinde tetiklenir (sayaç metin güncellemeleri iconify/applyFx'i tekrar tekrar çalıştırıyordu); sayaç süresi 900→420 ms; hover'da dev inset gölge kaldırıldı, parlama left yerine transform; giriş animasyon gecikmeleri 0; kart ::before/::after blur kaldırıldı; geçişler yalnız transform/gölge (.16s), will-change+contain. Tüm .customer-kpi kutucukları upgradeKpiTiles() ile ana sayfa kartına dönüştürülür (Hazırlık dahil). Bilinen: ilk veri render'ı tüm bulut belgeleri gelince (_cloudFirstRenderDone) — erken çizim yapılmadı.
- 2026-10-13: Mobil kartlar masaüstüyle aynı tasarım: üst 5 kart tam genişlik donut+liste, üretim/kimyasal kartlarında halka+açıklama mobilde de görünür, kartlar mobilde otomatik yükseklik.
- 2026-10-13: Kullanıcı form dosyalarını GitHub kök dizinine (klasörleriyle) yüklemişti; hepsi formlar/ altına taşındı (alt klasörler korunur: '0. Ön Hazırlık…', '7. Boyahane…'). Sıradaki: formlar/manifest.json + otomatik içe aktarma (prosedurler/ mantığı), alt klasör adları Form Arşivi klasörleri.
- 2026-10-13: FORM ARŞİVİ DOSYALARI: formlar/ (manifest.json, 73 dosya; kullanıcının 9 klasörü = Form Arşivi klasörleri + İplik Bölümü + Diğer Formlar; kök kopyalar eski sürüm olduğu için formlar/_eski/ içinde). _formsImportMaybe: yönetici girişinde bir kez dosyalar buluta yüklenir (store 'forms', officefile), kodu+adı eşleşen eski bağlantılı forma dosya eklenir ve klasörüne taşınır; Prosedür klasörlerini taklit eden eski klasörler bir kez temizlenir (formsCleanupV1). Bulutta: formsImportV1 / formsImportRevV1. Yeni form eklemek: dosyayı formlar/ altına koy + manifest.json'a {code,file,name,folder,order,ext,rev}. Kart: dosya varsa önizleme/site içinde açılır, yoksa link.

## 2026-10-13 FORM ARŞİVİ — 2. YÜKLEME ANALİZİ
- Kullanıcı eski numaralı klasör setini de yükledi (1. Kumaş-Aksesuar, 2. Kesimhane, 3. Dikimhane, Yıkama, kök kopyalar). Hepsi tarandı: birebir aynı (hash) kopyalar silindi (18), aynı formun eski sürümleri `formlar/_eski/`ye alındı (aynı formda en yeni "modified" kazanır), kalan eski klasör dosyaları güncel klasörlere taşındı.
- Yükleme 5 yeni sürümü (00.02, 05.01, 05.02, 05.03, 06.01) eski sürümle ezmişti — önceki commit'ten geri getirildi.
- Manifest 92 form: 11 klasör (yeni: "Yıkama Bölümü (ERTELENDİ)" sıra 9). Mevcut `code` anahtarları korundu (tekrar içe aktarma yok), 19 yeni form.
- Dikkat: aynı form kodu farklı formlarda kullanılmış (03.05, 03.07) — içe aktarma kod+ad eşleştirir, çakışmaz. "KUMAŞ KONTROL FORMU.xlsx" (kodsuz) 01.03'ten farklı içerik olduğu için tutuldu.

## 2026-10-13 FORM ARŞİVİ — YALNIZ NUMARALI FORMLAR
- Kullanıcı kararı: yalnız form numarası (EMS.XX.FRM/KRT/RPR.NN.NN) olanlar kullanılır; numarasız 26 dosya formlar/ ve manifest.json'dan silindi. Manifest 66 form, "Diğer Formlar" yok. Bulutta daha önce içe aktarılmış numarasız belgeler siteden elle silinmeli.

## 2026-10-13 MÜŞTERİ KARTI KOCAMAN YUVARLAK HATASI
- Logo kutusu position:static olunca "Fotoğrafı Değiştir" düğmesi (inset:0, yuvarlak) tüm kartı kaplıyordu. Düğme artık logo kutusunun köşesinde 22px; kutu position:relative. (Boş halka -> yazı değişikliği geri alındı, kullanıcı istemedi.)

## 2026-10-13 MÜŞTERİ KARTI AD YAZISI
- Kullanıcı istemedi: müşteri kartlarında ad yazısı (ring-card-title) gizlendi; ad logoda. İstenmeyen ekleme yapma, önce sor.

## 2026-10-13 MÜŞTERİ SAYFASI TEK SAYFA
- Müşteri panosu sekmesiz tek sayfa: 4 donut kart (Tamamlanan/Devam/Başlanmayan soru + Genel Uyum; antrasit şerit, tıklayınca soru filtresi), Bulgu Dağılımı + Denetim Geçmişi (tarih, denetçi, CAP), Denetim Soruları (tüm denetimler birleşik: _brandSet), altta katlanır "Bulgu Detayları" ve "Denetim Kayıtlarını Yönet". Denetçi: a.auditor (forma eklendi) yoksa nottan _custAuditor. Eski sekme çubuğu gizli; switchCustomerProfileTab bölüme kaydırır. Fotoğraf ekleme örneği gösterildi, onay bekliyor (uygulanmadı).

## 2026-10-13 MÜŞTERİ LOGO + KANIT FOTOĞRAFI
- Logo yüklenince _fitLogoToBox: boş kenarlar kırpılır, 7:4 kutuya (448x256 PNG, beyaz zemin) ortalanıp sığdırılır. Müşteri sayfası başlığında logo (_renderCustomerHeaderLogo, admin köşe kamera/Logo ekle). Müşteri soru satırlarında kanıt hücresi (_questionPhotoCellHtml), yükleme sonrası _custRefreshIfOpen.

## 2026-10-13 LOGO GÖSTERİMDE OTOMATİK + DENETİM GEÇMİŞİ
- Kayıtlı (eski) logolar da gösterilirken _fitLogoCached ile kutuya göre kırpılıp ortalanır (arka plan rengi köşelerden, tolerans 40; tuval 504x240). Denetim Geçmişi satırlarından Açık/Kapandı rozeti kaldırıldı, başlıktan denetçi eki temizlendi.

## 2026-10-13 MÜŞTERİ SAYFASI SADELEŞTİRME
- Denetim geçmişi satırları tıklanmaz; Bulgu Detayları/CAP kartı gizli (#cust-details-findings display:none, DOM duruyor çünkü _moveFindingsCore kullanıyor); soru satırlarındaki bulgu çipleri tıklanmaz. Soru listesi başlığında "Yeni Bulgu Ekle" (openAddFindingForm) ve "Rapor İndir" (exportCustomerPPTX). Kanıt fotoğrafı + hücresi zaten satırlarda. Antrasit şerit (strip-pending, yerel dal) onay bekliyor.

## 2026-10-13 ANTRASİT ŞERİT ONAYLANDI
- Tüm kartlara border-top:4px #2b2d31 (ring/kpi/about-hub/crp/cust-sum/srp/cert-hub/fin/pgx/pcx/main-dept) yayında.

## 2026-10-13 MÜŞTERİ TEK LİSTE (SORU + BULGU)
- Müşteri sayfası "Denetim Soruları" listesi = bs.qs + soruya bağlanmamış bulgular (_custExtraItems); bulgu satırı _custFindingRowHtml (durum changeCustFindingStatus -> changeFindingStatus, kanıt şartı aynı, fotoğraf _findingPhotoCellHtml). Üst 4 kart ve calcCustomerStats aynı toplamı kullanır. Genel Uyum kartı tıklanmaz.

## 2026-10-13 MÜŞTERİ: FOTOĞRAF SÜTUNU, KAYIT YÖNETİMİ GİZLİ
- Soru/bulgu satırında Detaylar ile Durum arasında ayrı "Fotoğraf" sütunu (.cust-photo-box, kullanıcının kırmızı işaretli alanı). "Denetim Kayıtlarını Yönet" (#cust-details-audits) gizli (DOM duruyor).

## 2026-10-13 MÜŞTERİ TABLO DÜZENİ
- Soru tablosu sabit sütun genişlikleri (No44/Modül92/Kriter esnek/Detay170/Foto96/Durum176), çerçevesiz fotoğraf hücresi, silme düğmesi küçük "Sil" altında (kırmızı x yok).

## 2026-10-13 BİLGİLENDİRME PENCERESİ: AÇILIŞTA GÖSTER/GÖSTERME (onay bekliyor, dalda)
- Pencere başlığında kişisel düğme (#ann-autoshow-btn), localStorage ems_ann_auto_off; admin genel anahtarı (siteAnnouncement.autoOpen) aynen duruyor.

## 2026-10-13 ESKİ MÜŞTERİ DENETİMLERİ + DENETİME HAZIRLIK KALDIRILDI; MENÜ ADI
- Kaldırıldı: Müşteri Denetimleri sayfası (#customer-audits-modal, openCustomerAudits, renderCustomerAudits, saveCustomerAudit, changeAuditCapStatus, deleteCustomerAudit, downloadAuditsKPIJPG), Müşteri Bulgu Grafiği modalı (openCustomerFindingsChart), Denetim Kayıtlarını Yönet (HTML + saveCustomerProfileAudit), Denetime Hazırlık sayfası (#readiness-modal, openReadiness, renderReadiness, menü/altbilgi bağlantıları). Veriler (customerAudits) duruyor. audit-findings-modal DOM kalır (_moveFindingsCore kullanıyor).
- "Müşteriler" menü/altbilgi/geri adı = "Müşteriler & Denetimler / Customers & Audits / العملاء والتدقيقات".

## 2026-10-13 YÖNETİM ÖZETİ: MÜŞTERİ HAZIRLIĞI KALDIRILDI
- Ekrandaki ve indirilen Yönetim Özeti raporundaki "Müşteri Bazında Denetim Hazırlığı" bölümü, gezinme düğmesi ve _fxCustomerReadiness kaldırıldı. "Denetime Hazırlık" artık sitede hiçbir yerde yok (menü, altbilgi, sayfa, rapor).

## 2026-10-13 MÜŞTERİ: KANIT SATIRDA GÖRÜNÜR
- Durum kuralı (changeQ/changeFindingStatus) kanıtı birleşik grup üyesi ve bağlı bulgudan da sayıyor; müşteri tablosunda bu kanıt görünmediği için "fotoğrafsız durum değişti" izlenimi oluyordu. _custPhotoSource ile satırda gösterilir. Kural gevşetilmedi.

## 2026-10-13 MÜŞTERİ TABLOSU: FOTOĞRAF SİLME YENİLER
- deleteQuestionPhoto/deleteFindingPhoto müşteri tablosunu yenilemiyordu (fotoğraf silinmiş ama ekranda kalıyordu). _custRefreshIfOpen eklendi. Not: bağlı üretim kontrol maddesi (productionChecklist linkedQId) ile kanıt iki yönlü kopyalanır (_qsSyncEvidence); silinen kanıt karşı taraftan geri gelebilir — gelirse karşı tarafı da silmeyi düşün.

## 2026-10-13 MÜŞTERİ UYUM TEK KAYNAK
- Müşteri uyumu = calcCustomerStats(key) (soru + soruya bağlanmamış bulgu, birleşik gruplar bir kez). Seçim sayfası halkası/rakamları (Tamamlanan x/N, Devam eden, Başlanmayan), üstteki bar grafik, müşteri sayfası Genel Uyum kartı ve genel rapordaki müşteri uyumu aynı kaynaktan. Eskiden seçim kartı ve bar grafik ham bulgu kapanma oranını (%46) kullanıyordu, sayfa %48 gösteriyordu.

## 2026-10-13 YENİLEYİNCE BOŞ EKRAN (şüpheli, sertleştirme)
- Kök neden kesin bulunamadı (sandbox bulut/Firebase CDN erişimsiz). enterApp içindeki startCloudDataLoadOnce/calcMetrics/applyFilter/maybeShowViewerWelcomePopup çağrıları try/catch içine alındı: biri hata verse bile site açılır (eskiden authLoading gizlenip welcome/mainApp gösterilmeden kalırsa boş ekran). Hâlâ boşsa kullanıcıdan F12 Console kırmızı hata metni iste.

## 2026-10-13 DİL DEĞİŞİNCE AYNI YERDE KAL
- setLanguage artık sarmalayıcı: _setLanguageCore çağrılırken saveLastView/geçmiş kaydı kapalı (_langRerendering), açık pencereler/üstteki/kaydırma/ems_last_view önce-sonra aynen geri yüklenir. Önceki hata: yeniden çizim openDetailModal vb. çağırıp son görünümü ve geçmişi değiştiriyor, yenileyince içeriksiz "Record Details" açılıyordu. Ayrıca kabuk openOv: içeriksiz global-filter-modal açılmaz.

## 2026-10-13 POPUP PROGRAM KUTUSU + ARTIK TEMİZLİĞİ
- Bilgilendirme penceresinde yönetici "Bugünkü Program"a doğrudan yazı ekler/siler (annAddProgram/annDelProgram; Yönetim Merkezi > Yapılacaklar ile aynı liste _todo -> siteAnnouncement.todos).
- Kaldırılan artıklar: müşteri sekme çubuğu + renderCustomerTabsBar, boş denetim paneli, ölü fonksiyonlar (downloadCustomerFindingsJPG, setCustomerSection, _customerQuestions, setCustomerCategoryFilter, changeCustomerStatus, _qAppliesToCustomer, filterCfAuditList, _fxStatusTxt, _fxCertBadgeHtml), ilgili CSS. Bulgu Dağılımı kartı artık her durumda yenilenir.
- Hâlâ kullanılmayan (dokunulmadı, Performans/yönetim parçaları): _reportSignatureRows, _appendDailyAuditEmailPoolItem, _teamOkrObjScore, _teamRefreshKpiScoreCells, _csvCell, teamToggleItemAssignment, teamTogglePersonItemCompletion, toggleSiteAnnouncementAutoOpen, approveUserAccount, saveUserDepartments, changeDeptReportsMonth, recoverFromAutoBackup, showDataDefaultedBanner, hideDataDefaultedBanner, restoreViewFromHash, restoreLastView, downloadCertFile, _overallFindingGroups.
- Halka renk kuralı (onay bekliyor): Tamamlanan antrasit, Devam gri, Başlanmayan kırmızı tüm halkalarda.

## 2026-10-13 FORM SHAREPOINT LİNKLERİ + HALKA RENKLERİ + ARTIK TEMİZLİĞİ
- Form Arşivi: dosyası siteye yüklenmiş formlardan eski SharePoint/ssg bağlantısı silinir (_formIsSharepoint; içe aktarmada ve _formsLinkCleanMaybe ile bulut kaydında bir kez, 14sn/40sn). Dosyası olmayan ya da SharePoint dışı bağlantı korunur.
- Halka renkleri: üretim kategori halkaları, ana sayfa WIP ve kimyasal halkaları antrasit (#2b2d31); durum halkaları zaten antrasit/gri/kırmızı. Chart.js grafikleri (gelir-gider, kimyasal kategori, Performans) durum grafiği olmadığı için değişmedi.
- Silinen ölü fonksiyonlar: _csvCell, _appendDailyAuditEmailPoolItem, changeDeptReportsMonth, saveUserDepartments, approveUserAccount, downloadCertFile, restoreViewFromHash, restoreLastView, _overallFindingGroups, _reportSignatureRows. Performans (team*) ve güvenlik (recoverFromAutoBackup, showDataDefaultedBanner, toggleSiteAnnouncementAutoOpen) fonksiyonlarına dokunulmadı.

## 2026-10-13 YENİLEYİNCE BOŞ PENCERE — GENEL ÇÖZÜM
- Önceki çözüm yalnız global-filter-modal içindi; document-library-modal da boş açılıyordu. Kabuk openOv: açıcı fonksiyonu (fn) bilinmeyen pencere hiç açılmaz; onOpen: fn yoksa ov_ kaydı yazılmaz (pencerenin kendi kaydı docLibrary/detailModal geçerli kalır); openDocumentLibrary(storeKey yok) ve openDetailModal(type yok) boş pencere açmaz. Test: geçersiz kayıtlar ana sayfa, geçerliler doğru açılır.

## 2026-10-13 POPUP PROGRAM KUTUSU BOŞKEN GİZLENİYORDU
- Metin ve program satırı yokken popup gövdesi (bodyEl) gizleniyordu, yönetici ekleme kutusu da görünmüyordu. Yönetici için gövde hep açık. Test: boş popup, yönetici kutuyu görür, ziyaretçi görmez.

## 2026-10-13 UYUM ORANI KARTLARI TIKLANMAZ
- Detay pencerelerindeki "Uyum Oranı" kartı ve ana sayfadaki "Genel Uyum Oranı" kartı artık tıklanmaz/açılmaz, hover dolgu efekti de yok (data-noclick; ems-fx atlanır). "Genel Başarı Detayı" penceresi (overall-success-modal, openOverallSuccessDetail, openComplianceDetail, downloadOverallSuccessJPG) tamamen kaldırıldı. KURAL: bilgi kartı (uyum oranı) tıklanabilir yapılmaz; yalnız filtre kartları (Toplam/Tamamlandı/Devam/Başlanmadı) tıklanır.

- 2026-10-13 21:30: Sol menüde video üstü/altı kırmızı ayraç şeridi (#side-nav-stats-widget ::before/::after).

- 2026-10-13 21:33: Sol menüden 'Son yedek' kartı kaldırıldı (yedek bilgisi Yönetim Merkezi > Yedekleme Geçmişi'nde). updateBackupInfo öğe yoksa sessizce çıkar.

- 2026-10-13 21:36: Yönetim Merkezi butonu sol menüden sağ üst banner köşesine (.ahub-top, admin-only-el) taşındı; #admin-nav-group gizli (rozet kimlikleri için duruyor).

- 2026-10-13 21:38: Alt bilgideki Eroğlu Grubu üst çizgisi gri yerine kırmızı (2px #E11D2E).

- 2026-10-13 21:39: Sağ üst Yönetim Merkezi butonu küçültüldü (Yönetim Özeti boyutu); sınıf adı .ahub-top -> .ahub-corner (.ahub-top Yönetim Merkezi panosunda kullanılıyor, çakışmaydı).

- 2026-10-13 21:39: Köşe butonu ölçüsü düzeltildi (ems-sade emoji kutusu 36px zorlaması ezildi).

- 2026-10-13 21:41: Videonun altındaki kırmızı çizgi kaldırıldı; gri kullanıcı çizgisi (side-nav-footer border-top) yerine kırmızı şerit (::before) konuldu.

- 2026-10-13 21:45: Alt telif/sürüm şeridi sol menü rengi (#202226) + beyaz yazı (team sayfası hariç).

- 2026-10-13 21:47: Video sol menüden alt bilgiye taşındı (footer-video-band, seçenek B); sol menü bölüm başlıkları büyütüldü (14px) ve kırmızı (#FF3B47). snw-video-box CSS artık kullanılmıyor.

- 2026-10-13 21:51: Telif şeridi sol menü kullanıcı bloğuyla aynı hizada: ≥901px'te main-content/side-nav alt boşluk 0, şerit yüksekliği --sf-h (syncFootBar, ResizeObserver) + kırmızı üst şerit.

- 2026-10-13 21:53: Yüzen düğmeler (yukarı, zil, WhatsApp) 58px eşit boyut/hiza; içerik–alt bilgi boşluğu 40→12px.

- 2026-10-13 21:54: Alt bilgi bağlantıları ≥1520px'te tek satır (nowrap, grid auto sütun, max 1440px).

- 2026-10-13 21:57: 'ResizeObserver loop' uyarısı kullanıcıya alert olarak çıkıyordu (syncFootBar kaynaklı): global error handler bu zararsız uyarıyı yoksayar, syncFootBar rAF + değişince yazar.

- 2026-10-13 21:59: Telif şeridi yükseklik/hiza eşitleme GERİ ALINDI (kullanıcı isteği): --sf-h, syncFootBar, ≥901px bloğu kaldırıldı. Şerit rengi (#202226) + beyaz yazı kalıyor. ResizeObserver alert filtresi kalıyor.

- 2026-10-13 22:04: ≥901px'te main-content ve side-nav alt boşluğu 0: siyah telif şeridi sayfa dibinde, altında boşluk yok; sol menü kullanıcı bloğu ile aynı alt çizgi.

- 2026-10-13 22:06: Yüzen düğmeler (WhatsApp/zil/yukarı) ≥901px'te 60px yukarı (80/150/220) — siyah şerit sayfa dibinde olduğu için.

- 2026-10-13 22:10: Sol menü kullanıcı bloğu üst kırmızı şeridi sağdaki Eroğlu Grubu kırmızı çizgisiyle aynı hiza: syncFootBar (rAF, değişince yazar) --sf-h = group-logo-footer üstü → şerit alt; side-nav-footer min-height. ≥901px.

- 2026-10-13 22:11: Ana alt bilgi e-postası info@ → abdullah.baydogan@eroglums.com (tek satır, nowrap). Performans sayfası alt bilgisi (info@) bilerek değişmedi.

- 2026-10-13 22:14: Alt bilgi e-postası kenardan taşıyordu: son sütun min 270px, e-posta 13px, sütun aralığı 26px (1520–2200px test: taşma yok, tek satır).

- 2026-10-13 22:19: Alt bilgi sütunları eşit aralıklı (space-between): marka sütunu 170–240px, bağlantı sütunları auto, iletişim 270px; min boşluk 28px.

- 2026-10-13 22:22: Alt bilgi videosu yalnız ana sayfada (#view-dashboard.active) görünür; diğer sayfalarda ve alt bilgi kopyalarında gizli. KURAL: kullanıcı onayı + örnek olmadan hiçbir değişiklik yapma.

- 2026-10-13 22:55: Alt bilgi 5 sütun eşit aralık (≥1520px): auto sütunlar + space-between, min boşluk 20px, fitFooter (yazı 13.5→10.5px kademeli küçülür, rAF+ResizeObserver), başlıklar nowrap. KURAL: onay+örnek olmadan değişiklik yok.

- 2026-10-13 23:17: KALİTE YÖNETİM SİSTEMİ (QMS) iskeleti: openQmsPage → _qmsRender (süreç haritası 11 bölüm; bölüm sekmeleri Akış/Prosedür/Talimat/Form/Kayıt/DOP; Doküman Kontrol, DOP Merkezi, Uygunsuzluk, İzlenebilirlik). Veri: procedures belgesinde qmsRecords/qmsDops (yalnız admin yazar), fotoğraf ems_csr_files 'qms'. İçerik QMS_DEPTS benim taslağım; belgeler 'Taslak'. Excel formları sonra eklenecek. Kaynak: uploads/12a87131-gemini-code.html.

- 2026-10-13 23:44: QMS tam sayfa + şifre (özet _QMS_PIN_HASH, oturum boyunca açık; ziyaretçiye kapalı), kendi geri/ileri/ana sayfa (_qmsHist), gerçek akış sırası (Örme→Boyahane→Kumaş Kontrol→…), yeni bölümler (Ön Hazırlık, Kumaş Kontrol, Yıkama[ertelendi], Aksesuar paralel hat), Form Arşivi gerçek formları adımlara bağlandı, her bölümde SOP sekmesi (yazdır/PDF), 7 destek süreci (Makine Bakım, Kalibrasyon, Eğitim, Tedarikçi, Şikâyet, İç Denetim, Yönetim Gözden Geçirme). Şifre değiştirmek için _QMS_PIN_HASH = sha256('ems-qms-v1:'+şifre).

- 2026-10-13 23:49: QMS: EMS logosu üst çubuk solunda (46px, tüm sayfalarda aynı) + Rapor İndir butonları (hub/bölüm/kayıtlar/SOP/DOP/uygunsuzluk/doküman/izlenebilirlik) — ortak PDF hattı (_h2c, _pdfKpiBandHtml, imza). PDF üretimi sandbox'ta CDN engelli olduğundan uçtan uca denenemedi.

- 2026-10-14 00:04: Sol menü: Performans Sistemi + Kalite Yönetim Sistemi yanına kilit (svg .nav-lock); Yönetim Merkezi sağ üst köşeden sol menüye (QMS altı, admin-only, kilitli, diğer butonlar gibi); Müşteriler & Denetimler 'Denetim & Uygunluk' bölümünün en üstüne. Köşe butonu (.ahub-corner) kaldırıldı.

- 2026-10-14 00:14: Kurumsal SOP (14 başlık, doküman bilgi kutusu, imza kutuları): QMS_SOP_RICH[bölüm] + _qmsSopRichHtml(d,forPdf); şimdilik yalnız İplik (SOP-IPL-01) tam; diğer bölümler genel SOP gösterir — sıradaki iş diğer bölümlerin zengin SOP'ları (TR→EN→AR). Kullanıcı kuralı: her değişiklik önce örnekle gösterilir.

- 2026-10-14 00:18: QMS üst çubuk: ← ⌂ → grubu (ev=kırmızı yuvarlak ikon, oklar çerçevesiz beyaz) Siteye dön yanında; emojiler yerine QMS_ICONS svg ikon seti (_qmsSvg); animasyonlar (giriş kayması, hover, ok nabzı, yanlış PIN sallanma; prefers-reduced-motion saygılı).

- 2026-10-14 00:36: QMS: yenilemede QMS'te kalma (URL #v=qms&view=..&dept=..&tab=..&step=.., _qmsSyncHash replaceState; restore case qms → openQmsPage(params)); QMS çubuğuna dil seçici + tarih rozeti.

- 2026-10-14 00:39: QMS üst çubuk son düzen: sol=logo+←⌂→, orta=başlık+yol, sağ=kilit+Siteye dön; dil seçici+tarih her sayfada sağ üstte Rapor İndir'in üstünde (_qmsPlaceLang).
- QMS: Rapor İndir düğmesi sekme satırına (sağda) alındı; onay bekliyor (2026-10-14 00:41).
- QMS: Ön Hazırlık, Satın Alma, Depo Kabul, Laboratuvar SOP'ları siteye eklendi (Taslak, kullanıcı onayladı) (2026-10-14 00:47).
- QMS: örnek sipariş (DEMO-2026-001) yükle/sil eklendi, dalda bekliyor (2026-10-14 00:52).
- QMS: kalan 18 bölümün SOP'u eklendi (toplam 22, hepsi Taslak, kullanıcı 'iplik referans, göstermene gerek yok' dedi) (2026-10-14 00:53).
- Prosedürler: 42 QMS prosedürü 29 resmî belgeye bağlandı (19 mevcut prosedür genişletilip birleştirildi R01, 10 yeni; EN+AR tek dosya, imza bloğu + hazırlayan + Kalite Müdürü satırı; kod yoksa boş bırakıldı: bölüm müdürü/Kalite Müdürü ADLARI girilecek). SOP imzalarına 'Kalite Müdürü' eklendi. Belgeler prosedurler/ klasöründe, manifest rev r1-2026-10-14 (2026-10-14 01:07).
- Prosedür/SOP imza satırlarına rol unvanları eklendi (Fabrika/Üretim/Satın Alma/İplik·Örme·Boyahane Fabrika Müdürü, Kalite Müdürü); ADLAR kullanıcıdan gelecek. rev r2 (2026-10-14 01:08).
- QMS verisi (qmsRecords/qmsDops) artık ayrı Firestore belgesi ems_csr/qms; eski procedures kayıtları admin açılışında bir kez taşınır; günlük yedek/geri yüklemeye dahil (_extraBackupFields). firestore.rules'a 'qms' (yalnız admin yazar) eklendi — KULLANICI konsola yapıştırmalı. QMS adım sorumlularına 'Kalite Güvence · Kalite Müdürü' (2026-10-14 01:11).
- 22 SOP'un İngilizce ve Arapça çevirisi eklendi (QMS_SOP_EN / QMS_SOP_AR); dil değişince SOP o dilde açılır (yardımcı çeviri, gözden geçirilmeli) (2026-10-14 01:18).
- QMS Doküman Dizini + arama (üst çubuk), 'ilgili belgeler' listesi, prosedurler/refs.json (belge atıf haritası; belge eklenince yeniden üretilmeli). Kullanıcı kuralı: mevcut belge varsa birleştir (CLAUDE.md'ye yazıldı). SIRADA: QMS talimat(TLM) ve form(FRM) kayıtlarını mevcut TL docx / formlar xlsx ile karşılaştırıp birleştirme (2026-10-14 01:20).
- Talimatlar: 90 QMS talimatı 46 resmî talimat belgesine bağlandı (25 mevcut TL genişletilip birleştirildi, 21 yeni; EN+AR tek dosya; imza satırları unvanlı). refs.json yeniden üretildi (256 belge). Formlar (FRM-xxx taslaklar) henüz mevcut formlarla birleştirilmedi — Excel, birlikte yapılacak (2026-10-14 09:15).
- Örnek sipariş: fotoğraflı kanıt (8 kayıt + 2 DOP), DOP durumları (açık/devam/kapalı+onaylı), örnek onay etiketleri (yalnız unvan, kişi imzası yok); silince fotoğraflar da silinir (2026-10-14 09:17).
- DOP→DÖF (Türkçe; EN CAPA, AR 'DOP' kalır; başlıkta ' / ' yerine ' · ' çünkü site i18n ' / ' ile böler). DÖF ekranına bilgi satırı. Yeni DÖF numarası DÖF-001; eski DOP- kayıtlar durur (2026-10-14 09:27).
- QMS: sipariş takip çizelgesi (İzlenebilirlik), gerçek Onayla/kilit (kayıt+DÖF), belge durumu Taslak→Onayda→Onaylı (Kalite Müdürü + Fabrika Müdürü; qmsDocStates qms belgesinde; imza-* rev'li eski belgeler 'Onaylı (imzalı)') (2026-10-14 09:41).
- Kayıtlar sekmesine bölüm bilgi satırı (22 bölüm, 3 dil: yapılan iş + kaydedilecekler) (2026-10-14 09:48).
- QMS ana ekran yalınlaştırma (dalda, onay bekliyor): KPI şeridi + kompakt bölüm haritası + ortak araç düğmeleri + katlanır deneme (2026-10-14 10:03).
- KURAL: Excel formlar birleştirilmez (kullanıcı: 'formlar aynı değil'); birleştirme yalnız prosedür/talimat/SOP için. CLAUDE.md güncellendi.
- QMS ana ekran 2. yalın sürüm (dalda, onay bekliyor): ikonsuz kısa kutular, tek satır sayılar, katlanır destek+deneme (2026-10-14 10:07).
- 37 taslak form AYRI Excel olarak üretildi (logo, EN+AR, amaca göre; EMS.ÜR/SA/DP/LB/BK/EG/QA/YS.FRM.xx.xx), formlar/ yeni bölüm klasörleri + manifest; QMS'te _FD→_F (eski FRM-xxx kodu 'eski kod' olarak aranabilir); _formCode regex Türkçe büyük harfi kabul eder. Mevcut Excel'lere dokunulmadı (2026-10-14 10:28).
- Performans Sistemi, Kalite Yönetim Sistemi, Yönetim Merkezi: her açılışta şifre (454236, üçü aynı), çıkışta kilit. Şifre özetleri değişmedi (zaten aynı PIN) (2026-10-14 10:30).
- QMS ana ekran A+B birleşik tasarım (arama merkezli + 6 kutu + akış şeridi + destek hapları), dalda onay bekliyor (2026-10-14 10:32).
- BELGE ADLARI UYUMU: 75 docx içindeki eski PRS-/TLM-/FRM- kodları resmî EMS.xx.PRO/TL/FRM kodlarına çevrildi (manifest rev r3), SOP metinleri de; QMS satır rozeti resmî kod gösterir (eski kod title'da, Doküman Dizini'nde 'eski kod' aranabilir). refs.json yenilendi. Karşılığı olmayan atıflar (eski belgelerde): EMS.QA.PRO.02.01/02/03/05/06, EMS.SA.PRO.04.01 — kullanıcıya sorulacak. Ana ekran şerit açıklaması eklendi (2026-10-14 10:41).
- Eksik 6 prosedür yazıldı (EMS.QA.PRO.02.01/02/03/05/06, EMS.SA.PRO.04.01; EN+AR); Arapça bitişik yazılmış eski kodlar da çevrildi (recode regex lookbehind). Tüm atıflar artık gerçek dosyaya gidiyor (2026-10-14 10:47).
- QMS ana ekrandan 'İSG · Çevre' kutusu kaldırıldı (5 kutu), dalda onay bekliyor (2026-10-14 10:49).
- QMS parlatma: ikonlu kutular, ikonlu süreç şeridi, animasyonlar (belirme, hover, nabız), bölüm sayfalarında arka plan gradyan büyük bölüm ikonu; reduced-motion destekli (2026-10-14 10:57).
- Destek Süreçleri bölümü ikonlu kart tasarımı (4x2, hover animasyon, DÖF rozeti) (2026-10-14 11:04).
- QMS ana ekran: bölüm sıra numaraları kaldırıldı, bölümler arası çizgi akan kırmızı tire (onay bekliyor, main'e alınmadı).
- QMS ana ekran: 'Kalite Yönetim Sistemi' başlığı üst çubuktan ana sayfa gövdesine (sol üst) taşındı; diğer sayfalarda üst çubukta kalır (onay bekliyor).
- QMS ana sayfa: Rapor İndir düğmesi dil/tarih ile aynı hizaya alındı (masaüstü); başlık onaylı, main'e alındı.
- Ütü·Final·Paket·AQL bölümü 8 adım (Kalite kontrol, Ütü, Optik, Dedektör, Paketleme, Lotlama, Kolileme, Final inspection); 5 yeni form; belgeler yazılıyor (dalda, main'e alınmadı).
- Ütü·Final·Paket 8 adım: 7 yeni belge (QA.PRO.02.13/02.14, QA.TL.02.08, ÜR.PRO.05.11/05.12, ÜR.TL.05.13/05.14), 7 belge güncellendi (R04; ÜR.TL.05.06 artık 'Pressing and Steaming'), 5 yeni form (ÜR.FRM.05.09/05.10/05.11, QA.FRM.05.04/05.05), refs.json yenilendi. Main'e onay bekliyor (2026-10-14 14:22).
- QMS üst çubuk arama kutusu 'İzlenebilirlik' oldu: sipariş/lot no yazılınca izlenebilirlik sayfasında bulur (onay bekliyor, 2026-10-14 14:57).
- Müşteri sayfası soru tablosunda (yalnız admin) her sorunun altında 'Soruyu sil' düğmesi (deleteCustomerQuestion → deleteModalItem; birleşik soruda onay metni diğer bölümleri sayar). Onay bekliyor (2026-10-14 15:21).
- 'Soruyu sil' düğmesi (admin) müşteri sayfası + tüm soru listeleri (CSR, İSG, Çevre vb.) soru metninin altında (2026-10-14 15:23).
- Halka (sec-donut) kartları: sabit 256px yükseklik yüzünden üst üste binen içerik düzeltildi; yükseklik içeriğe göre uzar (CSS sonda, onay bekliyor 2026-10-14 15:25).
- Kimyasal: Denetçi raporları (Aylık + Günlük + Denetçi Paketi PDF, Excel) — openChemAudit; kimyasal ana ekrandan ve rapor modalından erişilir. Veri yerleşimi (Eylül/Ekim) kullanıcıdan onay bekliyor; yeni dosya Ekim 1–14 verisi (2026-10-14 15:57).
- Kimyasal Ekim dosyası güncellendi (1–14 Ekim, rev 2026-10-14); kullanıcı onayı: Ekim'e yazıldı, Eylül'e dokunulmadı. Dosyada MT657 TURQUOISE BLUE 14 Ekim üretime çıkış 135 kg (stok 5,2) → eksi stok; kullanıcıya bildirildi (2026-10-14 16:05).
- Kimyasal Ekim dosyasında MT657 TURQUOISE BLUE 14 Ekim üretime çıkış 135 → 0,135 düzeltildi (kullanıcı isteği), rev 2026-10-14b (2026-10-14 16:06).
- Kimyasal Ağustos/Eylül malzeme listesi Ekim listesine (97 kalem) göre azaltıldı: 8 malzeme (chem_default_078/092/093/094/098/100/102/103) + kayıtları kaldırılır; bir kerelik bulut geçişi CHEM_TRIM_V=2026-10-14a (yalnız admin açılışında), yedek bulutta chemTrimBackup. CHEM_SEED_V değişmedi (2026-10-14 16:08).
- QMS belge onayı yalnız Yönetici (QMS_DOC_APPROVERS=['Yönetici']); tüm belgeler (prosedür/talimat/SOP/politika/taslak form) bir kerelik otomatik 'Onaylı' (işaret kaydı __bulk_approve_v1, admin QMS açılışında) + Doküman Kontrol'de 'Tüm belgeleri onayla (Yönetici)' düğmesi (2026-10-14 16:10).
