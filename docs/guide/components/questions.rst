.. _questions:
Questions
=========

Questions are the way in which :ref:`actors` establish the state of the system.  They often manifest themselves as
read-only actions, such as reading text in a web browser or querying a database table.

Questions, like interactions, are enabled by abilities.  Questions may be asked by using the `Actor.sees` method::

    wilfred = Actor.called("Wilfred").who_can(BrowseTheWeb)
    message = wilfred.sees(Text.on(welcome.heading))

The Code
--------
Here is what a rudimentary implementation of the Text question might look like::

    from screenpy.web.abilities.browse_the_web import BrowseTheWeb


    class Text:
        def __init__(self, by):
            self.by = by

        @classmethod
        def on(cls, by):
            return cls(locator)

        def answered_by(self, actor):
            return actor.ability_to(BrowseTheWeb).driver.find_element(self.by).text

A question must have:
    1. An `answered_by` method
        a. that accepts an actor
        b. retrieves the required ability instance from the actor and
        c. returns the answer to the question

Any class that implements this interface will be compatible with the other components.

.. note::
    Questions should never change the state of the system.

Creating Your Own Questions
---------------------------
Creating your own questions is possible. As with :ref:`interactions`, questions are often agnostic of the specific app
and relate to devices that are used by many.  If you need to make a new question, please consider doing it
as part of this project.