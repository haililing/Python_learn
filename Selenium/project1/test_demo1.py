from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from coupon_page import CouponPage


def test_apply_coupon(coupon_page):
    page = CouponPage(coupon_page)
    page.apply_coupon("SAVE20")
    wait = WebDriverWait(coupon_page, 10)
    wait.until(
        lambda driver: driver.find_element(
            By.ID, "final-price"
        ).text == "¥80"
    )