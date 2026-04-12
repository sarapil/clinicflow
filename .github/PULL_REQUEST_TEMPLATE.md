## الوصف | Description
<!-- وصف مختصر للتغييرات — Brief description of changes -->


## نوع التغيير | Type of Change
- [ ] 🐛 Bug fix — إصلاح خطأ
- [ ] ✨ New feature — ميزة جديدة
- [ ] 💥 Breaking change — تغيير كسري
- [ ] 📝 Documentation — توثيق
- [ ] 🧪 Tests — اختبارات
- [ ] 🔧 Refactoring — إعادة هيكلة
- [ ] 🎨 UI/UX — واجهة المستخدم
- [ ] ⚡ Performance — أداء
- [ ] 🔒 Security — أمان
- [ ] 🌐 Translation / i18n — ترجمة

## المشكلات المرتبطة | Related Issues
<!-- Fixes #123, Relates to #456 -->

## التغييرات الرئيسية | Key Changes
-
-

## لقطات الشاشة | Screenshots
<!-- إذا كان التغيير مرئياً — If the change is visual -->

## خطة الاختبار | Test Plan
- [ ] Unit tests pass — اختبارات الوحدة ناجحة
- [ ] Integration tests pass — اختبارات التكامل ناجحة
- [ ] Manual testing done — الاختبار اليدوي تم

## قائمة التحقق | Checklist

### الكود | Code
- [ ] Follows [Arkan Lab Standards](/.github/copilot-instructions.md)
- [ ] Self-reviewed the code
- [ ] No `frappe.db.commit()` inside document events
- [ ] No raw SQL without parameterization
- [ ] All `@frappe.whitelist()` APIs have permission checks
- [ ] Uses `extend_doctype_class` NOT `override_doctype_class`

### الاختبارات | Tests
- [ ] Tests added/updated for changes
- [ ] All existing tests pass

### التوثيق والترجمة | Docs & Translation
- [ ] New strings wrapped in `__()`
- [ ] Arabic translation added
- [ ] Help files updated (if DocType changed)

### الأمان | Security
- [ ] No SQL injection vectors
- [ ] No XSS vectors
- [ ] External API calls use timeout
