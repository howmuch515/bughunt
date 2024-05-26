.PHONY: install lint test format clean

PROJECT_NAME = bughunt-cli

install:
	rye sync && rye build && rye install --path ./dist/*.whl $(PROJECT_NAME)

reinstall: clean install
	
lint:
	rye run ruff check

test:
	rye run pytest tests/

fmt:
	rye run ruff format

clean:
	rye uninstall $(PROJECT_NAME)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +
