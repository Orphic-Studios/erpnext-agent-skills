---
name: tutorial-erpnext-erpnext-integrations
description: Educational and trainer skill for ERPNext v15 Business Integrations module. Use when generating training lessons on online payment gateways (Stripe, PayPal, Razorpay), E-commerce synchronization (Shopify, WooCommerce), banking feeds (Plaid), and integration quizzes.
---

# ERPNext v15 Business Integrations Training & Tutorial Skill

## 1. Instructional Objectives & Pedagogy
- **Target Audience**: E-commerce Managers, Billing Specialists, Treasury Accountants, and Integration Architects.
- **Learning Outcomes**:
  - Configure payment gateways to email customers dynamic payment links on invoices.
  - Set up bidirectional inventory and order synchronization with Shopify and WooCommerce.
  - Link live corporate bank feeds via Plaid for automated transaction reconciliation.

---

## 2. Structured Curriculum & Lesson Plans

### Lesson 1: Payment Gateways (Stripe / PayPal)
- Entering API publishable and secret keys in sandbox vs production.
- Setting up the Payment Gateway Account and mapping gateway processing fees.
- Verifying the automated creation of `Payment Entry` upon customer card payment.

### Lesson 2: E-Commerce Storefront Synchronization
- Mapping web items to ERPNext Item masters.
- Pulling web orders into ERPNext `Sales Orders` and syncing inventory counts back to the website.

---

## 3. Real-World Hands-on Scenario
**Scenario**: "Connect a Stripe sandbox account, generate a payment request link for a $500 Sales Invoice, and simulate an online payment to verify ledger booking."
- **Task for Learner**:
  1. Configure Stripe Settings with test keys.
  2. Create a Sales Invoice and click `Create > Payment Request`.
  3. Simulate test checkout and verify that the invoice status updates to `Paid`.

---

## 4. End-of-Module Quiz & Assessment
1. *What happens in ERPNext when an online customer successfully pays an invoice via Stripe payment link?*
   - [ ] The invoice is deleted.
   - [x] A `Payment Entry` is automatically created, allocated to the invoice, and submitted.
