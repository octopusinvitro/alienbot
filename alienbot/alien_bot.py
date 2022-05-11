class AlienBot:
    def __init__(self, alien_babble):
        self._alien_babble = alien_babble

    def greet(self):
        self._name = input(self._alien_babble.greet())
        will_help = input(self._alien_babble.ask_for_help(self._name))

        if self._is_negative(will_help) or self._is_exit(will_help):
            return print(self._alien_babble.bye())

        return True

    def chat(self):
        response = input(self._alien_babble.ask_question())
        while not self._alien_babble.is_exit(response):
            response = self._next_response(response)

        print(self._alien_babble.bye())

    def _next_response(self, response):
        match, bot_response = self._alien_babble.lookup(response)
        reflected = bot_response.format(*[self._reflect(group) for group in match.groups()])
        return input(reflected)

    def _reflect(self, group):
        words = group.split()

        for index, word in enumerate(words):
            reflection = self._alien_babble.reflection(word)
            if reflection:
                words[index] = reflection

        return ' '.join(words)

    def _is_negative(self, response):
        return self._alien_babble.is_negative(response)

    def _is_exit(self, response):
        return self._alien_babble.is_exit(response)
