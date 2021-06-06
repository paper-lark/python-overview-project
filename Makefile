.PHONY: init format

init:
	echo -e "#!/usr/bin/env bash\nmake check" > .git/hooks/pre-commit
	chmod 755 .git/hooks/pre-commit
	poetry install

format:
	poetry run isort --line-length 88 overview
	poetry run black overview

check:
	# max length is based on Black defaults
	poetry run black --check overview
	# poetry run isort --line-length 88 --check-only overview
	poetry run flake8 --builtins='_' --extend-ignore=E203 --max-line-length 88 overview
	poetry run pydocstyle overview

l10n-update:
	poetry run pybabel extract overview -o overview/locale/base.pot
	poetry run pybabel update -i overview/locale/base.pot -d overview/locale

l10n-compile:
	poetry run pybabel compile -d overview/locale

unit-test:
	env PYTHONPATH=. poetry run pytest

sphinx-remake:
	-rm sphinx/src/overview.*
	poetry run sphinx-apidoc --implicit-namespaces -o sphinx/src overview
	poetry run sphinx-build -M html "sphinx" "sphinx/build"

sphinx-update:
	poetry run sphinx-apidoc --implicit-namespaces -o sphinx/src overview
	poetry run sphinx-build -M html "sphinx" "sphinx/build"
