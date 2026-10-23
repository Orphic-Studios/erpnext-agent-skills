---
name: erpnext-settings
description: Advisory, analytical, and executive agent skill for ERPNext v15 Settings module. Use when consulting on Company masters, Global Defaults, System Settings, Naming Series, Print Settings, Email Accounts, and Workflow Configurations.
---

# ERPNext v15 Settings Module Skill

## 1. Domain Architecture & Business Logic
The Settings module establishes the macro-configuration for the entire instance, including company structures, fiscal boundaries, naming conventions, and system-wide automation triggers.

### Key Concepts
- **Company**: Master entity establishing default currency, chart of accounts template, country, and default tax templates. Multi-company setups support parent-child consolidation.
- **Global Defaults**: System-wide defaults: active fiscal year, default company, date format, and number formatting.
- **Naming Series**: Prefix and numbering rules for every transaction (e.g., `ACC-SINV-.YYYY.-.#####`).
- **Workflow & Workflow State**: State machine engine replacing default submit/cancel actions with multi-step review stages (e.g., `Draft -> Pending HOD Approval -> Pending Finance -> Approved`).

---

## 2. Core DocTypes & Relational Model

| DocType | Submittable? | Mandatory Fields | Common Filtering Keys |
|---|---|---|---|
| `Company` | No | `company_name`, `default_currency`, `country` | `company_name`, `is_group` |
| `Global Defaults` | No | Single Document | Single |
| `Workflow` | No | `workflow_name`, `document_type`, `workflow_state_field` | `document_type`, `is_active` |
| `Naming Series` | No | Tool / Single | Single |

---

## 3. Executive API Operations (Frappe REST API v15)

### Configuring Global Defaults via REST
```python
defaults_payload = {
    "default_company": "Your Company LLC",
    "default_currency": "USD",
    "date_format": "yyyy-mm-dd",
    "time_format": "HH:mm:ss"
}
# PUT to /api/resource/Global Defaults/Global Defaults
```

---

## 4. Analytical & Advisory Recipes
- **Multi-Company Consolidation Setup**: Guide administrators on inter-company transactions and chart of accounts alignment.
- **Naming Series Collisions**: Detect duplicate prefixes across DocTypes to prevent ledger confusion.
