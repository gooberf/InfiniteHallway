import os
import rich
from rich.console import Console
import traceback


console = Console()

def clear():
    """Clear the terminal screen. Works on both Windows and Unix systems."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def run(cmd):
    os.system(cmd)
    
def genTraceback(msg):
    raise ValueError(msg)

def print_traceback(msg):
    try:
        genTraceback(msg)
    except:
        console.print_exception(show_locals=True)

def logTraceback(msg):
    print("I'm sorry, an uncaught exception occured!\nCheck traceback.txt for more details.")
    with open('traceback.txt', 'w') as tb:
        try:genTraceback(msg)
        except Exception:
            log = traceback.format_exc()
            tb.write(f"I'm sorry, but an uncaught exception occured!\n{log}")