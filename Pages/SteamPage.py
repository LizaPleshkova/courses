from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .BasePage import BasePage


class SteamPage(BasePage):
    # locators
    about_button = (By.XPATH, "//div[@class='content']//a[contains(@class, 'menuitem') and contains(@href, 'about')]")
    carousel_container = (By.ID, "home_maincap_v7")

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.do_get_url('https://store.steampowered.com/')

    @property
    def get_about_button(self):
        return self.driver.find_element(*SteamPage.about_button)

    @property
    def get_carousel_cpntainer(self):
        return self.driver.find_element(*SteamPage.carousel_container)

    def do_click_about_button(self):
        self.do_click(self.about_button)

    def is_page_opened(self):
        is_opened = self.is_exist(self.carousel_container)
        print('is_opened',is_opened)
        return is_opened
