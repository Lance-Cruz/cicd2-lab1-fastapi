# CICD-2 FastAPI Lab 3

This repository contains a FastAPI lab for the CICD-2 module.  

---

## Lab 3 — FastAPI + SQLAlchemy + SQLite

This lab replaces the in-memory Python list with a real SQLite database.

---
## Repository Structure

```text
cicd2-lab1-fastapi/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│ 
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── tests/
│   ├── conftest.py
│   ├── test_health.py
│   └── test_users.py
│
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```