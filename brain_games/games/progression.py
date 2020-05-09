import random
DESCRIPTION = "What number is missing in the progression?"


def algorithm():
    start_choice = random.randrange(50)
    progression = random.randrange(1, 11)
    index = random.randrange(10)
    result = []
    for i in range(1, 11):
        start_choice += progression
        result.append(str(start_choice))
    answer = result[index]
    result[index] = '..'
    question = ' '.join(result)
    return question, answer
