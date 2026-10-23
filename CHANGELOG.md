# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-10-23

### Added
- **Master Cross-Functional Orchestrator**:
  - Added `core-orchestrator/SKILL.md` covering macro-cycles: `Lead-to-Cash`, `Procure-to-Pay`, `Plan-to-Produce`, `Project-to-Billing`, and `Issue-to-Resolution`.
- **18 Operational Agent Skills (`skills-operational/`)**:
  - `erpnext-home`: Workspace dashboards, KPI number cards, shortcuts.
  - `erpnext-accounting`: Chart of accounts, Sales/Purchase Invoices, Payment Entries, Journal Entries.
  - `erpnext-buying`: Material Requests, RFQs, Supplier Quotations, Purchase Orders.
  - `erpnext-selling`: Customer management, Quotations, Sales Orders, Pricing Rules.
  - `erpnext-stock`: Item masters, Warehouses, Stock Entries, Stock Reconciliation, Serial/Batch tracking.
  - `erpnext-assets`: Fixed asset registration, depreciation schedules, repairs, scrapping.
  - `erpnext-manufacturing`: Bills of Materials (BOM), Work Orders, Job Cards, Operations.
  - `erpnext-quality`: Quality Inspections (Incoming, In-Process, Outgoing), Criteria, CAPA Actions.
  - `erpnext-projects`: Projects, Tasks, Gantt charts, Dependencies, Timesheets.
  - `erpnext-support`: Issues, Service Level Agreements (SLA), Warranties, Maintenance Visits.
  - `erpnext-users`: Role-Based Access Control (RBAC), Role Profiles, User Permissions.
  - `erpnext-website`: Web Pages, Blog Posts, Web Forms, Customer/Supplier Portal.
  - `erpnext-crm`: Leads, Opportunities, Pipelines, Campaigns, Communications.
  - `erpnext-tools`: ToDos, Calendar Events, Notes, Newsletters.
  - `erpnext-settings`: Company configurations, Global Defaults, Naming Series, Workflows.
  - `erpnext-integrations`: Webhooks, OAuth, Social Login, Slack, Google Calendar.
  - `erpnext-erpnext-integrations`: Stripe, PayPal, Razorpay, Plaid, Shopify, WooCommerce.
  - `erpnext-build`: Low-code studio, Custom Fields, Client Scripts, Server Scripts, Print Formats.
- **18 Educational & Training Skills (`skills-educational/`)**:
  - Parallel educational track covering step-by-step user onboarding, real-world business scenarios, and comprehension quizzes across all 18 modules.
- **Enterprise Customization Overlay**:
  - Added `templates/COMPANY_CUSTOMIZATION_GUIDE.md` enabling organizations to overlay custom fields and approval matrices without modifying vanilla skills.
- **Developer Tools & CI/CD**:
  - Added `client-tools/frappe_client.py` (standardized Python REST client for Frappe v15).
  - Added GitHub Actions workflow (`.github/workflows/validate-skills.yml`) for automated frontmatter and syntax validation.
  - Added community files: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, and Issue Templates.
