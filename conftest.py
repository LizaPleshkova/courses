import time
import pytest
from selenium import webdriver


# driver = webdriver.Chrome()
# driver.get("https://www.aviasales.by/")
# driver.implicitly_wait(10)
# yield driver
# driver.quit()

@pytest.fixture(scope="class")
def setup(request):
    global driver
    # browser_name = request.config.getoption("browser_name")
    # if browser_name == "chrome":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    # s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome()
    # elif browser_name == "firefox":
    #     f = fService(GeckoDriverManager().install())
    #     driver = webdriver.Firefox(service=f)

    driver.get('https://store.steampowered.com/')
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()
