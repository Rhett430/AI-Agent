import os


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = abs_working_dir
    if file_path:
        target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" is not a file'
    try:
        MAX_CHARS = 10000

        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            content = f.read()
            words = content.split()

        if len(words) > 10000:
            return f'{file_content_string}...File "{target_file}" truncated at 10000 characters'
        
        else:
            return file_content_string
    except Exception as e:
        return f"Error reading file: {e}"
