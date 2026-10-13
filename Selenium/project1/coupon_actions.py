from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def enter_coupon(driver,code):
    input_el = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(
            (By.ID,"coupon-code")
        )
    )

    input_el.clear()
    input_el.send_keys(code)

def apply_coupon(driver,code):
    enter_coupon(driver,code)
    WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(
            (By.ID,"apply-coupon")
        )
    ).click()

