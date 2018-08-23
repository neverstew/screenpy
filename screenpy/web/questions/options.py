from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from screenpy.web.abilities.browse_the_web import BrowseTheWeb


class Options:
    def __init__(self, locator, strategy=By.CSS_SELECTOR):
        self.locator = locator
        self.strategy = strategy

    @classmethod
    def of(cls, locator):
        return cls(locator)

    def found(self, strategy):
        self.strategy = strategy
        return self

    def answered_by(self, actor):
        return Select(actor.ability_to(BrowseTheWeb).driver.find_element(self.strategy, self.locator)).options
