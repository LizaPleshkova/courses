import json
import pytest
from WebDriver import WebDriver
from selenium.webdriver.chrome.options import Options

DEFAULT_WAIT_TIME = 10


@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dict
    with open('config.json') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope="class")
def setup(request, config_browser, config_wait_time, config):
    global driver
    # Initialize WebDriver
    if config_browser == 'chrome':
        chrome_opts = Options()
        # chrome_opts.add_argument("--headless")
        # chrome_opts.add_argument("--window-size=1920x1080")
        chrome_opts.add_argument("--incognito")
        driver = WebDriver(chrome_opts).driver
        driver.get(config['url'])
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
