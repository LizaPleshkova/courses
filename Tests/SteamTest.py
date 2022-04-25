import time

import pytest

from Pages.AboutSteamPage import AboutSteamPage
from Pages.TopSellersPage import TopSellerPage
from Tests.BaseTest import BaseTest
from Pages.SteamPage import SteamPage
from Pages.GamePage import GamePage


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

    def test_case2(self):
        self.stream_page = SteamPage(self.driver)
        self.top_seller_page = TopSellerPage(self.driver)
        assert self.stream_page.is_page_opened()

        self.stream_page.move_to_noteworthy_sellers()
        assert self.top_seller_page.is_page_opened()

        self.top_seller_page.do_click_block_search(self.top_seller_page.block_os)
        self.top_seller_page.do_click_checkbox(self.top_seller_page.linux_checkbox)
        assert self.top_seller_page.is_checked(self.top_seller_page.linux_checkbox)

        self.top_seller_page.do_click_block_search(self.top_seller_page.block_quantity_gamers)
        self.top_seller_page.do_click_checkbox(self.top_seller_page.cooperative_lan_checkbox)
        assert self.top_seller_page.is_checked(self.top_seller_page.cooperative_lan_checkbox)
        time.sleep(2)
        self.top_seller_page.do_click_block_search(self.top_seller_page.block_tags)
        self.top_seller_page.search_action_block_tags()
        self.top_seller_page.do_click_checkbox(self.top_seller_page.action_checkbox)
        assert self.top_seller_page.is_checked(self.top_seller_page.action_checkbox)
        time.sleep(4)
        title, released_date, price = self.top_seller_page.get_data_first_el()
        self.top_seller_page.do_click_first_search_result()
        # time.sleep(5)
        self.game_page = GamePage(self.driver)
        assert title == self.game_page.title.text
        assert released_date == self.game_page.released_date.text
        assert price == self.game_page.price.text.split(' ')[0]
