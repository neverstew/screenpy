from screenpy.web.locators import Locate


def material_design_dropdown(field_name):
    """
    The material design dropdown menu is implemented with a ul/li structure.  The <select> and <option> elements are
    hidden.  This prevents Selenium from interacting with them.

    This method provides you with the locator for the input field (which a user would normally click).

    :param field_name: name attribute of the form field
    """
    return Locate.by_xpath("//div[@id='id_{}_container']//input".format(field_name))


def material_design_dropdown_option(field_name, option_text):
    """
    The material design dropdown menu is implemented with a ul/li structure.  The <select> and <option> elements are
    hidden.  This prevents Selenium from interacting with them.

    This method provides you with the locator for the list elements (which a user would normally click after selecting
    the input field).

    :param field_name: name attribute of the form field
    :param option_text: the text of the option that should be located
    """
    return Locate.by_xpath("//div[@id='id_{}_container']//ul//span[contains(., '{}')]".format(field_name, option_text))
