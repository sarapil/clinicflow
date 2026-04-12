# Security Policy — سياسة الأمان

## Supported Versions — الإصدارات المدعومة

| Version | Supported             |
| ------- | --------------------- |
| 1.x     | ✅ Actively supported |
| < 1.0   | ❌ Not supported      |

## Reporting a Vulnerability — الإبلاغ عن ثغرة أمنية

**English:** If you discover a security vulnerability in ClinicFlow, please **do not** open a public GitHub issue. Instead, report it privately to:

**عربي:** إذا اكتشفت ثغرة أمنية في ClinicFlow، يرجى **عدم** فتح مشكلة عامة على GitHub. بدلاً من ذلك، أبلغ عنها بشكل خاص على:

📧 **security@arkan.it.com**

Please include:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Any suggested fixes

يرجى تضمين:

- وصف الثغرة
- خطوات إعادة الإنتاج
- التأثير المحتمل
- أي إصلاحات مقترحة

## Response Timeline — جدول الاستجابة

| Step              | Deadline  |
| ----------------- | --------- |
| Acknowledgment    | 48 hours  |
| Assessment        | 1 week    |
| Fix               | 2 weeks   |
| Release           | 30 days   |
| Public disclosure | After fix |

## Scope — النطاق

In-scope vulnerabilities:

- Patient data exposure (HIPAA/NDPR relevant)
- Authentication bypass in appointment/consultation APIs
- SQL injection via ClinicFlow endpoints
- CAPS permission bypass allowing unauthorized access to patient records
- Insurance claim data tampering
- Remote code execution

Out of scope:

- Vulnerabilities in third-party dependencies (Frappe, ERPNext)
- Social engineering attacks
- Physical access attacks

## Patient Data Protection — حماية بيانات المرضى

ClinicFlow handles sensitive patient health information. We take special care to ensure:

- Patient records are access-controlled via CAPS capabilities
- Lab results and clinical notes are encrypted at rest
- All API access requires authentication and proper authorization
- Audit logs track all access to patient data

ClinicFlow يتعامل مع المعلومات الصحية الحساسة للمرضى ويلتزم بـ NDPR (نيجيريا) و HIPAA (دولياً).

## Security Standards — معايير الأمان

ClinicFlow follows:

- OWASP Top 10 mitigation
- NDPR (Nigeria Data Protection Regulation) compliance
- Frappe v16 security best practices
- Parameterized SQL queries (no raw SQL interpolation)
- CAPS capability checks on all patient-facing API endpoints
- No PHI (Protected Health Information) in logs

## Acknowledgments — الشكر والتقدير

We thank all security researchers who responsibly disclose vulnerabilities.
نشكر جميع باحثي الأمن الذين يُفصحون عن الثغرات بمسؤولية.
