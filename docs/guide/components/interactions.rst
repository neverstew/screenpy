.. _interactions:
Interactions
============

Interactions are the way that actors change their surroundings.  We'll dive straight into an example.

We've already encountered two very common interactions - `Type` and `Click`.  They are some
of the most commonly used interactions in the framework as (along with `Open`) make up the core elements of navigating
the web. In our login task we saw::

    Type.into(login.email).the_words(self.email),
    Type.into(login.password).the_words(self.password),
    Click.on(login.sign_in)

The screenpy library currently comes with browser interactions built-in.  There is scope to incorporate other interaction
methods.  Raise an issue on the repo!

.. note::
   Though we've covered a lot of web-specific interactions, they are not always the only way that a user will interact with our
   system.  There could be access via an API, an email client, SMS, mobile apps and many more.

Enabling Interactions
---------------------
One of the fundamental aspects of the interactions is that they must be *enabled* by :ref:`abilities`.

.. seealso::
   :ref:`abilities` will be covered in more depth later.  As an easy example, for an actor to open a web page they must have
   the ability to `BrowseTheWeb`.

The Code
--------
The in-built `Open` interaction looks roughly like this::

    import os
    import urllib.parse

    from ..abilities.browse_the_web import BrowseTheWeb

    class Open:
        def __init__(self, url):
            base_url = os.getenv("APP_BASE_URL", "http://localhost:8000/")
            self.url = urllib.parse.urljoin(base_url, url)

        def perform_as(self, actor):
            actor.ability_to(BrowseTheWeb).driver.get(self.url)

        def __str__(self):
            return "Open URL: {}".format(self.url)


Interactions must:
    1. implement the `perform_as` method
        a. accepting an actor
        a. calling `actor.ability_to(AbilityClass)` in order to enable the interaction


Creating Your Own Interactions
------------------------------
As long as your interactions follow the above interface, they can be consumed by the screenpy components.

That said, interactions tend to be agnostic of any particular testing framework and are instead specific to the platform
that the user is interacting with.  If you happen to develop a new form of interaction - please consider doing so as a
part of this framework.

Performing Interactions
-----------------------
The primary way to perform an interaction is for it to be part of a task.  However, it is also possible for actors to
directly perform interactions for those instances when a test needs to describe an edge-case interaction.

Interactions may also be passed to the `Actor.attempts_to` method.