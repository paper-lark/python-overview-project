.PHONY: init format

init:
	echo -e "#!/usr/bin/env bash\nmake check" > .git/hooks/pre-commit
	chmod 755 .git/hooks/pre-commit
	poetry install

format:
	poetry run isort --line-length 88 src
	poetry run black src

check:
	# max length is based on Black defaults
	poetry run black --check src
	poetry run isort --line-length 88 --check-only src
	poetry run flake8 --max-line-length 88 src
	poetry run pydocstyle src
