import pytest
from dsa_prereq_lab import create_app

@pytest.fixture()
def client():
    app = create_app({"TESTING": True})
    return app.test_client()

def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"DSA Launchpad" in response.data

def test_complexity_api(client):
    response = client.get("/api/complexity?kind=linear&n=20")
    payload = response.get_json()
    assert response.status_code == 200
    assert payload["operations"] == 20

def test_factorial_api(client):
    response = client.get("/api/recursion/factorial?value=4")
    assert response.get_json()["result"] == 24

def test_quiz_api(client):
    response = client.post("/api/quiz/check", json={
        "answers": {
            "q1": "O(1)",
            "q2": "base-case",
            "q3": "dict",
            "q4": "alias",
            "q5": "O(n)",
        }
    })
    assert response.get_json()["score"] == 5
