import allure
import pytest

from pages.sauce_demo.login_page import SauceDemoLoginPage
from pages.sauce_demo.inventory_page import SauceDemoInventoryPage


@pytest.mark.inventory_page
@allure.suite("Inventory page")
@allure.title("The sorting function should have 4 options")
@allure.testcase("#", "TC-1214")
@allure.description(
    """
    Test steps:
        1. Login to the page
        2. Get the sort function options
        3. Verify the length of the sort function
    """
)
def test_verify_sort_options_length(browser, open_and_login):
    expected_length = 4
    sauce_inventory_page = SauceDemoInventoryPage(browser)

    with allure.step(
            f"Verify the length of the sort function is {expected_length}"):
        assert sauce_inventory_page.sort_function_get_list_length == expected_length


@pytest.mark.inventory_page
@allure.suite("Inventory page")
@allure.title("The sorting function should contains particular names")
@allure.testcase("#", "TC-1330")
@allure.description(
    """
    Test steps:
        1. Login to the page
        2. Get the sort function options
        3. Verify whether list contains particular name
    """
)
@pytest.mark.parametrize("name", [
    "Name (A to Z)",
    "Name (Z to A)",
    "Price (low to high)",
    "Price (high to low)",
])
def test_verify_sort_function_names(browser, open_and_login, name):
    sauce_inventory_page = SauceDemoInventoryPage(browser)

    with allure.step(f"Verify '{name}' is in the list"):
        assert name in sauce_inventory_page.sort_function_get_list_of_options_text
