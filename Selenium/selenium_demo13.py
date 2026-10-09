from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_input_value_and_submit():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        element1 = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable(
                (By.ID,"my-text-id")
            )
        )

        element1.send_keys("Akiha2026")
        element2 = driver.find_element(By.TAG_NAME,"button")
        element2.click()
        element3 = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable(
                (By.ID,"message")
            )
        )

        assert "Received!" == element3.text
    finally:
        driver.quit()