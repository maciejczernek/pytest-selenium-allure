import os

from base.base_page import BasePage
from utilities.locator import Locator
from selenium.webdriver.common.by import By
from allure import step
from tests.config import SauceDemoPageConfig


class SauceDemoInventoryPage(BasePage, SauceDemoPageConfig):
    URL = "/inventory.html"
    PAGE_URL = os.path.join(SauceDemoPageConfig.BASE_URL, URL)

    SORT_FIELD = Locator(By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = self.PAGE_URL

    @property
    @step("Get the number of the sort options")
    def sort_function_get_list_length(self):
        return len(self.element_select_get_options(self.SORT_FIELD))

    @property
    @step("Get the sort options text")
    def sort_function_get_list_of_options_text(self):
        return [opt.text for opt in
                self.element_select_get_options(self.SORT_FIELD)]

    @step("Click the sort field")
    def sort_function_click(self):
        self.element_click(self.SORT_FIELD)
