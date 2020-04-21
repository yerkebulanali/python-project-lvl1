import random
import math
description = "Find the greatest common divisor of given numbers."
attempts = 3


def algorithm():
    first = random.randrange(100)
    second = random.randrange(100)
    question_value = "{} {}".format(first, second)
    return question_value, str(math.gcd(first, second))
