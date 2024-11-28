def write_output(file_path, data):
    """
    Write the given data to the specified file.

    Args:
    - file_path: The path of the file where the data should be written.
    - data: The content to write into the file.
    """
    with open(file_path, 'w') as f:
        f.write(data)
