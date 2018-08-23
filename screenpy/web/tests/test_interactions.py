from unittest import TestCase
from unittest.mock import patch
from selenium.webdriver.common.by import By

from ..abilities.browse_the_web import BrowseTheWeb
from ..interactions.click import Click
from ..interactions.type import Type
from ...core.actor import Actor


class TestClickInteractions(TestCase):

    def test_click_constructed_with_locator_and_strategy(self):
        """
        Click interaction can be constructed either: directly, using class method, using method to change selector strategy
        """
        examples = {
            "click constructed with constructor": Click("element", By.ID),
            "click constructed using class method and strategy": Click.on("element").finding(By.ID)
        }
        for desc, click in examples.items():
            with self.subTest(desc):
                self.assertEqual(click.locator, "element")
                self.assertEqual(click.strategy, By.ID)

    def test_click_defaults_to_css_selector(self):
        """
        The Click interaction should default to finding elements using css selectors
        """
        self.assertEqual(Click("#element").strategy, By.CSS_SELECTOR)

    @patch.object(Actor, 'called')
    def test_click_performance_calls_appropriate_methods(self, mock_actor):
        """
        The click interaction checks to be enabled and calls driver with correct info
        """
        mock_ability = mock_actor.return_value.ability_to.return_value

        big_fred = Actor.called("big fred")
        click = Click.on("element").finding(By.ID)
        click.perform_as_actor(big_fred)

        mock_actor.return_value.ability_to.assert_called_with(BrowseTheWeb)
        mock_ability.driver.find_element.assert_called_with(By.ID, "element")


class TestTypeInteractions(TestCase):

    def test_type_constructed_with_locator_and_strategy(self):
        """
        Type interaction can be constructed either: directly, using class methods
        """
        examples = {
            "type constructed with constructor": Type("element", strategy=By.ID, text="words"),
            "type constructed using class method, text and strategy": Type.into("element").the_words("words").finding(By.ID)
        }
        for desc, type in examples.items():
            with self.subTest(desc):
                self.assertEqual(type.locator, "element")
                self.assertEqual(type.strategy, By.ID)
                self.assertEqual(type.text, "words")

    def test_type_defaults(self):
        """
        The Type interaction should default to css selector and text=None
        """
        self.assertEqual(Type("#element").strategy, By.CSS_SELECTOR)
        self.assertEqual(Type("#element").text, None)

    @patch.object(Actor, 'called')
    def test_type_performance_calls_appropriate_methods(self, mock_actor):
        """
        The Type interaction checks to be enabled and calls driver with correct info
        """
        mock_ability = mock_actor.return_value.ability_to.return_value

        gertrude = Actor.called("gertrude")
        type_interaction = Type.into("element").the_words("burritos are my fave").finding(By.ID)
        type_interaction.perform_as_actor(gertrude)

        mock_actor.return_value.ability_to.assert_called_with(BrowseTheWeb)
        mock_ability.driver.find_element.assert_called_with(By.ID, "element")
        mock_ability.driver.find_element.return_value.send_keys.assert_called_with("burritos are my fave")
