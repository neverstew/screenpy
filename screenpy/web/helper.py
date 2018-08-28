import allure
import traceback

from .abilities import BrowseTheWeb


def save_allure_screenshot_using(actor):
    try:
        allure.attach(actor.ability_to(BrowseTheWeb).get_screenshot(), "screenshot", allure.attachment_type.PNG)
    except:
        tb = traceback.format_exc()
        allure.attach(tb, "screenshot-error", allure.attachment_type.TEXT)
