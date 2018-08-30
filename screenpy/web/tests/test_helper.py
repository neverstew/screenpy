from unittest import TestCase
from unittest.mock import patch

from screenpy.core import Actor
from screenpy.web.helper import *


class TestHelper(TestCase):

    @patch('allure.attach')
    @patch.object(Actor, 'called')
    def test_attach_screenshot_calls_allure(self, mock_actor, mock_attach):
        """
        screenshot helper method calls allure plugin with correct arguments
        """
        mock_actor.ability_to.return_value.get_screenshot.return_value = "image"

        save_allure_screenshot_using(mock_actor)

        mock_attach.assert_called_once_with("image", "screenshot", allure.attachment_type.PNG)

    @patch('allure.attach')
    @patch.object(Actor, 'called')
    def test_attach_screenshot_error_prints_out(self, mock_actor, mock_attach):
        """
        screenshot helper method calls allure plugin with correct arguments
        """
        error = RuntimeError("error")
        mock_actor.ability_to.return_value.get_screenshot.side_effect = error

        save_allure_screenshot_using(mock_actor)

        call_args_list = mock_attach.call_args_list
        self.assertEqual(1, len(call_args_list))
        call_args = call_args_list[0]
        self.assertTrue('RuntimeError: error' in call_args[0][0], "RuntimeError: error not in {}".format(call_args[0]))
        self.assertEqual("screenshot-error", call_args[0][1])
        self.assertEqual(allure.attachment_type.TEXT, call_args[0][2])
