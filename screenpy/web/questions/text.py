import allure
from pprint import pformat
from selenium.webdriver.common.by import By

from screenpy.web.abilities.browse_the_web import BrowseTheWeb
from ..helper import save_allure_screenshot_using


class Text:
    def __init__(self, locator, strategy=By.CSS_SELECTOR, multiple=False):
        self.locator = locator
        self.strategy = strategy
        self.multiple = multiple

    @classmethod
    def on(cls, locator):
        try:  # assume conforms to locator interface
            return cls(locator.locator, locator.strategy)
        except AttributeError:
            return cls(locator)

    @classmethod
    def on_all(cls, locator):
        try:  # assume conforms to locator interface
            return cls(locator.locator, locator.strategy, multiple=True)
        except AttributeError:
            return cls(locator, multiple=True)

    def found(self, strategy):
        self.strategy = strategy
        return self

    def answered_by(self, actor):
        with allure.step(self.__str__()):
            save_allure_screenshot_using(actor)
            if self.multiple:
                return list(map(lambda el: el.text,
                           actor.ability_to(BrowseTheWeb).driver.find_elements(self.strategy, self.locator)))

            return actor.ability_to(BrowseTheWeb).driver.find_element(self.strategy, self.locator).text

    def __str__(self):
        return "examines element text on {}".format(pformat(vars(self)))
