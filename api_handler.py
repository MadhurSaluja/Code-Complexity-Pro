import requests

def send_code_to_groq(api_key, code, model):
    # Define the base URL for the GrowCloud API (hardcoded in this example)
    url = "https://api.groq.com/openai/v1/chat/completions"  # Example base URL for GrowCloud API

    # Set up the headers required for the API request, including API key and content type
    headers = {
        "Authorization": f"Bearer {api_key}",  # Authorization header with the provided API key
        "Content-Type": "application/json"     # Specifying the request content type as JSON
    }

    # Define the request payload with the model and the messages
    data = {
        "model": "llama3-70b-8192",  # Model name (hardcoded in this case)
        "messages": [
            {"role": "system", "content": "You are a code complexity analyzer."},  # Instruction for the system
            {"role": "user", "content": f"Analyze the complexity of this code:\n{code}"}  # User prompt with the code
        ]
    }

    # Send a POST request to the API with the payload and headers
    response = requests.post(url, json=data, headers=headers)

    # If the request is successful (status code 200), return the analysis from the response
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"], response.json().get("usage", {})  # Extract and return the response content and the token usage
    else:
        # Raise an exception if the request fails, including the status code and error message
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
