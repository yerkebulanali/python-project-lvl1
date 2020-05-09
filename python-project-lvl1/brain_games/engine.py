import prompt


def greet(description):
    print('\nWelcome to the Brain Games!')
    print(description)
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def run(game, attempts=3):
    name = greet(game.DESCRIPTION)
    for i in range(attempts):
        question_value, answer_correct = game.play_round()
        print('\nQuestion: {}'.format(question_value))
        answer_player = prompt.string('Your answer: ')
        if not answer_player == answer_correct:
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'.".format(answer_player,
                                                    answer_correct))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')
    print('Congratulations, {}!'.format(name))
