import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_create_post():
    payload = {
        "title": "Тестовый пост",
        "body": "Это тело поста",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data  # API возвращает созданный ID


def test_update_post():
    updated_payload = {
        "id": 1,
        "title": "Обновлённый заголовок",
        "body": "Обновлённое тело",
        "userId": 1
    }

    response = requests.put(f"{BASE_URL}/posts/1", json=updated_payload)

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == updated_payload["title"]
    assert data["body"] == updated_payload["body"]
    assert data["id"] == updated_payload["id"]


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
    assert response.text == "{}"  # Пустой JSON в ответе
