from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CouponPage:
    COUPON_INPUT = (By.ID, "coupon-code")
    APPLY_BUTTON = (By.ID, "apply-coupon")
    FINAL_PRICE = (By.ID, "final-price")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_clickable(self,locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def enter_coupon(self,code):
        input_el = self.wait_clickable(self.COUPON_INPUT)
        input_el.clear()
        input_el.send_keys(code)

    def apply_coupon(self,code):
        self.enter_coupon(code)
        self.wait_clickable(self.APPLY_BUTTON).click()
        self.wait_clickable(self.APPLY_BUTTON)

    def get_final_price(self):
        return self.wait_clickable(self.FINAL_PRICE).text
