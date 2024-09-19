import argparse
import os
from dotenv import load_dotenv
from complexity_analyzer import analyze_complexity
from utils import write_output

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')

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
    #  --token-usage or -t flag to the argument parser and pass it to the analyze_complexity() function
    parser.add_argument('--token-usage', '-t', action='store_true', help='Display token usage information')
    
    args = parser.parse_args()

    for file_path in args.files:
        try:
            # Read the file contents
            with open(file_path, 'r') as f:
                code = f.read()

            # Analyze the code complexity with or without token usage display
            result = analyze_complexity(code, API_KEY, args.model, show_token_usage=args.token_usage)

            # Determine output file
            output_file = args.output if args.output else f"{file_path}_analysis.txt"
            
            # Save the result to the output file
            write_output(output_file, result)

        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == '__main__':
    main()
