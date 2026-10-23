# Enterprise Customization Guide & Overlay Template
## How to adapt ERPNext v15 Standard Skills to your Company's Customizations

This template allows organizations to augment the standard ERPNext v15 Agent Skills with company-specific customizations (Custom Fields, Custom DocTypes, Client/Server Scripts, Workflow Approval Matrices, and Pricing Policies) without altering or breaking the core vanilla skills.

---

### Step 1: Where to place your customization file
Save a copy of this file in your project or repository as:
`customizations/company_overlay.md` or directly inside the relevant skill folder as `customizations.md`.

---

### Step 2: Fill in the Company Customization Manifest

```markdown
# Company ERPNext Profile: [Your Company Name]
- **Target ERPNext Version**: 15.x
- **Frappe Framework Version**: 15.x
- **Installed Custom Apps**: [e.g., custom_ecommerce, saudi_e_invoicing, custom_payroll]
- **Default Currency**: [e.g., SAR / USD / AED / EGP]
- **Fiscal Year Start**: [e.g., 01-01]

---

## 1. Custom Fields Inventory (الحقول المخصصة)
Add any custom fields added via "Customize Form" or Custom Apps.

| Target DocType | Fieldname (ID) | Label | Type | Mandatory? | Default / Formula / Options | Notes & Purpose |
|---|---|---|---|---|---|---|
| `Sales Invoice` | `custom_zatca_uuid` | ZATCA UUID | Data | Yes (on submit) | Generated via QR script | E-Invoicing Phase 2 Compliance |
| `Item` | `custom_temp_zone` | Storage Temperature | Select | No | Ambient, Chilled, Frozen | Warehouse routing constraint |
| `Customer` | `custom_national_id` | National ID / CR | Data | Yes | Regex validation | Required for local tax authorities |
| `Purchase Order` | `custom_budget_code` | Project Budget Code | Link (Budget Code) | Yes | Filtered by Cost Center | Finance budget check |

---

## 2. Custom DocTypes (الجداول والمستندات المخصصة)
List newly created DocTypes created via "Build > DocType".

### DocType: `Company Fleet Inspection`
- **Module**: Quality / Assets
- **Is Submittable**: Yes
- **Key Fields**:
  - `vehicle` (Link -> Asset: Vehicle)
  - `inspector` (Link -> User)
  - `odometer_reading` (Int)
  - `status` (Select: Passed, Needs Maintenance, Grounded)
- **Workflow & Rules**:
  - If status == "Needs Maintenance", trigger an Asset Repair ticket automatically.

---

## 3. Workflow & Approval Matrix (سلاسل الاعتماد والسياسات الداخلية)
Override standard single-step submissions with company multi-tier approvals.

| DocType | Value / Condition | Required Approver Role | Next State | Action on Rejection |
|---|---|---|---|---|
| `Purchase Order` | `grand_total <= 10,000` | Purchase Manager | Approved | Cancelled |
| `Purchase Order` | `grand_total > 10,000` | CFO / General Manager | Approved | Return to Draft |
| `Leave Application` | `total_leave_days > 5` | HR Director | Approved | Rejected |
| `Journal Entry` | Any amount | Finance Controller | Submitted | Draft |

---

## 4. Custom Scripts & Business Rules (قواعد العمل المخصصة)
Summarize Client Scripts or Server Scripts so the AI agent accounts for them:

- **Server Script on `Sales Invoice` Before Submit**:
  - The script checks customer credit limit against outstanding receivables. If exceeded and no bypass role (`Credit Controller`) is present, it aborts submission with `frappe.throw("Credit limit exceeded")`.
- **Client Script on `Quotation`**:
  - Auto-applies standard volume discount if quantity >= 100.

---

## 5. Security & Sensitive Field Restrictions (قيود الخصوصية)
- Fields that the AI agent must **never display or log in plaintext**:
  - `bank_account_no`
  - `tax_id` (partial mask allowed)
  - `salary_slip` details (restricted to HR Manager role only)
```

---

### Step 3: Instructing the AI Agent to Use the Customization
In your agent system prompt or session start, add:
> *"Always check and apply the rules in `customizations/company_overlay.md` in addition to the standard ERPNext v15 skills."*
