---
name: erpnext-home
description: Advisory, analytical, and executive agent skill for ERPNext v15 Home & Workspace navigation. Use when consulting on Workspace layouts, Shortcuts, Number Cards, Quick Lists, Custom Dashboards, and Onboarding tours.
---

# ERPNext v15 Home & Workspaces Skill

## 1. Domain Architecture & Business Logic
The Home module serves as the primary operational cockpit for users in ERPNext v15, utilizing customizable desk **Workspaces** with interactive KPI number cards, shortcuts, charts, and onboarding checklists.

### Key Concepts
- **Workspace**: Categorized dashboards (e.g., Accounting Workspace, Stock Workspace) composed of blocks:
  - `Shortcut`: Direct links to filtered lists or reports.
  - `Card`: Grouped document lists with badge counters (e.g., "Draft Invoices: 4").
  - `Number Card`: Real-time aggregated numeric KPI (Sum, Count, Average).
  - `Dashboard Chart`: Time-series and categorical charts.
- **Onboarding**: Step-by-step guidance for new enterprise rollouts (Company setup -> COA -> First Item -> First Sale).

---

## 2. Core DocTypes & Relational Model

| DocType | Submittable? | Mandatory Fields | Common Filtering Keys |
|---|---|---|---|
| `Workspace` | No | `title`, `label`, `module` | `is_standard`, `public`, `module` |
| `Number Card` | No | `label`, `document_type`, `function` | `document_type`, `is_public` |
| `Dashboard Chart` | No | `chart_name`, `chart_type`, `document_type` | `chart_type`, `document_type` |

---

## 3. Executive API Operations (Frappe REST API v15)

### Creating a Real-Time KPI Number Card
```python
number_card_payload = {
    "doctype": "Number Card",
    "label": "Total Unpaid Receivables",
    "document_type": "Sales Invoice",
    "function": "Sum",
    "aggregate_function_based_on": "outstanding_amount",
    "filters_json": '[["Sales Invoice","status","in",["Unpaid","Overdue"]]]',
    "is_public": 1
}
```

---

## 4. Analytical & Advisory Recipes
- **Executive Cockpit Design**: Guide administrators on structuring personalized workspaces for executives (high-level charts) versus operational clerks (actionable shortcuts and task cards).
- **Workspace Clutter Elimination**: Audit public workspaces to remove redundant shortcuts and accelerate desk load times.
