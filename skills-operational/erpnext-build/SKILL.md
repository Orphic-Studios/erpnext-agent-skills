---
name: erpnext-build
description: Advisory, analytical, and executive agent skill for Frappe Framework & ERPNext v15 Build & Customization module. Use when consulting on low-code app building, DocType creation, Custom Fields, Client Scripts (JS), Server Scripts (Python), Property Setters, Custom Reports, and Print Formats (Jinja).
---

# Frappe & ERPNext v15 Build & Customization Skill

## 1. Domain Architecture & Business Logic
The Build module exposes the Frappe Framework's metadata-driven engine, allowing developers and system architects to extend the data model, inject server/client logic, and build custom business applications without editing core repository files.

### Key Concepts
- **DocType**: The fundamental data model. Stored as JSON schema in custom apps or directly in the database (`custom=1`).
- **Custom Field**: Injects fields into existing standard DocTypes (e.g., adding national tax ID to Customer).
- **Client Script**: JavaScript executed inside the desk browser on form events (`refresh`, `validate`, `field_name_change`).
- **Server Script**: Sandboxed Python script executed on the backend on document events (`before_save`, `after_insert`, `on_submit`) or as an API endpoint / background scheduled job.
- **Property Setter**: Overrides field attributes (e.g., making an optional field mandatory, or changing a default value) safely without code changes.
- **Print Format**: Jinja2 + HTML/CSS templating for PDF generation.

---

## 2. Core DocTypes & Relational Model

| DocType | Submittable? | Mandatory Fields | Common Filtering Keys |
|---|---|---|---|
| `DocType` | No | `name`, `module`, `custom` | `custom`, `module`, `issubmittable` |
| `Custom Field` | No | `dt` (target DocType), `fieldname`, `fieldtype`, `label` | `dt`, `fieldname` |
| `Client Script` | No | `dt`, `script_type`, `script` | `dt`, `enabled` |
| `Server Script` | No | `script_type`, `script` | `reference_doctype`, `disabled` |
| `Print Format` | No | `name`, `doc_type`, `html` | `doc_type`, `standard` |

---

## 3. Executive API Operations (Frappe REST API v15)

### A. Creating a Custom Field via REST
```python
custom_field_payload = {
    "doctype": "Custom Field",
    "dt": "Customer",
    "fieldname": "commercial_registration_no",
    "label": "Commercial Registration (CR)",
    "fieldtype": "Data",
    "insert_after": "customer_name",
    "reqd": 1,
    "description": "Required for national trade compliance"
}
```

### B. Creating a Server Script for Validation
```python
server_script_payload = {
    "doctype": "Server Script",
    "title": "Validate Customer Credit On Sales Order",
    "script_type": "DocType Event",
    "reference_doctype": "Sales Order",
    "doctype_event": "Before Submit",
    "disabled": 0,
    "script": """
# Check if customer has outstanding unpaid overdue invoices
customer = doc.customer
overdue_invoices = frappe.db.count('Sales Invoice', {
    'customer': customer,
    'status': 'Overdue',
    'docstatus': 1
})

if overdue_invoices > 2:
    frappe.throw(f"Cannot submit Sales Order: Customer {customer} has {overdue_invoices} overdue invoices.")
"""
}
```

---

## 4. Analytical & Advisory Recipes

### Best Practice Rules for Safe Customization
1. **Never edit core files in `apps/erpnext` or `apps/frappe`**: Always use `Custom Field`, `Property Setter`, or a standalone Custom App.
2. **Server Script Sandboxing**: Server scripts run with a restricted Python environment (no `import os`, no direct file system access).
3. **Database Indexing**: Add indexes (`in_list_view` or `search_index`) to custom fields heavily used in search filters to avoid query slowdowns.
