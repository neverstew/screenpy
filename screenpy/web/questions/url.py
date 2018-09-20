import allure
from pprint import pformat

from screenpy.web.abilities.browse_the_web import BrowseTheWeb
from ..helper import save_allure_screenshot_using


class URL:
    def answered_by(self, actor):
        with allure.step(self.__str__()):
            save_allure_screenshot_using(actor)
            return actor.ability_to(BrowseTheWeb).driver.current_url

    def __str__(self):
        return "Sees URL: {}".format(pformat(vars(self)))
