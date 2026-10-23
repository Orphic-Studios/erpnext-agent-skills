---
name: tutorial-erpnext-projects
description: Educational and trainer skill for ERPNext v15 Projects module. Use when generating project manager training lessons, Gantt chart tutorials, task assignment and dependency walkthroughs, employee timesheet tracking guides, and project costing assessments.
---

# ERPNext v15 Projects Training & Tutorial Skill

## 1. Instructional Objectives & Pedagogy
- **Target Audience**: Project Managers, Scrum Masters, Service Delivery Leads, Consultants, and Engineers.
- **Learning Outcomes**:
  - Plan projects using milestones, Gantt charts, and task dependencies.
  - Track employee billable and non-billable hours via Timesheets.
  - Monitor actual project costs against allocated budgets and generate client invoices.

---

## 2. Structured Curriculum & Lesson Plans

### Lesson 1: Project Structuring & Milestones
- **Creating a Project**: Setting start date, expected delivery, and budget limits.
- **Project Templates**: Reusing standardized work breakdowns for recurring project types.

### Lesson 2: Tasks, Assignments & Dependencies
- **Task Hierarchy**: Parent tasks, sub-tasks, and predecessor dependencies (`depends_on`).
- **Gantt Chart View**: Visualizing critical path and resolving scheduling bottlenecks.

### Lesson 3: Timesheet Logging & Customer Billing
- **Daily Time Logs**: Employees logging hours per activity type (Consulting, Coding, QA).
- **Auto-Billing**: Generating a Sales Invoice directly from approved Timesheet hours.

---

## 3. Real-World Hands-on Scenario
**Scenario**: "Deliver a website redesign for a client: 3 weeks planned. Project consists of 3 tasks: UI Design (40h), Frontend Build (60h), Client Review (10h). UI Design must finish before Frontend Build begins."
- **Task for Learner**:
  1. Create Project record linked to the Client.
  2. Create Task 1 and Task 2 with `depends_on` configured.
  3. Submit a Timesheet for 16 hours of UI Design marked as billable.
  4. Generate a draft Sales Invoice from the timesheet.

---

## 4. End-of-Module Quiz & Assessment
1. *Can a Task depend on another Task belonging to a different Project?*
   - [ ] Yes, any task can link to any task.
   - [x] No, task dependencies are scoped to the parent project structure.
