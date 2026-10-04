from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

input_box = driver.find_element(By.ID, "chat-textarea")

input_box.send_keys("pytest selenium page object")

input("按回车结束...")

driver.quit()