import os
import subprocess
import platform
from typing import List, Union

def run_command(command: Union[str, List[str]], shell: bool = False) -> None:
    print(f"Running: {command}")
    subprocess.run(command, shell=shell, check=True)

def main():
    # Step 1: Create virtual environment if it doesn't exist
    if not os.path.isdir("venv"):
        run_command(["python", "-m", "venv", "venv"])
    else:
        print("Virtual environment already exists.")

    # Step 2: Define venv paths
    venv_dir = os.path.join("venv", "Scripts" if platform.system() == "Windows" else "bin")
    venv_python = os.path.join(venv_dir, "python")
    pip_path = os.path.join(venv_dir, "pip")

    # Step 3: Install dependencies inside venv
    run_command([venv_python, "-m", "pip", "install", "django", "djangorestframework", "drf-yasg"])

    # Step 4: Django setup with venv's Python
    run_command([venv_python, "manage.py", "makemigrations"])
    run_command([venv_python, "manage.py", "migrate"])

    # Step 5: Run dev server using venv's Python
    run_command([venv_python, "manage.py", "runserver"])

if __name__ == "__main__":
    main()
