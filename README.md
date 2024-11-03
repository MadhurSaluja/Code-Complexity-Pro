# Code Complexity Pro

This is a command-line tool that analyzes the complexity of source code files using Groq's LLM API. It supports multiple file inputs, customizable AI model selection, and various configuration options to suit your workflow. The project is **Code-Complexity-Pro**, and here you will find everything you need to know about using this tool.

## Features

- **Version Display**: Use the `--version` or `-v` flag to display the tool's name and current version.
- **Help/Usage Instructions**: Use the `--help` or `-h` flag to display how to run the tool, along with available flags and arguments.
- **File Input**: Analyze one or more source code files.
- **Customizable Output**: By default, results are printed to the terminal (stdout), but you can specify an output file using the `--output` or `-o` flag.
- **AI Model Selection**: Specify a model for the analysis using the `--model` or `-m` flag (default is `llama-v2`).
- **API Key Configuration**: API keys can be passed via the `--api-key` or `-a` flag, or you can configure them in a `.env` file.
- **Error Logging**: All debug and error messages are logged to `stderr`, keeping output clean.

## Usage

You can run the tool from the command line with various flags and options. Here are some examples:

### 1. Display Version
```bash
python main.py --version
```

### 2. Show Help/Usage
```bash
python main.py --help
```

### 3. Run the Analyzer on a Single File
```bash
python main.py path/to/your_file.py
```

### 4. Analyze Multiple Files
```bash
python main.py file1.py file2.py
```

### 5. Save Results to a File
```bash
python main.py your_file.py --output analysis_results.txt
```

### 6. Specify a Different AI Model
```bash
python main.py your_file.py --model gpt-3.5
```

### 7. Pass API Key and Base URL via Command Line
```bash
python main.py your_file.py --api-key your_grok_api_key --base-url https://api.custom-url.com
```

### 8. Error Handling
For example:
```bash
python main.py nonexistent_file.py
```

## Examples

For sample files, check out the `examples/` directory in this repository. It contains test files that you can use to run the tool and see how it works.

### Running on Example File
```bash
python main.py examples/test_code.py
```

## New Features

### 1. Support for Multiple Files or Directories
You can now provide multiple files and directories as input for complexity analysis. The tool will recursively process directories and analyze all relevant files within them.

### 2. Enhanced Error Handling with Exit Codes
The tool now properly exits with a status code based on success or failure:
- Exit code `0` for successful processing.
- Exit code `1` for errors such as missing files, invalid inputs, or missing API keys.

## Demo

[Demo Video](https://github.com/user-attachments/assets/f4ddfe70-82d3-460e-bab7-fa0fe5c8121c)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/MadhurSaluja/Release-0.1/blob/main/LICENSE) file for details.
