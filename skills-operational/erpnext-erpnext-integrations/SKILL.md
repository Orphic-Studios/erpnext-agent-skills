---
name: erpnext-erpnext-integrations
description: Advisory, analytical, and executive agent skill for ERPNext v15 Business Integrations module. Use when consulting on Payment Gateways (Stripe, PayPal, Razorpay), E-commerce sync (Shopify, WooCommerce, Amazon), Banking aggregators (Plaid), and automated tax engines (TaxJar, Avalara).
---

# ERPNext v15 Business Integrations Skill

## 1. Domain Architecture & Business Logic
The ERPNext Integrations module embeds native enterprise connectors for global payment processing, marketplace synchronization, bank feed reconciliation, and automated regional taxation.

### Key Concepts
- **Payment Gateway (Stripe / PayPal / Razorpay)**: Generates secure payment links on Sales Invoices, processes credit cards, and creates automated `Payment Entry` upon payment confirmation webhooks.
- **E-Commerce Connectors (Shopify / WooCommerce / Amazon)**: Synchronizes catalog items, inventories, incoming web orders into `Sales Order`, and updates fulfillment tracking.
- **Plaid Banking Integration**: Connects to commercial bank accounts to fetch live bank statements directly into `Bank Clearance` / `Bank Transaction`.

---

## 2. Core DocTypes & Relational Model

| DocType | Submittable? | Mandatory Fields | Common Filtering Keys |
|---|---|---|---|
| `Payment Gateway` | No | `gateway` | `gateway` |
| `Stripe Settings` | No | `publishable_key`, `secret_key` | Single |
| `Shopify Settings`| No | `shopify_url`, `api_key`, `password` | `enable_shopify` |
| `Plaid Settings` | No | `client_id`, `secret` | `enabled` |

---

## 3. Executive API Operations (Frappe REST API v15)

### Generating a Payment Link for a Sales Invoice via RPC
```python
# Create an online payment request link
payment_request = frappe_client.call_method(
    "erpnext.accounts.doctype.payment_request.payment_request.make_payment_request",
    dt="Sales Invoice",
    dn="ACC-SINV-2026-00001",
    recipient_id="customer@example.com",
    payment_gateway_account="Stripe - USD - YC"
)
```

---

## 4. Analytical & Advisory Recipes
- **Marketplace Reconciliation**: Detect discrepancies between Amazon/Shopify reported sales and generated ERPNext Sales Invoices.
- **Payment Gateway Fee Segregation**: Ensure processing fees (e.g., Stripe 2.9% + 30c) are booked to "Payment Gateway Charges Expense" rather than reducing net revenue.
