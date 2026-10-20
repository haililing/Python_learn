from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from coupon_actions import enter_coupon


class CouponPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_coupon(self,code):
        input_el = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(
                (By.ID,"coupon-code")
            )
        )
        input_el.clear()
        input_el.send_keys(code)

    def apply_coupon(self,code):
        enter_coupon(self.driver,code)
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(
                (By.ID,"apply-coupon")
            )
        ).click()