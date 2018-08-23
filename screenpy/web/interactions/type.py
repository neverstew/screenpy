from selenium.webdriver.common.by import By

from ..abilities.browse_the_web import BrowseTheWeb


class Type:
    def __init__(self, locator, strategy=By.CSS_SELECTOR, text=None):
        self.text = text
        self.locator = locator
        self.strategy = strategy

    @classmethod
    def into(cls, locator):
        return cls(locator)

    def the_words(self, text):
        self.text = text
        return self

    def finding(self, strategy):
        self.strategy = strategy
        return self

    def perform_as_actor(self, actor):
        actor.ability_to(BrowseTheWeb).driver.find_element(self.strategy, self.locator).send_keys(self.text)
