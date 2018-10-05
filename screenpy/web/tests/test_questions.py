import allure
from unittest import TestCase, skip
from unittest.mock import patch, MagicMock
from selenium.webdriver.common.by import By

from ..abilities.browse_the_web import BrowseTheWeb
from screenpy.web.questions import *
from screenpy.web.locators import Locate
from ...core.actor import Actor


class TestTextQuestion(TestCase):

    def test_text_constructed_with_locator_and_strategy(self):
        """
        text interaction can be constructed either: directly, using class methods
        """
        examples = {
            "text constructed with constructor": Text("element", strategy=By.ID),
            "text constructed using class method, text and strategy": Text.on("element").found(By.ID),
            "text constructed using class method for multiple elements": Text.on_all("element").found(By.ID)
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

    @patch.object(allure, 'attach')
    @patch.object(Actor, 'called')
    def test_text_question_calls_text_multiple_times_for_collections_of_elements(self, mock_actor, mock_attach):
        """
        The text interaction checks to be enabled and calls driver with correct info
        """
        mock_ability = mock_actor.return_value.ability_to.return_value
        mock_elements = [MagicMock(text=str(x)) for x in range(1, 3)]
        mock_ability.driver.find_elements.return_value = mock_elements

        leroy = Actor.called("leroy")
        text_interaction = Text.on_all("element").found(By.ID)
        text = text_interaction.answered_by(leroy)

        self.assertEqual(text, ["1", "2"])
        mock_actor.return_value.ability_to.assert_called_with(BrowseTheWeb)
        mock_ability.driver.find_elements.assert_called_once_with(By.ID, "element")


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


class TestClassQuestion(TestCase):
    def test_class_constructed_with_locator_and_strategy(self):
        """
        Clear question can be constructed either: directly, using class methods
        """
        examples = {
            "class constructed with constructor": Class("element", strategy=By.CSS_SELECTOR),
            "class constructed using class method, text and strategy": Class.on("element"),
            "class constructed using class method and Locator": Class.on(Locate.by_css("element"))
        }
        for desc, classs in examples.items():
            with self.subTest(desc):
                self.assertEqual(classs.locator, "element")
                self.assertEqual(classs.strategy, By.CSS_SELECTOR)

    @patch.object(allure, 'attach')
    @patch.object(Actor, 'called')
    def test_clear_performance_calls_appropriate_methods(self, mock_actor, mock_attach):
        """
        The class question checks to be enabled and calls driver with correct info
        """
        mock_ability = mock_actor.return_value.ability_to.return_value

        konrad = Actor.called("konrad")
        class_question = Class.on("element")
        class_question.answered_by(konrad)

        mock_actor.return_value.ability_to.assert_called_with(BrowseTheWeb)
        mock_ability.driver.find_element.assert_called_with(By.CSS_SELECTOR, "element")
        mock_ability.driver.find_element.return_value.get_attribute.assert_called_once_with('class')
