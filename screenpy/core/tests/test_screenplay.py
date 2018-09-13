from unittest import TestCase
from unittest.mock import patch as patch
from unittest.mock import MagicMock

from screenpy.core.actor import Actor
from screenpy.core.tests.abilities.take_notes import TakeNotes
from screenpy.core.tests.abilities.draw_pictures import DrawPictures
from screenpy.core.tests.interactions.draw_picture import DrawPicture


class TestActor(TestCase):

    def test_actor_can_have_name(self):
        """
        Actor has a name that allows him to be distinguised in an easy-to-read way.
        """

        name = "steven"
        examples = {
            "name via constructor": Actor(name),
            "name via class method": Actor.called(name)
        }
        for desc, actor in examples.items():
            with self.subTest(desc):
                self.assertEqual(actor.name, name)

    def test_actor_can_have_single_ability(self):
        """
        Actors can be assigned a single ability
        """
        henry = Actor.called("henry").who_can(TakeNotes)
        self.assertEqual(henry.can(TakeNotes), True)

    def test_actor_can_have_multiple_abilities(self):
        """
        Actors can be assigned multiple abilities in one call
        """
        henry = Actor.called("henry").who_can(TakeNotes, DrawPictures)
        self.assertEqual(henry.can(TakeNotes), True)
        self.assertEqual(henry.can(DrawPictures), True)

    def test_actor_can_have_abilities_with_attributes(self):
        """
        Actors can be assigned abilities using instances as well as types
        """
        alison = Actor.called("alison").who_can(TakeNotes.using(dict()))
        self.assertEqual(alison.can(TakeNotes), True)

    def test_actor_returns_false_when_asked_for_ability_not_present(self):
        """
        The 'can' method returns false when the ability is not present
        """
        gob = Actor.called("Gob")
        self.assertEqual(gob.can(TakeNotes), False)

    def test_actor_returns_original_ability_object(self):
        """
        The ability object returned on querying the actor is the original object used.  In other words,
        the object attributes on abilities are maintained.
        """
        ability = DrawPictures.using("brushes")
        ellie = Actor.called("ellie").who_can(ability)
        self.assertEqual(ellie.ability_to(DrawPictures), ability)

    def test_ability_to_returns_ability_instance_if_class_provided(self):
        """
        Given you specified the ability of the actor with the class name of the ability,
        When you request the ability of the actor,
        Then you get a new instance of the ability
        """
        jane = Actor.called("jane").who_can(DrawPictures)
        ability = jane.ability_to(DrawPictures)
        self.assertTrue(isinstance(ability, DrawPictures),
                        "ability {} not instance of {}".format(ability, DrawPictures.__name__))

    def test_actor_attempts_to_perform_single_interaction(self):
        """
        Actor calls the 'perform_as' method on the given interactions to enact them
        """
        interaction = Interaction()

        james = Actor.called("james")
        james.attempts_to(interaction)
        self.assertEqual(interaction.call_count, 1)

    def test_actor_attempts_to_perform_multiple_interactions(self):
        """
        Actor calls the 'perform_as' method on the given interactions to enact them
        """
        interaction = Interaction()

        james = Actor.called("james")
        james.attempts_to([interaction, interaction])
        self.assertEqual(interaction.call_count, 2)

    def test_interactions_not_passed_as_iterable(self):
        """
        Actor passed actions not as iterable should blow up
        """
        jerry = Actor.called("jerry")
        with self.assertRaises(TypeError):
            jerry.attempts_to(
                DrawPicture.titled("the vast nothingness of outer space"),
                DrawPicture.titled("swans on holiday")
            )

    def test_actor_attempts_to_perform_tasks(self):
        """
        Actors can perform tasks (made up of interactions) if they provide an 'interactions' attribute
        """
        interaction = Interaction()

        examples = {
            "one task with one interaction": ([PerformTask([interaction])], 1),
            "one task with multiple interactions": ([PerformTask([interaction, interaction, interaction])], 3),
            "multiple tasks with multiple interactions": ([
                PerformTask([interaction, interaction, interaction]),
                PerformTask([interaction, interaction, interaction])
            ], 6)
        }

        for desc, (interactions, expected_call_count) in examples.items():
            with self.subTest(desc):
                interaction.reset()
                Actor.called("attenborough").attempts_to(PerformTask(interactions))
                self.assertEqual(interaction.call_count, expected_call_count)

    def test_actor_attempts_to_perform_arbitrary_mixture_of_interactions(self):
        """
        Actors can perform tasks (made up of interactions) if they provide an 'interactions' attribute
        """
        interaction = Interaction()

        Actor.called("harriet").attempts_to([
            PerformTask([interaction]),
            interaction,
            [interaction, interaction],
            PerformTask([interaction, interaction])
        ])
        self.assertEqual(interaction.call_count, 6)

    def test_actor_asks_questions_about_their_environment(self):
        """
        Actors can seek answers to questions about their environment and
        resolve answers if the question provides an 'answered_by' method.

        These questions would normally be answered using the abilities of the actor (here it is simplified).
        """
        class NumberOfRedBalloons:
            @classmethod
            def left(cls):
                return cls()

            def answered_by(self, actor):
                return 99

        self.assertEqual(Actor.called("nena").sees(NumberOfRedBalloons.left()), 99)


class Interaction:
    def __init__(self):
        self.call_count = 0

    def perform_as(self, _):
        self.call_count += 1

    def reset(self):
        self.call_count = 0


class PerformTask:
    def __init__(self, *things):

        self.interactions = [thing for thing in things]
