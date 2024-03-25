from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, \
    ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.action_chains import ActionChains


class BaseElement:

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5,
                                  ignored_exceptions=[NoSuchElementException,
                                                      ElementNotVisibleException,
                                                      ElementNotSelectableException])

    def get_element(self, locator):
        element = self.wait.until(lambda _: self.driver.find_element(*locator))
        return element

    def get_elements(self, locator):
        elements = self.wait.until(
            lambda _: self.driver.find_elements(*locator))
        return elements

    def element_get_text(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator)).text

    def element_get_attribute_value(self, locator, attr_name):
        element_attr = self.wait.until(
            ec.presence_of_element_located(locator)).get_attribute(attr_name)
        return element_attr

    def element_click(self, locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        element.click()

    def element_send_keys(self, locator, keys):
        element = self.wait.until(ec.element_to_be_clickable(locator))
        element.send_keys(keys)

    def element_select_by_index(self, locator, index):
        element = Select(
            self.wait.until(ec.visibility_of_element_located(locator)))
        element.select_by_index(index)

    def element_select_by_value(self, locator, value):
        element = Select(
            self.wait.until(ec.visibility_of_element_located(locator)))
        element.select_by_value(value)

    def element_select_by_text(self, locator, text):
        element = Select(
            self.wait.until(ec.visibility_of_element_located(locator)))
        element.select_by_visible_text(text)

    def element_deselect_by_index(self, locator, index):
        element = Select(
            self.wait.until(ec.visibility_of_element_located(locator)))
        element.deselect_by_index(index)

    def element_deselect_by_value(self, locator, value):
        element = Select(
            self.wait.until(ec.visibility_of_element_located(locator)))
        element.deselect_by_value(value)

    def element_deselect_by_text(self, locator, text):
        element = Select(
            self.wait.until(ec.visibility_of_element_located(locator)))
        element.deselect_by_visible_text(text)

    def element_select_get_options(self, locator):
        element = Select(
            self.wait.until(ec.visibility_of_element_located(locator)))
        return element.options

    def element_switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def element_switch_to_frame(self, locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        self.driver.switch_to.frame(element)

    def element_move_to_element(self, locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        self.actions.move_to_element(element)

    def element_context_click(self, locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        self.actions.context_click(element)

    def element_click_and_hold(self, locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        self.actions.click_and_hold(element)

    def element_double_click(self, locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        self.actions.double_click(element)

    def element_drag_and_drop(self, source_locator, target_locator):
        element_source = self.wait.until(
            ec.visibility_of_element_located(source_locator))
        element_target = self.wait.until(
            ec.visibility_of_element_located(target_locator))
        self.actions.drag_and_drop(element_source, element_target)

    def element_perform_actions(self):
        self.actions.perform()

    def element_enabled(self, locator):
        return self.wait.until(
            ec.visibility_of_element_located(locator)).is_enabled()

    def element_is_enabled(self, locator):
        return self.wait.until(
            ec.visibility_of_element_located(locator)).is_enabled()

    def element_is_selected(self, locator):
        return self.wait.until(
            ec.visibility_of_element_located(locator)).is_selected()

    def element_is_displayed(self, locator):
        return self.wait.until(
            ec.visibility_of_element_located(locator)).is_displayed()
