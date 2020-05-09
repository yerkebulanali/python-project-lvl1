import random
import math
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    answer = 'yes'
    if (number <= 1) or (number > 2 and number % 2 == 0):
        answer = 'no'
    elif number == 2:
        answer = 'yes'
    for i in range(3, 1 + math.floor(math.sqrt(number)), 2):
        if number % i == 0:
            answer = 'no'
    return answer


def play_round():
    number = random.randrange(1, 100)
    question = str(number)
    return question, is_prime(number)
