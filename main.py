import argparse
import os
import toml
import sys
from dotenv import load_dotenv
from complexity_analyzer import analyze_complexity
from utils import write_output
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'
)

# Load environment variables from a .env file if present
load_dotenv()


def load_config():
    """Load configuration settings from the user's home directory."""
    config_path = os.path.expanduser("~/.Code-complexity-pro-config.toml")
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as file:
                return toml.load(file)
        except toml.TomlDecodeError:
            logging.error("Invalid TOML format in config file.")
            exit(1)
    return {}


def process_files(paths):
    """Process file and directory paths and return a list of valid file paths."""
    file_list = []
    for path in paths:
        if os.path.isfile(path):
            file_list.append(path)
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    file_list.append(os.path.join(root, file))
        else:
            logging.error(f"{path} is not a valid file or directory")
            sys.exit(1)
    return file_list


def parse_arguments():
    """Handle command-line argument parsing."""
    parser = argparse.ArgumentParser(
        description='Code Complexity Pro - Analyze code complexity using an AI model.'
    )
    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help="List of file paths or directories to analyze",
    )
    parser.add_argument(
        '--model', default="llama3-8b-8192", help="AI model to use (default: llama-v2)"
    )
    parser.add_argument('--api-key', help="API key for the AI model")
    parser.add_argument('--output', help="Optional output file to save the results")
    return parser.parse_args()


def main():
    args = parse_arguments()
    config_settings = load_config()

    # Validate API Key
    api_key = args.api_key or os.getenv("API_KEY") or config_settings.get('api_key')
    if not api_key:
        logging.error(
            "API key is required. Please set it in the .env file, config file, or pass via --api-key."
        )
        sys.exit(1)

    # Process the input files
    files_to_analyze = process_files(args.files)
    logging.info(f"Analyzing {len(files_to_analyze)} files.")

    for file in files_to_analyze:
        try:
            with open(file, 'r') as f:
                code = f.read()

            # Analyze code complexity using the AI model
            result = analyze_complexity(
                code,
                api_key=api_key,
                model=args.model,
            )
            logging.info(f"Successfully analyzed {file}.")

            if args.output:
                write_output(args.output, result)

        except Exception as e:
            logging.error(f"Error processing {file}: {e}")


if __name__ == "__main__":
    main()
