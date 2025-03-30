import sys
from app.all_commands import *
import subprocess

def main():
    # Uncomment this block to pass the first stage
    

    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        user_input = input()
        command = user_input.strip().split()[0]
        args = user_input.strip().split()[1:]
        if is_valid_builtin_command(command):
            valid_commands[command](*args)
        executable_path = search_as_executable(command)
        if executable_path:
            process = subprocess.Popen([command, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            print(stdout)
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
