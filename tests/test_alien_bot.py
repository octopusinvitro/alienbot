from io import StringIO
import sys

from unittest import TestCase, mock

from alienbot.alien_babble import AlienBabble
from alienbot.alien_bot import AlienBot


class TestAlienBot(TestCase):
    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output
        self.alien_bot = AlienBot(AlienBabble('tests/fixtures/testbabble.json'))

    def tearDown(self):
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

    def test_greets_the_user(self):
        sys.stdin = StringIO('irrelevant\nirrelevant\n')
        self.alien_bot.greet()
        self.assertIn('Hello', self.output.getvalue())

    def test_when_greeting_asks_for_help_using_user_name(self):
        sys.stdin = StringIO('Name\nirrelevant\n')
        self.alien_bot.greet()
        self.assertIn('Help me Name', self.output.getvalue())

    def test_when_greeting_exits_if_user_wants_to_exit(self):
        sys.stdin = StringIO('Name\nI want to exit\n')
        self.alien_bot.greet()
        self.assertIn('Bye', self.output.getvalue())

    def test_when_greeting_exits_if_user_wont_help(self):
        sys.stdin = StringIO('Name\nNo\n')
        self.alien_bot.greet()
        self.assertIn('Bye', self.output.getvalue())

    def test_when_greeting_does_not_exit_if_user_will_help(self):
        sys.stdin = StringIO('Name\nYes\n')
        self.alien_bot.greet()
        self.assertNotIn('Bye', self.output.getvalue())

    @mock.patch('random.choice')
    def test_when_chatting_starts_with_a_question(self, mock_choice):
        mock_choice.side_effect = ['How are you?']
        sys.stdin = StringIO('Exit\n')
        self.alien_bot.chat()
        self.assertIn('How are you', self.output.getvalue())

    def test_when_chatting_exits_if_user_wants_to_exit(self):
        sys.stdin = StringIO('Exit\n')
        self.alien_bot.chat()
        self.assertIn('Bye', self.output.getvalue())

    @mock.patch('random.choice')
    def test_when_chatting_prints_bot_response(self, mock_choice):
        mock_choice.side_effect = ['How are you?', 'Bot answer']
        sys.stdin = StringIO('Why?\nExit\n')
        self.alien_bot.chat()
        self.assertIn('Bot answer', self.output.getvalue())

    @mock.patch('random.choice')
    def test_when_chatting_reflects_bot_response_before_printing(self, mock_choice):
        mock_choice.side_effect = ['How are you?', 'Why do you think {0}?']
        sys.stdin = StringIO('I think I like you\nExit\n')
        self.alien_bot.chat()
        self.assertIn('Why do you think you like I?', self.output.getvalue())
