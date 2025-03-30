import sys
from all_commands import *


def main():
    # Uncomment this block to pass the first stage
    

    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        user_input = input()
        command = user_input.strip().split()[0]
        args = user_input.strip().split()[1:]
        if is_valid_command(command):
            valid_commands[command](*args)
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
