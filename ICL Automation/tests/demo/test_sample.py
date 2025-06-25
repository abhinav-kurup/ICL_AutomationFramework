import pytest
import allure

@allure.title("Positive Test: Always Passes")
def test_sample():
    assert True

@allure.title("Positive Test: Sum Check")
def test_sum():
    result = 2 + 3
    assert result == 5, "Expected sum to be 5"

# @allure.title("Negative Test: Always Fails")
# def test_failure():
#     assert False
