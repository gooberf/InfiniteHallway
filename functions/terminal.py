from multiprocessing import Value
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
    
def continuePlay():
    raise ValueError("Failed to continue playing.")

def nextDialogue():
    raise TypeError("Unexpected indent in terminal.py, line 24")

def choice():
    raise AttributeError("Function 'choice()' has no attribute 'display_two'")

def genTraceback(msg):
    raise ValueError(msg)
    choice()
    nextDialogue()
    continuePlay()


def print_traceback(msg):
    try:
        genTraceback(msg)
    except:
        genTraceback(msg)
        console.print_exception(show_locals=True)

def logTraceback(msg):
    print("I'm sorry, an uncaught exception occured!\nCheck traceback.txt for more details.")
    with open('traceback.txt', 'w') as tb:
        try:genTraceback(msg)
        except Exception:
            log = traceback.format_exc()
            tb.write(f"I'm sorry, but an uncaught exception occured!\n\n{log}")