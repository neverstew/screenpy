.. _abilities:
Abilities
=========

Once an actor has an ability, they can interact with the system using that ability.  Each ability encapsulates clients
such as a web driver, an http client or an email service.

Each interaction requests the ability from the actor that is attempting the interaction.  If the actor has that ability,
the ability will be passed back to the interaction along with the client it needs.  If the actor doesn't have the required
ability, then an exception will be thrown.

.. seealso::
    :ref:`questions` are also enabled by abilities.  We'll read more about them in the next section.

The Code
--------
Empowering an actor with an ability is done by calling the `who_can` method on the actor object.  Ability class names
can be passed as long as the constructor is empty, otherwise object instances must be passed::

    # okay
    Actor.called("dave").who_can(BrowseTheWeb)

    # okay
    Actor.called("helen").who_can(UseTheApp.on_a("iPhone X"))

    # not okay - class instance cannot be instantiated
    Actor.called("reginald").who_can(UseTheApp)

Instances of the abilities must (eventually) be used as this allows each actor to retain control over the lifecycle of their own
client(s).  This becomes especially important in more complex scenarios where we may want to test that, for example, a
change on the desktop client can also be seen in the mobile app.

Creating Your Own Abilities
---------------------------
Creating your own abilities is possible.  There is no set interface needed as this will differ depending on what
interactions/questions utilise the ability.

As with :ref:`interactions`, abilities are often agnostic of the specific app and relate to devices that are used by many.
If you need to make a new ability, please consider doing it as part of this project.

.. toctree::
    :caption: Built-in abilities:
    :glob:

    abilities/*