from unittest.mock import patch, Mock
from api_handler import send_code_to_groq

# Sample mock response data for successful API calls
mock_response_data = {
    "choices": [{"message": {"content": "Complexity analysis result: Simple"}}],
    "usage": {"prompt_tokens": 10, "completion_tokens": 15, "total_tokens": 25},
}


@patch("api_handler.requests.post")
def test_send_code_to_groq_success(mock_post):
    """
    Test `send_code_to_groq` with valid inputs and a successful API response.
    """
    # Configure the mock to return a response with JSON data
    mock_post.return_value = Mock(status_code=200)
    mock_post.return_value.json.return_value = mock_response_data

    # Define the test inputs
    api_key = "test_key"
    code = "def sample_function(): pass"
    model = "llama-v2"

    # Call the function and verify its output
    result, token_usage = send_code_to_groq(api_key, code, model)
    assert (
        result == mock_response_data["choices"][0]["message"]["content"]
    ), "Unexpected analysis result"
    assert token_usage == mock_response_data["usage"], "Unexpected token usage"
