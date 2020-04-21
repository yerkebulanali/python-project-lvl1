import prompt


def greet(description=None):
    print("\nWelcome to the Brain Games!")
    if description is not None:
        print(description)
    name = prompt.string('\nMay I have your name? ')
    print("Hello, {}!".format(name))
    return name


def run(game):
    name = greet(game.description)
    for i in range(game.attempts):
        question_value, answer_correct = game.algorithm()
        print("\nQuestion: {}".format(question_value))
        answer_player = prompt.string('Your answer: ')
        if answer_player == answer_correct:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'.".format(answer_player,
                                                    answer_correct))
            print("Let's try again, {}!".format(name))
            return
    print("Congratulations, {}!".format(name))
