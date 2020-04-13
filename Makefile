install:
	poetry install

config:
    poetry config repositories.yerkebulanali https://test.pypi.org/legacy/

build:
    poetry build

publish:
    poetry publish -r yerkebulanali

lint:
	poetry run flake8 brain_games