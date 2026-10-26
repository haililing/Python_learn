from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CouponPage:
    COUPON_INPUT = (By.ID, "coupon-code")
    APPLY_BUTTON = (By.ID, "apply-coupon")
    FINAL_PRICE = (By.ID, "final-price")
    COUPON_FEEDBACK = (By.ID,"coupon-feedback")
    APPLY_COUPON = (By.ID, "apply-coupon")
    RESET_COUPON = (By.ID,"reset-coupon")

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
        return self.get_text(self.FINAL_PRICE)

    def get_text(self,locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    def get_feedback(self):
        return self.get_text(self.COUPON_FEEDBACK)

    def is_apply_enabled(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.APPLY_COUPON)
        ).is_enabled()

    def button_reset_coupon(self):
        self.wait_clickable(self.RESET_COUPON).click()

    def get_coupon_code(self):
        input_el = self.wait.until(
            EC.visibility_of_element_located(self.COUPON_INPUT)
        )
        return input_el.get_attribute("value")