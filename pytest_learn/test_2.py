import pytest

@pytest.fixture()
def login():
    print("this is login fixture")
    user = "chen"
    pwd = 123456
    return user, pwd

def test_login(login):
    """将fixture修饰的login函数作为参数传递给本用例"""
    print(login)
    assert login[0] == "chen"
    assert login[1] == 123456
    assert "chen" in str(login)