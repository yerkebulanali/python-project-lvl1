import random


def main():
    operator = random.choice(['*', '+', '-'])
    first = random.randrange(100)
    second = random.randrange(100)
    question_value = "{} {} {}".format(first, operator, second)
    if operator == '-':
        return question_value, str(first - second)
    elif operator == '+':
        return question_value, str(first + second)
    elif operator == '*':
        return question_value, str(first * second)
