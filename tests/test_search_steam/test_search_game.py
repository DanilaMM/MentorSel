import pytest
from pages.steam_main import SteamMain
from pages.search_page import SearchPage
from itertools import product



class TestSteam:
    game_names = ['The witcher', 'Fallout']
    expected_counts = [10, 20]
    langs = ['ru', 'eng']

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
        steam_search.select_sorted_type('desc_price')
        list_name_games = len(steam_search.get_titles_games(expected_count))
        assert list_name_games == expected_count, f'Ожидаемая длина списка имен "{expected_count}", фактическая длина - "{list_name_games}"'
