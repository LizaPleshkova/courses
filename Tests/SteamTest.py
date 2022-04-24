import time

import pytest

from Pages.AboutSteamPage import AboutSteamPage
from Tests.BaseTest import BaseTest
from Pages.SteamPage import SteamPage


def convert_gamers_quantity(quantity: str) -> int:
    gamers = str(quantity).split(',')
    gamers = ''.join(gamers)
    return gamers


class TestStreamPage(BaseTest):
    # change time.sleep(2) - >

    def test_about_page(self):
        self.stream_page = SteamPage(self.driver)
        self.about_page = AboutSteamPage(self.driver)
        assert self.stream_page.is_page_opened()

        self.stream_page.do_click_about_button()
        time.sleep(2)
        # check that the about page was opened
        assert self.about_page.is_about_page_opened()
        time.sleep(2)

        gamers_online = convert_gamers_quantity(self.about_page.gamers_online.text)
        gamers_in_game = convert_gamers_quantity(self.about_page.gamers_in_game.text)
        assert gamers_in_game < gamers_online

        self.about_page.do_click_shop_link()
        time.sleep(2)
        assert self.stream_page.is_page_opened()
