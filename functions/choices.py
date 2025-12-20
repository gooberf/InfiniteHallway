import colorama
import os
from colorama import Fore, Style
import functions.terminal as clear_term

# Initialize colorama
colorama.init(autoreset=True)

# a function to give the player 2 options
# commenting out end_texts because it's easier to just print the text in the floor file with an if statement
def two_options(text, option1, option2, error_message="Invalid", input_func=input):
    option1_lower = option1.lower()
    option2_lower = option2.lower()
    while True:
        picked_option = input_func(f'{Fore.CYAN}{"=" * 32}{Style.RESET_ALL}\n{Fore.YELLOW}{text}{Style.RESET_ALL}\n{Fore.CYAN}{"-" * 32}{Style.RESET_ALL}\n{Fore.GREEN}{option1}{Style.RESET_ALL}\n{Fore.GREEN}{option2}{Style.RESET_ALL}\n{Fore.CYAN}{"=" * 32}{Style.RESET_ALL}\n').lower()
        if picked_option == option1_lower:
            clear_term.clear()
            return option1
        elif picked_option == option2_lower:
            clear_term.clear()
            return option2
        else:
            print(f'{Fore.RED}{error_message}{Style.RESET_ALL}')
            
# a function to give the player 4 options, probably only for movement, but we'll see.
def four_options(text, option1, option2, option3, option4, error_message='Invalid', input_func=input):
    option1_lower = option1.lower()
    option2_lower = option2.lower()
    option3_lower = option3.lower()
    option4_lower = option4.lower()
    while True:
        picked_option = input_func(f'{Fore.CYAN}{"=" * 32}{Style.RESET_ALL}\n{Fore.YELLOW}{text}{Style.RESET_ALL}\n{Fore.CYAN}{"-" * 32}{Style.RESET_ALL}\n{Fore.GREEN}{option1}{Style.RESET_ALL}\n{Fore.GREEN}{option2}{Style.RESET_ALL}\n{Fore.GREEN}{option3}{Style.RESET_ALL}\n{Fore.GREEN}{option4}{Style.RESET_ALL}\n{Fore.CYAN}{"=" * 32}{Style.RESET_ALL}\n').lower()
        if picked_option == option1_lower:
            clear_term.clear()
            return option1
        elif picked_option == option2_lower:
            clear_term.clear()
            return option2
        elif picked_option == option3_lower:
            clear_term.clear()
            return option3
        elif picked_option == option4_lower:
            clear_term.clear()
            return option4
        else:
            print(f'{Fore.RED}{error_message}{Style.RESET_ALL}')
        
def three_options(text, option1, option2, option3, error_message="Invalid", input_func=input):
    option1_lower = option1.lower()
    option2_lower = option2.lower()
    option3_lower = option3.lower()
    while True:
        picked_option = input_func(f'{Fore.CYAN}{"=" * 32}{Style.RESET_ALL}\n{Fore.YELLOW}{text}{Style.RESET_ALL}\n{Fore.CYAN}{"-" * 32}{Style.RESET_ALL}\n{Fore.GREEN}{option1}{Style.RESET_ALL}\n{Fore.GREEN}{option2}{Style.RESET_ALL}\n{Fore.GREEN}{option3}{Style.RESET_ALL}\n{Fore.CYAN}{"=" * 32}{Style.RESET_ALL}\n').lower()
        if picked_option == option1_lower:
            clear_term.clear()
            return option1
        elif picked_option == option2_lower:
            clear_term.clear()
            return option2
        elif picked_option == option3_lower:
            clear_term.clear()
            return option3
        else:
            print(f'{Fore.RED}{error_message}{Style.RESET_ALL}')

# a function to give the player options from a python list
def list_options(text, options_list, error_message="Invalid", input_func=input):

    if not options_list or len(options_list) == 0:
        raise ValueError("options_list must contain at least one option")
    
    options_lower = [opt.lower() for opt in options_list]
    
    while True:
        options_display = '\n'.join([f'{Fore.GREEN}{opt}{Style.RESET_ALL}' for opt in options_list])
        
        picked_option = input_func(f'{Fore.CYAN}{"=" * 32}{Style.RESET_ALL}\n{Fore.YELLOW}{text}{Style.RESET_ALL}\n{Fore.CYAN}{"-" * 32}{Style.RESET_ALL}\n{options_display}\n{Fore.CYAN}{"=" * 32}{Style.RESET_ALL}\n').lower()
        
        if picked_option in options_lower:
            clear_term.clear()
            index = options_lower.index(picked_option)
            return options_list[index]
        else:
            print(f'{Fore.RED}{error_message}{Style.RESET_ALL}')