from code_complexity_pro.api_handler import send_code_to_groq
import requests  # Import requests to handle API-specific exceptions
import sys


def analyze_complexity(code, api_key, model="llama-v2", show_token_usage=False):
    """
    Analyze the complexity of the given source code using Grok's API.

    Args:
    - code: The source code to analyze.
    - api_key: API key for authentication.
    - model: The AI model to use (default is 'llama-v2').

    Returns:
    - Complexity analysis result or an error message if it fails.
    """
    try:
        result, token_usage = send_code_to_groq(api_key, code, model)

        # Display token usage if the flag is set
        if show_token_usage and token_usage:
            prompt_tokens = token_usage.get('prompt_tokens', 0)
            completion_tokens = token_usage.get('completion_tokens', 0)
            total_tokens = token_usage.get('total_tokens', 0)
            print(
                f"Token Usage: Prompt Tokens = {prompt_tokens}, Completion Tokens = {completion_tokens}, Total Tokens = {total_tokens}",
                file=sys.stderr,
            )

        return result
    except requests.exceptions.RequestException as e:
        # Handle API-related exceptions such as connectivity issues
        return f"API error occurred: {str(e)}"
    except Exception as e:
        # Handle any other general exceptions
        return f"Error analyzing code complexity: {str(e)}"
