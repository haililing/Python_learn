import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from coupon_actions import apply_coupon,enter_coupon


TEST_CASES = [
    ("SAVE20", "优惠码应用成功，已减免 ¥20", "¥80"),
    ("EXPIRED", "优惠码已过期", "¥100"),
    ("WRONG", "优惠码无效", "¥100"),
]


@pytest.mark.parametrize(
    "couponcode,hint,expected_price",
    TEST_CASES
)
def test_apply_coupon(coupon_page, couponcode, hint, expected_price):

    apply_coupon(coupon_page, couponcode)

    wait = WebDriverWait(coupon_page, 10)

    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "coupon-feedback"),
            hint
        )
    )

    wait.until(
        lambda d: d.find_element(
            By.ID, "final-price"
        ).text == expected_price
    )

@pytest.mark.parametrize("couponcode",[""," "])
def test_empty_coupon(coupon_page,couponcode):
    enter_coupon(coupon_page, couponcode)
    btn = coupon_page.find_element(By.ID,"apply-coupon")
    assert not btn.is_enabled()


def test_reset_coupon(coupon_page):
    wait = WebDriverWait(coupon_page, 10)
    apply_coupon(coupon_page, "SAVE20")
    wait.until(
        lambda d: d.find_element(
            By.ID, "final-price"
        ).text == "¥80"
    )
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "reset-coupon")
        )
    ).click()
    wait.until(
        lambda d: d.find_element(
            By.ID, "final-price"
        ).text == "¥100"
    )
    assert coupon_page.find_element(
        By.ID, "coupon-code"
    ).get_attribute("value") == ""

    assert not coupon_page.find_element(
        By.ID, "apply-coupon"
    ).is_enabled()

    apply_coupon(coupon_page,"SAVE20")
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "coupon-feedback"),
            "优惠码应用成功，已减免 ¥20"
        )
    )
    wait.until(
        lambda d: d.find_element(
            By.ID, "final-price"
        ).text == "¥80"
    )