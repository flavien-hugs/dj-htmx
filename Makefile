MANAGE := python manage.py

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv: ## Make a new virtual environment
	pipenv shell

.PHONY: install
install: venv ## Install or update dependencies
	pipenv install

freeze: ## Pin current dependencies
	pipenv run pip freeze > requirements.txt

migrate: ## Make and run migrations
	$(MANAGE) makemigrations
	$(MANAGE) migrate

collectstatic: ## Run collectstatic
	$(MANAGE) collectstatic --noinput

changepassword: ## Change password superuser
	$(MANAGE) changepassword admin@pm.me

.PHONY: createsuperuser
createsuperuser: ## Run the Django server
	$(MANAGE) createsuperuser --email="admin@pm.me"

.PHONY: dumpdata
dumpdata: ## dumpdata on database
	$(MANAGE) dumpdata --indent=4 --natural-foreign --natural-primary -e contenttypes --format=json tasks.collection > fixtures/collection.json

.PHONY: loaddata
loaddata: ## Load default data
	$(MANAGE) loaddata fixtures/*.json
