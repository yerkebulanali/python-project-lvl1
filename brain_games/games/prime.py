import random


def main():
    number = random.randrange(1, 100)
    question_value = '{}'.format(number)
    for i in list(range(2, number)):
        if (number % i) == 0:
            return question_value, 'no'
            break
    return question_value, 'yes'
