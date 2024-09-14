import requests

def send_code_to_grok(api_key, code, model):
    # Hardcode the URL
    url = "https://api.growcloud.com/completions"  # Example base URL for GrowCloud API

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

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
