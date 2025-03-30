import os
import sys
import subprocess
from collections import deque

class Navigation:
    
    _instance = None

    def __init__(self):
        self.set_current_dir(os.getcwd())
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

        if path.startswith("~"):
            path = path.replace("~", os.environ.get("HOME"))

        if os.path.isabs(path):
            if os.path.isdir(path):
                self.set_current_dir(path)
                return
            else:
                print(f"cd: {path}: No such file or directory")
                return
        path_seqments = path.split("/")

        q = deque(path_seqments)
        while q:
            ele = q.popleft()
            # work
            if ele == "..":
                new_path = self.current_directory.rsplit("/", maxsplit=1)[0] 
                new_path = new_path if new_path else "/"
                self.set_current_dir(new_path)
            elif ele == ".":
                pass
            else:
                new_path = os.path.join(self.current_directory, ele)
                if os.path.isdir(new_path):
                    self.set_current_dir(new_path)
                else:
                    print(f"cd: {path}: No such file or directory")
                    break
    

    def set_current_dir(self, new_path):
        self.current_directory = self.clear_ending_path_seperator(new_path)

    @staticmethod
    def clear_ending_path_seperator(path):
        if path == "/":
            return path
        if path.endswith("/"):
            cleared_path = path.rsplit("/", 1)[0]
            if cleared_path:
                return cleared_path
        return path
