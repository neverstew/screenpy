from screenpy.web.locators import Locate


news = Locate.by_css('header #brand span.gs-u-vh')
sport = Locate.by_class_name('global-header__logo')
weather = Locate.by_css('.wr-c-masthead foreignObject')
