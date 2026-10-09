from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_input_value():
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        element1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "my-text-id"))
        )
        element1.send_keys("Akiha2026")
        assert "Akiha2025" == element1.get_attribute("value")
    finally:
        driver.quit()