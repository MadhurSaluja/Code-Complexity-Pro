def write_output(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Output successfully written to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {str(e)}")
