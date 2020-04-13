import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main
result = []
greet = main()
name = welcome_user()
key = ["no", "yes", "no"]
list = [15, 6, 7]


def even_odd():
    for number in list:
        print("Question: {}".format(number))
        answer = prompt.string("Your answer: ")
        if number % 2 == 0 and answer == "yes":
            print("Correct!")
        elif number % 2 == 0 and answer != "yes":
            print("'{}' is wrong answer ;(."
                  "Correct answer was 'yes'.".format(answer))
            print("Let's try again, {}!".format(name))
            break
        elif number % 2 != 0 and answer == "no":
            print("Correct!")
        elif number % 2 != 0 and answer != "no":
            print("'{}' is wrong answer ;(."
                  "Correct answer was 'no'.".format(answer))
            print("Let's try again, {}!".format(name))
            break
        result.append(answer)
    if result == key:
        print("Congratulations, {}!".format(name))
