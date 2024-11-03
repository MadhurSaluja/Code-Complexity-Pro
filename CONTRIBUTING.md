
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
   cd Release-0.1
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
