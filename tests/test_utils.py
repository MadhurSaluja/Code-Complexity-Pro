import pytest
from code_complexity_pro.utils import write_output
# The rest of the test file remains unchanged



def test_write_output_basic(tmp_path):
    # Basic test: Write a standard string to a file
    test_data = "This is a simple test."
    test_file = tmp_path / "output_basic.txt"

    write_output(test_file, test_data)

    assert test_file.exists(), "File was not created."
    with open(test_file, 'r') as f:
        content = f.read()
    assert content == test_data, "File content does not match expected."


def test_write_output_empty_string(tmp_path):
    # Test: Write an empty string to a file
    test_data = ""
    test_file = tmp_path / "output_empty.txt"

    write_output(test_file, test_data)

    assert test_file.exists(), "File was not created."
    with open(test_file, 'r') as f:
        content = f.read()
    assert content == test_data, "File content should be empty but is not."


def test_write_output_large_string(tmp_path):
    # Test: Write a very large string to a file
    test_data = "a" * 10000  # 10,000 characters
    test_file = tmp_path / "output_large.txt"

    write_output(test_file, test_data)

    assert test_file.exists(), "File was not created."
    with open(test_file, 'r') as f:
        content = f.read()
    assert content == test_data, "File content does not match expected for large input."


def test_write_output_none_data(tmp_path):
    # Test: Passing None as data should raise an exception
    test_file = tmp_path / "output_none.txt"

    with pytest.raises(TypeError):
        write_output(test_file, None)


def test_write_output_invalid_file_path():
    # Test: Passing an invalid path should raise an IOError or OSError
    invalid_path = "/invalid/path/output.txt"
    test_data = "Test data for invalid path."

    with pytest.raises(OSError):
        write_output(invalid_path, test_data)
