// ═══════════════════════════════════════════════════════════════════════════
// EMS CSR PORTAL — Firebase Cloud Messaging Service Worker
// Bu dosya, site KAPALIYKEN (arka planda) gelen push bildirimlerini yakalayıp
// cihazın bildirim merkezinde göstermek için gereklidir. index.html (ems_mobile.html)
// ile TAM OLARAK AYNI KLASÖRE (GitHub Pages kök dizinine) yüklenmelidir, adı
// değiştirilmeden: firebase-messaging-sw.js /
// This file is required to catch push notifications that arrive while the site
// is CLOSED (in the background) and show them in the device's notification
// center. It must be uploaded to the EXACT SAME FOLDER as index.html
// (ems_mobile.html) — the GitHub Pages root — without renaming it:
// firebase-messaging-sw.js
// ═══════════════════════════════════════════════════════════════════════════

importScripts('https://www.gstatic.com/firebasejs/10.13.1/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.13.1/firebase-messaging-compat.js');

// ═══ ÖNEMLİ ═══ Bu değerler, index.html içindeki "firebaseConfig" ile BİREBİR AYNI olmalıdır.
// Zaten EMS projesinin gerçek değerleriyle önceden dolduruldu — değiştirmene gerek yok. /
// ═══ IMPORTANT ═══ These values must be IDENTICAL to the "firebaseConfig" inside index.html.
// Already pre-filled with the EMS project's real values — no need to change anything.
firebase.initializeApp({
  apiKey: "AIzaSyBPMQTrPrZzxG68TnMsmeEd5cDOUej_cjs",
  authDomain: "ems-csr-dashboard-3f420.firebaseapp.com",
  projectId: "ems-csr-dashboard-3f420",
  storageBucket: "ems-csr-dashboard-3f420.firebasestorage.app",
  messagingSenderId: "95779649376",
  appId: "1:95779649376:web:1d2732971a8ebba9229005",
  measurementId: "G-NPQ2TZ8Z2D"
});

const messaging = firebase.messaging();

// Site kapalıyken/arka plandayken gelen bildirimleri işler ve cihazda gösterir /
// Handles notifications that arrive while the site is closed/in the background
// and displays them on the device
messaging.onBackgroundMessage((payload) => {
  const title = (payload.notification && payload.notification.title) || 'EMS — Önemli Bilgilendirme';
  const body = (payload.notification && payload.notification.body) || '';
  const options = {
    body,
    icon: 'https://em-content.zobj.net/source/apple/391/loudspeaker_1f4e2.png',
    badge: 'https://em-content.zobj.net/source/apple/391/loudspeaker_1f4e2.png'
  };
  self.registration.showNotification(title, options);
});
