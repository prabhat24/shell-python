import os
from app.navigation_commands import Navigation


def is_valid_builtin_command(command):
    if command in valid_commands.keys():
        return True
    return False

def do_exit(*args):
    args = [ int(i) for i in args ]
    exit(args[0])

def do_echo(*args):
    text = " ".join(args)
    print(text)

def type_command(*args):
    arg_command = args[0]
    if is_valid_builtin_command(arg_command):
        print(f"{arg_command} is a shell builtin")
        return
    executable_path = search_as_executable(arg_command)
    if executable_path:
        print(f"{arg_command} is {executable_path}")
    else:
        print(f"{arg_command}: not found")
    
def search_as_executable(command):
    path_list = os.environ.get("PATH").split(":")
    
    for path in path_list:
        if os.path.isdir(path):
            path_files = os.listdir(path)
            for file in path_files:
                if file == command and \
                        os.path.isfile(os.path.join(path, file)) \
                        and os.access(os.path.join(path, file), os.X_OK):
                    return os.path.join(path, file)
    return ""

def completer(text, state):
    """Autocomplete function for built-in commands."""
    options = [cmd for cmd in valid_commands.keys() if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    return None

           
valid_commands = {
    "exit": do_exit,
    "echo": do_echo,
    "type": type_command,
    "pwd": Navigation.get_instance().pwd,
    "cd": Navigation.get_instance().cd
}


