from brain_games.cli import welcome_user
from brain_games.engine import engine
from brain_games.games.progression import main


def brain_progression():
    slogan = "What number is missing in the progression?\n"
    name = welcome_user(slogan)
    return engine(main, name)
