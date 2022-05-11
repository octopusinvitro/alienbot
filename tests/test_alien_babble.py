from unittest import TestCase, mock

from alienbot.alien_babble import AlienBabble


class TestAlienBabble(TestCase):
    def setUp(self):
        self.alien_babble = AlienBabble('tests/fixtures/testbabble.json')

    def test_greets_the_user(self):
        self.assertEqual(self.alien_babble.greet(), 'Hello')

    def test_asks_someone_for_help(self):
        self.assertEqual(self.alien_babble.ask_for_help('Jane Doe'), 'Help me Jane Doe please')

    def test_detects_negative_answer(self):
        self.assertEqual(self.alien_babble.is_negative('no'), True)

    def test_detects_negative_answer_ignoring_case(self):
        self.assertEqual(self.alien_babble.is_negative('NO'), True)

    def test_detects_positive_answer(self):
        self.assertEqual(self.alien_babble.is_negative('Yes'), False)

    def test_detects_answer_with_exit_command(self):
        self.assertEqual(self.alien_babble.is_exit('I want to exit.'), True)

    def test_detects_answer_with_no_exit_command(self):
        self.assertEqual(self.alien_babble.is_exit('Hi.'), None)

    @mock.patch('random.choice')
    def test_asks_starter_question(self, mock_choice):
        mock_choice.side_effect = ['How are you?']
        self.assertEqual(self.alien_babble.ask_question(), 'How are you?\n')

    def test_says_goodbye(self):
        self.assertEqual(self.alien_babble.bye(), 'Bye\n')

    @mock.patch('random.choice')
    def test_returns_match_from_matching_choice(self, mock_choice):
        mock_choice.side_effect = ['Why not?!']
        self.assertEqual(self.alien_babble.lookup('why?')[0].group(), 'why?')

    @mock.patch('random.choice')
    def test_returns_random_answer_from_matching_choice(self, mock_choice):
        mock_choice.side_effect = ['Why not?!']
        self.assertEqual(self.alien_babble.lookup('why?')[1], 'Why not?!\n')

    @mock.patch('random.choice')
    def test_returns_random_answer_from_matching_choice_ignoring_case(self, mock_choice):
        mock_choice.side_effect = ['Why not?!']
        self.assertEqual(self.alien_babble.lookup('Why?')[1], 'Why not?!\n')

    def test_returns_default_answer_if_no_lookup_match(self):
        self.assertEqual(self.alien_babble.lookup('Hello'), AlienBabble.DEFAULT_ANSWER + '\n')

    def test_returns_reflection_from_lowercased_key(self):
        self.assertEqual(self.alien_babble.reflection("i'm"), 'you are')

    def test_returns_no_reflection_if_no_key(self):
        self.assertEqual(self.alien_babble.reflection('inexistent'), None)
