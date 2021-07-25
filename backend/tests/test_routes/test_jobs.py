import json


def test_create_job(client, normal_user_token_headers):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "doodle",
        "company_url": "https://www.fdj.com",
        "location": "USA, NY",
        "description": "Testing",
        "date_posted": "2022-07-22"
    }

    response = client.post("/job/create-job", data=json.dumps(data), headers=normal_user_token_headers)
    assert response.status_code == 200
    assert response.json()["company"]=="doodle"
    assert response.json()["description"]=="Testing"


def test_retreive_job_by_id(client, normal_user_token_headers):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "testhoo",
        "company_url": "https://www.fdj.com",
        "location": "USA, NY",
        "description": "Testing",
        "date_posted": "2022-07-22"
    }

    response = client.post("/job/create-job", json.dumps(data), headers=normal_user_token_headers)
    assert response.json()["title"] == "SDE 1 Yahoo"
    response = client.get("/job/get/1")
    assert response.status_code == 200
    assert response.json()["title"] == "SDE 1 Yahoo"

