import random


def main():
    number = random.randrange(1, 100)
    question_value = "{}".format(number)
    if number % 2 == 0:
        return question_value, 'yes'
    else:
        return question_value, 'no'
