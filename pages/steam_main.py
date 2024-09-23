from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec



class SteamMain(BasePage):
    HREF_ENTER = (By.XPATH, "//*[@id='global_actions']//a[contains(text(), 'войти')]")
    INPUT_NAME = (By.XPATH, "//form//input[@type='text']")
    INPUT_PASSWORD = (By.XPATH, "//form//input[@type='password']")
    BUTTON_ENTER = (By.XPATH, "//form//button[@type='submit']")
    DIV_TEXT_ERROR = (By.XPATH, "//form//div[contains(text(),'Пожалуйста, проверьте свой пароль')]")
    SPAN_LANG = (By.XPATH, "//span[@id='language_pulldown']")
    SELECT_LANG = {
        "eng": (By.XPATH, "//div[@class='popup_body popup_menu']//a[contains(text(), 'English')]"),
        "ru": (By.XPATH, "//div[@class='popup_body popup_menu']//a[contains(text(), 'Русс')]"),
    }

    INPUT_NAME_GAME = (By.XPATH, "//input[@id='store_nav_search_term']")
    A_ACCEPT_SEARCH_GAME = (By.XPATH, "//a[@id='store_search_link']")

    def change_lang(self, lang):
        my_lang = self.wait.find_element(By.TAG_NAME, 'html').get_attribute('lang')
        if my_lang != lang:
            self.wait.until(ec.element_to_be_clickable(self.SPAN_LANG)).click()
            self.wait.until(ec.element_to_be_clickable(self.SELECT_LANG[lang])).click()

    def search_game(self, name):
        self.wait.until(ec.visibility_of_element_located(self.INPUT_NAME_GAME)).send_keys(name)
        self.wait.until(ec.element_to_be_clickable(self.A_ACCEPT_SEARCH_GAME)).click()

    def click_href_enter(self):
        self.wait.until(ec.element_to_be_clickable(self.HREF_ENTER)).click()

    def login_account(self, name, password):
        self.wait.until(ec.visibility_of_element_located(self.INPUT_NAME)).send_keys(name)
        self.wait.until(ec.visibility_of_element_located(self.INPUT_PASSWORD)).send_keys(
            password)
        self.wait.until(ec.element_to_be_clickable(self.BUTTON_ENTER)).click()

    def get_element_error(self):
        return self.wait.until(ec.presence_of_element_located(self.DIV_TEXT_ERROR, )).text
