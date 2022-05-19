SHELL := /bin/bash

manage_py := python app/manage.py

migrate:
	$(manage_py) migrate

shell:
	$(manage_py) shell_plus --print-sql

run:
	$(manage_py) runserver 0:8000

run-dev: migrate \
	run

worker:
	cd app && celery -A settings worker -l info -c 2

beat:
	cd app && celery -A settings beat -l info

pytest:
	pytest ./app/tests --cov=app --cov-report html -vv && coverage report --fail-under=67
