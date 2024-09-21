# Code Complexity Analyzer

This command-line tool analyzes the complexity of source code files using Grok's LLM API.

## Requirements

- Python 3.x
- Groq API Key (store in `.env` file)

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/code-complexity-analyzer.git


2. Install dependencies:

pip install -r requirements.txt


3. Create a `.env` file with your Grok API key:

API_KEY=your-grok-api-key-here BASE_URL=[https://console.groq.com](https://api.groq.com/openai/v1/chat/completions)

## Usage

Analyze a single file:
python main.py path/to/file.py


Analyze multiple files:
python main.py file1.py file2.js


Specify a model:

python main.py file.py --model llama-v2

Specify an output file:

python main.py file.py --output analysis.txt


For help:


## Features

- Analyze source code complexity using Grok's LLM.
- Output results to the terminal or a file.
- Specify the model and API configuration through `.env` or command-line arguments.


