---
name: erpnext-integrations
description: Advisory, analytical, and executive agent skill for Frappe Framework & ERPNext v15 Integrations module. Use when consulting on Webhooks, OAuth Client/Provider, Social Login, Slack Webhooks, Google Drive/Calendar sync, LDAP, and S3 Backup settings.
---

# Frappe & ERPNext v15 Integrations Skill

## 1. Domain Architecture & Business Logic
The Integrations module connects the Frappe Framework to third-party microservices, event streams, identity providers, and cloud storage providers.

### Key Concepts
- **Webhook**: Real-time HTTP POST callback triggered on DocType events (`after_insert`, `on_update`, `on_submit`, `on_cancel`). Essential for event-driven architectures.
- **Connected App & OAuth**: Allows external clients to authorize via OAuth2 (Authorization Code flow).
- **Google Settings**: Synchronizes Google Contacts, Google Calendar events, and stores backups to Google Drive.
- **Slack Webhook**: Sends automated alerts to Slack channels upon urgent issues or high-value purchase orders.

---

## 2. Core DocTypes & Relational Model

| DocType | Submittable? | Mandatory Fields | Common Filtering Keys |
|---|---|---|---|
| `Webhook` | No | `webhook_doctype`, `webhook_docevent`, `request_url` | `webhook_doctype`, `enabled` |
| `Connected App` | No | `app_name`, `client_id` | `app_name` |
| `Slack Webhook URL` | No | `webhook_name` | `webhook_name` |

---

## 3. Executive API Operations (Frappe REST API v15)

### Registering an Automated Webhook via REST
```python
webhook_payload = {
    "doctype": "Webhook",
    "webhook_doctype": "Sales Invoice",
    "webhook_docevent": "on_submit",
    "request_url": "https://api.external-tax-system.com/v1/invoices",
    "request_structure": "JSON",
    "enabled": 1,
    "webhook_headers": [
        {"key": "Authorization", "value": "Bearer YOUR_EXTERNAL_SECRET_TOKEN"}
    ],
    "webhook_data": [
        {"fieldname": "name", "key": "invoice_id"},
        {"fieldname": "grand_total", "key": "total_amount"},
        {"fieldname": "customer", "key": "customer_id"}
    ]
}
```

---

## 4. Analytical & Advisory Recipes
- **Webhook Failure Triage**: Query `Webhook Request Log` to diagnose 4xx and 5xx failures and inspect payload retries.
- **API Security Hardening**: Ensure external callbacks use HMAC secret verification or SSL bearer tokens.
