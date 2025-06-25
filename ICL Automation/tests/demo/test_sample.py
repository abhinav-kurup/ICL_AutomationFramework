# import pytest
# import allure

# @allure.title("Positive Test: Always Passes")
# def test_sample():
#     assert True

# @allure.title("Positive Test: Sum Check")
# def test_sum():
#     result = 2 + 3
#     assert result == 5, "Expected sum to be 5"

# @allure.title("Negative Test: Always Fails")
# def test_failure():
#     assert False

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# ------------------------
# Fixture to set up driver
# ------------------------
@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")  # Comment out if you want visible browser
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

# ------------------------
# Valid login test
# ------------------------
@allure.title("Login with valid credentials")
def test_valid_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url, "Valid login should navigate to inventory page"

# ------------------------
# Invalid login test
# ------------------------
@allure.title("Login with invalid credentials")
def test_invalid_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    error_element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error_element.is_displayed(), "Error message should appear for invalid login"

# ------------------------
# Inventory items test
# ------------------------
@allure.title("Verify inventory items are visible after login")
def test_inventory_items(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) > 0, "No inventory items found after login"
