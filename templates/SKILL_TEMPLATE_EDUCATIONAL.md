---
name: tutorial-erpnext-[module_name]
description: Educational and training skill for ERPNext v15 [Module Name] module. Use when designing user training curriculums, interactive walkthroughs, hands-on business scenarios, step-by-step how-to guides, and comprehension quizzes for ERPNext end users and administrators.
---

# ERPNext v15 - [Module Name] Educational & Training Skill

## 1. Pedagogical Objective & Target Audience
- **Target Learner**: [e.g., End-user, Junior Accountant, Operations Manager, System Admin]
- **Learning Outcomes**:
  - Understand core business concepts underlying the [Module Name] module.
  - Navigate ERPNext v15 Workspace, List Views, and Form Views with confidence.
  - Perform daily transactions accurately without triggering validation errors.
  - Review reports and self-audit discrepancies.

---

## 2. Structured Learning Path (Curriculum)

### Level 1: Foundations (المفاهيم الأساسية)
- Conceptual explanation in simple business terms (no jargon).
- Visual mental model: Where does this module sit in the enterprise?
- Key terminology dictionary (e.g., DocType, Child Table, Submit, Cancel, Amend).

### Level 2: Hands-on Step-by-Step Walkthroughs (التدريب العملي)
1. **Lab 1: First Transaction**
   - Scenario setup (Business Context).
   - Step 1: Navigation path (`Home > [Module] > [DocType] > New`).
   - Step 2: Form filling (Mandatory vs Optional fields explained).
   - Step 3: Saving as Draft (`Ctrl+S`).
   - Step 4: Submission & Verification.

### Level 3: Real-World Business Scenarios (محاكاة سيناريوهات حقيقية)
- **Scenario A (Standard flow)**: Step-by-step instructions with expected outputs.
- **Scenario B (Edge case / Exception handling)**: How to handle returns, cancellations, or disputed amounts.

---

## 3. Interactive Knowledge Checks & Quizzes (اختبارات الفهم)
Provide multiple-choice questions and practical challenges:
1. *Question 1*: What happens to inventory/GL when you click Submit vs Save?
2. *Practical Exercise*: "Create a test record with a 15% tax rate and verify the ledger impact."

---

## 4. Common Mistakes & Self-Troubleshooting Guide (دليل حل المشاكل للمتدربين)
| What Happened | Why It Happened | How to Fix It in UI |
|---|---|---|
| Red banner: "Mandatory fields required" | A red-asterisk field was left blank | Check highlighted red fields |
| "Cannot cancel document linked to..." | Document has active downstream links | Cancel child document first |
