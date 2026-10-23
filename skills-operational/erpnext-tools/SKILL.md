---
name: erpnext-tools
description: Advisory, analytical, and executive agent skill for ERPNext v15 Tools module. Use when consulting on ToDo assignments, Calendar Events, Notes, Newsletter distribution, File Manager, and Data Import / Bulk Operations.
---

# ERPNext v15 Tools Module Skill

## 1. Domain Architecture & Business Logic
The Tools module encompasses system-wide collaborative utilities: personal productivity, task delegation, corporate calendar events, internal notes, newsletter campaigns, and document attachment storage.

### Key Concepts
- **ToDo**: Individual action item assigned to any user. Can be auto-created by Frappe assignment rules or manually generated.
- **Event**: Calendar meetings, customer appointments, or system milestones with invitees and Google Calendar synchronization.
- **Note**: Internal wiki or personal scratchpad with public/private visibility.
- **File**: Document attachments (PDFs, images, CSVs) attached to any DocType, stored privately or publicly on disk or S3.
- **Newsletter**: Mass outbound email distribution with recipient lists and unsubscribe compliance.

---

## 2. Core DocTypes & Relational Model

| DocType | Submittable? | Mandatory Fields | Common Filtering Keys |
|---|---|---|---|
| `ToDo` | No | `description`, `allocated_to` | `status` (`Open`/`Closed`), `allocated_to`, `priority` |
| `Event` | No | `subject`, `starts_on` | `event_type`, `starts_on`, `owner` |
| `Note` | No | `title`, `content` | `public`, `owner` |
| `File` | No | `file_name` | `attached_to_doctype`, `attached_to_name`, `is_private` |
| `Newsletter` | Yes (`docstatus=1`) | `subject`, `email_group`, `message` | `status`, `schedule_send` |

---

## 3. Executive API Operations (Frappe REST API v15)

### A. Assigning a ToDo to an Employee
```python
todo_payload = {
    "doctype": "ToDo",
    "description": "Review and approve pending Purchase Order PUR-ORD-2026-00045",
    "allocated_to": "purchase.manager@company.com",
    "reference_type": "Purchase Order",
    "reference_name": "PUR-ORD-2026-00045",
    "priority": "High",
    "status": "Open"
}
```

### B. Scheduling a Company Event
```python
event_payload = {
    "doctype": "Event",
    "subject": "Quarterly Financial Close Review",
    "starts_on": "2026-10-31 10:00:00",
    "ends_on": "2026-10-31 11:30:00",
    "event_type": "Public",
    "description": "Review Q3 revenue recognition and auditor comments."
}
```

---

## 4. Analytical & Advisory Recipes
- **Employee Task Velocity**: Measure average days to close `ToDo` tasks by department.
- **File Storage Cleanup**: Query orphaned `File` records where `attached_to_name` is null or deleted to reclaim server storage.
