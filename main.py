import argparse
import os
import sys
from dotenv import load_dotenv
from complexity_analyzer import analyze_complexity
from utils import write_output

TOOL_NAME = "Code Complexity Pro"

# Load environment variables from a .env file if present
load_dotenv()

def process_files(paths):
    """
    Process the provided file and directory paths.
    
    Args:
    - paths: List of file or directory paths.

    Returns:
    - List of valid file paths to analyze.
    """
    file_list = []
    for path in paths:
        if os.path.isfile(path):
            file_list.append(path)
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    file_list.append(os.path.join(root, file))
        else:
            print(f"Error: {path} is not a valid file or directory", file=sys.stderr)
            sys.exit(1)
    return file_list

def main():
    """
    Main function to handle command-line arguments, analyze code, and save the results.
    
    - Accepts one or more source code files to analyze.
    - Allows specification of the AI model and output file.
    """
    parser = argparse.ArgumentParser(description=f'{TOOL_NAME} - Analyze code complexity using an AI model.')

    # Optional arguments
    parser.add_argument('-o', '--output', type=str, help='Output file name (default: stdout)', default=None)
    parser.add_argument('-m', '--model', type=str, help='Model to use for analysis (default: llama-v2)', default='llama-v2')
    
    # Add an optional API key argument
    parser.add_argument('-a', '--api-key', type=str, help='API key for the analysis service')

    # Accept multiple files or directories
    parser.add_argument('files', nargs='+', help='One or more source code files or directories to analyze.')
    
    args = parser.parse_args()

    # Use the API key from the command line or fall back to environment variable
    api_key = args.api_key or os.getenv("API_KEY")
    
    if not api_key:
        print("Error: API key must be provided either via --api-key or in the .env file.", file=sys.stderr)
        sys.exit(1)

    # Process the provided paths (files or directories)
    files_to_analyze = process_files(args.files)

    # Process each file and analyze complexity
    for file in files_to_analyze:
        with open(file, 'r') as f:
            code = f.read()
        result = analyze_complexity(code, api_key, args.model)
        
        # Output result
        if args.output:
            write_output(args.output, result)
        else:
            print(result)

if __name__ == "__main__":
    main()
