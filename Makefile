#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = weather-prediction-model
PYTHON_VERSION = 3.10

# Detect operating system
UNAME := $(shell uname)

# Define the virtual environment activation command and Python command based on OS
ifeq ($(UNAME), Linux)
    ACTIVATE_VENV = . .venv/bin/activate
    PYTHON_INTERPRETER = python
else ifeq ($(UNAME), Darwin)  # macOS
    ACTIVATE_VENV = source .venv/bin/activate
    PYTHON_INTERPRETER = python3
else ifeq ($(OS), Windows_NT)  # Windows
    ACTIVATE_VENV = .venv\Scripts\activate
    PYTHON_INTERPRETER = python
endif

#################################################################################
# COMMANDS                                                                      #
#################################################################################

# Composite target: Set up virtual environment, install dependencies, and run flask
run: create_environment requirements run_flask

## Install Python Dependencies
.PHONY: requirements
requirements:
	@$(ACTIVATE_VENV) && $(PYTHON_INTERPRETER) -m pip install -U pip
	@$(ACTIVATE_VENV) && $(PYTHON_INTERPRETER) -m pip install -r requirements.txt

## Set up virtual environment
.PHONY: create_environment
create_environment:
	$(PYTHON_INTERPRETER) -m venv .venv
	@echo ">>> Virtual environment created. Activate with:"
	@echo "$(ACTIVATE_VENV)"

## Run Flask Application
.PHONY: run_flask
run_flask:
	@$(ACTIVATE_VENV) && cd api && $(PYTHON_INTERPRETER) -m flask --app app run --debug

## Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8 and black (use `make format` to do formatting)
.PHONY: lint
lint:
	@$(ACTIVATE_VENV) && flake8 src
	@$(ACTIVATE_VENV) && isort --check --diff --profile black src
	@$(ACTIVATE_VENV) && black --check --config pyproject.toml src

## Format source code with black
.PHONY: format
format:
	@$(ACTIVATE_VENV) && black --config pyproject.toml src

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

## Make Dataset
.PHONY: data
data:
	@$(ACTIVATE_VENV) && $(PYTHON_INTERPRETER) src/dataset.py

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := run

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)