import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "payload",
    ["Akiha2026", "Akiha 2026", "a" * 1000]
)
def test_text_input(browser, payload):
    browser.get(
        "https://www.selenium.dev/selenium/web/web-form.html"
    )

    element = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(
            (By.ID, "my-text-id")
        )
    )

    element.clear()
    element.send_keys(payload)

    assert element.get_attribute("value") == payload
