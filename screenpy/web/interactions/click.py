from selenium.webdriver.common.by import By

from ..abilities.browse_the_web import BrowseTheWeb


class Click:
    def __init__(self, locator, strategy=By.CSS_SELECTOR):
        self.locator = locator
        self.strategy = strategy

    @classmethod
    def on(cls, locator):
        return cls(locator)

    def finding(self, strategy):
        self.strategy = strategy
        return self

    def perform_as_actor(self, actor):
        actor.ability_to(BrowseTheWeb).driver.find_element(self.strategy, self.locator).click()
