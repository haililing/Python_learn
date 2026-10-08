from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/iframes.html")

iframe = driver.find_element(By.ID,"iframe1")

driver.switch_to.frame(iframe)

email = driver.find_element(By.ID,"email")

email.send_keys("hello")

input()