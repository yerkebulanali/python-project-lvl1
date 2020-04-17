from brain_games.cli import welcome_user
from brain_games.engine import engine
from brain_games.games.calc import main


def brain_calc():
    slogan = "What is the result of the expression?\n"
    name = welcome_user(slogan)
    return engine(main, name)
