# ClinicFlow — Dependency Graph
# كلينك فلو — مخطط التبعيات

```mermaid
graph TD
    frappe["frappe v16"]
    frappe_visual["frappe_visual"]
    arkan_help["arkan_help"]
    caps["caps"]
    medcode["medcode"]
    clinicflow["ClinicFlow"]
    frappe --> clinicflow
    frappe_visual --> clinicflow
    arkan_help --> clinicflow
    caps --> clinicflow
    medcode --> clinicflow
    style clinicflow fill:#EF4444,color:#fff
    style frappe fill:#0089FF,color:#fff
```
