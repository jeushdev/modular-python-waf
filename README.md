# Ironclad WAF Engine: Object-Oriented Web Application Firewall & SOC Sandbox

A highly modular, production-grade Web Application Firewall (WAF) microservice built from scratch using strict **Object-Oriented Design Principles (SOLID)**. This system normalizes incoming HTTP traffic, executes polymorphic rule checking, and pipes real-time security telemetry to an interactive Security Operations Center (SOC) visual dashboard. The entire application is fully containerized for frictionless cloud deployment.

## 🚀 Architectural Key Features

* **Polymorphic Rule Set Architecture:** Built on top of abstract structural contracts (`BaseRule`). Adding new security pattern filters (e.g., SQLi, XSS, Path Traversal) requires zero modification to the core execution engine, satisfying the Open/Closed Principle.
* **Impedance Mismatch Mitigation:** Implements an immutable Request Context Data Transfer Object (DTO) that automatically decodes and normalizes nested URL-percent encodings *before* structural pattern inspection runs, preventing evasion bypass tactics.
* **Granular Perimeter Auditing:** Leverages custom exception bubbling (`MaliciousRequestException`) to pass rich threat metadata—including rule identifiers, severity matrix markers, and raw offending string payloads—up the execution stack.
* **Volatile RAM Telemetry Stream:** Features a thread-safe, in-memory logging database warehouse to capture forensic payloads with zero disk-I/O overhead, updating the monitoring panel in real-time.
* **Interactive Threat Simulation Sandbox:** Includes a web-based testing playground containing pre-built, click-to-attack scenario nodes, allowing anyone to safely simulate and audit cyberattack vectors with a single click.

---

## 🛠️ System Architecture Directory Layout

```text
modular-python-waf/
├── app/
│   ├── routes.py            # Sandbox Playground & Admin Dashboard Blueprint Routes
│   ├── templates/
│   │   ├── index.html       # Click-to-Attack Simulation Interface Frontend
│   │   └── dashboard.html   # Real-Time Security Operations Center (SOC) Data Grid
│   └── waf/
│       ├── engine.py        # Core Polymorphic Validation & Rules Factory Engine
│       ├── middleware.py    # Request Interception Triage Gate & Exception Handler
│       ├── telemetry.py     # Volatile RAM Security Incident Datastore
│       ├── exceptions.py    # Custom Forensic Security Exception Definitions
│       └── models/
│           ├── base_rule.py       # Abstract Base Rule Class Contract
│           ├── request_context.py # Normalization DTO Layer
│           └── rules.py           # Concrete SQLi and XSS Custom Rule Filters
├── Dockerfile               # Production Container Environment Recipe
├── requirements.txt         # Hardened System Dependency Constraints
└── tests/                   # Automated Pytest Adversarial Regression Suites

```

---

## 📦 Tech Stack

* **Backend Engine:** Python 3 (Flask Microframework)
* **DevOps Environment:** Docker (Linux Containerization Layer)
* **Frontend Design:** HTML5 / CSS3 (Dark-Mode UI) / Jinja2 Templating
* **Testing Infrastructure:** Pytest (Adversarial Simulation Assertions)

---

## ⚙️ Installation & Single-Command Deployment

This project is completely containerized. Ensure you have **Docker Desktop** installed and running on your machine, then execute these commands in your terminal:

### 1. Clone the Environment

```bash
git clone [https://github.com/jeushdev/modular-python-waf.git](https://github.com/jeushdev/modular-python-waf.git)
cd modular-python-waf

```

### 2. Build the Production Container Box

```bash
docker build -t ironclad-waf-engine .

```

### 3. Boot the Secure Microservice Gateway

```bash
docker run -p 5000:5000 ironclad-waf-engine

```

The application environment will instantly spin up live at: `http://127.0.0.1:5000/`

---

## 🔒 Interactive Security Verification Scenarios

Once the container boots, open `http://127.0.0.1:5000/` in your browser to access the **Simulation Playground**. You can trigger these explicit test vectors:

1. **Scenario A: Normal User Verification**
* **Action:** Click "Launch Clean Request" (Sends `username=goodcitizen`).
* **Result:** Passes through transparently. Returns an HTTP `200 OK` success message.


2. **Scenario B: SQL Injection (SQLi) Mitigation**
* **Action:** Click "Launch SQLi Attack" (Sends `username=admin' OR 1=1 --`).
* **Result:** WAF interceptor triggers `SQL Injection Engine` rule, drops the connection with an HTTP `403 Forbidden` block, and logs the forensic anomaly data.


3. **Scenario C: Cross-Site Scripting (XSS) Mitigation**
* **Action:** Click "Launch XSS Attack" (Sends code containing `<script>`).
* **Result:** WAF interceptor captures HTML injection boundaries, drops the request context with an HTTP `403 Forbidden`, and increments the global telemetry threshold clock.



*Click the blue **Open SOC Admin Dashboard** link at the bottom of the playground to view your captured real-time security incident matrix table layout.*

---

## 👤 Author

* **Jeush Samuel L. Bantayaon** - Computer Science Student
* **Connect:** https://www.linkedin.com/in/jeush-samuel-bantayaon-2ab40b370/

```

