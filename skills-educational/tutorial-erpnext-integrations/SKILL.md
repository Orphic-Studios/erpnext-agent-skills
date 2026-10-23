---
name: tutorial-erpnext-integrations
description: Educational and trainer skill for Frappe Framework & ERPNext v15 Integrations module. Use when generating developer integration lessons, Webhook setup tutorials, OAuth configuration guides, Slack alert walkthroughs, and API integration quizzes.
---

# Frappe & ERPNext v15 Integrations Training & Tutorial Skill

## 1. Instructional Objectives & Pedagogy
- **Target Audience**: Backend Developers, Integration Engineers, DevOps, and Automation Specialists.
- **Learning Outcomes**:
  - Configure real-time outbound Webhooks for event-driven integration.
  - Set up OAuth 2.0 authentication for third-party client apps.
  - Connect communication channels like Slack and Google Calendar.

---

## 2. Structured Curriculum & Lesson Plans

### Lesson 1: Real-Time Webhooks
- Understanding Frappe document triggers: `after_insert`, `on_update`, `on_submit`, `on_cancel`.
- Structuring JSON payload templates and passing HMAC authorization headers.
- Inspecting the `Webhook Request Log` to debug payload deliveries.

### Lesson 2: OAuth 2.0 & Third-Party Apps
- Registering a `Connected App` with Redirect URIs and Scopes.
- Exchanging authorization codes for access and refresh tokens.

---

## 3. Real-World Hands-on Scenario
**Scenario**: "Whenever a high-priority customer Issue is created in ERPNext, automatically send an alert message to a dedicated Slack channel via Webhook."
- **Task for Learner**:
  1. Create a `Webhook` for DocType `Issue` triggered on `after_insert`.
  2. Set filter condition: `priority == 'Urgent'`.
  3. Send test payload and verify delivery in the Webhook Request Log.

---

## 4. End-of-Module Quiz & Assessment
1. *Where can an administrator inspect why a webhook failed to deliver to an external URL?*
   - [ ] In the General Ledger.
   - [x] In the `Webhook Request Log` list view.
