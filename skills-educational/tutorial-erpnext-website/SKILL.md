---
name: tutorial-erpnext-website
description: Educational and trainer skill for ERPNext v15 Website module. Use when generating webmaster training lessons, portal onboarding, content publishing tutorials, web form creation walkthroughs, and website management quizzes.
---

# ERPNext v15 Website Training & Tutorial Skill

## 1. Instructional Objectives & Pedagogy
- **Target Audience**: Webmasters, Content Creators, Digital Marketers, and Portal Administrators.
- **Learning Outcomes**:
  - Build and publish responsive Web Pages and Blog Posts using Markdown and HTML.
  - Deploy public intake Web Forms mapped directly to ERPNext DocTypes.
  - Configure the self-service Customer and Supplier Portals.

---

## 2. Structured Curriculum & Lesson Plans

### Lesson 1: Publishing Web Pages & Blogs
- Setting up routes, page titles, and meta descriptions for SEO.
- Embedding rich media, images, and Markdown styling.

### Lesson 2: Interactive Web Forms
- Generating a public intake form (e.g., "Contact Us" or "Vendor Application").
- Testing field validations and verifying automatic record creation in ERPNext.

---

## 3. Real-World Hands-on Scenario
**Scenario**: "The marketing department needs a public Web Form on route `/apply-distributor` that creates a new Lead with source set to 'Distributor Form'."
- **Task for Learner**:
  1. Create a `Web Form` linked to DocType `Lead`.
  2. Select fields: Name, Email, Phone, Annual Turnover.
  3. Publish the form and submit a test record from an incognito window.

---

## 4. End-of-Module Quiz & Assessment
1. *Can an unauthenticated guest user submit a Web Form?*
   - [ ] No, they must always register.
   - [x] Yes, if the Web Form has "Allow Guest" enabled.
