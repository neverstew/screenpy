*******
Usage
*******

This library provides a friendlier way to write tests, based loosely upon the screenplay_ pattern.
It is primarily designed for use in conjunction with Selenium, but those modules are completely optional.

.. _screenplay: https://serenity-js.org/design/screenplay-pattern.html

A simple test might look like::

    from screenpy.core import Actor
    from screenpy.web.abilities import BrowseTheWeb
    from screenpy.web.questions import Text

    from .tasks import OpenTheBBCWebsite, Navigate
    from .page_objects import header


    def test_navigation_to_news():
        eddy = Actor.called("eddy").who_can(BrowseTheWeb)

        eddy.attempts_to([
            OpenTheBBCWebsite(),
            Navigate.to_news()
        ])

        assert eddy.sees(Text.on(header.news)) == "BBC News"

This would launch a local chrome driver, open the bbc website, navigate to the news section and then assert the heading
was displayed as expected.

The language that is used is important for multiple reasons:
    1. It makes it easy for *anyone* to understand what your functional tests are doing.  This is good for:
        a. Developers trying to debug why they broke something
        b. Business Analysts trying to determine what a test is doing
    2. It highlights the behaviour of the system by abstracting away the specifics of *how* the actor is achieving their goals,
       instead describing the *goals* that the actor has.

A clear distinction of responsibilities is an important concept in any object-oriented programming project.
It encourages SOLID code and helps with maintainability.  The screenplay model creates clear responsibilities across
your testing framework and keeps your test code as SOLID as your production code.

Installation
------------

This framework is available and open to download as a python module.  It must be grabbed straight from the source.  This
can be done by adding the following line to your requirements/pip file::

    -e git+https://bitbucket.org/wspdigitaluk/ui-testing.git#egg=screenpy

