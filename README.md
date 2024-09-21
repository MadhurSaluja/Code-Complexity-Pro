
# Code Complexity Analyzer

This command-line tool analyzes the complexity of source code files using Grok's LLM API. It supports multiple file inputs, customizable AI model selection, and configurable API settings.

## Features
- **Version Display**: Use `--version` or `-v` to display the tool's name and current version.
- **Help**: Use `--help` or `-h` to display the tool’s help message, showing how to run it, along with all available flags and arguments.
- **File Input**: Accept one or more files for analysis.
- **Output to stdout or file**: By default, outputs to stdout. You can specify an output file using the `--output` or `-o` flag.
- **LLM Model Selection**: Specify a model using the `--model` or `-m` flag (default: `llama-v2`).
- **API Key Configuration**: Optionally pass an API key via the `--api-key` or `-a` flag or configure it in the `.env` file.
- **Base URL Configuration**: Optionally pass a base API URL via the `--base-url` or `-u` flag or configure it in the `.env` file.
- **Error Handling**: Any errors, including missing files, are logged to `stderr`.

## Requirements

- Python 3.x
- Grok API Key (stored in `.env` file or passed via command line)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/code-complexity-analyzer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd code-complexity-analyzer
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file with your Grok API key and base URL:

    ```
    API_KEY=your-grok-api-key
    BASE_URL=https://api.groq.com
    ```

## Usage

### 1. Display Version

Use the `--version` or `-v` flag to display the tool's version:

```bash
python main.py --version
```

### 2. Display Help

Use the `--help` or `-h` flag to display the usage instructions:

```bash
python main.py --help
```

### 3. Run with a Single File

Specify a single file to analyze:

```bash
python main.py ./file.js
```

### 4. Run with Multiple Files

Provide multiple files for analysis:

```bash
python main.py file1.js file2.js
```

### 5. Output to a File

To save the result to a file, use the `--output` or `-o` flag:

```bash
python main.py file1.js -o result.txt
```

### 6. Specify an AI Model

You can specify an AI model to use for analysis (default: `llama-v2`):

```bash
python main.py file1.js --model gpt-3.5
```

or

```bash
python main.py file1.js -m gpt-3.5
```

### 7. API Key and Base URL

You can pass the API key and base URL via the command line if not using the `.env` file:
- **API Key**:
  ```bash
  python main.py file1.js --api-key your_api_key
  ```
  or
  ```bash
  python main.py file1.js -a your_api_key
  ```

- **Base URL**:
  ```bash
  python main.py file1.js --base-url https://api.custom-url.com
  ```
  or
  ```bash
  python main.py file1.js -u https://api.custom-url.com
  ```

### 8. Error Handling

If a file is missing, or any other error occurs, it will be logged to `stderr`:

```bash
python main.py non_existing_file.js
```

# Code Complexity Analyzer

This command-line tool analyzes the complexity of source code files using Grok's LLM API. It supports multiple file inputs, customizable AI model selection, and configurable API settings.

## Features
- **Version Display**: Use `--version` or `-v` to display the tool's name and current version.
- **Help**: Use `--help` or `-h` to display the tool’s help message, showing how to run it, along with all available flags and arguments.
- **File Input**: Accept one or more files for analysis.
- **Output to stdout or file**: By default, outputs to stdout. You can specify an output file using the `--output` or `-o` flag.
- **LLM Model Selection**: Specify a model using the `--model` or `-m` flag (default: `llama-v2`).
- **API Key Configuration**: Optionally pass an API key via the `--api-key` or `-a` flag or configure it in the `.env` file.
- **Base URL Configuration**: Optionally pass a base API URL via the `--base-url` or `-u` flag or configure it in the `.env` file.
- **Error Handling**: Any errors, including missing files, are logged to `stderr`.

## Requirements

- Python 3.x
- Grok API Key (stored in `.env` file or passed via command line)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/code-complexity-analyzer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd code-complexity-analyzer
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file with your Grok API key and base URL:

    ```
    API_KEY=your-grok-api-key
    BASE_URL=https://api.groq.com
    ```

## Usage

### 1. Display Version

Use the `--version` or `-v` flag to display the tool's version:

```bash
python main.py --version
```

### 2. Display Help

Use the `--help` or `-h` flag to display the usage instructions:

```bash
python main.py --help
```

### 3. Run with a Single File

Specify a single file to analyze:

```bash
python main.py ./file.js
```

### 4. Run with Multiple Files

Provide multiple files for analysis:

```bash
python main.py file1.js file2.js
```

### 5. Output to a File

To save the result to a file, use the `--output` or `-o` flag:

```bash
python main.py file1.js -o result.txt
```

### 6. Specify an AI Model

You can specify an AI model to use for analysis (default: `llama-v2`):

```bash
python main.py file1.js --model gpt-3.5
```

or

```bash
python main.py file1.js -m gpt-3.5
```

### 7. API Key and Base URL

You can pass the API key and base URL via the command line if not using the `.env` file:
- **API Key**:
  ```bash
  python main.py file1.js --api-key your_api_key
  ```
  or
  ```bash
  python main.py file1.js -a your_api_key
  ```

- **Base URL**:
  ```bash
  python main.py file1.js --base-url https://api.custom-url.com
  ```
  or
  ```bash
  python main.py file1.js -u https://api.custom-url.com
  ```

### 8. Error Handling

If a file is missing, or any other error occurs, it will be logged to `stderr`:

```bash
python main.py non_existing_file.js
```
