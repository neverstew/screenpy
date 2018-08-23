from selenium.webdriver.common.by import By

from screenpy.web.abilities.browse_the_web import BrowseTheWeb


class Text:
    def __init__(self, locator, strategy=By.CSS_SELECTOR):
        self.locator = locator
        self.strategy = strategy

    @classmethod
    def on(cls, locator):
        return cls(locator)

    def found(self, strategy):
        self.strategy = strategy
        return self

    def answered_by(self, actor):
        return actor.ability_to(BrowseTheWeb).driver.find_element(self.strategy, self.locator).text()