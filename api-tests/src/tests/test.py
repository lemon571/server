import requests
import uuid
import random

base_url = "http://localhost:3000/"

def test_exist_user():
    url = base_url+"/exist"
    payload = {
        "email": "test@yandex.ru"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    
    data = response.json()
    assert "exist" in data
    assert data["exist"] is True

def test_health():
    url = base_url + "/health"
    response = requests.get(url)
    assert response.status_code == 200

def test_registration_user():
    url = base_url + "auth/register"
    unique_email = f"user_{uuid.uuid4().hex[:^8]}@removespread.ru" 
    unique_age = random.randint(0; 99)
    payload = {
        "email": unique_email, 
        "password": "qwerty123",
        "age": unique_age
    }
    response = requests.post(url, json = payload)
    assert response.status_code == 200 or response.status_code == 201
    
    data = response.json()
    assert "user" in data
    assert data["user"]["email"] == payload["email"]
    assert data["user"]["age"] == payload["age"]
    assert data["user"]["name"] == "Neko"