import colorama
from colorama import Fore, Style
import functions.clear_terminal as clear_term
# a function to give the player 2 options
# commenting out end_texts because it's easier to just print the text in the floor file with an if statement
def two_options(text, option1, option2, error_message="Invalid", input_func=input):
    while True:
        picked_option = input_func(f'--------------------------------\n{text}\n------\n{option1}\n{option2}\n--------------------------------\n').lower()
        if picked_option == option1:
            clear_term.clear()
            return picked_option
        elif picked_option == option2:
            clear_term.clear()
            return picked_option
        else:
            print(error_message)
            
# a function to give the player 4 options, probably only for movement, but we'll see.
def four_options(text, option1, option2, option3, option4, error_message, input_func=input):
    while True:
        picked_option = input_func(f'--------------------------------\n{text}\n------\n{option1}\n{option2}\n{option3}\n{option4}\n--------------------------------\n').lower()
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
            print(error_message)
def three_options(text, option1, option2, option3, error_message="Invalid", input_func=input):
    while True:
        picked_option = input_func(f'--------------------------------\n{text}\n------\n{option1}\n{option2}\n{option3}\n--------------------------------\n').lower()
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
            print(error_message)