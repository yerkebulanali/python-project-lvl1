import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!\n".format(name))
    return name
