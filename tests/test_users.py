def user_payload(
    uid=1,
    name="Lance",
    email="lance@atu.ie",
    age=21,
    student_id="S1234567"
):

    return {
        "user_id": uid,
        "name": name,
        "email": email,
        "age": age,
        "student_id": student_id,
    }

def test_create_user_returns_201(client):
    response = client.post("/api/users", json=user_payload())

    assert response.status_code == 201
    data = response.json()
    assert data["user_id"] == 1
    assert data["name"] == "Lance"
    assert data["email"] == "lance@atu.ie"
    assert data["age"] == 21
    assert data["student_id"] == "S1234567"