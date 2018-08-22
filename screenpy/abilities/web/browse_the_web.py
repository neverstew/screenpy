import os
from selenium import webdriver


class BrowseTheWeb:
    def __init__(self):
        self.driver = webdriver.Remote(
            command_executor=os.getenv("SELENIUM_HUB_ADDRESS", "http://localhost:4444/wd/hub"),
            desired_capabilities={
                # Browser capabilities
                'browserName': os.getenv("SELENIUM_DRIVER_TYPE", "chrome"),
                # Hub connection capabilities
                'browserTimeout': os.getenv("SELENIUM_BROWSER_TIMEOUT", "5"), # 5 seconds
                'cleanUpCycle': os.getenv("SELENIUM_CLEANUP", "5000"), # 5 seconds
                'timeout': os.getenv("SELENIUM_TIMEOUT", "60"), # 60 seconds
                'sessionTimeout': os.getenv("SELENIUM_SESSION_TIMEOUT", "60") # 60 seconds
            }
        )
