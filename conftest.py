import time
import pytest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# driver = webdriver.Chrome()
# driver.get("https://www.aviasales.by/")
# driver.implicitly_wait(10)
# yield driver
# driver.quit()
from WebDriver import WebDriver


@pytest.fixture(scope="class")
def setup(request):
    global driver
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver = WebDriver().driver
    driver.get('https://store.steampowered.com/')
    driver.implicitly_wait(30)
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()
