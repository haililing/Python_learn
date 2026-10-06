from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/dynamic.html")

driver.find_element(By.ID, "reveal").click()

wait = WebDriverWait(driver, 10)

input_box = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#revealed")
    )
)

input_box.send_keys("Hello Selenium")

input("按回车结束...")