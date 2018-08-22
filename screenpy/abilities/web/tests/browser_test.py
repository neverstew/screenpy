from unittest import TestCase, skip

from ....abilities.web.browse_the_web import BrowseTheWeb


class TestBrowseTheWebAbility(TestCase):

    @skip
    def test_driver_lifecycle(self):
        """
        Sample test to check browser lifecycle
        """
        ability = BrowseTheWeb()
        ability.driver.get("http://www.google.com")
        self.assertTrue(ability.driver.title, "Google")
