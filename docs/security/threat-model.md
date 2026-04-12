# ClinicFlow — Threat Model
# كلينك فلو — نموذج التهديدات

## OWASP Top 10 Assessment

| # | Threat | Mitigation | Status |
|---|--------|-----------|--------|
| 1 | Broken Access Control | CAPS capability enforcement | ✅ |
| 2 | Cryptographic Failures | Frappe password hashing | ✅ |
| 3 | Injection (SQL/XSS) | Parameterized queries, output sanitization | ✅ |
| 4 | Insecure Design | Thin controller + service layer | ✅ |
| 5 | Security Misconfiguration | Standard Frappe security headers | ✅ |
| 6 | Vulnerable Components | Regular dependency updates | ⚠️ Monitor |
| 7 | Auth Failures | Frappe session management + CAPS | ✅ |
| 8 | Data Integrity | Frappe document versioning | ✅ |
| 9 | Logging Failures | CAPS audit log | ✅ |
| 10 | SSRF | No external URL fetching | ✅ |
