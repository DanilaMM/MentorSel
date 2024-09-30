import pytest
from pages.steam_main import SteamMain
from pages.search_page import SearchPage, SortType
from itertools import product
from configurations.read_config import ConfigReader
from configurations.test_data import TestData


class TestSteam:
    game = TestData.CONFIG['game_names']
    counts = TestData.CONFIG['expected_counts']

    @pytest.mark.steam
    @pytest.mark.check_games_list
    @pytest.mark.parametrize("game_name,expected_count", ['ru', 'eng'])
    @pytest.mark.parametrize("game_name,expected_count", ([game[0], counts[0]], [game[1], counts[1]]))
    def test_check_games_list(self, driver, game_name, expected_count, lang):
        steam_main = SteamMain(driver)
        steam_search = SearchPage(driver)
        steam_search.wait_load_page()
        steam_main.change_lang(lang)
        steam_main.search_game(game_name)
        steam_search.select_sorted_type(SortType.DESC_PRICE)
        list_name_games = len(steam_search.get_titles_games(expected_count))
        assert list_name_games == expected_count, f'Ожидаемая длина списка имен "{expected_count}",фактическая длина - "{list_name_games}"'
