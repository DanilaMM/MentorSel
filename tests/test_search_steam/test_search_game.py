import pytest
from pages.steam_main import SteamMain
from pages.search_page import SearchPage, SortType
from itertools import product
from configurations.read_config import ConfigReader


class TestSteam:
    read_json = ConfigReader()
    game_names = read_json.get_params("game_names")
    expected_counts = read_json.get_params("expected_counts")
    langs = read_json.get_params("langs")

    parametrized_data = list(product(game_names, expected_counts, langs))

    @pytest.mark.steam
    @pytest.mark.check_games_list
    @pytest.mark.parametrize("game_name,expected_count,lang", parametrized_data)
    def test_check_games_list(self, driver, game_name, expected_count, lang):
        steam_main = SteamMain(driver)
        steam_search = SearchPage(driver)
        steam_search.wait_load_page()
        steam_main.change_lang(lang)
        steam_main.search_game(game_name)
        # я должен использовать еще 1 импорт для юзания Enum??Нельзя никак это обойти?
        steam_search.select_sorted_type(SortType.DESC_PRICE)
        list_name_games = len(steam_search.get_titles_games(expected_count))
        assert list_name_games == expected_count, f'Ожидаемая длина списка имен "{expected_count}",фактическая длина - "{list_name_games}"'
