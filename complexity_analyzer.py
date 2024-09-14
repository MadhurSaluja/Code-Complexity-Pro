import requests  
from api_handler import send_code_to_groq


def analyze_complexity(code, api_key, model="llama3-70b-8192"):
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
        result = send_code_to_groq(api_key, code, model)
        return result
    except requests.exceptions.RequestException as e:
        # Handle API-related exceptions such as connectivity issues
        return f"API error occurred: {str(e)}"
    except Exception as e:
        # Handle any other general exceptions
        return f"Error analyzing code complexity: {str(e)}"
