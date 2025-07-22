import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    else:
        try:
            result = subprocess.run(["python3",file_path], capture_output=True, timeout=30, cwd=abs_working_dir, text=True)
            output = f'STDOUT:{result.stdout}\nSTDERR:{result.stderr}'
            if result.returncode != 0:
                output += f'\nProcess exited with code {result.returncode}'
            if result.stdout.strip() == "" and result.stderr.strip() == "":
                return "No output produced."
            return output
        except Exception as e:
            return f"Error: executing Python file: {e}"