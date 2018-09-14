.. _actors:
Actors
======

Actors are the central component of the screenplay pattern.  They represent users interacting with the system under test,
be that a human user, another machine communicating using the API or any other consumer of information.

All actors have a name.  As humans, we understand objects better when we can personify them.  By giving your actor objects
a name you make them instantly recognisable to those reading the test and give yourself some help remembering what the
actor is doing.

Create a new actor by giving it a name::

    from screenpy.core import Actor

    alex = Actor.called("Alex")

Actors do three things:
    1. Have abilities
    2. Interact with the system, usually when trying to complete tasks.
    3. Question the state of the system

Actors are given abilities with `who_can`, interact with the system using the `attempts_to` method and question the system with the `sees` method::

    from screenpy.web.abilities import BrowseTheWeb
    from screenpy.web.questions import Text
    from .tasks import Login

    jane = Actor.called("Jane").who_can(BrowseTheWeb)
    jane.attempts_to(Login.with_credentials("e@mail.com", "1234"))
    welcome = jane.sees(Text.on(landing_page.heading))

How each of these other components work will be detailed in later pages.  What's clear already is that Jane is trying to
accomplish the *task* of logging in.  :ref:`Tasks` are the way in which actors go about interacting with a system.

Read on to find out more about tasks.