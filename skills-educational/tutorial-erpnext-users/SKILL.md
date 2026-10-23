---
name: tutorial-erpnext-users
description: Educational and trainer skill for ERPNext v15 Users & Security module. Use when generating administrator onboarding lessons, Role-Based Access Control (RBAC) tutorials, User Permission (row-level security) guides, and security audit quizzes.
---

# ERPNext v15 Users & Security Training & Tutorial Skill

## 1. Instructional Objectives & Pedagogy
- **Target Audience**: System Administrators, IT Security Officers, HR Managers, and Department Leads.
- **Learning Outcomes**:
  - Provision users and assign standardized Role Profiles.
  - Configure the Role Permissions Manager (Read, Write, Create, Submit, Cancel, Amend).
  - Implement row-level security using User Permissions (e.g., branch-restricted access).

---

## 2. Structured Curriculum & Lesson Plans

### Lesson 1: Users, Roles, and Role Profiles
- Creating a new user account and sending welcome invites.
- Bundling roles into `Role Profile` to prevent privilege creep.
- Using `Module Profile` to hide irrelevant workspaces from specific job roles.

### Lesson 2: Granular Role Permissions
- Opening the `Role Permissions Manager`.
- Inspecting permission levels (Level 0: standard fields, Level 1+: sensitive financial or payroll fields).
- Managing submittable rights: separating who can create Drafts from who can Submit.

### Lesson 3: Row-Level Security (User Permissions)
- Restricting sales reps to view only their assigned Customer territory.
- Restricting branch managers to view only their branch's Accounting records.

---

## 3. Real-World Hands-on Scenario
**Scenario**: "Onboard a new warehouse assistant who should only be able to view and create Stock Entries for the 'East Coast Warehouse', and must never see sales prices or customer data."
- **Task for Learner**:
  1. Create the User account with role `Stock User`.
  2. Create a `User Permission` restricting `Warehouse` to `East Coast Warehouse`.
  3. Verify by logging in as the new user and confirming that other warehouses are hidden.

---

## 4. End-of-Module Quiz & Assessment
1. *What is the difference between a Role and a User Permission?*
   - [ ] They are identical.
   - [x] A Role controls what actions you can perform (RBAC), while a User Permission controls which specific records you can see (row-level security).
