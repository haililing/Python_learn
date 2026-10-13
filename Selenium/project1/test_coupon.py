import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from coupon_actions import apply_coupon, enter_coupon


TEST_CASES = [
    ("SAVE20", "优惠码应用成功，已减免 ¥20", "¥80"),
    ("EXPIRED", "优惠码已过期", "¥100"),
    ("WRONG", "优惠码无效", "¥100"),
]

@pytest.mark.parametrize("couponcode,hint,expected_price",TEST_CASES)
def test_apply_coupon(couponcode,hint,expected_price):
    apply_coupon()