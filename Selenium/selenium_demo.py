from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

input_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "kw"))
)

input_box.send_keys("pytest selenium page object")

search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "su"))
)

search_button.click()

input("按回车结束...")

driver.quit()