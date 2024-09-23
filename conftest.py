from faker.contrib import pytest
from selenium.webdriver import Chrome


class SingletonDriver:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = Chrome()
        return cls.__instance

    @classmethod
    def get_driver(cls):
        return cls.__instance

    @classmethod
    def quit(cls):
        cls.__instance.quit()
        cls.__instance = None


@pytest.fixture(scope="function")
def driver():
    b = SingletonDriver()
    yield b
    SingletonDriver.quit()
