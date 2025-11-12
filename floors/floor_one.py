from ..functions import inventory as inv
from ..functions import choices as choose
import random

inventory = []

possible_rooms = [  
    "The room is dark and smells faintly of rust.",
    "It looks like a birthday party. Balloons are everywhere.",
    "There is a soft hum from exposed wires on the ground.",
    "It's bright. The room is loud aswell. It overwhelms you."
]

def floor_one(inventory):
    while True:
        choice = choose.two_options("Do you want to go left or right?", "left", "right", "you go left", )
        current_index = random.randint(0, len(possible_rooms) - 1)
        current_room = possible_rooms[current_index]
        pass