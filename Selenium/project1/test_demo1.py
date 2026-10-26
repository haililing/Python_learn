import pytest

@pytest.mark.parametrize(
    "code,expected_price,feedback",
    [
        ("SAVE20", "¥80","优惠码应用成功，已减免 ¥20"),
        ("EXPIRED", "¥100","优惠码已过期"),
        ("WRONG", "¥100","优惠码无效"),
    ],
)
def test_apply_coupon(coupon_page_object,code,expected_price,feedback):
    coupon_page_object.apply_coupon(code)
    actual_price = coupon_page_object.get_final_price()
    assert actual_price == expected_price
    assert coupon_page_object.get_feedback() == feedback

@pytest.mark.parametrize(
    "code",
    [
        " ",
        "",
    ],
)
def test_empty_coupon(coupon_page_object,code):
    coupon_page_object.enter_coupon(code)
    assert coupon_page_object.is_apply_enabled() is False

@pytest.mark.parametrize(
    "code,expected_price,feedback",
    [
        ("SAVE20", "¥80","优惠码应用成功，已减免 ¥20"),
    ]
)
def test_button_reset_coupon(coupon_page_object,code,expected_price,feedback):
    test_apply_coupon(coupon_page_object,code,expected_price,feedback)
    coupon_page_object.button_reset_coupon()
    assert coupon_page_object.is_apply_enabled() is False
    assert coupon_page_object.get_coupon() == ""
    assert coupon_page_object.get_final_price() == "¥100"
    test_apply_coupon(coupon_page_object,code,expected_price,feedback)