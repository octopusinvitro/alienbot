import json
import random
import re


class AlienBabble:
    DEFAULT_ANSWER = '...'

    def __init__(self, filepath):
        self._alienbabble = self._read(filepath)

    def greet(self):
        return self._alienbabble['greet_message']

    def ask_for_help(self, name):
        return self._alienbabble['help_message'].format(name)

    def is_negative(self, response):
        return response.lower() in self._alienbabble['negative_responses']

    def is_exit(self, response):
        for exit_command in self._alienbabble['exit_commands']:
            if exit_command in response.lower():
                return True

    def ask_question(self):
        return self._line(random.choice(self._alienbabble['starter_questions']))

    def bye(self):
        return self._line(self._alienbabble['bye_message'])

    def lookup(self, response):
        for regex, responses in self._alienbabble['lookups']:
            match = re.match(regex, response.lower())
            if match:
                return (match, self._line(random.choice(responses)))

        return self._line(self.DEFAULT_ANSWER)

    def reflection(self, key):
        reflections = self._alienbabble['reflections'].items()
        return {key.lower(): value for key, value in reflections}.get(key, None)

    def _line(self, text):
        return text + '\n'

    def _read(self, filepath):
        with open(filepath, 'r') as file:
            return json.load(file)
