from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/dynamic.html")

wait = WebDriverWait(driver, 10)

driver.find_element(By.ID, "reveal").click()

element = wait.until(
    EC.presence_of_element_located(
        (By.ID, "revealed")
    )
)

print("找到元素了")

print("是否显示：", element.is_displayed())

input("按回车结束...")