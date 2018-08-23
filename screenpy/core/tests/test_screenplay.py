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

    @patch.object(DrawPicture, 'titled')
    def test_actor_attempts_to_perform_interactions(self, mock_draw):
        """
        Actor calls the 'perform_as_actor' method on the given interactions to enact them
        """
        james = Actor.called("james")
        examples = {
            "actor performs single interaction":
                [DrawPicture.titled('masterpiece')],
            "actor performs multiple interactions":
                [DrawPicture.titled('masterpiece'),
                 DrawPicture.titled('poor sequel')]
        }
        for desc, interact in examples.items():
            with self.subTest(desc):
                mock_draw.reset_mock()
                james.attempts_to(interact)
                self.assertEqual(mock_draw.return_value.perform_as_actor.call_count, len(interact))

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

    def test_can_perform_single_action_not_as_iterable(self):
        """
        A single, non-iterable, item can be attempted without blowing up
        """
        reginald = Actor.called("reginald").who_can(DrawPictures)
        reginald.attempts_to(DrawPicture.titled("memories of lie-ins"))

    def test_actor_performs_a_task(self):
        """
        Actors can perform tasks (made up of interactions) if they provide an 'interactions' attribute
        """
        interaction = MagicMock()

        class PerformTask:
            def __init__(self, things):
                self.interactions = things

        examples = {
            "task with one interaction": interaction,
            "task with one interaction in list": [interaction],
            "task with multiple interactions": [interaction, interaction, interaction]
        }

        for desc, interactions in examples.items():
            with self.subTest(desc):
                interaction.reset_mock()
                Actor.called("attenborough").attempts_to(PerformTask(interactions))
                self.assertEqual(interaction.perform_as_actor.call_count, len(interactions))

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
