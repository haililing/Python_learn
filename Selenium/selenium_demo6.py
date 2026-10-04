from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)

driver.get(
    "https://www.selenium.dev/selenium/web/web-form.html"
)

text_box = driver.find_element(
    By.NAME,
    "my-text"
)

text_box.send_keys("first")

check_box = driver.find_element(By.CSS_SELECTOR, '[type="checkbox"][name="my-check"]')

print("第一次：")
print(text_box.get_attribute("value"))

text_box.clear()

text_box.send_keys("selenium")

print("第二次：")
print(text_box.get_attribute("value"))

print("是否显示：")
print(text_box.is_displayed())

print("是否启用：")
print(text_box.is_enabled())

print("标签：")
print(text_box.tag_name)

print("复选框:")
print(check_box.is_selected())

check_box.click()

print("复选框:")
print(check_box.is_selected())

input("按回车关闭...")
driver.quit()