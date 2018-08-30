from unittest import TestCase, skipUnless
from urllib import parse
from selenium.common.exceptions import WebDriverException, NoSuchElementException
import os
import requests
import time

from screenpy.web.abilities.browse_the_web import BrowseTheWeb


def hub_running():
    hub_address = os.getenv("SELENIUM_HUB_ADDRESS", "http://localhost:4444/wd/hub")
    hub_url = parse.urlparse(hub_address)
    try:
        r = requests.get("{}://{}/grid/console/".format(hub_url.scheme, hub_url.netloc))
        return True if r.status_code == 200 else False
    except requests.ConnectionError:
        return False


@skipUnless(hub_running(), "hub not running - skipping driver configuration tests")
class TestBrowseTheWebAbility(TestCase):

    def tearDown(self):
        self.ability.driver.quit()

    def test_driver_lifecycle(self):
        """
        Simple test to check browser lifecycle
        """
        self.ability = BrowseTheWeb()
        self.ability.driver.get("http://www.google.com")
        self.assertTrue(self.ability.driver.title, "Google")

    def test_driver_timeout(self):
        """
        The nodes should be configured to shut down sessions after 60 seconds of inactivity.  This provides a fallback
        for tests that crash out and a general cleanup mechanism.
        These options are set in the docker-compose file as environment variables.
        The hub takes:
        - GRID_TIMEOUT=60
        - GRID_BROWSER_TIMEOUT=60
        The nodes take:
        - SE_OPTS=-timeout 60 -browserTimeout 60
        """
        self.ability = BrowseTheWeb()
        self.ability.driver.get("http://www.google.com")
        time.sleep(61)
        with self.assertRaises(WebDriverException):
            self.ability.driver.get("http://www.google.com")


    def test_implicit_wait_five_seconds(self):
        """
        The web drivers will try to find elements on a page, waiting for a maximum of 5 seconds for them to appear.
        """
        self.ability = BrowseTheWeb()
        self.ability.driver.get("http://www.google.com")
        start = time.perf_counter()
        with self.assertRaises(NoSuchElementException):
            self.ability.driver.find_element_by_class_name("non-existent-element")
        end = time.perf_counter()
        self.assertAlmostEqual(5.0, end - start, delta=0.5,
                               msg="The find element method did not take marginally longer\
                                    than the implicit wait time (5s).")
