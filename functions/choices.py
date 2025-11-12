# a function to give the player 2 options
def two_options(text, option1, option2, end_text_1, end_text_2, error_message="Invalid", input_func=input):
    while True:
        picked_option = input_func(f'{text}').lower()
        if picked_option == option1:
            print(end_text_1)
            return picked_option
        elif picked_option == option2:
            print(end_text_2)
            return picked_option
        else:
            print(error_message)
            
# a function to give the player 4 options, probably only for movement, but we'll see.
def four_options(text, option1, option2, option3, option4, end_text_1, end_text_2, end_text_3, end_text_4, error_message, input_func=input):
    while True:
        picked_option = input_func(f'{text}').lower()
        if picked_option == option1:
            print(end_text_1)
            return picked_option
        elif picked_option == option2:
            print(end_text_2)
            return picked_option
        elif picked_option == option3:
            print(end_text_3)
            return picked_option
        elif picked_option == option4:
            print(end_text_4)
            return picked_option
        else:
            print(error_message)