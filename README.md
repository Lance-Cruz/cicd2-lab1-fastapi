# CICD-2 FastAPI Lab 5

This repository contains a FastAPI lab for the CICD-2 module.  

---

## Lab 5 — Two FastAPI Microservices with HTTPX

This lab adds a separate Product Service and allows the main User API to call it using HTTPX.

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
│   ├── product_client.py
│   └── schemas.py
│
├── tests/
│   ├── conftest.py
│   ├── test_health.py
│   ├── test_remote_products.py
│   └── test_users.py
│
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---
## Running Both Services in Codespaces

The two FastAPI services should be run at the same time using two seperate terminals.

### Terminal 1 - Main Service

Start the main FastAPI application:
```
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
This runs the main service on port 8000.

### Terminal 2 - Product Service

Open a second terminal in Codepsaces and start the Product Service:
```
python -m uvicorn product_service.main:app --host 0.0.0.0 --port 8001 --reload
```
This runs the product service on port 8001.

The main User API uses PRODUCT_SERVICE_URL to know where the Product Service is running. When running both services in Codespaces, the Product Service run on port 8001, so the URL points to that service.

The Product Service has a GET endpoint:
```
GET /api/products/{product_id}
```
This endpoint is used to retrieve a product by its ID.