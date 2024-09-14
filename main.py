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
    parser.add_argument('--output', '-o', help='File to write the output (optional, default is <filename>_analysis.txt)')
    
    args = parser.parse_args()

    for file_path in args.files:
        try:
            # Read the file contents
            with open(file_path, 'r') as file:
                code = file.read()
            
            # Analyze the complexity using the API key only
            result = analyze_complexity(code, API_KEY, args.model)
            
            # Print the result to terminal
            print(f"Analysis for {file_path}:\n{result}")
            
            # Generate the output file name if not provided
            if args.output:
                output_file = args.output
            else:
                output_file = f"{os.path.splitext(file_path)[0]}_analysis.txt"
            
            # Write the result to the file
            with open(output_file, 'w') as file:
                file.write(result)
            
            print(f"Result saved to {output_file}")
            
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
