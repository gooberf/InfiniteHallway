import functions.choices as cho

possible_rooms = [
    "The room seems to stretch forever, yet also folds in on itself. Every time you blink, the walls are closer.",#index 0
    "There's grass beneath you, soft and cold. The ceiling above is a perfect blue sky... until you notice clouds moving underneath it.",
    "Everything here glows faintly, like it's sunlight but not. Furniture floats a few inches off the floor, gently spinning in slow circles.",
    "Mirrors line the walls, but none show your reflection. Instead, you see the rooms you entered on the first floor in them."#index 4
]

ver_pos = 0

def floor_two(inventory):
    global ver_pos
    while True:
        if ver_pos == 0:
            choice = cho.three_options("Move up the hall, into the room on your right, or into the room on your left?", "up", "left", "right")
            if choice == "up":
                ver_pos += 1
                print("You go up the hall")
                continue
            elif choice == "left":
                print(f"You enter the room on your left.\n{possible_rooms[0]}")
                choice = cho.two_options("Do you want to look around the room?", "yes", "no")
                if choice == "yes":
                    print("You look around the room, examining every last nook and cranny of it.\n You find nothing of interest yet.") # come back with a certain item, and smth else will happen (just an idea)
                    continue
                elif choice == "no":
                    print("You turn back around and leave the room, not really caring about what is inside.")
                    continue
            elif choice == "right":
                print(f"You enter the room on your right. \n{possible_rooms[3]}")
                continue # work on this one second
        elif ver_pos == 1:
            choice = cho.three_options("Move down the hall, into the room on your right, or into the room on your left?", "down", "left", "right")
            if choice == "down":
                ver_pos += -1
                print("You go back down the hall")
                continue
            elif choice == "left":
                print(f"You enter the room on your left.\n{possible_rooms[2]}")
                continue # work on this one third
            elif choice == "right":
                print(f"You enter the room on your right.\n{possible_rooms[1]}")
                continue # work on this one last
       