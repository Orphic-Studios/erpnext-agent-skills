# 🌐 ERPNext v15 Universal AI Agent Skills Suite
> **Comprehensive Modular Skills for Autonomous, Advisory, and Educational AI Agents interfacing with Frappe Framework & ERPNext v15.**

[![ERPNext Version](https://img.shields.io/badge/ERPNext-v15.x-blue.svg)](https://erpnext.com)
[![Frappe Framework](https://img.shields.io/badge/Frappe-v15.x-orange.svg)](https://frappe.io)
[![Release Version](https://img.shields.io/badge/Release-v1.0.0-brightgreen.svg)](https://github.com/Orphic-Studios/erpnext-agent-skills/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Standard](https://img.shields.io/badge/Standard-Vanilla%20Standard-success.svg)](#)

---

## 📖 Overview
This repository provides an enterprise-grade suite of **37 specialized AI Agent Skills** adhering to open agent standards (`SKILL.md`). It transforms any modern AI coding or conversational agent into an **expert ERPNext v15 consultant, analyst, executor, and instructor**.

The suite is divided into three architectural layers:
1. **Master Orchestrator**: Teaches the agent cross-module coordination and End-to-End business cycles (`Lead-to-Cash`, `Procure-to-Pay`, `Plan-to-Produce`, etc.).
2. **18 Operational Skills (Advisory & Executive)**: One skill for every navigation item in ERPNext v15 desk, equipped with Frappe REST API v15 payloads, validations, and KPI recipes.
3. **18 Educational Skills (Training & Onboarding)**: Dedicated skills to generate interactive user guides, real-world business scenarios, and comprehension quizzes for end-user training.
4. **Enterprise Customization Overlay**: A standardized template for organizations to overlay custom fields, approval workflows, and scripts without modifying vanilla skills.

---

## 🗂️ Suite Architecture & Directory Structure

```text
erpnext-agent-skills/
├── core-orchestrator/                  # ★ Master Cross-Module Integration Skill
│   └── SKILL.md                        # Cross-functional workflow routing & E2E flows
│
├── skills-operational/                 # 18 Operational Skills (Advisory + Executive)
│   ├── erpnext-home/SKILL.md           # Workspaces, KPI Number Cards, Dashboards
│   ├── erpnext-accounting/SKILL.md     # Chart of Accounts, Invoices, Payments, GL
│   ├── erpnext-buying/SKILL.md         # Requisitions, RFQs, Purchase Orders
│   ├── erpnext-selling/SKILL.md        # Quotations, Sales Orders, Pricing Rules
│   ├── erpnext-stock/SKILL.md          # Items, Warehouses, Stock Ledger, Serial/Batch
│   ├── erpnext-assets/SKILL.md         # Fixed Assets, Depreciation, Asset Repairs
│   ├── erpnext-manufacturing/SKILL.md  # BOM, Work Orders, Job Cards, Operations
│   ├── erpnext-quality/SKILL.md        # Quality Inspections, Criteria, CAPA Actions
│   ├── erpnext-projects/SKILL.md       # Gantt, Tasks, Dependencies, Timesheets
│   ├── erpnext-support/SKILL.md        # Issues, SLA Timers, Warranties, Maintenance
│   ├── erpnext-users/SKILL.md          # RBAC, Role Profiles, Row-Level Permissions
│   ├── erpnext-website/SKILL.md        # Web Pages, Blogs, Portal, Web Forms
│   ├── erpnext-crm/SKILL.md            # Leads, Opportunities, Pipelines, Campaigns
│   ├── erpnext-tools/SKILL.md          # ToDos, Calendar Events, Notes, Newsletters
│   ├── erpnext-settings/SKILL.md       # Company Masters, Naming Series, Workflows
│   ├── erpnext-integrations/SKILL.md   # Webhooks, OAuth, Slack, Google Calendar
│   ├── erpnext-erpnext-integrations/   # Stripe, PayPal, Razorpay, Plaid, Shopify
│   └── erpnext-build/SKILL.md          # DocTypes, Custom Fields, Client/Server Scripts
│
├── skills-educational/                 # 18 Educational Skills (Interactive Training)
│   ├── tutorial-erpnext-home/          # Desk navigation & Awesome Bar tutorials
│   ├── tutorial-erpnext-accounting/    # Bookkeeping & invoice walkthroughs
│   ├── tutorial-erpnext-buying/        # Procurement & bidding simulations
│   ├── tutorial-erpnext-selling/       # Order-to-cash sales simulations
│   ├── tutorial-erpnext-stock/         # Warehouse storekeeper onboarding
│   ├── tutorial-erpnext-assets/        # CapEx & depreciation training
│   ├── tutorial-erpnext-manufacturing/ # BOM & shop floor operator training
│   ├── tutorial-erpnext-quality/       # QA inspection & rejection workshops
│   ├── tutorial-erpnext-projects/      # Project manager & timesheet guides
│   ├── tutorial-erpnext-support/       # Helpdesk & SLA response workshops
│   ├── tutorial-erpnext-users/         # Security administrator role workshops
│   ├── tutorial-erpnext-website/       # Webmaster & portal training
│   ├── tutorial-erpnext-crm/           # Sales pipeline & qualification training
│   ├── tutorial-erpnext-tools/         # Employee productivity tutorials
│   ├── tutorial-erpnext-settings/      # System administrator config workshops
│   ├── tutorial-erpnext-integrations/  # Webhook & API integration labs
│   ├── tutorial-erpnext-erpnext-integrations/ # Payment gateway labs
│   └── tutorial-erpnext-build/         # Low-code developer scripting labs
│
├── templates/
│   ├── COMPANY_CUSTOMIZATION_GUIDE.md  # Template for adding company-specific fields
│   ├── SKILL_TEMPLATE_OPERATIONAL.md   # Standard template for operational skills
│   └── SKILL_TEMPLATE_EDUCATIONAL.md   # Standard template for educational skills
│
├── client-tools/
│   └── frappe_client.py                # Standalone Python REST Client for Frappe v15
├── LICENSE                             # MIT Open Source License
└── README.md
```

---

## 🚀 How to Use with AI Agents

### 1. Antigravity & Claude Code
Clone the repository into your workspace skills directory or link individual folders:
```bash
git clone https://github.com/Orphic-Studios/erpnext-agent-skills.git
```
To enable all skills, add the skill paths to your workspace configuration or point your agent prompt to the repository root.

### 2. Cursor, Continue, or Copilot
Add this repository to your project context or rules:
* Include `.cursorrules` or instructions referencing:
  `Follow instructions and schema definitions in ./skills-operational/ for any ERPNext operations.`

### 3. Python Multi-Agent Frameworks (CrewAI / AutoGen / LangChain)
Load the `SKILL.md` contents dynamically as system prompts for domain agents, and equip them with `client-tools/frappe_client.py` as an execution tool:
```python
from erpnext_agent_skills.client_tools.frappe_client import FrappeClient

client = FrappeClient(
    base_url="https://erp.yourcompany.com",
    api_key="your_api_key",
    api_secret="your_api_secret"
)

# Example: Read unpaid invoices
invoices = client.get_list("Sales Invoice", filters=[["status", "=", "Unpaid"]])
```

---

## 🏢 Customizing for Your Company

If your enterprise uses custom fields, custom DocTypes, or specific approval workflows:
1. Open `templates/COMPANY_CUSTOMIZATION_GUIDE.md`.
2. Fill in your custom fields, approval matrices, and business rules.
3. Place your completed file in `customizations/company_overlay.md`.
4. Your AI agent will automatically respect both standard ERPNext v15 rules and your company's custom requirements.

---

## 🤝 Contributing
Contributions are warmly welcomed! Please review `templates/SKILL_TEMPLATE_OPERATIONAL.md` and ensure any PR conforms to standard ERPNext v15 vanilla conventions.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
