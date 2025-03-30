def is_valid_command(command):
    if command in valid_commands.keys():
        return True


def do_exit(*args):
    args = [ int(i) for i in args ]
    exit(args[0])

def do_echo(*args):
    text = " ".join(args)
    print(text)
    
def type_command(*args):
    arg_command = args[0]
    if is_valid_command(arg_command):
        print(f"{arg_command} is a shell builtin")
    else:
        print(f"{arg_command}: not found")
    

valid_commands = {
    "exit": do_exit,
    "echo": do_echo,
    "type": type_command
}


