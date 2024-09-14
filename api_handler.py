import requests
import os
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Load environment variables from the .env file
load_dotenv()

def send_code_to_grok(api_key, code, model):
    """
    Send code to Grok's API for complexity analysis.
    
    Args:
    - api_key: Your API key for authentication.
    - code: The source code to analyze.
    - model: The AI model to use for analysis (e.g., llama-v2).
    
    Returns:
    - The complexity analysis result from the API.
    
    Raises:
    - Exception if the API request fails.
    """
    # Fetch the base URL from environment variables, or use a default backup URL
    url = os.getenv('BASE_URL', 'https://default-backup-url.com')
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Payload for the API request
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a code complexity analyzer."},
            {"role": "user", "content": f"Analyze the complexity of this code:\n{code}"}
        ]
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
