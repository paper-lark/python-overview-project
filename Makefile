.PHONY: init format

init:
	echo -e "#!/usr/bin/env bash\nmake check" > .git/hooks/pre-commit
	chmod 755 .git/hooks/pre-commit
	poetry install

format:
	poetry run isort src
	poetry run black src

check:
	poetry run black --check src
	poetry run isort --check-only src
	poetry run flake8 --max-line-length 88 src # max length is based on Black defaults
	poetry run pydocstyle src
