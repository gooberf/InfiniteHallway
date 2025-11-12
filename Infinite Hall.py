import random
# all rooms that the game has
possible_rooms = [  
    "The room is dark and smells faintly of rust.",
    "It looks like a birthday party. Balloons are everywhere.",
    "There is a soft hum from exposed wires on the ground.",
    "It's bright. The room is loud aswell. It overwhelms you."
]
f2_possible_rooms = [
    "The room seems to stretch forever, yet also folds in on itself. Every time you blink, the walls are closer.",
    "There's grass beneath you, soft and cold. The ceiling above is a perfect blue sky... until you notice clouds moving underneath it.",
    "Everything here glows faintly, like it's sunlight but not. Furniture floats a few inches off the floor, gently spinning in slow circles.",
    "Mirrors line the walls, but none show your reflection. Instead, you see the rooms you entered on the first floor in them."
]
# player's inventory
inventory = []
# determines if the merchant spawns. They do because it is false.
bought_key = False
# this makes floor 1
def floor_one():
    global bought_key
    while True:
        # determining the room. the choice of left or right doesn't matter yet though. It's just random.
        choice = input('Do you want to go left or right? ')
        print(f"You enter the room on your {choice}")
        # current_index is the index for the rooms. 0 is the rust room for example.
        current_index = random.randint(0, len(possible_rooms) - 1)
        current_room = possible_rooms[current_index]
        # prints the current room's description
        print(current_room)
        # checks if the player wants to explore the room instead of leaving immediately
        choice = input('Would you like to look around? (yes/no) ')
        if choice.lower() == "no":
            print("You leave the room and continue down the hallway.")
            continue  # move to next room
        elif choice.lower() == "yes":
            print("You look around the room before leaving.")
            # this checks the room so it can do room-specific things. The "not in inventory" makes sure you can't get extra axes in this case.
            if current_index == 0 and "Rusted Axe" not in inventory:
                # in this case, in the rusty room, the player finds an axe.
                print("You find a rusted axe. Might be useful.")
                choice = input('Would you like to take it? (yes/no) ')
                # if yes, takes the axe and leaves the room. if no, just leaves the room.
                if choice.lower() == "yes":
                    inventory.append("Rusted Axe")
                    print("Axe added to inventory")
                    # tells the player what they have in their inventory
                    print(f"You now have {inventory} in your inventory!")
                    print("You leave the room.")
                    continue
                elif choice.lower() == "no":
                    print("You leave the axe and exit the room.")
                    continue
            elif current_index == 0 and "Rusted Axe" in inventory:
                print("You enter again, but it's the same as last time.")
                print("The axe that was here before is with you.")
                print("There is nothing here for you now. You leave the room")
                continue
            if current_index == 1 and bought_key == False:
                print("You look around the room and see... someone?")
                print("Merchant - Hello wanderer. I didn't think another unfortunate soul would be trapped here.")
                choice = input('Merchant - Would you like to look at my wares? ')
                if choice.lower() == "yes":
                    print("Key - Cost = 1 Ladder.")
                    print("Merchant - This is all I have now, wanderer.")
                    choice = input('Merchant - Buy it? ')
                    if choice.lower() == "yes" and "Ladder" in inventory:
                        inventory.remove("Ladder")
                        inventory.append("Key")
                        print("You bought a key!")
                        # Makes it so the merchant wont spawn here after buying the key.
                        bought_key = True
                        continue
                    elif choice.lower() == "yes" and "Ladder" not in inventory:
                        print("Merchant - This isn't a charity! You don't have the item.")
                        print("The merchant kicks you out. Maybe return when you have it.")
                        continue
                    elif choice.lower() == "no":
                        print("Merchant - Come back later then.")
                        print("You go back into the hallway.")
                        continue
            elif current_index == 1 and bought_key == True:
                print("You look around for the merchant, but they aren't here.")
                print("You go back to the hallway.")
                continue
            elif current_index == 2:
                print("There is a ladder where the wires are.")
                choice = input('Take the risk for the ladder? ')
                if choice.lower() == "yes" and "Ladder" not in inventory:
                    random_number = random.randint(1,2)
                    if random_number == 1:
                        print("You get the ladder!")
                        inventory.append("Ladder")
                        print(f"You now have {inventory} in your inventory!")
                        print("After getting back out of the wires, you leave the room.")
                        continue
                    else:
                        print("You get shocked and fall unconscious.")
                        print("When you awaken, you are in the hallway again.")
                        continue
                elif choice.lower() == "no":
                    print("You leave the ladder and exit the room.")
                    continue
            elif current_index == 3:
                print("It hurts to look around here...")
                print("Through some luck, you find a door.")
                choice = input('Open it? ')
                if choice.lower() == "yes":
                    print("The door is locked.")
                    print(f"you have {inventory}")
                    if "Key" in inventory:
                        choice = input('Open it? ')
                        if choice.lower() == "yes":
                            print("You unlock the door. The key gets stuck in the door.")
                            inventory.remove("Key")
                            print(f"You now have {inventory}.")
                            # change this later, make it bring player somewhere
                            print("You walk through it, but the path is blocked by wooden boards nailed to the wall.")
                            print("You need something to break it to get through.")
                            if "Rusted Axe" in inventory:
                                choice = input('Break the boards with the axe? ')
                                if choice.lower() == "yes":
                                    inventory.remove("Rusted Axe")
                                    print("You break through the boards and walk through.")
                                    print(f"The axe breaks in the process. You now have {inventory}")
                                    print("It seems like a second floor to the hallway.")
                                    print("You enter the second floor, stumbling into the hallway as the door behind you dissapears.")
                                    print("You look around, and it seems to be the exact same as the first floor.")
                                    second_floor()
                                    break
                            continue
                        elif choice.lower() == "no":
                            print("You leave the room, not touching the door.")
                    elif "Key" not in inventory:
                        print("You don't have anything to open it.")
                        print("After looking around some more, you find nothing else.")
                        print("You leave the room, taking note of the locked door.")
                        continue
# this makes the second floor
def second_floor():
    down_coordinate = 0
    while True:
        if down_coordinate == 0:
            choice = input('Go up the hall, into the room on your right, or the room on your left? ')
            if choice.lower() == "up":
                print("You move up the hall.")
                down_coordinate += 1
                continue
            elif choice.lower() == "left":
                print("You enter the room on your left.")
                print(f2_possible_rooms[0])
                choice = input('Would you like to look around? (yes or no)')
                if choice.lower() == "yes":
                    print("I still need to do this part.")
                    break
        elif down_coordinate == 1:
            choice = input('Go back down the hall, into the room on your right, or the room on your left?')
            if choice.lower() == "down":
                print("You move down the hall.")
                down_coordinate += -1
                continue

# this actually starts the game
floor_one()