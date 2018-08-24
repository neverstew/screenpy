from selenium.webdriver.common.by import By


class _TypedLocator:
    def __init__(self, strategy, locator):
        self.strategy = strategy
        self.locator = locator


class _ClassNameLocator(_TypedLocator):
    def __init__(self, locator):
        super(_ClassNameLocator, self).__init__(By.CLASS_NAME, locator)


class _CssLocator(_TypedLocator):
    def __init__(self, locator):
        super(_CssLocator, self).__init__(By.CSS_SELECTOR, locator)


class _IdLocator(_TypedLocator):
    def __init__(self, locator):
        super(_IdLocator, self).__init__(By.ID, locator)


class _LinkTextLocator(_TypedLocator):
    def __init__(self, locator):
        super(_LinkTextLocator, self).__init__(By.LINK_TEXT, locator)


class _NameLocator(_TypedLocator):
    def __init__(self, locator):
        super(_NameLocator, self).__init__(By.NAME, locator)


class _PatialLinkTextLocator(_TypedLocator):
    def __init__(self, locator):
        super(_PatialLinkTextLocator, self).__init__(By.PARTIAL_LINK_TEXT, locator)


class _TagNameLocator(_TypedLocator):
    def __init__(self, locator):
        super(_TagNameLocator, self).__init__(By.TAG_NAME, locator)


class _XPathLocator(_TypedLocator):
    def __init__(self, locator):
        super(_XPathLocator, self).__init__(By.XPATH, locator)


class Locate:
    @staticmethod
    def by_class_name(locator):
        return _ClassNameLocator(locator)

    @staticmethod
    def by_css(locator):
        return _CssLocator(locator)

    @staticmethod
    def by_id(locator):
        return _IdLocator(locator)

    @staticmethod
    def by_link_text(locator):
        return _LinkTextLocator(locator)

    @staticmethod
    def by_name(locator):
        return _NameLocator(locator)

    @staticmethod
    def by_partial_link_text(locator):
        return _PatialLinkTextLocator(locator)

    @staticmethod
    def by_tag_name(locator):
        return _TagNameLocator(locator)

    @staticmethod
    def by_xpath(locator):
        return _XPathLocator(locator)
