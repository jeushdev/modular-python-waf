# modular-python-waf

> An Object-Oriented Application Security Microservice — polymorphic regex threat defense + a live interactive SOC analytics sandbox.  
> Intercepts attacks at the network boundary. Normalizes payloads. Maps analytics instantly.

---

## The Defenses

### 🛡️ Polymorphic Threat Engine

Evaluates Layer-7 HTTP request parameters against pluggable signature sets (SQLi & XSS) via strict abstract contracts (`BaseRule`). Satisfies the Open/Closed Principle — new protection filters can be added without altering the core execution pipeline.

* **Anti-Evasion Normalization:** Automatically decodes nested percent-encoding values inside an immutable Request Context DTO *before* analysis, neutralizing impedance-mismatch bypass vectors.
* **Granular Exception Bubbling:** Uses a custom `MaliciousRequestException` lifecycle to pass rule names, attack severity markers, and raw forensic payloads straight up the execution stack.

### 📊 SOC Analytics Dashboard & Sandbox

A dual-purpose web portal featuring a secure administrative telemetry interface and a click-to-attack simulation panel.

```text
[ Attacker Payload ] ──► [ Decoding Context DTO ] ──► [ Polymorphic Rules Engine ] ──► [ Volatile RAM Store ] ──► [ Visual Dashboard UI ]

```

* **Interactive Testing Sandbox (`/`):** Pre-built attack buttons execute packaged SQLi and XSS payloads, dropping malicious clients into immediate `403 Forbidden` wall states with a single click.
* **Real-Time SOC Monitor (`/admin/dashboard`):** Reads security forensics directly out of a thread-safe, volatile RAM data warehouse list to populate an analytical grid instantaneously with zero disk-I/O overhead.

---

## System Architecture Layout

```text
modular-python-waf/
├── app/
│   ├── routes.py            # Sandbox Testing Nodes & SOC Dashboard Gateways
│   ├── templates/           # Jinja2 Dark-Mode Dark Web Panel Interface Templates
│   └── waf/
│       ├── engine.py        # Core Polymorphic Validation Engine
│       ├── middleware.py    # Request Interception Triage Gate & Exception Catching
│       ├── telemetry.py     # Volatile RAM Security Incident Datastore Warehouse
│       └── models/
│           ├── base_rule.py       # Abstract Base Rule Class Blueprint
│           └── request_context.py # Normalization DTO Layer
└── tests/                   # Automated Pytest Adversarial Regression Suites

```

---

## Stack

| Layer | Component Technology |
| --- | --- |
| Core Backend Engine | Python 3 / Flask Microframework / Blueprint Routing |
| Container DevOps | Docker (Linux Environment Containerization) |
| Security Operations | Native Regex (`re`) Compiler Rules Factory |
| Presentation Layer | HTML5 / CSS3 / Jinja2 Analytics Data Pipelines |
| Quality Assurance | Pytest Automation (Mock Request Interceptions) |

---

## Deployment & Verification Sandbox

This microservice is completely containerized. Ensure you have **Docker Desktop** running, then execute these commands sequentially in your local terminal:

```bash
# 1. Clone and enter the repository environment
git clone [https://github.com/jeushdev/modular-python-waf.git](https://github.com/jeushdev/modular-python-waf.git)
cd modular-python-waf

# 2. Compile the production container blueprint
docker build -t ironclad-waf-engine .

# 3. Boot the live secure microservice gateway
docker run -p 5000:5000 ironclad-waf-engine

```

Now, navigate to `http://127.0.0.1:5000/` to open the attack simulator pad, launch a payload node, and refresh the dashboard to watch your security data live stream!

---

> ⚠️ Production architecture configured inside a decoupled microservice structure. Volatile telemetry logs reset cleanly on container restart.


## 👤 Author

* **Jeush Samuel L. Bantayaon** - Computer Science Student
* **Connect:** https://www.linkedin.com/in/jeush-samuel-bantayaon-2ab40b370/

```

