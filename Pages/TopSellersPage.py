from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from .BasePage import BasePage


class TopSellerPage(BasePage):
    # locators
    _sortbox = (By.XPATH, "//div[contains(@class,'sortbox')]")
    _block_os = (By.XPATH, "//div[contains(@data-collapse-name,'os')]")
    _linux_checkbox = (By.XPATH, '//div[contains(@data-loc,"SteamOS + Linux")]')

    _block_quantity_gamers = (By.XPATH, "//div[contains(@data-collapse-name,'category3')]")
    _cooperative_lan_checkbox = (By.XPATH, '//div[contains(@data-loc,"Кооператив (LAN)")]')

    _block_tags = (By.XPATH, "//div[contains(@data-collapse-name,'tags')]")
    _search_tags = (By.XPATH, "//input[contains(@id,'TagSuggest')]")
    _action_checkbox = (By.XPATH, "//div[contains(@data-loc,'Экшен')]")

    _search_result = (By.ID, 'search_resultsRows')
    _first_search_result = (By.XPATH, "//*[contains(@id,'search_resultsRows')]//a[1]//descendant-or-self::*")

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get('https://store.steampowered.com/about/')

    @property
    def sortbox(self):
        return self.driver.find_element(*TopSellerPage._sortbox)

    @property
    def block_os(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self._block_os)
        )
        return el

    @property
    def linux_checkbox(self):
        el = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self._linux_checkbox)
        )
        return el

    @property
    def cooperative_lan_checkbox(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self._cooperative_lan_checkbox)
        )
        return el

    @property
    def block_quantity_gamers(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self._block_quantity_gamers)
        )
        return el

    @property
    def block_tags(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self._block_tags)
        )
        return el

    @property
    def search_tags(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self._search_tags)
        )
        return el

    @property
    def action_checkbox(self):
        try:
            el = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self._action_checkbox)
            )
            return el
        except TimeoutException as exc:
            print(f'Element not found on the page!\n{exc}')
            return None

    @property
    def first_search_result(self):
        # el = self.driver.find_elements(*TopSellerPage._first_search_result)
        el = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self._first_search_result)
        )
        el.get_attribute('innerHTML')
        return el

    def get_data_first_el(self):
        i = self.first_search_result

        title = i.find_element_by_xpath('//*[contains(@class, "title")]').text
        released_date = i.find_element_by_xpath('//*[contains(@class, "search_released")]').text
        price = i.find_element_by_xpath('//*[contains(@class, "search_price")]').text
        return title, released_date, price

    def do_click_first_search_result(self):
        i = self.first_search_result

        search_result = i.find_element_by_xpath('//*[contains(@class, "search_result_row")]')
        search_result.click()

    def do_click_block_search(self, element):
        if self.is_collapsed(element):
            element.click()

    def search_action_block_tags(self, search_tag=None):
        self.search_tags.send_keys('Экшен')
        self.search_tags.click()

    #
    # def do_click_block_quantity_gamers(self, element):
    #     if self.is_collapsed(self.block_quantity_gamers):
    #         print('was clicked')
    #         self.do_click(self._block_quantity_gamers)

    def do_click_checkbox(self, checkbox):
        checkbox.click()

    def is_page_opened(self) -> bool:
        is_opened = self.is_exist(self._sortbox)
        return is_opened
