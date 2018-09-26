from screenpy.web.locators import Locate


def field(field_name):
    """
    Return the locator for any field displayed on a django model form.

    :param field_name: name of the field
    :return: the locator for the field with the corresponding name
    """
    return Locate.by_name(field_name)


def field_error(field_name):
    """
    Return the locator for the error message associated with a model field widget.

    :param field_name: name of the field
    :return: the locator for the field error associated with the field
    """
    return Locate.by_css("#id_{}_container .errors .error".format(field_name))


submit = Locate.by_css("button[type='submit']")
