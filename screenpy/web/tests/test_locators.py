from unittest import TestCase
from selenium.webdriver.common.by import By

from screenpy.web.locators import Locate


class TestLocatorClasses(TestCase):

    def test_each_class_sets_correct_strategy(self):
        """
        Each of the typed locator classes correctly define their locating strategy and locator
        """
        locator = '#my_button'

        examples = {
            Locate.by_class_name(locator): By.CLASS_NAME,
            Locate.by_css(locator): By.CSS_SELECTOR,
            Locate.by_id(locator): By.ID,
            Locate.by_link_text(locator): By.LINK_TEXT,
            Locate.by_name(locator): By.NAME,
            Locate.by_partial_link_text(locator): By.PARTIAL_LINK_TEXT,
            Locate.by_tag_name(locator): By.TAG_NAME,
            Locate.by_xpath(locator): By.XPATH
        }

        for locate, strat in examples.items():
            with self.subTest(locate.__str__()):
                self.assertEqual(locate.strategy, strat)
                self.assertEqual(locate.locator, locator)
