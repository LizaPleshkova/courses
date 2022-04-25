from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:
    class __WebDriver:
        def __init__(self,options=[] ):
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver = None

    def __init__(self, options=[]):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver(options).driver
