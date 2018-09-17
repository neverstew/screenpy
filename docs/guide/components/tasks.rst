.. _tasks:
Tasks
=====

Tasks group interactions into sets that represent a task the user is trying to perform.  For example, the
interaction scenario we saw in the previous section represents the actor trying to login to a website.

Tasks are a robust way of describing how a user interacts with your system in order to accomplish something.  To understand
this concept, let's imagine a common scenario...

Goals Over Actions
------------------
Let's revisit the login scenario.  Our login process requires each user to enter a username and password, then submit
these input fields with a click of a button.  We start developing our test suite and quickly this becomes one of the most
duplicated bits of code.  Everyone has to login to perform anything on the system - so all the tests do it.

Three months later, a new story appears describing that the business wants to change the login process such that each
user must log in using a third-party service such as Facebook, Google or Github.  Now our login process has completely changed!
We're going to have to go through every single test and change it so that it performs a different selection of clicks and
input values in order to log in.

This is a bad place to be in as it makes your tests hard to maintain.  Many of you reading may have already guessed this
was coming as soon as I mentioned duplication - great!  This library asks you to use it in such a way that you reduce that
duplication by extracting all of the nitty-gritty interactions out into tasks.  What's more, by doing this you perform a
crucial thought exercise - extracting your business logic from your framework.

Creating Layers
---------------
Extracting business logic from view/interaction logic might sound familiar to anyone who's done any front end development
(or indeed any kind of development on a large-scale system).
Creating layers of abstraction is how a robust framework is built, as it allows the layers to change independently of each
other.

This framework is designed around many layers - so far we've pieced together two of them (actors and tasks).

Speed Bonus!
------------
On top of all of the benefits we've already been through, structuring tests this way means we can write out a test script
really quickly by thinking about the behaviour of the actor and writing this out in plain English.
The specifics of how a user does something can be worked out later. This is essential in being able to write tests from
the very beginning of the development cycle.

Without even knowing how the framework really fits together yet, we could write out most of a test script::

    derrick = Actor.called("Derrick").who_can(BrowseTheWeb)
    derrick.attempts_to([
        Login.with_credentials("derrick01", "D3rr1ck"),
        RequestPasswordChange.to("bigD2k18"),
        ConfirmPasswordChange.usingEmailLink("mysite.com/resetpassword/somehash")
    ])

    # now assert acceptance criteria 5, 6, 7

When working in a team, this is an activity that everyone on the team can get involved in and that means that everyone on the team has visibility
and crucially *confidence* in what has been/will be tested.

The Code
--------
Task objects must have an `interactions` attribute that returns an iterable containing the :ref:`Interactions` to perform.  That's it!

Let's have a look at an example::

    from screenpy.web.interactions import Type, Click
    from .page_objects import login
    from .tasks import NavigateToTheApp

    class Login:
        def __init__(self, email, password):
            self.email = email
            self.password = password

            self.interactions = [
                NavigateToTheApp,
                Type.into(login.email).the_words(self.email),
                Type.into(login.password).the_words(self.password),
                Click.on(login.sign_in)
            ]

        @classmethod
        def using(cls, email, password):
            return cls(email, password)

This task has a few notable things about it:
    1. We have added a class method that allows us to reference the class with a fluid syntax e.g. `Login.using(email, password)`
    2. We have set the interactions attribute with
        a. Another task - tasks can reference other tasks!
        b. Interactions objects performing the specifics of the task.

Creating Your Own Tasks
-----------------------
As long as your tasks follow the above interface, they can be performed by actors.