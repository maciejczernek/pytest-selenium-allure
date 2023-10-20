from base.base_page import BasePage
from utilities.locator import Locator
from selenium.webdriver.common.by import By
from allure import step


class StackoverflowMainPage(BasePage):
    PAGE_URL = "https://stackoverflow.com/"

    ACCEPT_BUTTON = Locator(
        by=By.XPATH,
        value="//button[normalize-space()='Accept all cookies']"
    )
    LOGIN_LINK = Locator(by=By.XPATH, value="//a[normalize-space()='Log in']")
    LOGIN_FIELDS_CONTAINER = Locator(by=By.ID, value="formContainer")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = self.PAGE_URL

    @step(f"Get the page")
    def get_page(self):
        self.driver.get(self.url)
        self.accept_cookies()

    @step("Accept cookies")
    def accept_cookies(self):
        self.element_click(self.ACCEPT_BUTTON)

    @step("Click the login button")
    def click_login_button(self):
        self.element_click(self.LOGIN_LINK)
