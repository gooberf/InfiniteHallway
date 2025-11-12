import random
import functions.inventory as inv
import functions.choices as choose
import os

if os.path.exists("LLMsEnabled"):
    with open("LLMsEnabled", "r") as file:
        data = file.read()
    if data == "1":
        LLMsEnabled = True
    else:
        LLMsEnabled = False

inventory = []

possible_rooms = [  
    "The room is dark and smells faintly of rust.",
    "It looks like a birthday party. Balloons are everywhere.",
    "There is a soft hum from exposed wires on the ground.",
    "It's bright. The room is loud aswell. It overwhelms you."
]

def floor_one():
    while True:
        choice = choose.two_options("Do you want to go left or right?", "left", "right", "you go left", )
        current_index = random.randint(0, len(possible_rooms) - 1)
        current_room = possible_rooms[current_index]
        pass
