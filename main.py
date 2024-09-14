import argparse
import os
from dotenv import load_dotenv
from complexity_analyzer import analyze_complexity
from utils import write_output

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')

def main():
    parser = argparse.ArgumentParser(description="Code Complexity Analyzer using GrowCloud API")
    parser.add_argument('files', nargs='+', help='Source code files to analyze')
    parser.add_argument('--model', '-m', default="llama-v2", help='LLM model to use')
    parser.add_argument('--output', '-o', help='File to write the output')
    
    args = parser.parse_args()

    for file_path in args.files:
        try:
            # Read the file contents
            with open(file_path, 'r') as file:
                code = file.read()
            
            # Analyze the complexity using the API key only
            result = analyze_complexity(code, API_KEY, args.model)
            
            # Output the result
            if args.output:
                write_output(args.output, result)
            else:
                print(result)
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
