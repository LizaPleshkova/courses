import time
import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("https://www.aviasales.by/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class TestAvia:

    @staticmethod
    def test_aviasales_page(browser):
        driver = browser
        assert 'Дешёвые авиабилеты онлайн, цены. Поиск билетов на самолёт и сравнение цен — Aviasales.by' == driver.title

        # 2
        destination_input = browser.find_element_by_xpath('//input[contains(@id,"destination")]')
        destination_input.send_keys("Омск")
        time.sleep(2)
        destination_new = browser.find_element_by_xpath(
            "//*[@data-test-id='autocomplete-destination']//*[@class='autocomplete__iata']"
        )
        assert 'OMS' == destination_new.text

        # 3
        destination_input = browser.find_element_by_xpath(
            "//*[@data-test-id='autocomplete-destination']//*[@class='autocomplete__iata']"
        ).text

        swap_button = browser.find_element_by_xpath(
            '//div[contains(@data-test-id,"swap-places")]'
        )
        swap_button.click()
        origin_input = browser.find_element_by_xpath(
            "//*[@data-test-id='autocomplete-origin']//*[@class='autocomplete__iata']"
        )

        assert destination_input == origin_input.text
