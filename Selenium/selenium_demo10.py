import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()

start_time = time.time()


def check(driver):
    elapsed = time.time() - start_time

    print(f"检查一次：{elapsed:.2f} 秒")

    if elapsed >= 3:
        return True

    return False


wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5
)

wait.until(check)

print("等待结束")

driver.quit()