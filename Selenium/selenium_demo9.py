from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

html_file = Path("wait_state_demo.html").resolve().as_uri()

driver.get(html_file)

wait = WebDriverWait(driver, 10)

driver.find_element(By.ID, "start").click()

wait.until(
    EC.text_to_be_present_in_element(
        (By.ID, "result"),
        "提交成功"
    )
)

print("检测到提交成功")

input("按回车结束...")