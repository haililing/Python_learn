import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

file_path = Path("test_009_coupon_lab.html").resolve()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

TEST_CASES=[
    ("SAVE20","优惠码应用成功，已减免 ¥20","¥80"),
    ("EXPIRED","优惠码已过期","¥100"),
    ("WRONG","优惠码无效","¥100"),
]

TEST_CASES1=[
    "",
    " ",
]

def apply_coupon(driver,code):
    wait = WebDriverWait(driver,10)
    input_el = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#coupon-code")
        )
    )
    input_el.clear()
    input_el.send_keys(code)
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#apply-coupon")
        )
    ).click()

@pytest.mark.parametrize("couponcode,hint,expected_price", TEST_CASES)
def test_apply_coupon(driver, couponcode, hint,expected_price):
    driver.get(file_path.as_uri())
    apply_coupon(driver, couponcode)
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.ID, "coupon-feedback"), hint
        )
    )
    WebDriverWait(driver, 10).until(
        lambda d:d.find_element(By.ID, "final-price").text == expected_price
    )

@pytest.mark.parametrize("couponcode", TEST_CASES1)
def test_discount_code_2(driver,couponcode):
    driver.get(file_path.as_uri())
    selenium1 = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,"#coupon-code")
        )
    )
    selenium1.clear()
    selenium1.send_keys(couponcode)
    btn = driver.find_element(By.ID, "apply-coupon")
    assert not btn.is_enabled()

def test_reset_coupon(driver):
    driver.get(file_path.as_uri())
    wait = WebDriverWait(driver,10)
    apply_coupon(driver, "SAVE20")
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "coupon-feedback"),"优惠码应用成功，已减免 ¥20"
        )
    )
    wait.until(
        lambda d:d.find_element(By.ID, "final-price").text == "¥80"
    )
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "reset-coupon")
        )
    ).click()

    assert driver.find_element(By.ID, "coupon-code").get_attribute("value") == ""

    assert driver.find_element(By.ID, "final-price").text == "¥100"

    assert not driver.find_element(By.ID, "apply-coupon").is_enabled()