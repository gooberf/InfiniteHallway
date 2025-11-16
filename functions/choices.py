import colorama
import os
from colorama import Fore, Style
import functions.terminal as clear_term

# Initialize colorama
colorama.init(autoreset=True)

# a function to give the player 2 options
# commenting out end_texts because it's easier to just print the text in the floor file with an if statement
def two_options(text, option1, option2, error_message="Invalid", input_func=input):
    while True:
        picked_option = input_func(f'{Fore.CYAN}{"=" * 32}{Style.RESET_ALL}\n{Fore.YELLOW}{text}{Style.RESET_ALL}\n{Fore.CYAN}{"-" * 32}{Style.RESET_ALL}\n{Fore.GREEN}{option1}{Style.RESET_ALL}\n{Fore.GREEN}{option2}{Style.RESET_ALL}\n{Fore.CYAN}{"=" * 32}{Style.RESET_ALL}\n').lower()
        if picked_option == option1:
            clear_term.clear()
            return picked_option
        elif picked_option == option2:
            clear_term.clear()
            return picked_option
        else:
            print(f'{Fore.RED}{error_message}{Style.RESET_ALL}')
            
# a function to give the player 4 options, probably only for movement, but we'll see.
def four_options(text, option1, option2, option3, option4, error_message='Invalid', input_func=input):
    while True:
        picked_option = input_func(f'{Fore.CYAN}{"=" * 32}{Style.RESET_ALL}\n{Fore.YELLOW}{text}{Style.RESET_ALL}\n{Fore.CYAN}{"-" * 32}{Style.RESET_ALL}\n{Fore.GREEN}{option1}{Style.RESET_ALL}\n{Fore.GREEN}{option2}{Style.RESET_ALL}\n{Fore.GREEN}{option3}{Style.RESET_ALL}\n{Fore.GREEN}{option4}{Style.RESET_ALL}\n{Fore.CYAN}{"=" * 32}{Style.RESET_ALL}\n').lower()
        if picked_option == option1:
            clear_term.clear()
            return picked_option
        elif picked_option == option2:
            clear_term.clear()
            return picked_option
        elif picked_option == option3:
            clear_term.clear()
            return picked_option
        elif picked_option == option4:
            clear_term.clear()
            return picked_option
        else:
            print(f'{Fore.RED}{error_message}{Style.RESET_ALL}')
        
def three_options(text, option1, option2, option3, error_message="Invalid", input_func=input):
    while True:
        picked_option = input_func(f'{Fore.CYAN}{"=" * 32}{Style.RESET_ALL}\n{Fore.YELLOW}{text}{Style.RESET_ALL}\n{Fore.CYAN}{"-" * 32}{Style.RESET_ALL}\n{Fore.GREEN}{option1}{Style.RESET_ALL}\n{Fore.GREEN}{option2}{Style.RESET_ALL}\n{Fore.GREEN}{option3}{Style.RESET_ALL}\n{Fore.CYAN}{"=" * 32}{Style.RESET_ALL}\n').lower()
        if picked_option == option1:
            clear_term.clear()
            return picked_option
        elif picked_option == option2:
            clear_term.clear()
            return picked_option
        elif picked_option == option3:
            clear_term.clear()
            return picked_option
        else:
            print(f'{Fore.RED}{error_message}{Style.RESET_ALL}')