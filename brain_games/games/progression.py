import random


def main():
    start_choice = random.randrange(50)
    progression = random.randrange(1, 11)
    index = random.randrange(10)
    result = []
    for i in list(range(1, 11)):
        start_choice += progression
        result.append(start_choice)
    answer = result[index]
    result[index] = '..'
    question_value = ('{} '*len(result)).format(*result)
    return question_value, str(answer)
