
# Code Complexity Pro

This is a command-line tool that analyzes the complexity of source code files using Grok's LLM API. It supports multiple file inputs, customizable AI model selection, and various configuration options to suit your workflow. The project is part of **Release-0.1**, and here you will find everything you need to know about using and extending this tool.

## Features

- **Version Display**: Use the `--version` or `-v` flag to display the tool's name and current version.
- **Help/Usage Instructions**: Use the `--help` or `-h` flag to display how to run the tool, along with available flags and arguments.
- **File Input**: Analyze one or more source code files.
- **Customizable Output**: By default, results are printed to the terminal (stdout), but you can specify an output file using the `--output` or `-o` flag.
- **AI Model Selection**: Specify a model for the analysis using the `--model` or `-m` flag (default is `llama-v2`).
- **API Key Configuration**: API keys can be passed via the `--api-key` or `-a` flag, or you can configure them in a `.env` file.
- **Error Logging**: All debug and error messages are logged to `stderr`, keeping output clean.
---
## Requirements

- Python 3.x
- Grok API Key (can be stored in `.env` file or passed via command line)
---
## Installation

1. **Clone the Repository**:
   Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/MadhurSaluja/Release-0.1
   cd Release-0.1
   ```

2. **Install Dependencies**:
   Install the required dependencies with:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Credentials**:
   Create a `.env` file in the root of the project with your Grok API credentials:
   ```bash
   API_KEY=your-grok-api-key
   BASE_URL=https://api.groq.com/openai/v1/chat/completions
   ```
---
## Usage

You can run the tool from the command line with various flags and options. Here are some examples:

### 1. Display Version

Use the following command to check the tool's version:
```bash
python main.py --version
```
---
### 2. Show Help/Usage

Use the `--help` or `-h` flag to display usage information:
```bash
python main.py --help
```
---
### 3. Run the Analyzer on a Single File

To analyze the complexity of a single file, use:
```bash
python main.py path/to/your_file.py
```
---
### 4. Analyze Multiple Files

To analyze multiple files at once:
```bash
python main.py file1.py file2.py
```
---
### 5. Save Results to a File

Use the `--output` or `-o` flag to save the analysis to a file:
```bash
python main.py your_file.py --output analysis_results.txt
```
---
### 6. Specify a Different AI Model

By default, the tool uses the `llama-v2` model for analysis. You can specify another model like this:
```bash
python main.py your_file.py --model gpt-3.5
```
---
### 7. Pass API Key and Base URL via Command Line

If you don’t want to use a `.env` file, you can pass the API key and base URL directly:
```bash
python main.py your_file.py --api-key your_grok_api_key --base-url https://api.custom-url.com
```
---
### 8. Error Handling

Errors, such as missing files or invalid input, will be printed to `stderr`. For example:
```bash
python main.py nonexistent_file.py
```
Will return:
```
Error: File nonexistent_file.py not found
```
---
## Examples

For sample files, check out the `examples/` directory in this repository. It contains test files that you can use to run the tool and see how it works.

### Running on Example File

```bash
python main.py examples/test_code.py
```
---
#### Example:
```bash
python main.py non_existent_file.py --api-key YOUR_API_KEY
```
This will return an error message and exit with code `1`.
---

### Version Flag
You can now use the `--version` flag to see the current version of the tool.
```bash
python main.py --version
```
---
### API Key Handling
You can provide the API key via the `--api-key` command-line argument or store it in a `.env` file.
```plaintext
API_KEY=your_api_key
```
---
## Demo 



https://github.com/user-attachments/assets/f4ddfe70-82d3-460e-bab7-fa0fe5c8121c





---

## New Features Added

### 1. Support for Multiple Files or Directories
You can now provide multiple files and directories as input for complexity analysis. The tool will recursively process directories and analyze all relevant files within them.

#### Example:
```bash
python main.py file1.py file2.py directory/ --api-key YOUR_API_KEY
```
---
### 2. Enhanced Error Handling with Exit Codes
The tool now properly exits with a status code based on success or failure:
- Exit code `0` for successful processing.
- Exit code `1` for errors such as missing files, invalid inputs, or missing API keys.
---



## Configuration

### TOML Configuration File Support
You can now use a TOML configuration file to store default values for the API key and model. This allows the tool to run without needing to pass these values via the command line every time.

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
- For example:
  
  ```bash
  python main.py --model gpt-3.5 --api-key new-api-key your_file.py
  ```

  This command will override the values from the TOML config file.

### Example:
Without passing command-line arguments, the tool will automatically use values from the TOML file:
```bash
python main.py your_file.py
```
## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/MadhurSaluja/Release-0.1/blob/main/LICENSE) file for details.


