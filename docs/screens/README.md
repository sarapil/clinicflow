# ClinicFlow — Screen Design Specs
# كلينك فلو — مواصفات تصميم الشاشات

## Screens

- [Dashboard](dashboard.md) — Main workspace dashboard
- [Responsive Matrix](responsive-matrix.md) — Breakpoint behavior

## Design Guidelines

Every screen MUST:
- Use at least 1 `frappe_visual` component
- Have at least 3 `.fv-fx-*` CSS effect classes
- Have GSAP entrance animation
- Support dark mode (CSS variables only)
- Use CSS Logical Properties (not margin-left/right)
- All icons via `frappe.visual.icons`
- All strings wrapped in `__()`
