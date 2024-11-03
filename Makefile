# Variables (if you want to make the tools configurable)
PYTHON = python3
FORMATTER = black
LINTER = flake8
TEST_RUNNER = pytest

# Format code with Black
format:
	$(FORMATTER) .

# Run tests with Pytest
test:
	$(TEST_RUNNER)

# Install dependencies
install:
	$(PYTHON) -m pip install -r requirements.txt

# Lint code with Flake8
lint:
	$(LINTER) .

# Format and lint in one step
check: format lint
