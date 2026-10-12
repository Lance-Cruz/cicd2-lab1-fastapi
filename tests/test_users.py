import pytest

def user_payload(
    name="Lance",
    email="lance@atu.ie",
    age=21,
    sid="S1234567"
):

    return {
        "name": name,
        "email": email,
        "age": age,
        "student_id": sid,
    }

def test_create_user_returns_201(client):
    response = client.post("/api/users", json=user_payload())

    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Lance"
    assert data["email"] == "lance@atu.ie"
    assert data["age"] == 21
    assert data["student_id"] == "S1234567"

def test_duplicate_user_returns_409(client):
    client.post("/api/users", json=user_payload())

    response = client.post(
        "/api/users",
        json=user_payload(),
    )

    assert response.status_code == 409
    assert "exists" in response.json()["detail"].lower()

@pytest.mark.parametrize(
    "bad_student_id",
    ["1234567", "s1234567", "S1234", "S12345678"],
)
def test_bad_student_id_returns_422(client, bad_student_id):
    response = client.post(
        "/api/users",
        json=user_payload(uid=2, student_id=bad_student_id),
    )

    assert response.status_code == 422

def test_get_users_returns_created_users(client):
    client.post("/api/users", json=user_payload())

    response = client.get("/api/users")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["id"] == 1
    assert data[0]["name"] == "Lance"

def test_get_existing_users_returns_200(client):
    created = client.post(
        "/api/users",
        json=user_payload(),
        ).json()

    user_id = created["id"]
    response = client.get(f"/api/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["email"] == "lance@atu.ie"

def test_get_missing_user_returns_404(client):
    response = client.get("/api/users/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_delete_user(client):
    created = client.post(
        "/api/users",
        json=user_payload(),
    ).json()

    user_id = created["id"]

    response = client.delete(f"/api/users/{user_id}")
    assert response.status_code == 204

    response = client.get(f"/api/users/{user_id}")
    assert response.status_code == 404


def test_deleted_missing_user_returns_404(client):
    response = client.delete("/api/users/21")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"