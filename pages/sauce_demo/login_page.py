from base.base_page import BasePage
from utilities.locator import Locator
from selenium.webdriver.common.by import By
from allure import step
from tests.config import SauceDemoPageConfig


class SauceDemoLoginPage(BasePage, SauceDemoPageConfig):
    PAGE_URL = SauceDemoPageConfig.BASE_URL

    USERNAME = Locator(By.ID, "user-name")
    PASSWORD = Locator(By.ID, "password")
    LOGIN_BUTTON = Locator(By.ID, "login-button")
    ERROR_CONTAINER = Locator(By.CLASS_NAME, "error-message-container.error")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = self.PAGE_URL

    @step("Send keys to the username field")
    def username_send_keys(self, keys):
        self.element_send_keys(self.USERNAME, keys)

    @step("Send keys to the password field")
    def password_send_keys(self, keys):
        self.element_send_keys(self.PASSWORD, keys)

    @step("Click the login button")
    def login_button_click_button(self):
        self.element_click(self.LOGIN_BUTTON)

    @property
    def error_container_enabled(self):
        return self.element_enabled(self.ERROR_CONTAINER)
