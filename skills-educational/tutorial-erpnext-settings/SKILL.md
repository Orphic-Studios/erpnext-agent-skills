---
name: tutorial-erpnext-settings
description: Educational and trainer skill for ERPNext v15 Settings module. Use when generating administrator configuration training lessons, multi-company setup tutorials, Naming Series workshops, Workflow builder guides, and system configuration quizzes.
---

# ERPNext v15 Settings Training & Tutorial Skill

## 1. Instructional Objectives & Pedagogy
- **Target Audience**: ERP Implementation Consultants, System Administrators, and Operations Directors.
- **Learning Outcomes**:
  - Configure multi-company setups, default currencies, and fiscal year boundaries.
  - Structure clean transaction document codes using Naming Series.
  - Implement multi-stage document approval chains using the Workflow engine.

---

## 2. Structured Curriculum & Lesson Plans

### Lesson 1: Company Master & Global Defaults
- Setting up company currency, default bank, and tax accounts.
- Managing multi-currency exchange rates and auto-fetching rates from European Central Bank.

### Lesson 2: Designing Naming Series
- Structuring prefixes: `ACC-SINV-.YYYY.-.#####` (Yearly resetting counter).
- Best practices for avoiding collision and ensuring audit compliance.

### Lesson 3: Building Multi-Tier Approval Workflows
- Replacing default Submit with approval stages (`Draft -> Pending Dept Head -> Approved -> Rejected`).
- Restricting state transitions by Role (e.g., only `Purchase Manager` can transition to `Approved`).

---

## 3. Real-World Hands-on Scenario
**Scenario**: "Enforce that all Purchase Orders above $5,000 must be approved by the Finance Director before they can be sent to the supplier."
- **Task for Learner**:
  1. Open the `Workflow` builder.
  2. Create a workflow for `Purchase Order` with states `Draft`, `Pending Approval`, `Approved`.
  3. Restrict the transition from `Pending Approval` to `Approved` exclusively to the `Finance Director` role.

---

## 4. End-of-Module Quiz & Assessment
1. *What happens to a document's default "Submit" button when an active Workflow is attached to that DocType?*
   - [ ] Both buttons appear simultaneously.
   - [x] The default Submit button is replaced by the Workflow Action transition buttons (e.g., Approve / Reject).
