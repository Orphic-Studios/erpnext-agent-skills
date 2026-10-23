# Security Policy

## Supported Versions
Security updates and patches are actively maintained for the following versions:

| Suite Version | ERPNext Target | Supported |
|---|---|---|
| `1.0.x` | ERPNext v15.x | :white_check_mark: |
| `< 1.0.0` | ERPNext v14.x | :x: |

---

## Reporting a Vulnerability

The security of enterprise ERP data and autonomous agent operations is our highest priority. If you discover a security vulnerability or exploit vector within these skills or client tools, please **do NOT report it in public GitHub issues**.

Instead, please send an email to:
**security@orphic-studios.com**

Please include:
1. Description of the vulnerability.
2. Step-by-step reproduction instructions or a proof-of-concept.
3. Affected skills or client scripts.
4. Any potential impact on ERPNext database integrity or authentication secrets.

We will acknowledge receipt within 48 hours and coordinate a coordinated disclosure timeline.

---

## Security Best Practices for Agent Deployment

1. **Token Principle of Least Privilege**:
   Never provide an AI agent with an API Token belonging to the `Administrator` account in production. Always create a dedicated `System User` with specific Role Profiles limited to the agent's scope.
2. **Environment Variable Protection**:
   Store `FRAPPE_API_KEY` and `FRAPPE_API_SECRET` exclusively in protected environment variables or secret vaults. Never commit credentials to version control.
3. **Audit Trails**:
   Frappe maintains full audit trails via `Version` and `Activity Log`. Regularly monitor agent actions to verify compliance with internal segregation of duties (SoD).
