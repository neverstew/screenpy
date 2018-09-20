import allure
import os
from unittest import TestCase, skip
from unittest.mock import patch
from selenium.webdriver.common.by import By

from ..abilities.browse_the_web import BrowseTheWeb
from screenpy.web.questions import *
from ...core.actor import Actor


class TestReadInteraction(TestCase):

    def test_text_constructed_with_locator_and_strategy(self):
        """
        text interaction can be constructed either: directly, using class methods
        """
        examples = {
            "text constructed with constructor": Text("element", strategy=By.ID),
            "text constructed using class method, text and strategy": Text.on("element").found(By.ID)
        }
        for desc, text in examples.items():
            with self.subTest(desc):
                self.assertEqual(text.locator, "element")
                self.assertEqual(text.strategy, By.ID)

    def test_text_defaults(self):
        """
        The text interaction should default to css selector and text=None
        """
        self.assertEqual(Text("#element").strategy, By.CSS_SELECTOR)

    @patch.object(allure, 'attach')
    @patch.object(Actor, 'called')
    def test_text_question_calls_appropriate_methods(self, mock_actor, mock_attach):
        """
        The text interaction checks to be enabled and calls driver with correct info
        """
        mock_ability = mock_actor.return_value.ability_to.return_value
        mock_ability.driver.find_element.return_value.text = "My$ecretPa$$word"

        randy = Actor.called("randy")
        text_interaction = Text.on("element").found(By.ID)
        text = text_interaction.answered_by(randy)

        self.assertEqual(text, "My$ecretPa$$word")
        mock_actor.return_value.ability_to.assert_called_with(BrowseTheWeb)
        mock_ability.driver.find_element.assert_called_with(By.ID, "element")


class TestOptionsQuestion(TestCase):

    def test_options_constructed_with_locator_and_strategy(self):
        """
        options interaction can be constructed either: directly, using class methods
        """
        examples = {
            "options constructed with constructor": Options("element", strategy=By.ID),
            "options constructed using class method, text and strategy": Options.of("element").found(By.ID)
        }
        for desc, options in examples.items():
            with self.subTest(desc):
                self.assertEqual(options.locator, "element")
                self.assertEqual(options.strategy, By.ID)

    def test_options_defaults(self):
        """
        The options interaction should default to css selector and text=None
        """
        self.assertEqual(Options("#element").strategy, By.CSS_SELECTOR)

    @skip  # until I figure out how to mock out the select class (as it has validation on the constructor input type)
    @patch.object(Actor, 'called')
    def test_options_question_calls_appropriate_methods(self, mock_actor):
        """
        The options interaction checks to be enabled and calls driver with correct info
        """
        mock_ability = mock_actor.return_value.ability_to.return_value
        mock_ability.driver.find_element.return_value.text.return_value = ["one", "two"]

        ellie = Actor.called("ellie")
        options_interaction = Options.of(".super-dropdown").found(By.ID)
        text = options_interaction.answered_by(ellie)

        self.assertEqual(text, ["one", "two"])
        mock_actor.return_value.ability_to.assert_called_with(BrowseTheWeb)
        mock_ability.driver.find_element.assert_called_with(By.ID, "element")


class TestURLQuestion(TestCase):
    @patch.object(allure, 'attach')
    @patch.object(Actor, 'called')
    def test_url_answer_calls_appropriate_methods(self, mock_actor, mock_attach):
        """
        The URL question checks to be enabled and calls driver with correct info
        """
        mock_ability = mock_actor.return_value.ability_to.return_value
        mock_ability.driver.current_url = "this"

        timmy = Actor.called("jimmy")
        question = URL()
        answer = question.answered_by(timmy)

        self.assertEqual("this", answer)
        mock_actor.return_value.ability_to.assert_called_with(BrowseTheWeb)
