import prompt


def welcome_user(slogan):
    print("Welcome to the Brain Games!")
    print(slogan)
    name = prompt.string('May I have your name? ')
    print("Hello, {}!\n".format(name))
    return name
