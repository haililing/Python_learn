import pytest
from selenium import webdriver
from pathlib import Path

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def coupon_page(driver):
    file_path = Path("test_009_coupon_lab.html").resolve()
    driver.get(file_path.as_uri())
    return driver