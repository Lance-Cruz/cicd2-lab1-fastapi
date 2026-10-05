# CICD-2 FastAPI Lab 2

This repository contains a FastAPI lab for the CICD-2 module.  

---

## Lab 2 — FastAPI Testing, Coverage, and CI

This lab adds automated testing to our FastAPI endpoints with pytest, coverage reporting, and a GitHub Actions CI workflow

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
│   ├── main.py
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