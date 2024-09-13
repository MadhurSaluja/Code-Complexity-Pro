import argparse
import os
from dotenv import load_dotenv
from complexity_analyzer import analyze_complexity
from utils import write_output

# Load environment variables
load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')

def main():
    parser = argparse.ArgumentParser(description="Code Complexity Analyzer using Grok API")
    parser.add_argument('files', nargs='+', help='Source code files to analyze')
    parser.add_argument('--model', '-m', default="llama-v2", help='LLM model to use')
    parser.add_argument('--output', '-o', help='File to write the output')
    
    args = parser.parse_args()

    for file_path in args.files:
        try:
            # Analyze the complexity of the code in the file
            with open(file_path, 'r') as file:
                code = file.read()
            result = analyze_complexity(code, API_KEY, BASE_URL, args.model)
            
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
