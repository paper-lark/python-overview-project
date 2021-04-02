.PHONY: init format

init:
	echo "#!/usr/bin/env bash\npoetry run black --check .\npoetry run isort --check-only .\npoetry run flake8 .\npoetry run pydocstyle ." > .git/hooks/pre-commit
	chmod 755 .git/hooks/pre-commit
	poetry install

format:
	poetry run isort .
	poetry run black .
