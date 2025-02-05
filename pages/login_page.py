from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from waits.wait_ready_state import WaitDoc
from enum import StrEnum


class SortType(StrEnum):
    DESC_PRICE = "desc_price"
    ASC_PRICE = "asc_price"


class SearchPage(BasePage):
    INPUT_NAME_GAME = (By.XPATH, "//*[@id='store_nav_search_term']")
    A_ACCEPT_SEARCH_GAME = (By.XPATH, "//*[@id='store_search_link']")
    ALL_TITLE_GAME = (By.XPATH, "//span[@class='title']")
    OPEN_SORT_WINDOW = (By.ID, "sort_by_trigger")
    SORTED_TYPE = {
        SortType.DESC_PRICE: (By.XPATH, "//a[@id='Price_DESC']"),
        SortType.ASC_PRICE: (By.XPATH, "//a[@id='Price_ASC']")
    }

    def wait_load_page(self):
        wait_el = WaitDoc(self.INPUT_NAME_GAME, 'placeholder', 'поиск')
        wait_el(self.driver)

    def select_sorted_type(self, sort_type):
        self.wait.until(ec.element_to_be_clickable(self.SORTED_TYPE[sort_type])).click()

    def get_titles_games(self, count):
        list_titles = self.wait.until(ec.presence_of_element_located(self.ALL_TITLE_GAME, )).find_elements(
            *self.ALL_TITLE_GAME)
        name_list = []
        for wbel in list_titles[0:count]:
            title = wbel.text
            name_list.append(title)
            return name_list
