compile:
	pip-compile

install:
	pip install -r requirements.txt

setup: compile install

run:
	flask run --reload --debugger

test:
	pytest
