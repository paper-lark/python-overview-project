.PHONY: init format

init:
	echo "#!/usr/bin/env bash\nmake check" > .git/hooks/pre-commit
	chmod 755 .git/hooks/pre-commit
	poetry install

format:
	poetry run isort .
	poetry run black .

check:
	poetry run black --check .
	poetry run isort --check-only .
	poetry run flake8 .
	poetry run pydocstyle .
