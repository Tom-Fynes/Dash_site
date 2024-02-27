project_dir := $(shell pwd)
artifact_dir := dist
app_loc := $(wildcard logic)
logic_dir := $(wildcard logic/)
tests_dir := $(wildcard tests)
unit_tests_dir := $(tests_dir)/unit

.PHONY: run
run:
	poetry run python $(app_loc)/app.py

.PHONY: test
test:
	poetry run python -m pytest -s $(unit_tests_dir)

.PHONY: lint
lint:
	poetry run isort $(logic_dir) $(tests_dir)
	poetry run black $(logic_dir) $(tests_dir)
	poetry run python -m flake8 $(logic_dir) $(tests_dir)

.PHONY: install
install:
	poetry install
	pre-commit install

.PHONY: precommit
precommit:
	poetry run pre-commit run 
	poetry run pre-commit run check-merge-conflict