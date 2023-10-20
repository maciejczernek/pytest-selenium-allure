import allure

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_element import BaseElement


class BasePage(BaseElement):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.driver = webdriver.Chrome()
        self.url = None

    @allure.step(f"Get the page")
    def get_page(self):
        self.driver.get(self.url)

    @property
    def get_page_title(self):
        title = self.driver.title
        return title

    def page_refresh(self):
        self.driver.refresh()

    def page_close(self):
        self.driver.close()

    def page_quit(self):
        self.driver.quit()

    def alert_accept(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def alert_dismiss(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.dismiss()

    @property
    def alert_text(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert_txt = self.driver.switch_to.alert.text
        return alert_txt

    def page_scroll_by(self, x, y):
        self.driver.execute_script(f"window.scrollBy({x},{y});")

    @property
    def get_page_window_size(self):
        height = self.driver.execute_script("return window.innerHeight;")
        width = self.driver.execute_script("return window.innerWidth;")
        return [width, height]

    def page_switch_to_window(self, handle):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[handle])

    def page_switch_to_new_window(self):
        self.driver.switch_to.new_window()

    @property
    def get_all_cookies(self):
        return self.driver.get_cookies()

    def get_cookie(self, name):
        return self.driver.get_cookie(name)

    def add_cookie(self, item: dict):
        self.driver.add_cookie(item)

    def delete_cookie(self, name):
        self.driver.delete_cookie(name)

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    @property
    def get_current_url(self):
        return self.driver.current_url

    @property
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Verify the page title")
    def verify_page_title(self, expected_result):
        assert expected_result in self.get_page_title, \
            f"{expected_result} not in {self.get_page_title}"
