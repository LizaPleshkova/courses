from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .BasePage import BasePage


class AboutSteamPage(BasePage):
    # locators
    # как лучше выбрать уникальный элемент, луше что-то маленькое или то, где есть id
    _about_games_area = (By.XPATH, "//div[contains(@id,'about_games_cta_area')]")

    _gamers_online = (By.XPATH, "//div[contains(@class,'gamers_online')]//parent::*")
    _gamers_in_game = (By.XPATH, "//div[contains(@class,'gamers_in_game')]//parent::*")

    _shop_link = (By.XPATH, "//div[contains(@id,'about_games_cta')]//descendant::div[@class='cta_content']//a")

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get('https://store.steampowered.com/about/')

    @property
    def gamers_online(self):
        return self.driver.find_element(*AboutSteamPage._gamers_online)

    @property
    def gamers_in_game(self):
        return self.driver.find_element(*AboutSteamPage._gamers_in_game)

    @property
    def shop_link(self):
        return self.driver.find_element(*AboutSteamPage._shop_link)

    def do_click_shop_link(self):
        self.do_click(self._shop_link)

    def is_about_page_opened(self):
        is_opened = self.is_exist(self._about_games_area)
        return is_opened
