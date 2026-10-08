from itertools import dropwhile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get(
    "https://www.selenium.dev/selenium/web/web-form.html"
)

dropdown_elements = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.NAME, "my-select")
    )
)

dropdown = Select(dropdown_elements)

dropdown.select_by_value("Two")

print(dropdown.first_selected_option.text)

input()
driver.quit()