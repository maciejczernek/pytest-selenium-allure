import allure
import pytest

from pages.sauce_demo.login_page import SauceDemoLoginPage
from pages.sauce_demo.inventory_page import SauceDemoInventoryPage


@pytest.mark.login_page
@allure.suite("Login page")
@allure.title("Login as a valid user")
@allure.testcase("#", "TC-1230")
@allure.description(
    """
    Test steps:
        1. Open the login page
        2. Send keys to the username field
        3. Send keys to the password field
        4. Click the login button
        5. Verify the inventory page loaded properly
    """
)
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
])
def test_login_valid_data(browser, username, password):
    sauce_login_page = SauceDemoLoginPage(browser)
    sauce_inventory_page = SauceDemoInventoryPage(browser)

    sauce_login_page.get_page()
    sauce_login_page.username_send_keys(username)
    sauce_login_page.password_send_keys(password)
    sauce_login_page.login_button_click_button()

    with allure.step("Verify the inventory page loaded properly"):
        assert sauce_inventory_page.URL in sauce_login_page.get_current_url


@pytest.mark.login_page
@allure.suite("Login page")
@allure.title("Login as an invalid user")
@allure.description(
    """
    Test steps:
        1. Open the login page
        2. Send keys to the username field
        3. Send keys to the password field
        4. Click the login button
        5. Verify the error container appeared
    """
)
@allure.testcase("#", "TC-1234")
@pytest.mark.parametrize("username, password", [
    ("standard_user", ""),
    ("", "secret_sauce"),
    ("", ""),
])
def test_login_invalid_data(browser, username, password):
    sauce_login_page = SauceDemoLoginPage(browser)

    sauce_login_page.get_page()
    sauce_login_page.username_send_keys(username)
    sauce_login_page.password_send_keys(password)
    sauce_login_page.login_button_click_button()

    with allure.step("Verify the error container appeared"):
        assert sauce_login_page.error_container_enabled
