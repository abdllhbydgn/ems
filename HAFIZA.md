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
- Denetim/sertifika tarihlerini kullanıcıdan alıp Takvim'e 30 gün önceden uyarıyla ekleme.

## Günlük
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
