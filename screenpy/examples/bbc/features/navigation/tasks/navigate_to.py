from screenpy.web.interactions import Click
from ....pages import navbar


class Navigate:
    def __init__(self, locator):
        self.interactions = [
            Click.on(locator)
        ]

    @classmethod
    def to_news(cls):
        return cls(navbar.news)

    @classmethod
    def to_sport(cls):
        return cls(navbar.sport)

    @classmethod
    def to_weather(cls):
        return cls(navbar.weather)