from screenpy.web.locators import Locate


sport = Locate.by_class_name('global-header__logo')
weather = Locate.by_css('.wr-c-masthead foreignObject')


class News:

    @staticmethod
    def heading():
        return Locate.by_css('header #brand span.gs-u-vh')

    @staticmethod
    def nav_link(text):
        return Locate.by_xpath("//nav[@class='nw-c-nav__wide']//span[text()='{}']/parent::a".format(text))
