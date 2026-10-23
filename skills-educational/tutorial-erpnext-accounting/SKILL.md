---
name: tutorial-erpnext-accounting
description: Educational and trainer skill for ERPNext v15 Accounting module. Use when generating step-by-step training lessons, interactive user onboarding, accounting hands-on scenarios, double-entry bookkeeping walkthroughs, and comprehension quizzes for finance teams.
---

# ERPNext v15 Accounting Training & Tutorial Skill

## 1. Instructional Objectives & Pedagogy
- **Target Audience**: Chief Financial Officers, Controllers, Staff Accountants, Bookkeepers, and Auditors.
- **Learning Outcomes**:
  - Understand ERPNext's multi-currency General Ledger and Chart of Accounts hierarchy.
  - Master the end-to-end invoice lifecycle (Draft -> Submit -> Payment -> Reconciliation).
  - Understand the difference between Perpetual vs Periodic inventory ledger impacts.
  - Successfully diagnose and resolve common accounting validation errors.

---

## 2. Structured Curriculum & Lesson Plans

### Lesson 1: Understanding the Chart of Accounts (COA)
- **Conceptual Metaphor**: The COA is the tree of life for enterprise finances.
- **Rule of Groups vs Ledgers**:
  - Groups: Categories that aggregate balances (cannot directly hold debit/credit).
  - Ledgers: Active leaf accounts where transactions are posted.
- **Hands-on Task**: Creating a sub-account under `Operating Expenses` for "Software Subscriptions".

### Lesson 2: The Sales Invoicing Lifecycle
- **Step 1**: Navigating to `Home > Accounting > Sales Invoice > New`.
- **Step 2**: Selecting Customer and understanding Payment Terms.
- **Step 3**: Adding Item rows, Income Accounts, and Cost Centers.
- **Step 4**: Applying Taxes and Charges templates.
- **Step 5**: Saving as Draft vs Submitting (Examining the GL entry generated: Debit Customer, Credit Income, Credit Tax).

### Lesson 3: Payment Entry & Reconciliation
- **Walkthrough**: Receiving payment via Bank Transfer.
- **Allocating Payments**: Matching against open Sales Invoices.
- **Bank Reconciliation Tool**: Matching ERP transactions against uploaded bank CSV statements.

---

## 3. Real-World Hands-on Scenario
**Scenario**: "Al-Amal Medical Co. purchased medical equipment for $12,000 on 30-day credit. After 15 days, they returned $2,000 worth of defective units, and paid the remaining $10,000 via wire transfer."
- **Task for Learner**:
  1. Create and submit the initial Sales Invoice.
  2. Create a Sales Return (Credit Note) linked to the invoice.
  3. Create the Payment Entry for the remaining balance.
  4. Verify the Customer Statement balance equals 0.00.

---

## 4. End-of-Module Quiz & Assessment
1. *Can you post a Journal Entry directly to a Group Account in the Chart of Accounts?*
   - [ ] Yes
   - [x] No, only Ledger accounts accept financial transactions.
2. *What happens in the General Ledger when an invoice is in "Draft" state?*
   - [ ] General Ledger is debited immediately.
   - [x] No GL entries are created until the document is Submitted (`docstatus=1`).
