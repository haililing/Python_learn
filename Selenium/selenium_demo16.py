import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

TEST_CASES = [
    ("tomsmith","SuperSecretPassword!","You logged into a secure area!","/secure"),
    ("admin","SuperSecretPassword!","Your username is invalid!","/login"),
    ("tomsmith","123456","Your password is invalid!","/login"),
]

@pytest.mark.parametrize("username,password,expected,url", TEST_CASES)
def test_login(driver,username,password,expected,url):
    driver.get("https://the-internet.herokuapp.com/login")
    usernames = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(
            (By.ID,"username")
        )
    )
    usernames.clear()
    usernames.send_keys(username)
    passwords = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(
            (By.ID,"password")
        )
    )
    passwords.clear()
    passwords.send_keys(password)

    btn = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[type="submit"]')
        )
    )
    btn.click()

    message = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located(
            (By.ID,"flash")
        )
    )
    assert expected in message.text

    expected_url = "https://the-internet.herokuapp.com" + url
    WebDriverWait(driver,10).until(
        EC.url_to_be(expected_url)
    )