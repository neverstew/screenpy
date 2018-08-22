import os
from selenium import webdriver


class BrowseTheWeb:
    def __init__(self):
        self.driver = webdriver.Remote(
            command_executor=os.getenv("SELENIUM_HUB_ADDRESS", "http://localhost:4444/wd/hub"),
            desired_capabilities={
                'browserName': os.getenv("SELENIUM_DRIVER_TYPE", "chrome")
            }
        )
