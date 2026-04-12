# Translation Guide — دليل الترجمة

## Supported Languages — اللغات المدعومة

| Tier | Languages | Status |
| ---- | --------- | ------ |
| T1 (Mandatory) | Arabic (`ar`), English (`en`) | ✅ Complete |
| T2 (High Priority) | Turkish (`tr`), French (`fr`) | 🔄 Planned |
| T3 (Marketplace) | Spanish (`es`), German (`de`) | ❌ Not yet |

## Adding Translations

```bash
# Extract untranslated strings
bench --site dev.localhost get-untranslated ar --app clinicflow

# Update translations/ar.csv with new entries
# Then clear cache
bench --site dev.localhost clear-cache
```

## RTL Support

All CSS uses logical properties (`margin-inline-start` not `margin-left`).
Arabic text auto-detected via `dir="auto"` on user-generated content fields.
