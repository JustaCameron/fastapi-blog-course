import json

def test_create_job(client):
    data = {
        "title":"Tester", 
        "company":"Test Corp",
        "company_url":"https://www.testcorp.com",
        "location":"somewhere street",
        "description":"Testing Stuff",
        "date_posted":"2023-07-04"
    }
    response = client.post("/job/create-job", json = data)
    assert response.status_code == 200

def test_retrieve_job_by_id(client):
    data = {
        "title":"Tester", 
        "company":"Test Corp",
        "company_url":"https://www.testcorp.com",
        "location":"somewhere street",
        "description":"Testing Stuff",
        "date_posted":"2023-07-04"
    }
    client.post("/job/create-job", json = data)
    response = client.get("/job/get/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Tester"