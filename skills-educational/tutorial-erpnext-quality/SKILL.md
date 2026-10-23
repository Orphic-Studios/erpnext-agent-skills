---
name: tutorial-erpnext-quality
description: Educational and trainer skill for ERPNext v15 Quality module. Use when generating quality assurance training lessons, QA inspector onboarding, inspection parameter setup tutorials, non-conformance walkthroughs, and quality quizzes.
---

# ERPNext v15 Quality Training & Tutorial Skill

## 1. Instructional Objectives & Pedagogy
- **Target Audience**: Quality Assurance (QA) Managers, QC Inspectors, Compliance Officers, and Shop Floor Auditors.
- **Learning Outcomes**:
  - Set up Quality Inspection Templates with defined numeric tolerances and qualitative criteria.
  - Execute Incoming, In-process, and Outgoing inspections.
  - Route non-conforming items to quarantine/rejected warehouses and open corrective action (CAPA) records.

---

## 2. Structured Curriculum & Lesson Plans

### Lesson 1: Quality Parameters & Templates
- Defining inspection criteria (e.g., pH Level, Resistance, Dimensions) with Min/Max acceptable values.
- Linking templates to Items so inspections auto-trigger upon Purchase Receipts or Deliveries.

### Lesson 2: Executing Inspections & Managing Rejections
- Sampling protocol and entering observed readings.
- Marking inspections as `Accepted` or `Rejected`.
- Handling rejected goods: Returning to vendor or scrapping.

---

## 3. Real-World Hands-on Scenario
**Scenario**: "A shipment of 500 precision bolts arrives. 20 samples are tested for tensile strength (tolerance: 800 - 850 MPa). 3 samples test at 740 MPa (below minimum threshold)."
- **Task for Learner**:
  1. Record the Quality Inspection as `Rejected`.
  2. Prevent the Purchase Receipt from posting into active warehouse stock.
  3. Open a `Quality Action` ticket to notify the supplier of non-conformance.

---

## 4. End-of-Module Quiz & Assessment
1. *What happens to inventory when an incoming item is marked "Rejected" during Quality Inspection?*
   - [ ] It is deleted from the database.
   - [x] It is routed to the designated "Rejected Warehouse" or returned to the supplier.
