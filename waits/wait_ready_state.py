class WaitDoc:
    def __init__(self, locator, attr, value):
        self._locator = locator
        self._atribute = attr
        self._attribute_value = value

    def __call__(self, driver):
        element = driver.find_element_by_xpath(self._locator)
        if element.get_attribute(self._atribute) == self._attribute_value:
            return element
        return False
