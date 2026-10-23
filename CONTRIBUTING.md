# Contributing to ERPNext Universal AI Agent Skills Suite

Thank you for your interest in contributing to the **ERPNext Universal AI Agent Skills Suite**! This project aims to maintain the highest quality, vanilla-compliant, modular skills for autonomous AI agents interfacing with ERPNext v15 and Frappe Framework.

---

## Code of Conduct
By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## Architectural Principles

1. **Standard Vanilla Compliance**:
   All core operational skills in `skills-operational/` must adhere strictly to standard ERPNext v15 and Frappe Framework v15 conventions without assuming custom apps or custom fields.
2. **Modular Granularity**:
   Each module corresponds to a single domain navigation unit. Do not merge unrelated DocTypes into a single skill.
3. **Dual-Track Discipline**:
   - Operational skills (`skills-operational/`) focus on advisory knowledge, data modeling, API payloads, and analytical formulas.
   - Educational skills (`skills-educational/`) focus on instructional pedagogy, step-by-step user walkthroughs, hands-on labs, and comprehension quizzes.
4. **Cross-Module Linkage**:
   Complex multi-step workflows spanning more than two modules belong in `core-orchestrator/SKILL.md`.

---

## How to Contribute

### 1. Proposing a New Skill or Improvement
- Open an issue using our [Skill Request Proposal Template](.github/ISSUE_TEMPLATE/skill_request.md).
- Discuss the proposed DocTypes, REST API endpoints, and validation rules.

### 2. Developing a Skill
- Copy the appropriate template from `templates/`:
  - `templates/SKILL_TEMPLATE_OPERATIONAL.md` for operational skills.
  - `templates/SKILL_TEMPLATE_EDUCATIONAL.md` for educational skills.
- Follow the standard YAML frontmatter:
  ```yaml
  ---
  name: erpnext-[module_name]
  description: Clear, action-oriented description detailing when an AI agent should activate this skill.
  ---
  ```
- Ensure all diagrams use Mermaid syntax.
- Ensure all API examples use standard Frappe REST endpoints (`/api/resource/...` or `/api/method/...`).

### 3. Submitting a Pull Request
1. Fork the repository and create your branch from `main`:
   ```bash
   git checkout -b feature/new-skill-healthcare
   ```
2. Commit your changes with clear, descriptive commit messages:
   ```bash
   git commit -m "feat(skills): add erpnext-healthcare operational skill"
   ```
3. Push to your fork and submit a Pull Request targeting `main`.
4. Ensure the CI validation action passes (`.github/workflows/validate-skills.yml`).

---

## Development Setup

```bash
# Clone the repository
git clone https://github.com/Orphic-Studios/erpnext-agent-skills.git
cd erpnext-agent-skills

# Install development dependencies
pip install -r requirements.txt
```

---

## Questions and Support
Feel free to open an issue or reach out to the maintainers at Orphic Studios.
