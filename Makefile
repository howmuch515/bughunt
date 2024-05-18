.PHONY: install lint test format clean

PROJECT_NAME = bughunt-cli

install:
	rye sync && rye build && rye install --path ./dist/*.whl $(PROJECT_NAME)

reinstall: clean install
	
lint:
	rye run flake8 src/

test:
	rye run pytest tests/

fmt:
	rye run black src/ tests/

clean:
	rye uninstall $(PROJECT_NAME)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +
