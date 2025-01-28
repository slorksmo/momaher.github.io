# Mo Maher's Personal Website

موقعي الشخصي ومدونتي التقنية مبنية باستخدام MkDocs مع Material theme.

## المميزات

- 🎨 تصميم عصري ومتجاوب
- 📱 واجهة متوافقة مع الأجهزة المحمولة
- 📝 مدونة تقنية مع تصنيفات ووسوم
- 💼 معرض الأعمال والمشاريع
- 📄 السيرة الذاتية المهنية
- 🏆 الإنجازات والشهادات
- 📬 نموذج التواصل
- 🌙 دعم الوضع الداكن/الفاتح
- 🔍 بحث نصي كامل
- 📰 تغذية RSS
- 🌐 مشاركة على وسائل التواصل الاجتماعي
- 💬 نظام التعليقات (Giscus)
- 📊 تكامل مع Google Analytics
- **Modern Design**: Clean and responsive layout with Material Design aesthetics
- **Dark/Light Mode**: Automatic theme switching based on system preferences
- **Interactive UI**: Smooth animations and hover effects
- **Optimized Icons**: Using Google's Material Icons for better performance
- **Responsive Layout**: Mobile-first design that works on all devices
- **Blog Section**: Technical articles and tutorials
- **Portfolio**: Showcase of projects and achievements
- **Skills Section**: Visual representation of technical skills
- **Social Links**: Easy access to professional profiles

## التثبيت

1. استنساخ المستودع:
```bash
git clone https://github.com/slorksmo/momaher.github.io.git
cd momaher.github.io
```

2. تثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

## التطوير المحلي

تشغيل الموقع محلياً:
```bash
mkdocs serve
```

سيكون الموقع متاحاً على `http://127.0.0.1:8000`

## بناء الموقع

لبناء الموقع الثابت:
```bash
mkdocs build
```

سيتم إنشاء الموقع في مجلد `site`

## النشر

يتم نشر الموقع تلقائياً على GitHub Pages عند دفع التغييرات إلى الفرع الرئيسي.

## هيكل المشروع

```
.
├── docs/
│   ├── assets/          # الصور والملفات الثابتة
│   ├── blog/           # مقالات المدونة
│   ├── portfolio.md    # صفحة معرض الأعمال
│   ├── resume.md       # السيرة الذاتية
│   ├── achievements.md # الإنجازات
│   └── contact.md      # صفحة التواصل
├── mkdocs.yml          # إعدادات MkDocs
└── requirements.txt    # متطلبات Python
```

## المتطلبات

يستخدم الموقع الحزم الرئيسية التالية:
- MkDocs v1.6.1
- MkDocs Material theme v9.5.3
- وإضافات MkDocs متنوعة لوظائف إضافية
- MkDocs (v1.5.3)
- Material for MkDocs (v9.5.3)
- Google Material Icons
- Custom CSS Animations
- Modern Web Technologies (HTML5, CSS3)

للقائمة الكاملة من المتطلبات، راجع ملف `requirements.txt`

## التخصيص

1. تحديث `mkdocs.yml` لتعديل إعدادات الموقع
2. تحرير الملفات في `docs/` لتحديث المحتوى
3. إضافة الصور إلى `docs/assets/images/`
4. إنشاء مقالات المدونة في `docs/blog/posts/`

## المساهمة

إذا وجدت أي مشاكل أو لديك اقتراحات:
1. افتح issue جديد
2. قدم pull request

## الترخيص

هذا المشروع مرخص تحت رخصة MIT - راجع ملف LICENSE للتفاصيل.

## التواصل

- GitHub: [@slorksmo](https://github.com/slorksmo)
- LinkedIn: [Mo_Maher94](https://linkedin.com/in/mo_maher94)
- Twitter: [@mo_maher94](https://twitter.com/mo_maher94)