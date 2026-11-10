# CICD-2 FastAPI Lab 6

This repository contains a FastAPI lab for the CICD-2 module.  

---

## Lab 6 — Containerising Microservices with Docker Compose and GHCR

This lab containerise both microservices, connects them using Docker Compose, and publish both images to GitHub Container Registry 

---
## Repository Structure

```text
cicd2-lab1-fastapi/
│
├── .github/
│   └── workflows/
│       ├── build-push-images.yml
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
├── product_service/
│   ├── __init__.py
│   └── main.py
│   
├── tests/
│   ├── conftest.py
│   ├── test_health.py
│   ├── test_remote_products.py
│   └── test_users.py
│
├── .dockerignore
├── .gitignore
├── Dockerfile.product
├── Dockerfile.user
├── README.md
├── compose.yaml
├── pytest.ini
└── requirements.txt
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

---
### Running Docker Compose
---
```
docker compose config
docker compose up --build -d
docker compose ps
curl -i http://127.0.0.1:8001/products/1
curl -i http://127.0.0.1:8000/api/products/1
```