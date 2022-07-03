from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["statusCode"] == 200
    assert response.json()["statusText"] == "Root Endpoint for ChatBot API"


def test_wakeup():
    response = client.get("/wakeup")
    assert response.status_code == 200
    assert response.json()["statusCode"] == 200
    assert response.json()["statusText"] == "API Wakeup Successful"


def test_chatbot_version():
    response = client.get("/chatbot-version")
    assert response.status_code == 200
    assert response.json()["statusCode"] == 200
    assert response.json()["statusText"] == "Chatbot Version Fetch Successful"
    assert response.json()["version"] == "0.0.1-alpha"


def test_telephone_banking():
    response = client.get("/telephone-banking")
    assert response.status_code == 200
    assert response.json()["statusCode"] == 200
    assert response.json()["statusText"] == "Telephone Banking FAQ Fetch Successful"
    assert len(response.json()["questions"]) == len(response.json()["answers"])


def test_mobile_banking():
    response = client.get("/mobile-banking")
    assert response.status_code == 200
    assert response.json()["statusCode"] == 200
    assert response.json()["statusText"] == "Mobile Banking FAQ Fetch Successful"
    assert len(response.json()["questions"]) == len(response.json()["answers"])


def test_internet_banking():
    response = client.get("/internet-banking")
    assert response.status_code == 200
    assert response.json()["statusCode"] == 200
    assert response.json()["statusText"] == "Internet Banking FAQ Fetch Successful"
    assert len(response.json()["questions"]) == len(response.json()["answers"])
