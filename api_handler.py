import requests


def send_code_to_groq(api_key, code, model):
    """Send code to Groq API for complexity analysis."""

    # Define the API endpoint and headers
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    # Prepare the request payload
    request_payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a code complexity analyzer."},
            {
                "role": "user",
                "content": f"Analyze the complexity of this code: \n{code}",
            },
        ],
    }

    # Send the request
    response = requests.post(url, json=request_payload, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"], response.json().get(
            "usage", {}
        )
    else:
        raise Exception(
            f"API request failed with status code {response.status_code}: {response.text}"
        )
