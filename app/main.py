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

        # command_subcommand = user_input.split(" ", 1)
        # command = command_subcommand[0]
        # args = []
        # if len(command_subcommand) >=2:
        #     subcommand = command_subcommand[1]
        #     args = shlex.split(subcommand)
        command_with_args = shlex.split(user_input)
        command = command_with_args[0]
        args = []
        if len(command_with_args) >=2:
            args = command_with_args[1:]

        if is_valid_builtin_command(command):
            valid_commands[command](*args)
            continue
        executable_path = search_as_executable(command)
        if executable_path:
            process = subprocess.Popen([command, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            sys.stdout.write(stdout)
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
