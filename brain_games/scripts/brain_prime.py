from brain_games.cli import welcome_user
from brain_games.engine import engine
from brain_games.games.prime import main


def brain_prime():
    slogan = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'
    name = welcome_user(slogan)
    return engine(main, name)
