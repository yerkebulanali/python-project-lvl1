import random
DESCRIPTION = "Find the greatest common divisor of given numbers."


def gcd(first, second):
    return first if second == 0 else gcd(second, first % second)


def algorithm():
    first = random.randrange(100)
    second = random.randrange(100)
    question = "{} {}".format(first, second)
    return question, str(gcd(first, second))
