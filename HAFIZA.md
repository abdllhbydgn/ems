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
- 2026-10-07: Arama yapılınca birleşik sorular ayrı ayrı sayılıp toplam şişiyordu (ör. 1920) — düzeltildi: KPI ve liste her zaman grubu 1 kez sayar, arama grubun tüm kopyalarında yapılır. Sorumlu düğmesi belirgin (mor/lacivert/kırmızı).
- 2026-10-07: Soru listesi penceresinde arama kutusu hep açık (Tüm Sorular + Tamamlandı/Devam/Başlanmadı listeleri; sorumlu adıyla da arar). "Yapılmadı" → "Başlanmadı" (sertifika "Başvuru Yapılmadı" ve günlük iç denetim metni değişmedi).
- 2026-10-07: Sorulara sorumlu + elle termin eklendi (👤 çip, admin atar, listeden/serbest, bölüme toplu atama, sorumluya göre süzme, termini geçen uyarısı). Fotoğraf zorunluluğu yalnız Tamamlandı/Devam Ediyor (bulgu: Kapandı/Devam Ediyor). İç denetimler (günlük/departman OK-NOK) değişmedi.
- 2026-10-07: "Silinen soru geri geliyor" sebebi: birleşik grupta yalnız görünen kopya siliniyordu. deleteModalItem artık grubun tüm üyelerini kalıcı siler (bölümleri listeleyip onay sorar; bulgu/fotoğraf kalır). Silme yalnız admin; personel talep gönderir.
- 2026-10-07: Prosedürlerdeki ZIP indirme kutusu kaldırıldı. Baskı: en çok kullanılan 2 malzeme stok < 3 ton uyarısı eklendi (_chemTopStockAlert; şerit, yönetim özeti, kimyasal ekranı, rapor, PDF). Gmail/otomatik rutin İSTEMİYOR (rutin silindi). E-posta iş adresinden (abdullah.baydogan@eroglums.com, Outlook) gider: uyarı kutusundaki "Mahmut Bey'e e-posta hazırla" düğmesi (_chemTopStockMail) PDF raporu indirir + Outlook'u hazır metinle açar; kullanıcı PDF'i ekleyip Gönder'e basar.
- 2026-10-06: Prosedürler İng+Ar, 3 imzalı (225 belge). Kimyasal rapor panosu yenilendi; aylık Giriş/Kullanım/Stok kurgusu (Ağu–Eyl–Eki), ay geçişi uzlaştırması, her açılışta veri ezilmesi kaldırıldı, Ekim Excel'i kimyasal/'a kondu. Sızan Firebase anahtarları silindi (No keys). Hafıza defteri açıldı.
- 2026-10-06 (2. sohbet): Bugün iş yok; sadece hafıza okundu. Bekleyen iki öneri (yönetim e-postası, takvim uyarıları) hâlâ karar bekliyor.
