.. _page_objects:
Page Objects
============

Page Objects are a way of organising the interfaces to your application under test.  When attempting to house all of the
information about how the pages of your application are represented on various screens/devices, it is extremely helpful
to have that information organised in a sensible way.

Organisation
------------
Page objects represent pages or, more commonly in the modern web, page components.  On these objects we store information
relating to how to find and interact with elements on the page.

Locators
--------
Locators can be managed in this framework using the builtin `Locate.by_x` methods::

    from screenpy.web.locators import Locate

    title = Locate.by_id("#title")
    top_story = Locate.by_xpath("//article")

The page objects are kept as simple as possible - as a collection of variables in a file. This is by design as our
interactions and tasks will do the heavy lifting of describing how to use these elements to achieve user goals.

From the original screenplay article:

    PageObjects have been the staple of automated web testing for over seven years. Simon Stewart wrote the original
    Selenium PageObject wiki entry in 2009. The concept was introduced to help test-developers reduce maintenance
    issues that, for many, resulted in flaky tests. Some mistook this as issues with Selenium,
    rather than with their own coding practices.

Page objects are often the end of testing frameworks.  Screenpy and the screenplay pattern treats them as just the start
of something much bigger.