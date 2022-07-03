from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_telephone_banking():
    response = client.get("/telephone-banking")
    assert response.status_code == 200
    assert response.json()["statusCode"] == 200
    assert response.json()["statusText"] == "Telephone Banking FAQ Fetch Successful"
    assert len(response.json()["questions"]) == len(response.json()["answers"])


def test_get_mobile_banking():
    response = client.get("/mobile-banking")
    assert response.status_code == 200
    assert response.json()["statusCode"] == 200
    assert response.json()["statusText"] == "Mobile Banking FAQ Fetch Successful"
    assert len(response.json()["questions"]) == len(response.json()["answers"])


def test_get_internet_banking():
    response = client.get("/internet-banking")
    assert response.status_code == 200
    assert response.json()["statusCode"] == 200
    assert response.json()["statusText"] == "Internet Banking FAQ Fetch Successful"
    assert len(response.json()["questions"]) == len(response.json()["answers"])
