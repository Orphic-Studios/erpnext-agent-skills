---
name: tutorial-erpnext-selling
description: Educational and trainer skill for ERPNext v15 Selling module. Use when generating step-by-step training lessons, sales rep onboarding, quotation and sales order tutorials, pricing rule workshops, and practical sales team assessments.
---

# ERPNext v15 Selling Training & Tutorial Skill

## 1. Instructional Objectives & Pedagogy
- **Target Audience**: Sales Managers, Account Executives, Sales Reps, and Order Desk Clerks.
- **Learning Outcomes**:
  - Understand the customer master setup, credit terms, and price list assignment.
  - Create and format professional Quotations with discounts and taxes.
  - Convert approved Quotations into binding Sales Orders.
  - Track fulfillment (Delivery Notes) and Billing (Sales Invoices) from the Sales Order dashboard.

---

## 2. Structured Curriculum & Lesson Plans

### Lesson 1: Customer Master & Credit Policies
- **Core Distinction**: Lead (prospect with potential interest) vs Customer (commercial entity with billing/tax details).
- **Credit Limit & Blocking**: What happens when a sales rep attempts to submit an order exceeding the customer credit threshold.

### Lesson 2: Crafting Winning Quotations
- **Step-by-step Form filling**: Adding items, price lists, volume discounts.
- **Validity Dates**: Setting `valid_till` and auto-expiration.
- **Sending Quotes via Email**: Attaching customized PDF print formats directly from ERPNext.

### Lesson 3: The Sales Order Engine
- **From Quote to Order**: Using the `Create > Sales Order` shortcut.
- **Understanding Delivery Schedules**: Specifying partial delivery dates per item line.
- **The Visual Status Dashboard**: Explaining the progression badges (`To Deliver`, `To Bill`, `Completed`).

---

## 3. Real-World Hands-on Scenario
**Scenario**: "A key customer requests 50 units of Solar Inverters. They are entitled to a 5% corporate discount, and request delivery split into two batches: 25 units today and 25 units next month."
- **Task for Learner**:
  1. Set up the Customer record with their assigned Price List.
  2. Create a Sales Order with two item rows reflecting the split delivery dates.
  3. Submit the order and verify that fulfillment status shows `To Deliver`.

---

## 4. End-of-Module Quiz & Assessment
1. *Does submitting a Quotation reserve physical inventory in the warehouse?*
   - [ ] Yes
   - [x] No, physical stock is reserved or deducted only upon Sales Order / Delivery Note.
2. *Where can a salesperson check whether an order has been invoiced?*
   - [ ] By opening the General Ledger directly.
   - [x] By checking the Billing Status badge on the Sales Order dashboard.
