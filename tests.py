from functions.run_python_file import run_python_file

tests = [run_python_file("calculator", "main.py"),
        run_python_file("calculator", "tests.py"),
        run_python_file("calculator", "../main.py"),
        run_python_file("calculator", "nonexistent.py")]

for test in tests:
    print(test)


