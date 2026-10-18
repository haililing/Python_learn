from selenium.webdriver.common.by import By
from coupon_page import CouponPage

def test_enter_coupon(coupon_page):
    page = CouponPage(coupon_page)
    page.enter_coupon("SAVE20")
    assert coupon_page.find_element(
        By.ID, "coupon-code"
    ).get_attribute("value") == "SAVE20"