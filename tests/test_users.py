import pytest
import requests
from env_config import Routes



user_data =\
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }


def test_create_user():
    # Отправка POST-запроса для создания нового пользователя
    response = requests.post(f"{Routes.BASE_URL}/users", json=user_data)

    # Проверка статуса ответа
    assert response.status_code == 200

    # Проверка содержимого ответа
    new_user = response.json()


def test_get_user():
    url = f"{Routes.BASE_URL}/user/1"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

def test_get_user_not_found():
    url = f"{Routes.BASE_URL}/user/999"
    response = requests.get(url)
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User not found"

def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

