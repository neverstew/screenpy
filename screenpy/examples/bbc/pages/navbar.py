from screenpy.web.locators import Locate

def _nav_locator(text):
    return Locate.by_css('nav li.orb-nav-{}'.format(text))

news = _nav_locator('news')
sport = _nav_locator('sport')
weather = _nav_locator('weather')

search = Locate.by_id('orb-search-q')
