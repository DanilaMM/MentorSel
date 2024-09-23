from selenium.webdriver.support.wait import WebDriverWait
from configurations.read_config import ConfigReader


class BasePage:
    TIMEOUT = ConfigReader.get_params('timeout')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.TIMEOUT)



