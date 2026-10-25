import pytest

@pytest.mark.parametrize(
    "code,expected_price",
    [
        ("SAVE20", "¥80"),
        ("EXPIRED", "¥100"),
        ("WRONG", "¥100"),
    ],
)
def test_apply_coupon(coupon_page_object,code,expected_price):
    coupon_page_object.apply_coupon(code)
    actual_price = coupon_page_object.get_final_price()
    assert actual_price == expected_price