# Variables (if you want to make the tools configurable)
PYTHON = python3
FORMATTER = black
LINTER = flake8
TEST_RUNNER = pytest

# Format code with Black
format:
	$(FORMATTER) .

# Run all tests
test:
	pytest

# Run a specific test file or function
test-one:
	@if [ -z "$(TEST)" ]; then \
		echo "Please specify a test file or function with TEST=<file>::<function>"; \
	else \
		pytest $(TEST); \
	fi

# Automatically rerun tests on file changes
watch:
	@echo "Watching for file changes... Press Ctrl+C to stop."
	@while inotifywait -r -e modify,create,delete ./; do \
		clear; \
		pytest; \
	done

# Install dependencies
install:
	$(PYTHON) -m pip install -r requirements.txt

# Lint code with Flake8
lint:
	$(LINTER) .

# Format and lint in one step
check: format lint
