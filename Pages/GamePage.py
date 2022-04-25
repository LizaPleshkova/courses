from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .BasePage import BasePage


class GamePage(BasePage):
    # locators
    _title = (By.ID, "appHubAppName")
    _released_date = (By.XPATH, "//div[@class='release_date']//div[@class='date']")
    _price = (
        By.XPATH, "//div[contains(@class,'game_area_purchase_game')]//div[contains(@class,'game_purchase_price')]")

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get('https://store.steampowered.com/about/')

    @property
    def title(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self._title)
        )
        return el

    @property
    def released_date(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self._released_date)
        )
        return el

    @property
    def price(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self._price)
        )
        return el
