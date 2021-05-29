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
	poetry run flake8 --builtins='_' --extend-ignore=E203 --max-line-length 88 src
	poetry run pydocstyle src

l10n-update:
	poetry run pybabel extract src -o src/locale/base.pot
	poetry run pybabel update -i src/locale/base.pot -d src/locale

l10n-compile:
	poetry run pybabel compile -d src/locale

unit-test:
	env PYTHONPATH=src poetry run pytest

sphinx-update:
	sphinx-apidoc --implicit-namespaces -o sphinx/src src
	sphinx-build -M html "sphinx" "sphinx/build"
