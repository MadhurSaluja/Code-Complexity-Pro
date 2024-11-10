
# Contributing to Code Complexity Pro

Thank you for your interest in contributing to Code Complexity Pro! This document will guide you through setting up and developing the project. Contributions are always welcome!

## Requirements

- Python 3.x
- Grok API Key (can be stored in a `.env` file or passed via command line)

## Installation

1. **Clone the Repository**
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/MadhurSaluja/Code-Complexity-Pro
   cd Code-Complexity-Pro
   ```

2. **Install Dependencies**
   Install the required dependencies with:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Credentials**
   Create a `.env` file in the root of the project with your Grok API credentials:
   ```bash
   API_KEY=your-grok-api-key
   BASE_URL=https://api.groq.com/openai/v1/chat/completions
   ```

## Code Formatting and Linting

To maintain a consistent code style, we use **Black** as our code formatter and **Flake8** as our linter.

### Black

- **Purpose**: Black automatically formats code to meet project standards.
- **Configuration**: Black’s line length is set to 88 characters to improve readability.
- **Usage**: Run Black manually or through the `Makefile` (see below), or configure it to format on save in your editor.

### Flake8

- **Purpose**: Flake8 is used to identify PEP 8 compliance and other coding issues.
- **Configuration**: We set Flake8’s max line length to 88 characters to match Black and ignore specific rules (`E203`, `E266`, `E501`, `W503`) to avoid conflicts.
- **Usage**: Run Flake8 manually or through the `Makefile` (see below), or set it up in your editor to check as you type.

### `.blackignore` File

The `.blackignore` file specifies files and directories Black should ignore, such as version control folders, virtual environments, and build artifacts.

## Makefile

A `Makefile` is included in the project to automate common tasks. Here are the main commands:

- **`make format`**: Formats all code with Black.
- **`make lint`**: Runs Flake8 to check for linting errors.
- **`make test`**: Runs all tests.
- **`make test-one TEST=<test_file>::<test_function>`**: Runs a specific test file or function.
- **`make watch`**: Automatically reruns tests on file changes.
- **`make install`**: Installs dependencies from `requirements.txt`.

Example usage:
```bash
make format    # Formats code
make lint      # Lints code
make test      # Runs all tests
make test-one TEST=tests/test_utils.py::test_function  # Runs a specific test
make watch     # Watches for changes and reruns tests
```

## Running Tests

We use **pytest** for testing.

1. **Run All Tests**:
   ```bash
   make test
   ```

2. **Run a Specific Test File or Function**:
   To run a specific test, specify the `TEST` variable:
   ```bash
   make test-one TEST=tests/test_utils.py::test_function
   ```

3. **Automatically Rerun Tests on Code Changes**:
   Use the `watch` command to monitor changes and rerun tests automatically:
   ```bash
   make watch
   ```

## Git Pre-Commit Hook

We use a pre-commit hook to automatically run Black and Flake8 on staged changes before they are committed.

1. **Install `pre-commit`**:
   ```bash
   pip install pre-commit
   ```

2. **Set Up the Hook**:
   The `.pre-commit-config.yaml` file defines the pre-commit hook settings.

3. **Activate the Pre-Commit Hook**:
   Run the following command to install the hook:
   ```bash
   pre-commit install
   ```

   **Result**: Black and Flake8 will now run on staged changes before every commit, ensuring compliance with project standards.

## Configuration

### TOML Configuration File Support

You can use a TOML configuration file to store default values for the API key and model, allowing the tool to run without needing to pass these values via the command line each time.

1. **Create a TOML Config File**:
   - In your home directory, create a hidden TOML config file named `.Code-complexity-pro-config.toml`.

   Example:
   ```toml
   model = "llama3-8b-8192"
   api_key = "your-api-key-here"
   ```

2. **Location**:
   - The tool will look for this configuration file in the home directory (`~/.Code-complexity-pro-config.toml`).

3. **Settings**:
   - `model`: The AI model to use for analysis (default: `llama3-8b-8192`).
   - `api_key`: Your API key for the analysis service.

### Command-Line Overrides

- If you provide `--model` or `--api-key` as command-line arguments, they will override the values in the TOML configuration file.

For example:
```bash
python main.py --model gpt-3.5 --api-key new-api-key your_file.py
```

This command will override the values from the TOML config file.

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.
