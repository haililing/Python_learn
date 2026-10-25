from coupon_page import CouponPage


def test_apply_coupon(coupon_page):
    page = CouponPage(coupon_page)
    page.apply_coupon("SAVE20")
    actual_price = page.get_final_price()
    assert actual_price == "¥80"