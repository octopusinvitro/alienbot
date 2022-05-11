from alienbot.alien_babble import AlienBabble
from alienbot.alien_bot import AlienBot


def main():
    alienbot = AlienBot(AlienBabble('data/alienbabble.json'))

    chat = alienbot.greet()
    if chat:
        alienbot.chat()


main()
