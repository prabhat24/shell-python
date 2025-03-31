import sys
from app.all_commands import *
import subprocess
import shlex
import readline

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")
readline.set_completion_display_matches_hook(display_matches)
readline.parse_and_bind("set bell-style audible")  # type: ignore
readline.set_auto_history(True)  # type: ignore

def main():
    # Wait for user input
    while True:
        user_input = input("$ ").strip()
        if not user_input:
            continue

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
