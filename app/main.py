import sys

def do_exit(*args):
    args = [ int(i) for i in args ]
    exit(args[0])

valid_commands = {
    "exit": do_exit
}

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

        print(f"{command}: command not found")

def is_valid_command(command):
    if command in ["exit"]:
        return True


if __name__ == "__main__":
    main()
