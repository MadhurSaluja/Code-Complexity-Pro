import pytest
from unittest.mock import patch, mock_open
import os
import toml
import logging

# Import the function from main.py
from code_complexity_pro.main import load_config

# Test the case where the config file exists and is valid.
@patch('os.path.exists')
@patch('builtins.open', new_callable=mock_open)
@patch('toml.load')
def test_load_config_success(mock_toml_load, mock_open, mock_exists):
    """Test case where the config file exists and is valid."""
    # Simulate that the file exists
    mock_exists.return_value = True

    # Sample TOML content to return
    mock_toml_load.return_value = {"key": "value"}

    # Run the function
    config = load_config()

    # Check that the file was opened correctly
    mock_open.assert_called_once_with(os.path.expanduser("~/.Code-complexity-pro-config.toml"), "r")

    # Check that the TOML content was loaded correctly
    mock_toml_load.assert_called_once_with(mock_open())
    assert config == {"key": "value"}

# Test the case where the config file does not exist.
@patch('os.path.exists')
@patch('builtins.open', new_callable=mock_open)
@patch('toml.load')
def test_load_config_file_not_found(mock_toml_load, mock_open, mock_exists):
    """Test case where the config file does not exist."""
    mock_exists.return_value = False

    # Run the function
    config = load_config()

    # Ensure the result is an empty dictionary
    assert config == {}

# Test the case where the config file exists but has an invalid TOML format.
@patch('os.path.exists')
@patch('builtins.open', new_callable=mock_open)
@patch('toml.load')
@patch('logging.error')
def test_load_config_invalid_toml(mock_logging_error, mock_toml_load, mock_open, mock_exists):
    """Test case where the TOML format is invalid."""
    mock_exists.return_value = True
    mock_open.return_value = mock_open(read_data="invalid_toml_data")
    
    # Simulate TOML decoding error
    mock_toml_load.side_effect = toml.TomlDecodeError("Invalid TOML format", "invalid_toml_data", 0)

    # Assert that a SystemExit is raised due to the exit in the function
    with pytest.raises(SystemExit):
        load_config()

    # Check if the error was logged
    mock_logging_error.assert_called_once_with("Invalid TOML format in config file.")
