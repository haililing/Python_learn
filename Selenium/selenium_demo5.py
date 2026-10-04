from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(
    "https://www.selenium.dev/selenium/web/web-form.html"
)

text_box = driver.find_element(By.XPATH, '//input[@name="my-text"]')
text_box.send_keys("selenium locator test")

password_box = driver.find_element(By.XPATH,'//input[@name="my-password"]')
password_box.send_keys("123456")

driver.find_element(By.XPATH,"//button").click()

driver.implicitly_wait(0.5)

message = driver.find_element(By.XPATH,'//p[@id="message"]')
print(message.text)

input("按回车关闭...")
driver.quit()