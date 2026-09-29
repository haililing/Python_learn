import pytest


def test_return_list(api_client):
    assert isinstance(api_client.get_users().json(), list)

def test_return_length(api_client):
    response = api_client.get_users()
    print(len(response.json()))
    assert len(response.json())>0

@pytest.mark.parametrize("user_id",[1,2,3,5])
def test_get_user(api_client,user_id):
    response = api_client.get_user(user_id)

    assert response.status_code == 200
    assert response.json()["id"] == user_id

def test_post(api_client):
    data = {
        "title": "pytest practice",
        "body": "hello api",
        "userId": 1
    }
    response = api_client.create_post(data)
    assert response.status_code == 201
    assert response.json()["title"] == data["title"]
    assert response.json()["body"] == data["body"]
    assert response.json()["userId"] == data["userId"]

def test_get_nonexistent_user(api_client):
    response = api_client.get_user(999)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 404