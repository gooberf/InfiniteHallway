import os
import rich
from rich.console import Console

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

def traceback(msg):
    try: genTraceback(msg)
    except:
        console.print_exception(show_locals=True)