from base.base_page import BasePage
from utilities.locator import Locator
from selenium.webdriver.common.by import By
from allure import step


class StackoverflowLoginPage(BasePage):
    PAGE_URL = "https://stackoverflow.com/users/login/"

    LOGIN_FIELDS_CONTAINER = Locator(by=By.ID, value="formContainer")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = self.PAGE_URL

    @step("Verify the login fields container displayed")
    def verify_login_container_displayed(self):
        assert self.element_is_displayed(self.LOGIN_FIELDS_CONTAINER), \
            "The login fields container not displayed"
