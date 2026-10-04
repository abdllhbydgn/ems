# EMS sitesi — kalıcı çalışma kuralları

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
