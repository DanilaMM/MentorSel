import pytest

from driver import SingletonDriver


# оставить фикстуру тут, синглтон в другое место
@pytest.fixture(scope="function")
def driver():
    b = SingletonDriver()
    yield b
    SingletonDriver.quit()
