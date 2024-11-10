import pytest
from unittest.mock import patch, Mock
from api_handler import send_code_to_groq

# Sample mock response data
mock_response_data = {
    "choices": [{"message": {"content": "This is a complexity analysis result."}}],
    "usage": {"prompt_tokens": 10, "completion_tokens": 15, "total_tokens": 25},
}


@patch("api_handler.requests.post")
def test_send_code_to_groq_success(mock_post):
    # Configure the mock to return a response with JSON data
    mock_post.return_value = Mock(status_code=200)
    mock_post.return_value.json.return_value = mock_response_data

    # Define the test inputs
    api_key = "test_key"
    code = "def example_function(): pass"
    model = "test-model"

    # Call the function and verify its output
    result, token_usage = send_code_to_groq(api_key, code, model)
    assert result == mock_response_data["choices"][0]["message"]["content"]
    assert token_usage == mock_response_data["usage"]


@patch("api_handler.requests.post")
def test_send_code_to_groq_failure(mock_post):
    # Configure the mock to return a response with a failure status code
    mock_post.return_value = Mock(status_code=400)
    mock_post.return_value.text = "Bad Request"

    # Define the test inputs
    api_key = "test_key"
    code = "def example_function(): pass"
    model = "test-model"

    # Verify that an exception is raised for a failed request
    with pytest.raises(
        Exception, match="API request failed with status code 400: Bad Request"
    ):
        send_code_to_groq(api_key, code, model)
