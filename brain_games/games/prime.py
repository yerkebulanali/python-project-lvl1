import random
import math
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_Prime(number):
    if number <= 1:
        return 'no'
    if number == 2:
        return 'yes'
    if number > 2 and number % 2 == 0:
        return 'no'
    for i in range(3, 1 + math.floor(math.sqrt(number)), 2):
        if number % i == 0:
            return 'no'
    return 'yes'


def algorithm():
    number = random.randrange(1, 100)
    question = str(number)
    return question, is_Prime(number)
