import sys
from app.all_commands import *
import subprocess
import shlex

def main():
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        user_input = input().strip()
        if not user_input:
            continue
        command, subcommand = user_input.split(" ", 1)
        args = [subcommand]
        if "'" in subcommand:
            args = shlex.split(subcommand)

        if is_valid_builtin_command(command):
            valid_commands[command](*args)
            continue
        executable_path = search_as_executable(command)
        if executable_path:
            process = subprocess.Popen([command, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            print(stdout)
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
