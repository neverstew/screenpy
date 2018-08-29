from screenpy.web.interactions import Click
from screenpy.examples.bbc.pages import navbar, header
from screenpy.examples.bbc.pages.news.uk import featured_story


class NavigateToUkTopStory:
    def __init__(self):
        self.interactions = [
            Click.on(navbar.news),
            Click.on(header.News.nav_link('UK')),
            Click.on(featured_story)
        ]