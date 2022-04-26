from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_get_url(self, url):
        self.driver.get(url)

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_exist(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_collapsed(self, item) -> bool:
        classes = item.get_attribute('class')
        return 'collapsed' in classes

    def is_checked(self, item) -> bool:
        classes = item.get_attribute('class')
        return 'checked' in classes

    # def find(self, timeout=10):
    #     """ Find element on the page. """
    #     element = None
    #     try:
    #         element = WebDriverWait(self._web_driver, timeout).until(
    #            EC.presence_of_element_located(self._locator)
    #         )
    #     except:
    #         print(colored('Element not found on the page!', 'red'))
    #
    #     return element
