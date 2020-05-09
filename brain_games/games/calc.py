import random
import operator
DESCRIPTION = "What is the result of the expression?"


def play_round():
    OPERATIONS = (('+', operator.add), ('-', operator.sub), ('*', operator.mul))
    first = random.randrange(100)
    second = random.randrange(100)
    operators_sign, operation = random.choice(OPERATIONS)
    answer = operation(first, second)
    question = "{} {} {}".format(first, operators_sign, second)
    return question, str(answer)
