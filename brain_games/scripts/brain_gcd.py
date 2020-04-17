from brain_games.cli import welcome_user
from brain_games.engine import engine
from brain_games.games.gcd import main


def brain_gcd():
    slogan = "Find the greatest common divisor of given numbers.\n"
    name = welcome_user(slogan)
    return engine(main, name)
