import argparse
import os
import toml
import sys
from dotenv import load_dotenv
from complexity_analyzer import analyze_complexity
from utils import write_output

TOOL_NAME = "Code Complexity Pro"
VERSION = "1.0.0"

# Load environment variables from a .env file if present
load_dotenv()

# Function to load config file from the home directory
def load_config():
    """
    Load configuration settings from the user's home directory.
    Returns a dictionary of configuration settings.
    """
    # Define the path to the config file in the home directory
    config_path = os.path.expanduser("~/.Code-complexity-pro-config.toml")

    # Check if the file exists
    if os.path.exists(config_path):
        try:
            # Open and parse the TOML file
            with open(config_path, "r") as file:
                return toml.load(file)
        except toml.TomlDecodeError:
            print("Error: Invalid TOML format in config file.")
            exit(1)  # Exit the program if the file is not valid TOML
    return {}  # Return an empty dictionary if no config file exists


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
    # Load configuration from TOML file
    config = load_config()

    parser = argparse.ArgumentParser(description=f'{TOOL_NAME} - Analyze code complexity using an AI model.')

    # Optional arguments
    parser.add_argument('-o', '--output', type=str, help='Output file name (default: stdout)', default=None)
    parser.add_argument('-m', '--model', type=str, help='Model to use for analysis (default: llama-v2)', default=config.get('model', 'llama-v2'))
    
    # Add an optional API key argument
    parser.add_argument('-a', '--api-key', type=str, help='API key for the analysis service')

    # Version and help flags
    parser.add_argument('-v', '--version', action='store_true', help='Display the version of the tool')
    
    # Accept multiple files or directories
    parser.add_argument('files', nargs='+', help='One or more source code files or directories to analyze.')
    
    args = parser.parse_args()

    # Handle version flag
    if args.version:
        print(f'{TOOL_NAME} version {VERSION}')
        sys.exit(0)

    # Ensure files are provided
    if not args.files:
        parser.print_help()
        sys.stderr.write("Error: No files provided for analysis\n")
        sys.exit(1)

    # Check if API key is available (from args, config, or environment variable)
    api_key = args.api_key or config.get('api_key') or os.getenv('API_KEY')
    if not api_key:
        sys.stderr.write("Error: API key not provided. Use --api-key or set it in the .env file.\n")
        sys.exit(1)

    # Process the provided paths (files or directories)
    files_to_analyze = process_files(args.files)

    success = True  # Track if all files are processed successfully

    # Process each file and analyze complexity
    for file in files_to_analyze:
        try:
            with open(file, 'r') as f:
                code = f.read()

            # Analyze the complexity of the code
            result = analyze_complexity(code, api_key=api_key, model=args.model)

            # Output result
            if args.output:
                write_output(args.output, result)
            else:
                print(result)

        except FileNotFoundError:
            sys.stderr.write(f"Error: File '{file}' not found\n")
            success = False
        except Exception as e:
            sys.stderr.write(f"Error: {str(e)} while processing '{file}'\n")
            success = False

    # Exit with 0 if all files were processed successfully, otherwise exit with 1
    if success:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
