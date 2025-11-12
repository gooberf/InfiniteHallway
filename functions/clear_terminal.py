import os

def clear():
    """Clear the terminal screen. Works on both Windows and Unix systems."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

