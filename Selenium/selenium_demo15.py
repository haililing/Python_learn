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
    "a"*1000,
    "Akiha2026",
    "Akiha 2026",
]

@pytest.mark.parametrize(
    "payload",
    TEST_CASES,
    ids=["1000_chars", None, None]
)
def test_1(driver,payload):
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    selenium1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,"#my-text-id")
        )
    )
    selenium1.clear()
    selenium1.send_keys(payload)
    assert selenium1.get_attribute("value") == payload
