from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from utilities.file_op import create_environment_properties_file


class Configuration:
    def __init__(self, browser_name, headless, resolution):
        self.headless = headless
        self.resolution = resolution
        self.get_browser = {
            "chrome": self.setup_chrome,
            "ff": self.setup_ff
        }[browser_name]
        self.env_prop_dict = {
            "headless": self.headless,
            "resolution": self.resolution
        }

    def setup_chrome(self):
        chrome_options = webdriver.ChromeOptions()
        if self.headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument(f"--window-size={self.resolution}")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        create_environment_properties_file(driver, self.env_prop_dict)
        return driver

    def setup_ff(self):
        ff_options = webdriver.FirefoxOptions()
        if self.headless:
            ff_options.add_argument("--headless")
        ff_options.add_argument(f"--window-size={self.resolution}")
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=ff_options)
        create_environment_properties_file(driver, self.env_prop_dict)
        return driver


class SauceDemoPageConfig:
    BASE_URL = "https://www.saucedemo.com"

