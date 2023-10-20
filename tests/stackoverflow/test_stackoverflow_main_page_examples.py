import allure

from pages.stackoverflow.main_page import StackoverflowMainPage
from pages.stackoverflow.login_page import StackoverflowLoginPage
from utilities.allure_project_structure import suite, sub_suite, parent_suite


@parent_suite
@suite
@sub_suite
@allure.title("Verify the login fields container exists")
def test_verify_login_fields_container_displays(browser):

    main_page = StackoverflowMainPage(browser)
    login_page = StackoverflowLoginPage(browser)

    main_page.get_page()
    main_page.click_login_button()
    login_page.verify_login_container_displayed()


@parent_suite
@suite
@sub_suite
@allure.title("False test example")
def test_return_false_after_get_the_page(browser):

    main_page = StackoverflowMainPage(browser)

    main_page.get_page()
    assert False, "Just for example purposes"
