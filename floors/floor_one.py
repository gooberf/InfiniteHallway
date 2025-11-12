from ..functions import inventory as inv
from ..functions import choices as choose

inventory = ["key", "rope", "Suspiciously human shaped ceiling decoration", "Sayori"]

possible_rooms = [  
    "The room is dark and smells faintly of rust.",
    "It looks like a birthday party. Balloons are everywhere.",
    "There is a soft hum from exposed wires on the ground.",
    "It's bright. The room is loud aswell. It overwhelms you."
]

blahblahblah = inv.cha("key", "rem", "You lost teh key ): nooo", inventory)
inventory = blahblahblah

print(inventory)

def floor_one():
    pass