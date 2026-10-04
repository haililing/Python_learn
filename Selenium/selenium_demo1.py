from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

input_box = driver.find_element(By.ID, "kw")

print("标签：", input_box.tag_name)
print("是否显示：", input_box.is_displayed())
print("是否启用：", input_box.is_enabled())
print("HTML：", input_box.get_attribute("outerHTML"))

input("按回车结束...")

driver.quit()