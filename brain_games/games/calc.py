import random
import operator
DESCRIPTION = "What is the result of the expression?"


def algorithm():
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    first = random.randrange(100)
    second = random.randrange(100)
    operators_sign = random.choice(list(operators.keys()))
    answer = operators[operators_sign](first, second)
    question = "{} {} {}".format(first, operators_sign, second)
    return question, str(answer)
