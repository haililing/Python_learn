from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

elements = driver.find_elements(
    By.CSS_SELECTOR,
    "input, textarea, [contenteditable='true']"
)

print("一共找到：", len(elements), "个可能的输入元素")

for index, element in enumerate(elements):
    print("\n========================")
    print("序号：", index)
    print("标签：", element.tag_name)
    print("id：", element.get_attribute("id"))
    print("name：", element.get_attribute("name"))
    print("type：", element.get_attribute("type"))
    print("placeholder：", element.get_attribute("placeholder"))
    print("contenteditable：", element.get_attribute("contenteditable"))
    print("是否显示：", element.is_displayed())
    print("是否启用：", element.is_enabled())
    print("尺寸位置：", element.rect)
    print("HTML：", element.get_attribute("outerHTML"))

input("按回车结束...")
driver.quit()