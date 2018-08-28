import allure
import os
import urllib.parse

from ..abilities.browse_the_web import BrowseTheWeb
from ..helper import save_allure_screenshot_using


class Open:
    def __init__(self, url):
        base_url = os.getenv("APP_BASE_URL", "http://localhost:8000/")
        self.url = urllib.parse.urljoin(base_url, url)

    def perform_as(self, actor):
        with allure.step(self.__str__()):
            actor.ability_to(BrowseTheWeb).driver.get(self.url)
            save_allure_screenshot_using(actor)

    def __str__(self):
        return "Open URL: {}".format(self.url)
