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
        self.driver.implicitly_wait(5) # 5 seconds to poll for any elements on the page
        self.driver.set_page_load_timeout(5)  # 5 seconds for any page to load

    def get_screenshot(self):
        return self.driver.get_screenshot_as_png()

    def __del__(self):
        """
        When ability ceases to be used - ensure all remnants of the driver are removed
        """
        try:
            self.driver.close()
        except:
            pass
        try:
            self.driver.quit()
        except:
            pass
