import pytest
from pages.steam_main import SteamMain
from faker import Faker


class TestSteam:
    fake = Faker()

    @pytest.mark.steam
    @pytest.mark.steam_login_error
    def test_steam_login_error(self, driver):
        steam_main = SteamMain(driver)
        steam_main.wait_load_page()
        steam_main.click_href_enter()
        fake_name = self.fake.name()
        fake_password = self.fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
        steam_main.login_account(fake_name, fake_password)
        text_error = steam_main.get_element_error()
        text_expected = 'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.'
        assert text_error == text_expected, f'Текст не соответствует ожидаемому. Ожидаемый текст "{text_expected}", текст элемента - "{text_error}"'
