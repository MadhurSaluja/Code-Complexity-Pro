
# Complexity Analyzer

## Overview

This project contains a set of Python scripts designed for complexity analysis of your code with use of API Handling

## Features

- **API Handling**: Efficiently handles API requests using `requests`.
- **Complexity Analysis**: Functions to calculate factorials and check if a number is prime, with time and space complexity analyses.
- **Command-line Interface**: User-friendly argument parsing with `argparse`.

## File Structure

- **main.py**: The main entry point for the project.
- **api_handler.py**: Handles API requests and responses.
- **complexity_analyzer.py**: Implements mathematical algorithms like factorial and primality testing, with complexity details.
- **utils.py**: Contains utility functions used throughout the project.
- **test_code.py**: Unit tests for the project's functions.
- **LICENSE**: The project's license.
- **requirements.txt**: List of dependencies required for the project.

## Setup

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/projectname.git
   cd projectname
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

The project relies on the following Python packages:

```text
python-dotenv  # Manage environment variables
requests       # For API calls
argparse       # Parse command-line arguments
```

You can install them using the `requirements.txt` file with the command mentioned in the setup section.

## Usage

### Running the Main Script

To run the main script, execute the following command:

```bash
python main.py --arg1 value1 --arg2 value2
```

For more information on available arguments, use the help flag:

```bash
python main.py --help
```

### Example

To calculate the factorial of a number:

```bash
python main.py --factorial 5
```

This will return the factorial of 5.

## Code Complexity Analysis

The project implements functions such as `calculate_factorial(n)` and `is_prime(num)`. Below is a summary of their complexity:

- **`calculate_factorial(n)`**:
  - Time complexity: O(n)
  - Space complexity: O(n)
  
- **`is_prime(num)`**:
  - Time complexity: O(n)
  - Space complexity: O(1)

More detailed analysis is available in `test_code.py_analysis.txt`.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
