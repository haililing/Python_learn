from selenium import webdriver

webdriver = webdriver.Chrome()

webdriver.get("https://www.baidu.com")

print(webdriver.current_url)
print(webdriver.title)

webdriver.get("https://www.selenium.dev/")
print(webdriver.current_url)
print(webdriver.title)

webdriver.back()
print(webdriver.current_url)

webdriver.forward()
print(webdriver.current_url)

webdriver.refresh()

webdriver.implicitly_wait(1)

input()

webdriver.quit()