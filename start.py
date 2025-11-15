import os
import time
import random

print("Ensuring you have required dependencies...")
time.sleep(random.randint(1,100)/100)

missingDependencies = []

def choose(text, option1, option2, error_message="Invalid", input_func=input):
    while True:
        picked_option = input_func(f'--------------------------------\n{text}\n------\n{option1}\n{option2}\n--------------------------------\n').lower()
        if picked_option == option1:
            return picked_option
        elif picked_option == option2:
            return picked_option
        else:
            print(error_message)

try:
    import colorama
except:
    missingDependencies.append("colorama")

try:
    import ollama
except:
    missingDependencies.append("ollama")

if missingDependencies == []:
    print("You have all required dependancies!")
else:
    output_string = ", ".join(missingDependencies)
    install_string = " ".join(missingDependencies)
    print(f"You are missing dependancies: {output_string}")
    print("Attempting to load functions/choices.py...")
    install = choose("Would you like to install all required dependancies?", "yes", "no")
    if install == "yes":
        pip_command = input("What command do you use for pip? (Python's package installer) [default: 'pip']").strip().lower()
        if pip_command == "":
            pip_command = "pip"
            os.system(f"{pip_command} install {install_string}")
    else:
        print("The game will not be playable without these dependancies.\nQuitting...")
        exit()

failed_installs = []

try: import colorama
except: failed_installs.append('colorama')

try: import ollama
except: failed_installs.append('ollama')


if failed_installs == []: print("All dependancies successfully installed!")
else: 
    print("One or more installs FAILED. Quitting...")
    exit()


print("Testing critical game functions...")
time.sleep(random.randint(1,100)/100)

try:
    import functions.choices
    import functions.save
    import functions.clear_terminal
    print("Critical files loaded.")
except:
    print("One or more CRITICAL functions failed to import. The game will NOT function without these. Please re-download the game from the following link:\nhttps://github.com/gooberf/InfiniteHallway")
    exit()

print("Attempting to load floor files...")
time.sleep(random.randint(1,100)/100)

try:
    import floors.floor_one
    import floors.floor_two
    print("Loaded floors.")
except:
    print("One or more floor files failed to load. These are CRITICAL to the game. Please re-download the game from the following link:\nhttps://github.com/gooberf/InfiniteHallway")
    exit()

print("Checking less critical files...")
time.sleep(random.randint(1,100)/100)

try:
    import functions.easyMode
    print("Loaded less critical files.")
except:
    print("At least one less important function FAILED to load. The game can run without it, but will most likely encounter issues. It is recommended to re-download the game from:\nhttps://github.com/gooberf/InfiniteHallway")
    continueQ = choose("Continue execution with damaged files?", "yes", "no")
    if continueQ == "yes":
        pass
    else:
        print("Quitting...")
        exit()
print("Attempting to start game...")
time.sleep(random.randint(1,100)/100)

import main

main.start()