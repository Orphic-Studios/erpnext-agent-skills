---
name: tutorial-erpnext-assets
description: Educational and trainer skill for ERPNext v15 Assets module. Use when generating fixed asset training lessons, accountant asset onboarding, depreciation schedule walkthroughs, repair and maintenance tutorials, and asset disposal quizzes.
---

# ERPNext v15 Assets Training & Tutorial Skill

## 1. Instructional Objectives & Pedagogy
- **Target Audience**: Fixed Asset Accountants, Facility Managers, Maintenance Engineers, and Compliance Auditors.
- **Learning Outcomes**:
  - Understand Capital Expenditure (CapEx) tracking from Purchase Receipt to Asset registration.
  - Set up Asset Categories and configure Straight Line vs Written Down Value depreciation.
  - Manage scheduled maintenance and process asset scrapping/disposal.

---

## 2. Structured Curriculum & Lesson Plans

### Lesson 1: Registering Fixed Assets
- **Asset Categories**: Setting up Asset Account, Accumulated Depreciation Account, and Depreciation Expense Account.
- **Asset Creation**: Purchasing an asset via Purchase Receipt vs creating an existing opening asset.

### Lesson 2: Depreciation Schedules & Automation
- **Depreciation Methods**: Calculating periodic charges across asset useful life.
- **Automated Bookkeeping**: Reviewing auto-generated Journal Entries on monthly depreciation runs.

### Lesson 3: Maintenance & Disposal
- Logging preventative maintenance visits and emergency repairs.
- Scrapping a damaged asset and recognizing loss on disposal in P&L.

---

## 3. Real-World Hands-on Scenario
**Scenario**: "The company purchases a company delivery van for $36,000. It has an estimated useful life of 5 years (60 months) and a salvage value of $3,000. Use straight-line depreciation."
- **Task for Learner**:
  1. Create the Asset record with `calculate_depreciation=1`.
  2. Inspect the auto-generated 60-month depreciation schedule.
  3. Verify the monthly depreciation charge equals ($36,000 - $3,000) / 60 = $550/month.

---

## 4. End-of-Module Quiz & Assessment
1. *What account is credited when an automated depreciation journal entry is posted?*
   - [ ] Fixed Asset Account directly.
   - [x] Accumulated Depreciation Account (contra-asset).
