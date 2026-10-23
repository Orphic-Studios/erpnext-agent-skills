---
name: tutorial-erpnext-build
description: Educational and trainer skill for Frappe Framework & ERPNext v15 Build (Low-Code Customization) module. Use when generating developer training lessons, Custom Field workshops, Client Script (JS) and Server Script (Python) tutorials, Print Format design guides, and customization quizzes.
---

# Frappe & ERPNext v15 Build & Customization Training & Tutorial Skill

## 1. Instructional Objectives & Pedagogy
- **Target Audience**: Frappe Developers, ERP Customizers, Business Analysts, and Technical Consultants.
- **Learning Outcomes**:
  - Extend the standard data model safely using Custom Fields and Property Setters.
  - Write Client Scripts (JavaScript) to enhance browser UX and dynamic form behavior.
  - Implement Server Scripts (sandboxed Python) for business validation and API endpoints.
  - Design pixel-perfect PDF Print Formats using Jinja2 and HTML/CSS.

---

## 2. Structured Curriculum & Lesson Plans

### Lesson 1: Extending the Data Model Safely
- The golden rule: Never edit core app files directly.
- Adding a `Custom Field` via Customize Form vs DocType builder.
- Using `Property Setter` to modify field requirements without affecting git tracked files.

### Lesson 2: Interactive Client Scripts (JavaScript)
- Form triggers: `refresh`, `validate`, `item_code_on_change`.
- Setting field properties dynamically with `frm.set_df_property()`.
- Showing alerts with `frappe.msgprint()` and prompt dialogs.

### Lesson 3: Server Scripts (Python Backend Logic)
- Document events: `before_save`, `on_submit`, `on_cancel`.
- Querying data using `frappe.db.get_value()` and `frappe.db.count()`.
- Halting invalid transactions with `frappe.throw()`.

---

## 3. Real-World Hands-on Scenario
**Scenario**: "On the Sales Order form, when the user selects a customer, write a Client Script that checks if the customer's territory is 'VIP', and if so, displays a green alert message at the top of the form."
- **Task for Learner**:
  1. Open `Client Script` and create a new record for `DocType: Sales Order`.
  2. Implement `frappe.ui.form.on('Sales Order', { customer(frm) { ... } })`.
  3. Test on a draft Sales Order and verify the alert triggers.

---

## 4. End-of-Module Quiz & Assessment
1. *Where are Server Scripts stored, and can they be executed safely on production?*
   - [ ] Stored in git repositories only.
   - [x] Stored as database records and executed within a secure restricted Python sandbox.
