compile:
	pip-compile

install:
	pip install -r requirements.txt

setup: compile install

run:
	python3 app/server.py
