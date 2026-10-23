---
name: tutorial-erpnext-stock
description: Educational and trainer skill for ERPNext v15 Stock (Inventory) module. Use when generating warehouse management training lessons, storekeeper onboarding, stock entry tutorials, batch/serial number tracking, inventory reconciliation walkthroughs, and stock assessments.
---

# ERPNext v15 Stock Training & Tutorial Skill

## 1. Instructional Objectives & Pedagogy
- **Target Audience**: Warehouse Managers, Inventory Controllers, Storekeepers, and Logistics Coordinators.
- **Learning Outcomes**:
  - Understand multi-warehouse hierarchies and stock balance bins.
  - Execute stock movements: Material Receipt, Material Issue, and Internal Warehouse Transfer.
  - Master Serial Number and Batch Number tracking with expiry dates.
  - Perform physical inventory counting using the Stock Reconciliation tool.

---

## 2. Structured Curriculum & Lesson Plans

### Lesson 1: Items & Warehouse Architecture
- **Item Master Setup**: Maintaining Stock UOM, valuation method (FIFO vs Moving Average), and reorder levels.
- **Warehouse Tree**: Creating parent warehouses (e.g., "Main Plant") and child storage bins (e.g., "Aisle 3, Shelf B").

### Lesson 2: Stock Entries & Warehouse Transfers
- **Material Issue**: Writing off damaged or sample stock.
- **Material Transfer**: Moving 50 units from "Raw Material Stores" to "WIP Warehouse".
- **Inspecting the Stock Ledger**: Checking ledger balance, valuation rate, and incoming rate.

### Lesson 3: Batch Numbers & Serialized Tracking
- Enabling `has_batch_no` and `has_serial_no` on sensitive/high-value products.
- Enforcing First-Expiry-First-Out (FEFO) on batch dispatches.

---

## 3. Real-World Hands-on Scenario
**Scenario**: "At year-end physical inventory count, the system shows 120 units of Item X in Warehouse A, but the physical count reveals only 114 units."
- **Task for Learner**:
  1. Open the `Stock Reconciliation` tool.
  2. Enter the actual physical count (114 units).
  3. Submit the document and review the generated Stock Adjustment expense entry in the general ledger.

---

## 4. End-of-Module Quiz & Assessment
1. *Can you directly edit an existing Stock Ledger Entry if a mistake was made?*
   - [ ] Yes, any System Manager can edit it.
   - [x] No, the Stock Ledger is immutable; you must cancel/amend the transaction or post a Stock Reconciliation.
