from brain_games.cli import welcome_user
from brain_games.engine import engine
from brain_games.games.even import main


def brain_even():
    slogan = 'Answer "yes" if number even otherwise answer "no".\n'
    name = welcome_user(slogan)
    return engine(main, name)
