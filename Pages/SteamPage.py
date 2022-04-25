from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .BasePage import BasePage


class SteamPage(BasePage):
    # locators
    _about_button = (By.XPATH, "//div[@class='content']//a[contains(@class, 'menuitem') and contains(@href, 'about')]")
    _carousel_container = (By.ID, "home_maincap_v7")  # for check that page was opened
    _new_and_noteworthy = (By.XPATH, "//div[contains(@id,'noteworthy_tab')]")
    _top_sellers = (By.XPATH, "//div[contains(@id,'noteworthy_flyout')]//descendant::a[contains(@href, 'topsellers')]")

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.do_get_url('https://store.steampowered.com/')

    @property
    def about_button(self):
        return self.driver.find_element(*SteamPage._about_button)

    @property
    def carousel_container(self):
        return self.driver.find_element(*SteamPage._carousel_container)

    @property
    def new_and_noteworthy(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self._new_and_noteworthy)
        )
        el2 = self.driver.find_element(*SteamPage._new_and_noteworthy)
        return el

    @property
    def top_sellers(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self._top_sellers)
        )
        el2 = self.driver.find_element(*SteamPage._top_sellers)
        return el

    def move_to_noteworthy_sellers(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.new_and_noteworthy).perform()
        action.move_to_element(self.top_sellers).perform()
        self.do_click_top_sellers()

    def do_click_about_button(self):
        self.do_click(self._about_button)

    def do_click_top_sellers(self):
        self.do_click(self._top_sellers)

    def is_page_opened(self):
        is_opened = self.is_exist(self._carousel_container)
        return is_opened
