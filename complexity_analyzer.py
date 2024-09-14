from api_handler import send_code_to_grok

def analyze_complexity(code, api_key, model="llama-v2"):
    try:
        result = send_code_to_grok(api_key, code, model)
        return result
    except Exception as e:
        return f"Error analyzing code complexity: {str(e)}"
