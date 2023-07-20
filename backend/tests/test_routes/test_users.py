import json

def test_create_user(client):
    data = {"username":"testusername", "email":"test@test.com","password":"12345"}
    response = client.post("/users/", json = data)
    assert response.status_code == 200