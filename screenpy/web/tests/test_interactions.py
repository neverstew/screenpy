import os
from unittest import TestCase
from unittest.mock import patch
from selenium.webdriver.common.by import By

from ..abilities.browse_the_web import BrowseTheWeb
from ..interactions.click import Click
from ..interactions.type import Type
from ..interactions.open import Open
from ..interactions.select import Select, Strategy
from ...core.actor import Actor


class TestClickInteractions(TestCase):

    def test_click_constructed_with_locator_and_strategy(self):
        """
        Click interaction can be constructed either: directly, using class method, using method to change selector strategy
        """
        examples = {
            "click constructed with constructor": Click("element", By.ID),
            "click constructed using class method and strategy": Click.on("element").found(By.ID)
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
        click = Click.on("element").found(By.ID)
        click.perform_as(big_fred)

        mock_actor.return_value.ability_to.assert_called_with(BrowseTheWeb)
        mock_ability.driver.find_element.assert_called_with(By.ID, "element")


class TestTypeInteractions(TestCase):

    def test_type_constructed_with_locator_and_strategy(self):
        """
        Type interaction can be constructed either: directly, using class methods
        """
        examples = {
            "type constructed with constructor": Type("element", strategy=By.ID, text="words"),
            "type constructed using class method, text and strategy": Type.into("element").the_words("words").found(By.ID)
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
        type_interaction = Type.into("element").the_words("burritos are my fave").found(By.ID)
        type_interaction.perform_as(gertrude)

        mock_actor.return_value.ability_to.assert_called_with(BrowseTheWeb)
        mock_ability.driver.find_element.assert_called_with(By.ID, "element")
        mock_ability.driver.find_element.return_value.send_keys.assert_called_with("burritos are my fave")


@patch.object(os, 'getenv')
class TestOpenInteraction(TestCase):

    def test_open_constructed_with_url(self, mock_getenv):
        """
        open interaction is constructed with relative url
        """
        mock_getenv.return_value = 'http://base_url.com/'
        self.assertEqual(Open("/login").url, "http://base_url.com/login")

    @patch.object(Actor, 'called')
    def test_open_performance_calls_appropriate_methods(self, mock_actor, mock_getenv):
        """
        The Type interaction checks to be enabled and calls driver with correct info
        """
        mock_getenv.return_value = 'http://base_url.com/'
        mock_ability = mock_actor.return_value.ability_to.return_value

        jimmy = Actor.called("jimmy")
        interaction = Open("/login")
        interaction.perform_as(jimmy)

        mock_actor.return_value.ability_to.assert_called_with(BrowseTheWeb)
        mock_ability.driver.get.assert_called_with("http://base_url.com/login")


class TestSelectInteraction(TestCase):

    def test_select_constructor_defaults(self):
        """
        The select interaction can be constructed with the constructor and sets defaults
        """
        select = Select("option 1")
        attributes = {
            "select default option value": (select.option_to_select, 'option 1'),
            "select default select_strategy value": (select.select_strategy, Strategy.text),
            "select default locator value": (select.locator, None),
            "select default locator_strategy value": (select.locator_strategy, By.CSS_SELECTOR)
        }
        for desc, data in attributes.items():
            with self.subTest(desc):
                self.assertEqual(data[0], data[1])

    def test_select_strategy_attribute_methods(self):
        """
        select_strategy attribute can be amended using class method
        """
        select = Select.option("one").by(Strategy.value)
        self.assertEqual(select.select_strategy, Strategy.value)

    def test_locator_attribute_methods(self):
        """
        locator attribute can be amended using class method
        """
        select = Select.option("one").from_dropdown("#dropdown")
        self.assertEqual(select.locator, "#dropdown")

    def test_locator_strategy_attribute_methods(self):
        """
        locator_strategy attribute can be amended using class method
        """
        select = Select.option("one").found(By.ID)
        self.assertEqual(select.locator_strategy, By.ID)
