#!./new_env/bin/python3

from main.console import Console

if __name__ == "__main__":
    welcome = f"------------------------------------------- Welcome to GHOST AI -----------------------------------------------------"
    job = f"--- Your AI Assistant is command-line application that helps users generate cold emails for your job applications ---"
    instructions = f"----------------- Please enter your job title and location. (Eg. Painter Jobs in San Francisco) ---------------------"
    quit_inst = f"------------------ When you're done, please type quit or exit to quit the application. Thank You --------------------"
    new_console = Console()
    new_console.prompt = "(GHOST AI): "
    new_console.intro = f"{welcome}\n{job}\n{instructions}\n{quit_inst}"
    new_console.cmdloop()
