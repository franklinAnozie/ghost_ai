#!./new_env/bin/python3

from main.console import Console

if __name__ == "__main__":
    new_console = Console()
    new_console.prompt = "##ask ghost$$  "
    new_console.cmdloop()
