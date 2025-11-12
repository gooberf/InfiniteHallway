import functions.choices as choose
import floors.floor_one as f1
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
# this runs the game itself
inventory = f1.floor_one()
