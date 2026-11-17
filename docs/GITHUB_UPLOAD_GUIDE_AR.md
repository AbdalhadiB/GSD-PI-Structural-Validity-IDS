# تعليمات إدخال حزمة GSD–PI إلى GitHub

**هذه نسخة مرشحة للنشر؛ لا ترفعها إلى الفرع الرئيسي وتصدر Zenodo DOI قبل استكمال البنود المبينة أدناه.**

## إذا كنت تستخدم واجهة GitHub

1. فك الضغط عن الملف `GSD_PI_GitHub_Release_Candidate_2026-11-16.zip` محليًا. **لا ترفع ملف ZIP نفسه بدل ملفات الشيفرة**.
2. افتح مستودعك الأصلي `AbdalhadiB/GSD-PI-Structural-Validity-IDS` وأنشئ فرعًا جديدًا باسم `review-revision-2026-11`.
3. أضف الملفات والمجلدات الجديدة إلى الفرع، مع **الحفاظ على سجل الإصدارات السابق وعدم حذف الملفات الأصلية دون مقارنة**.
4. راجع `README.md` و`docs/POLICY_SEMANTICS.md` و`docs/OPEN_ITEMS_BEFORE_RELEASE.md` قبل طلب دمج الفرع.
5. أضف أصلَي ملف الحساسية M4 من جهازك: `IEEE_Access_M4_Sensitivity_OAT.csv` و`IEEE_Access_M4_Sensitivity_Audit.py`. لا تصنع نسخة اصطناعية بديلة.
6. أكد بيانات المؤلفين واختر الترخيص؛ ثم راجع حماية البيانات وأي حقوق لإعادة توزيع المدخلات.
7. بعد اعتماد النسخة المطابقة للمخطوطة، أصدر GitHub Release ثم اربطه بـ Zenodo وسجّل الـ DOI الفعلي في المخطوطة ورد N8/D7.

## طريقة أكثر أمانًا عبر Git على Windows (PowerShell)

```powershell
git clone https://github.com/AbdalhadiB/GSD-PI-Structural-Validity-IDS.git
cd GSD-PI-Structural-Validity-IDS
git switch -c review-revision-2026-11
# انسخ محتويات المجلد المفكوك (وليس ملف ZIP) إلى هذا المجلد الآن
git status
git diff
# بعد فحص الملفات والتأكد من اكتمالها:
git add .
git diff --cached
git commit -m "Add curated IEEE Access revision evidence"
git push -u origin review-revision-2026-11
```

الخطوات أعلاه **لم تُنفذ نيابة عنك**؛ هي دليل لإتمامها بنفسك. ينصح باستخدام Pull Request وفحص الاختلافات قبل الدمج. لا تنشر Zenodo DOI ما دامت بقية الملفات المطلوبة لم تُطابق بعد.
