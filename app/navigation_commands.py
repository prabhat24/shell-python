import os
import sys

class Navigation:
    
    _instance = None

    def __init__(self):
        self.current_directory = os.getcwd()
        Navigation._instance = self

    def get_instance():
        if Navigation._instance:
            return Navigation._instance
        else:
            return Navigation()

    def pwd(self, *args):
        print(self.current_directory)

    def cd(self, *args):
        path = args[0]
        print
        if os.path.isabs(path) and os.path.isdir(path):
            self.current_directory = path
        else:
            print(f"cd: {path}: No such file or directory")

