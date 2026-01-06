# AI-Powered Incident Response & Ticket Triage System

A backend system built with **FastAPI** and **SQLAlchemy** that simulates how real-world IT and SOC (Security Operations Center) teams handle support tickets, automatically triage them, and escalate serious issues into incidents.

This project was built incrementally to demonstrate **backend engineering fundamentals**, **clean architecture**, and **enterprise-style workflows**.

---

## 🚀 Features

* ✅ Ticket creation and retrieval (REST APIs)
* ✅ Input validation with Pydantic
* ✅ Persistent storage using SQLite + SQLAlchemy ORM
* ✅ Automatic ticket triage (category & priority assignment)
* ✅ Incident escalation for high-priority tickets
* ✅ Modular, scalable FastAPI architecture

---

## 🧠 System Overview

### Ticket Lifecycle

1. A user submits a ticket via the API
2. The system validates the input
3. Ticket content is analyzed automatically
4. Category and priority are assigned
5. High-priority tickets can be escalated into incidents

```
Ticket → Automated Triage → (Optional) Incident Escalation
```

---

## 🏗️ Project Structure

```
incident-response-ticketing-system/
│
├── app/
│   ├── api/            # API route definitions
│   │   ├── tickets.py
│   │   └── incidents.py
│   │
│   ├── models/         # Database models
│   │   ├── ticket.py
│   │   └── incident.py
│   │
│   ├── schemas/        # Pydantic schemas (validation)
│   │   ├── ticket.py
│   │   └── incident.py
│   │
│   ├── services/       # Business logic
│   │   └── triage.py
│   │
│   ├── database.py     # Database configuration
│   └── main.py         # Application entry point
│
├── .gitignore
├── README.md
└── incident_response.db (local only)
```

---

## ⚙️ Tech Stack

* **Python 3**
* **FastAPI** – REST API framework
* **SQLAlchemy** – ORM & database layer
* **SQLite** – Local development database
* **Pydantic** – Data validation
* **Uvicorn** – ASGI server

---

## ▶️ Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Ebun-25/incident-response-ticketing-system.git

cd incident-response-ticketing-system
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy
```

### 4. Start the server

```bash
python -m uvicorn app.main:app --reload
```

### 5. Open Swagger UI

Visit:

```
http://127.0.0.1:8000/docs
```

---

## 🔌 API Endpoints

### Tickets

* **POST /tickets** – Create a new ticket
* **GET /tickets** – Retrieve all tickets

Example request:

```json
{
  "title": "Cannot log in",
  "description": "User receives invalid password error"
}
```

---

### Incidents

* **POST /incidents/{ticket_id}** – Escalate a ticket into an incident

Incidents inherit severity from ticket priority and are tracked separately.

---

## 🧠 Automated Triage Logic

Tickets are classified using rule-based logic that analyzes keywords in the title and description:

* **Security** → High priority
* **Network** → Medium priority
* **Hardware** → Low priority
* **Software** → Low priority (default)

This logic is isolated in a service layer and can later be replaced with machine learning.

---

## 📌 Development Phases

* **Phase 1:** FastAPI project setup
* **Phase 2:** Database design & SQLAlchemy models
* **Phase 3:** Ticket APIs & persistence
* **Phase 4:** Automated classification & triage
* **Phase 5:** Incident escalation

---

## 🔮 Future Improvements

* User authentication & roles
* Audit logging
* SLA tracking & escalation rules
* Machine learning–based triage
* Frontend dashboard
* Dockerization & deployment

---

## 🧑‍💻 Author

Built as a portfolio project to demonstrate backend engineering, system design, and real-world problem modeling.

---

## 📄 License

This project is open for learning and demonstration purposes.
