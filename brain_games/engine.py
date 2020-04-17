import prompt


def engine(key, name):
    answer_count = 0
    rounds = 3
    for i in range(1, rounds + 1):
        question_value, answer_correct = key()
        print("Question: {}".format(question_value))
        answer_player = prompt.string('Your answer: ')
        if answer_player == answer_correct:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'.".format(answer_player,
                                                    answer_correct))
            print("Let's try again, {}!".format(name))
            break
        answer_count += 1
    if answer_count == rounds:
        print("Congratulations, {}!".format(name))
