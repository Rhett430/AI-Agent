import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_path):
        try:
            open(file_path, "w").close()  # Create the file if it doesn't exist
        except Exception as e:
            return f'Error: Failed to create directory "{file_path}". Reason: {str(e)}'
    if os.path.exists(file_path):
        try:
            with open(file_path, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f'Error writing to file "{file_path}"'