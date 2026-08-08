# Menbr Chat (Production-Ready)

تطبيق دردشة فردية حقيقي يعتمد على `@username` بنسبة 100% مع ربط سحابي كامل عبر Firebase ومكالمات عالية الجودة عبر Agora.

## 📁 هيكلية المشروع (Project Architecture)
- **Frontend / UI**: واجهة مستخدم تفاعلية مطابقة لـ واتساب.
- **Backend / Database**: سحابي بالكامل عبر Firebase Firestore (بدون سيرفر تقليدي).
- **Authentication**: مصادقة المستخدمين والتحقق من فرز الـ `@username`.
- **Storage**: تخزين الملفات والميديا حتى حجم 2GB عبر Firebase Storage.
- **Calls**: نظام المكالمات الصوتية والفيديو الفردية عبر مكتبة Agora.

## 🚀 الخطوات لرفع المشروع على GitHub:
1. انشئ مستودعاً جديداً (Repository) على حسابك في GitHub باسم `menbr-chat`.
2. انسخ الملفات الأساسية للمشروع واقفل إعدادات الربط السحابي.
3. ارفع الملفات عبر أوامر التيرمنال:
   ```bash
   git init
   git add .
   git commit -m "Production release: Menbr Chat core architecture"
   git branch -M main
   git remote add origin [https://github.com/YOUR_USERNAME/menbr-chat.git](https://github.com/YOUR_USERNAME/menbr-chat.git)
   git push -u origin main
