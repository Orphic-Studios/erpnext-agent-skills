---
name: tutorial-erpnext-manufacturing
description: Educational and trainer skill for ERPNext v15 Manufacturing module. Use when generating production planning training lessons, plant manager onboarding, Bill of Materials (BOM) creation tutorials, Work Order and Job Card execution walkthroughs, and production quizzes.
---

# ERPNext v15 Manufacturing Training & Tutorial Skill

## 1. Instructional Objectives & Pedagogy
- **Target Audience**: Production Planners, Plant Managers, Industrial Engineers, Shop Floor Supervisors, and Machine Operators.
- **Learning Outcomes**:
  - Engineer multi-level Bills of Materials (BOM) with raw materials, operations, and workstations.
  - Release Work Orders and dispatch Job Cards to shop floor operators.
  - Execute material transfers for manufacture and receive finished goods into stock.

---

## 2. Structured Curriculum & Lesson Plans

### Lesson 1: Engineering the Bill of Materials (BOM)
- **Raw Materials vs Sub-Assemblies**: Multi-tier BOM nesting.
- **Operations & Workstations**: Calculating machine hour and labor hour rates.
- **Scrap & By-Products**: Accounting for expected manufacturing losses.

### Lesson 2: Work Orders & Shop Floor Execution
- **Work Order Lifecycle**: `Draft` -> `Not Started` -> `In Process` -> `Completed`.
- **Job Cards**: Tracking operator start/stop timers on workstation terminals.
- **Stock Entries**: Transferring materials from Stores to WIP, and booking finished output.

---

## 3. Real-World Hands-on Scenario
**Scenario**: "Assemble 10 ergonomic office chairs. Each chair requires: 1 seat cushion, 1 steel frame, 5 wheels, and 30 minutes of assembly on Workstation 1."
- **Task for Learner**:
  1. Create and submit the active default BOM for the Ergonomic Chair.
  2. Create a Work Order for 10 units.
  3. Transfer raw materials to WIP warehouse.
  4. Complete Job Cards and produce finished goods to Finished Goods Warehouse.

---

## 4. End-of-Module Quiz & Assessment
1. *Can a Work Order be submitted without an active, submitted BOM?*
   - [ ] Yes, if materials are added on the fly.
   - [x] No, a valid submitted BOM is mandatory for every Work Order.
