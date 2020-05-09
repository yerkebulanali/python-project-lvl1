import random
DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def play_round():
    number = random.randrange(1, 100)
    question = str(number)
    return question, 'yes' if number % 2 == 0 else 'no'
