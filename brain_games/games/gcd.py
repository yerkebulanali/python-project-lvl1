import random
import math


def main():
    first = random.randrange(100)
    second = random.randrange(100)
    question_value = "{} {}".format(first, second)
    return question_value, str(math.gcd(first, second))
