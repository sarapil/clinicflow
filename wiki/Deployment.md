# Deployment — النشر

## Production via Frappe Cloud

1. Create a site on [Frappe Cloud](https://frappecloud.com)
2. Install ClinicFlow from the Marketplace
3. Run initial setup wizard

## Self-Hosted

```bash
# On a fresh Frappe bench
bench get-app clinicflow https://github.com/sarapil/clinicflow
bench --site <production-site> install-app clinicflow
bench --site <production-site> migrate
bench build --app clinicflow
```

## Docker (Frappe Docker)

Add to `apps.json`:
```json
{"url": "https://github.com/sarapil/clinicflow", "branch": "main"}
```

## Post-Deployment Checklist

- [ ] Run `bench --site <site> migrate`
- [ ] Run `bench build --app clinicflow`
- [ ] Clear cache: `bench --site <site> clear-cache`
- [ ] Verify app icon on `/desk`
- [ ] Run smoke test: check DocType list loads
