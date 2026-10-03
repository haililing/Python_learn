import pytest


@pytest.fixture
def user():
    print("\n 准备")
    data = {
        "name" : "Akiha",
        "age" : 21
    }

    return data

def test_user_name(user):
    assert user["name"] == "Akiha"