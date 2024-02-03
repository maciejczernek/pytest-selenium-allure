import allure
import pytest

from .config import Configuration
from pages.sauce_demo.login_page import SauceDemoLoginPage
from utilities.file_op import copy_allure_history, generate_report, \
    create_report_folder


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices="chrome, ff")
    parser.addoption("--headless", default="True")
    parser.addoption("--resolution", default="1920,1080")


@pytest.fixture(scope="session")
@allure.title("Get the browser name")
def br(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
@allure.title("Get the headless setup")
def headless(request):
    value = request.config.getoption("--headless")
    if value.lower() == 'true':
        return True
    return False


@pytest.fixture(scope="session")
@allure.title("Get the browser resolution")
def resolution(request):
    return request.config.getoption("--resolution")


@pytest.fixture(scope="function")
@allure.title("Get the driver")
def driver(br, headless, resolution):
    dr = Configuration(br, headless, resolution).get_browser
    return dr()


@pytest.fixture(scope="function")
@allure.title("Setup/teardown the driver")
def browser(driver):
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        browser = item.funcargs['browser']
        allure.attach(
            browser.get_screenshot_as_png(),
            name='Screenshot',
            attachment_type=allure.attachment_type.PNG
        )


@pytest.fixture
@allure.title("Open the main page and login to the system")
def open_and_login(browser):
    # TODO: Hide sensitive data and use os.environ
    username = "standard_user"
    password = "secret_sauce"

    sauce_login_page = SauceDemoLoginPage(browser)

    sauce_login_page.get_page()
    sauce_login_page.username_send_keys(username)
    sauce_login_page.password_send_keys(password)
    sauce_login_page.login_button_click_button()


def pytest_sessionfinish():
    create_report_folder()
    copy_allure_history()
    generate_report()
