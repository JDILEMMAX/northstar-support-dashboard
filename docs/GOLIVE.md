# Northstar Retail Co. - Go-Live Readiness Note

**Document Purpose:** This 1-page readiness note details system capabilities, known edge cases and handover instructions to allow Northstar Retail Co.'s internal engineering team to take full ownership of the Support Deflection MVP without our development pod in the room.

---

## 1. Executive Summary
The Support Deflection MVP is an automated self-serve dashboard designed to reduce manual support ticket volume. Built using FastAPI, SQLite and vanilla JavaScript, the system processes customer queries directly to deflect tickets across three high-volume support categories: order status tracking, return/refund inquiries and stock availability checks.

---

## 2. What Works (Fully Functional Capabilities)

All 3 ticket deflection workflows are 100% operational and verified by automated test outputs.

| Category | Capability | Expected Behavior |
| :--- | :--- | :--- |
| **Order Status** | Self-serve Order Lookup | Customers enter an Order ID to retrieve real-time shipping status and carrier tracking links. |
| **Returns & Refunds** | Return Progress Tracking | Customers submit an Order ID to check return approval status and reasons. |
| **Stock Availability** | SKU Availability Search | Customers search products by SKU to check real-time inventory counts. |
| **User Interface** | Responsive Self-Serve Dashboard | Clean single-page web dashboard with visual feedback indicators and inline error handling. |
| **Backend Core** | RESTful FastAPI Endpoints | Structured API endpoints returning JSON responses with proper HTTP status codes. |

---

## 3. Known Limitations & Known-Broken Edge Cases
The prototype proves operational feasibility but contains known scope boundaries expected of a 1-week MVP:

* **Authentication & Session Persistence:** The MVP does not currently feature user login or OAuth2. Customer identity is validated solely via exact Order ID input.
* **Mock Carrier Webhooks:** Order status updates rely on seeded SQLite database records rather than live real-time webhooks from shipping carriers.
* **Multi-Item Return Selection:** The returns portal assumes an order level return status query. Partial line-item return processing requires backend model expansion.
* **API Rate Limiting:** Rate limiting middleware is not configured. High query volumes could impact database throughput in production.

---

## 4. Handover & Operational Takeover Guide
To transition this MVP into Northstar Retail Co.'s live production environment, Northstar's internal engineering team should execute the following steps:

### Step 1: Database Production Migration
* Replace the SQLite database (`data/northstar.db`) with Northstar's enterprise database instance (PostgreSQL or MySQL).
* Update `backend/database.py` connection strings to point to live production database credentials stored in environment variables.

### Step 2: Environment Configuration
* Create a `.env` file in the root directory using the following keys:
  ```text
  DATABASE_URL=postgresql://user:password@localhost:5432/northstar_db
  ALLOWED_ORIGINS=https://support.northstarretail.com
  ENVIRONMENT=production
  ```

### Step 3: Frontend Integration
* Embed `frontend/index.html` components into Northstar's existing customer portal or deploy as a standalone web application hosted on your CDN.
* Update `API_BASE_URL` in `frontend/app.js` from `http://127.0.0.1:8000` to your production API domain.

---

## 5. Maintenance Contact & Pod Sign-off
This MVP and natural paper trail have been prepared and audited by the 1MILL Devs Pod:

* **Jesse Vincent (`jdilemmax`)** - Team Lead & Backend Lead
* **Silvya Atieno (`oswaldsly`)** - Frontend Engineer
* **Peter Kuria (`peakaykush`)** - Frontend Engineer
* **Aphane Ginah (`ginahAphane`)** - Database Specialist
* **Ahmed Abdi Ibrahim (`ahmedabdy590-spec`)** - Backend Engineer