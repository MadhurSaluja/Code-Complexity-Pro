
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

The `.blackignore` file specifies files and directories Black should ignore, such as version control folders, virtual environments, and build artifacts. Here’s an example:

```plaintext
# .blackignore
.git/
__pycache__/
venv/
.venv/
build/
dist/
.vscode/
```

## Makefile

A `Makefile` is included in the project to automate common tasks. Here are the main commands:

- **`make format`**: Formats all code with Black.
- **`make lint`**: Runs Flake8 to check for linting errors.
- **`make install`**: Installs dependencies from `requirements.txt`.

Example usage:
```bash
make format    # Formats code
make lint      # Lints code
make install   # Installs dependencies
```

## Editor and IDE Integration

To ensure consistent styling and linting while coding, we recommend using **Visual Studio Code**. A `.vscode/settings.json` file is provided to configure Black and Flake8.

1. **Install the Python Extension**:
   - In VS Code, go to the Extensions view (⇧⌘X or Ctrl+Shift+X).
   - Search for "Python" by Microsoft and install it.

2. **Project Configuration**:
   - The `.vscode/settings.json` file configures Black as the formatter and Flake8 as the linter.
   - **Automatic Formatting**: Black will format code on save.
   - **Linting**: Flake8 will underline errors and warnings in real-time.

3. **Settings**:
   - Black’s line length and Flake8’s ignored errors are pre-configured in `.vscode/settings.json`:

     ```json
     {
       "python.formatting.provider": "black",
       "editor.formatOnSave": true,
       "python.linting.flake8Enabled": true,
       "python.linting.enabled": true,
       "python.formatting.blackArgs": ["--line-length", "88"],
       "python.linting.flake8Args": ["--max-line-length=88", "--ignore=E203,E266,E501,W503"],
       "files.exclude": {
         "**/__pycache__": true,
         "**/.git": true,
         "**/.vscode": true,
         "**/venv": true
       }
     }
     ```

## Git Pre-Commit Hook

We use a pre-commit hook to automatically run Black and Flake8 on staged changes before they are committed.

1. **Install `pre-commit`**:
   ```bash
   pip install pre-commit
   ```

2. **Set Up the Hook**:
   The `.pre-commit-config.yaml` file defines the pre-commit hook settings:

   ```yaml
   # .pre-commit-config.yaml
   repos:
     - repo: https://github.com/psf/black
       rev: 22.3.0  # Use the latest Black version
       hooks:
         - id: black
           args: ["--line-length", "88"]
     - repo: https://github.com/pycqa/flake8
       rev: 4.0.1  # Use the latest Flake8 version
       hooks:
         - id: flake8
           args: ["--max-line-length=88", "--ignore=E203,E266,E501,W503"]
   ```

3. **Activate the Pre-Commit Hook**:
   Run the following command to install the hook:
   ```bash
   pre-commit install
   ```

   **Result**: Black and Flake8 will now run on staged changes before every commit, ensuring compliance with project standards.

## Configuration

### TOML Configuration File Support

You can use a TOML configuration file to store default values for the API key and model, allowing the tool to run without needing to pass these values via the command line each time.

### How to Use the Configuration File

1. **Create a TOML Config File**:
   - In your home directory, create a hidden TOML config file named `.your-toolname-config.toml` (replace "your-toolname" with the actual tool name).

   Example:
   ```toml
   model = "llama-v2"
   api_key = "your-api-key-here"
   ```

2. **Location**:
   - The tool will look for this configuration file in the home directory (`~/.your-toolname-config.toml`).

3. **Settings**:
   - `model`: The AI model to use for analysis (default: `llama-v2`).
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
