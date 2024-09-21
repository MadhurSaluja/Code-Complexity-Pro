
import argparse
import os
import sys
from dotenv import load_dotenv
from complexity_analyzer import analyze_complexity
from utils import write_output

# Load environment variables from .env file
load_dotenv()

# Constants for the tool
TOOL_NAME = 'Code Complexity Analyzer'
VERSION = '1.0.0'
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')

def main():
    """
    Main function to handle command-line arguments, analyze code, and save the results.
    
    - Accepts one or more source code files to analyze.
    - Allows specification of the AI model and output file.
    """
    parser = argparse.ArgumentParser(description="Code Complexity Analyzer using Grok API")
    parser.add_argument('files', nargs='+', help='Source code files to analyze')
    parser.add_argument('--model', '-m', default="llama-v2", help='LLM model to use')
    parser.add_argument('--output', '-o', help='File to write the output (optional, default is <filename>_analysis.txt)')
    
    args = parser.parse_args()

    # Handle version flag
    if args.version:
        print(f'{TOOL_NAME} version {VERSION}')
        sys.exit(0)

    # Ensure files are provided if not using the version/help flags
    if not args.files:
        parser.print_help()
        sys.exit(1)

    # Process each file
    for file_path in args.files:
        try:
            with open(file_path, 'r') as f:
                code = f.read()

            # Analyze the code complexity
            result = analyze_complexity(code, API_KEY, args.model)

            # Output result
            if args.output:
                write_output(args.output, result)
            else:
                # Print to stdout
                print(result)

        except FileNotFoundError:
            print(f"Error: File {file_path} not found", file=sys.stderr)
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)

if __name__ == '__main__':
    main()
