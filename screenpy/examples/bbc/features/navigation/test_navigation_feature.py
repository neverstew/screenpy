import os
from unittest import TestCase, skipUnless
from screenpy.core import Actor
from screenpy.web.questions import Text
from screenpy.web.abilities import BrowseTheWeb

from ...pages import header
from ...pages import article
from ..common.tasks.open_the_bbc_site import OpenTheBBCWebsite
from .tasks.news_top_story import NavigateToUkTopStory
from .tasks.navigate_to import Navigate


@skipUnless(os.getenv("TEST_RUN_WEB") == 'True', "Tests skipped - only for demonstration purposes.")
class TestNavigation(TestCase):

    def setUp(self):
        self.eddy = Actor.called("eddy").who_can(BrowseTheWeb)
        self.eddy.attempts_to(OpenTheBBCWebsite())

    def tearDown(self):
        self.eddy.ability_to(BrowseTheWeb).driver.quit()

    def test_navigation_to_news(self):
        self.eddy.attempts_to(
            Navigate.to_news()
        )

        heading = self.eddy.sees(
            Text.on(header.News.heading())
        )

        self.assertEqual('BBC News', heading)

    def test_select_featured_story(self):
        self.eddy.attempts_to(
            NavigateToUkTopStory()
        )

        heading = self.eddy.sees(
            Text.on(article.heading)
        )

        print(heading)
