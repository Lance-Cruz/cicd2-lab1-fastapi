# CICD-2 FastAPI Lab 4

This repository contains a FastAPI lab for the CICD-2 module.  

---

## Lab 4 — Testing a Database-backed API

This lab repairs and extends the automated tests so that pytest uses its own isolated database 

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