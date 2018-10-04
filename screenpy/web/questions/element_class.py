import allure
from pprint import pformat
from selenium.webdriver.common.by import By

from screenpy.web.abilities.browse_the_web import BrowseTheWeb
from ..helper import save_allure_screenshot_using


class Class:
    def __init__(self, locator, strategy=By.CSS_SELECTOR):
        self.locator = locator
        self.strategy = strategy

    @classmethod
    def on(cls, locator):
        try: # assume conforms to locator interface
            return cls(locator.locator, locator.strategy)
        except AttributeError:
            return cls(locator)

    def found(self, strategy):
        self.strategy = strategy
        return self

    def answered_by(self, actor):
        with allure.step(self.__str__()):
            save_allure_screenshot_using(actor)
            return actor.ability_to(BrowseTheWeb).driver\
                .find_element(self.strategy, self.locator).get_attribute("class")

    def __str__(self):
        return "examines element class on {}".format(pformat(vars(self)))
