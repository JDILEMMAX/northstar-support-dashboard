# Repository Contribution Guidelines

To maintain code quality, ensure seamless collaboration and pass Northstar Retail Co.'s strict procurement audit, all contributors must adhere to these repository hygiene guidelines. Direct pushes to the `main` branch are disabled.

---

## 1. Branch Naming Conventions
Never work directly on the `main` branch. Always create a dedicated branch from `main` for your assigned task using the following prefix rules:

* **`feat/`** - New features, UI elements or backend endpoints.  
  *Example:* `feat/order-status-api`, `feat/dashboard-layout`
* **`fix/`** - Bug fixes or error resolution.  
  *Example:* `fix/search-button-alignment`, `fix/database-connection-timeout`
* **`docs/`** - Documentation updates or guide additions.  
  *Example:* `docs/update-charter`, `docs/contributing-guidelines`
* **`chore/`** - Setup, configuration or seed data scripts.  
  *Example:* `chore/sqlite-seed-script`, `chore/backend-dependencies`

---

## 2. Mandatory Commit Message Format
To satisfy procurement audit requirements, generic messages like "wip", "updates" or "fixed bug" are **strictly forbidden**. Every commit message must follow this exact format:

`<type>: <what changed> - <why it matters>`

### Allowed Types:
* `feat` - A new feature or user-facing functionality
* `fix` - A bug fix
* `docs` - Documentation changes only
* `style` - Formatting, missing semi-colons or UI aesthetic tweaks
* `refactor` - Code restructuring without changing functionality
* `chore` - Updating build tasks, packages or mock seed data

### Compliant Examples:
* `feat: add order status API endpoint - allows customers to query live shipping info`
* `fix: correct SQL search query string - prevents null response on missing order IDs`
* `docs: complete CONTRIBUTING guide - outlines PR and commit rules for the team`
* `chore: add 15 mock orders to seed script - provides test data for backend integration`

---

## 3. Pull Request (PR) Workflow
All changes enter `main` exclusively through Pull Requests. Follow this step-by-step process:

1. **Keep Branches Fresh:** Before starting work, pull the latest changes from `main` using `git pull origin main`.
2. **Create Your Feature Branch:** Run `git checkout -b feat/your-feature-name`.
3. **Commit Frequently:** Make small, clear commits using the mandatory commit message format above.
4. **Push Branch to GitHub:** Run `git push origin feat/your-feature-name`.
5. **Open a Pull Request:** Navigate to the repo on GitHub, click **Compare & pull request**.
6. **Link the Board Task:** In the PR description, link your board issue using keywords like `Closes #7` or `Resolves #3`. This automatically closes the board item when merged.
7. **Request a Review:** Tag at least one teammate or the Team Lead (`jdilemmax`) as a reviewer.
8. **Merge:** Once approved and conversation threads are resolved, merge your branch and delete the feature branch.

---

## 4. Board Status and Audit Trail
* **Same-Day Movement:** When you open a PR, move your assigned issue on the Project Board to **In Progress**. When the PR is merged, ensure the issue moves to **Done**.
* **Traceability:** Every pull request must map directly to an open issue on the project board. Unmapped code will fail the mid-sprint audit.