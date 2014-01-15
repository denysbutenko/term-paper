APP_DIR = ./app/
ENV_DIR = ./.venv/
MANAGE = $(APP_DIR)manage.py

all: version test syntax
	@echo "\n\nBuild SUCCESS!"

deploy:
	python fabs.py my_deploy

fun:
	python $(MANAGE) runserver

shell:
	$(ENV_DIR)bin/python $(MANAGE) shell

version:
	@echo "Django version: " && $(MANAGE) --version

install:
	pip install -r src/requirements.txt

upgrade:
	pip install --upgrade -r src/requirements.txt

syntax:
	pep8 $(APP_DIR)blog
	pyflakes $(APP_DIR)blog

sync:
	$(MANAGE) syncdb --noinput
