import os
import urllib.parse

from ..abilities.browse_the_web import BrowseTheWeb


class Open:
    def __init__(self, url):
        base_url = os.getenv("APP_BASE_URL", "http://localhost:8000/")
        self.url = urllib.parse.urljoin(base_url, url)

    def perform_as(self, actor):
        actor.ability_to(BrowseTheWeb).driver.get(self.url)
