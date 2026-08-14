# Northstar Retail Co. - Support Deflection MVP

An automated, self-serve customer support dashboard designed to deflect repetitive support tickets for Northstar Retail Co. This MVP reduces manual ticket handling across order status tracking, returns/refund processing and stock availability queries.

---

## 1. Project Context & Objectives
Northstar Retail Co. is a mid-size e-commerce business whose support team is overwhelmed by repetitive customer inquiries. Built for the 1MILL Devs Evaluation Phase under Power Learn Project Africa, this repository contains a 1-week industry simulation MVP engineered to automate support resolutions before a ticket is ever created.

### Ticket Categories Handled:
1. **Order Status:** "Where is my order?" / "Has this shipped yet?"
2. **Returns & Refunds:** "How do I return this?" / "When will I get my refund?"
3. **Stock Availability:** "Is this back in stock?" / "Do you have this in another size?"

---

## 2. Tech Stack & Architecture
* **Frontend:** Native HTML5, CSS3 and JavaScript (ES6 Fetch API)
* **Backend:** Python 3.10+ and FastAPI framework
* **Database:** SQLite 3 with custom mock data seeding script
* **Governance & Audit:** Git, GitHub Projects, Branch Protection Rules and Audit Logs

---

## 3. Team Roster & Role Distribution
Built by a 5-person engineering pod adhering to strict agile and version control workflows:

* **Jesse Vincent (`jdilemmax`):** Team Lead & Backend Lead (Order Status API, System Architecture, Repository Governance & Documentation)
* **Silvya Atieno (`oswaldsly`):** Frontend Engineer (Form Components, UI Layout & User Error Handling)
* **Peter Kuria (`peakaykush`):** Frontend Engineer (UI/UX Styling, Responsive Layout & API Integration)
* **Aphane Ginah (`ginahAphane`):** Database Specialist (SQLite Schema Design, Data Modeling & Mock Data Seed Scripting)
* **Ahmed Abdi Ibrahim (`ahmedabdy590-spec`):** Backend Engineer (FastAPI Skeleton, Returns API & Stock Availability API)

---

## 4. Repository Directory Structure
```text
northstar-support-dashboard/
│
├── frontend/                  # Assigned to Silvya Atieno & Peter Kuria
│   ├── index.html             # Self-serve dashboard layout & query forms
│   ├── styles.css             # Responsive styling & CSS animations
│   └── app.js                 # JS event listeners & API fetch requests
│
├── backend/                   # Assigned to Jesse Vincent & Ahmed Abdi Ibrahim
│   ├── main.py                # FastAPI routes, CORS middleware & app entry point
│   ├── database.py            # SQLite database connection & helper functions
│   └── models.py              # Data response schemas & Pydantic models
│
├── data/                      # Assigned to Aphane Ginah
│   ├── schema.sql             # Relational table definitions for orders, returns & stock
│   ├── seed.py                # Python script to populate 15+ mock records
│   └── northstar.db           # Local SQLite database instance
│
├── docs/                      # Documentation
│   ├── CHARTER.md             # Team Working Agreement & Rules
│   ├── CONTRIBUTING.md        # Git branching, PR workflow & commit standards
│   └── GOLIVE.md              # 1-Page Go-Live Readiness Note
├── README.md                  # Main project documentation & setup guide
├── requirements.txt           # Backend dependencies (fastapi, uvicorn)
└── .gitignore                 # Excludes cache files, db locks & virtual environments
```

---

## 5. Local Setup & Running Instructions

### Prerequisites:
* Python 3.10 or higher installed
* A modern web browser (Chrome, Firefox, Safari or Edge)

### Step 1: Clone the Repository
```bash
git clone https://github.com/JDILEMMAX/northstar-support-dashboard.git
cd northstar-support-dashboard
```

### Step 2: Set Up Backend & Database
1. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the database seed script to generate mock records:
   ```bash
   python data/seed.py
   ```
3. Start the FastAPI backend server:
   ```bash
   uvicorn backend.main:app --reload
   ```
   The backend API server will be live at `http://127.0.0.1:8000`. You can inspect interactive API docs at `http://127.0.0.1:8000/docs`.

### Step 3: Launch the Frontend
Open `frontend/index.html` directly in your web browser or serve it using a local server extension such as Live Server in VS Code.

---

## 6. Process Discipline & Governance
* **Team Working Agreement:** Review team norms, escalation paths and standup rules in [`docs/CHARTER.md`](./docs/CHARTER.md).
* **Git Guidelines:** All contributors must adhere to the branch naming and commit conventions in [`docs/CONTRIBUTING.md`](./docs/CONTRIBUTING.md).
* **Handover & Go-Live Note:** Comprehensive status report on working features, known issues and handover requirements is detailed in [`docs/GOLIVE.md`](./docs/GOLIVE.md).