import random
import functions.choices as choose

inventory = []

possible_rooms = [  
    "The room is dark and smells faintly of rust.",
    "It looks like a birthday party. Balloons are everywhere.",
    "There is a soft hum from exposed wires on the ground.",
    "It's bright. The room is loud aswell. It overwhelms you."
]

door_open = False

bought_key = False

def floor_one():
    global bought_key
    global door_open
    while True:
        choice = choose.two_options("Do you want to go left or right?", "left", "right", "you go left", )
        current_index = random.randint(0, len(possible_rooms) - 1)
        current_room = possible_rooms[current_index]
        print(current_room)
        choice = choose.two_options("Would you like to look around?", "yes", "no")
        if choice == "yes" and current_index == 0 and "Rusted Axe" not in inventory:
            inventory.append("Rusted Axe")
            print(f"You find an axe lying on the floor.\nIt's covered in rust\nYou now have {inventory} in your inventory :)")
            print("You leave the room")
            continue
        elif choice == "yes" and current_index == 0 and "Rusted Axe" in inventory:
            print("You enter again.\nThe room looks just like it did when you left it.\nYou check around the room again, the axe that was there didn't magically reappear.")
        elif choice == "yes" and current_index == 1 and not bought_key:
            print("You look around the room and see... someone\n-----Merchant-----\nOh, hello wanderer! I didn't think another unfortunate soul would end up here...")
            choice = choose.two_options("-----Merchant-----\nWould you like to look at my wares?", "yes", "no")
            if choice == "yes":
                print("-----Merchant-----\nItem: Old Key\nCost: Ladder\n-----Merchant-----\nThis is all I have as of now, wanderer.")
                choice = choose.two_options("-----Merchant-----\nBuy the Key?", "yes", "no")
                if choice == "yes" and "Ladder" in inventory:
                    inventory.remove("Ladder")
                    inventory.append("Old Key")
                    print(f"You bought an old key!\nYou now have {inventory} in your inventory!")
                    bought_key = True
                    continue
                elif choice == "yes" and "Ladder" not in inventory:
                    print("-----Merchant-----\nThis isn't a charity! Leave!\nThe merchant swiftly kicks you out. Maybe return when you have what they want.")
                    continue
                elif choice == "no":
                    print("-----Merchant-----\nAlright then, wanderer. Safe travels.\nYou leave the room, heading back to the hallway")
                    continue
            elif choice == "no":
                print("-----Merchant-----\nAlright then, wanderer. Safe travels.\nYou leave the room, heading back to the hallway")
                continue
        elif choice == "yes" and current_index == 1 and bought_key:
            print("You walk into the room, but the merchant isn't here.\nYou wonder where they went before heading back to the hallway.")
            continue
        elif current_index == 2 and "Ladder" not in inventory and not bought_key:
            print("There is a ladder in a pool of water...\nThe exposed wires are right next to the water.")
            choice = choose.two_options("Risk getting shocked to get the ladder?", "yes", "no")
            if choice == "yes":
                ran_num = random.randint(1,2)
                if ran_num == 1:
                    inventory.append("Ladder")
                    print(f"You got the ladder!\nYou now have {inventory} in your inventory.\nAfter getting back out of the pool of water, you leave the room.")
                    continue
                else:
                    print("You get shocked and fall unconscious!\nWhen you awaken, you are in the hallway again.")
                    continue
            elif choice == "no":
                print("You leave the ladder where it is, deciding not to try and grab it.\nYou leave the room.")
                continue
        elif current_index == 2 and "Ladder" in inventory and choice == "yes" or current_index == 2 and bought_key and choice == "yes":
            print("You enter the room, the pool of water still on the floor.\nThis time, you notice that a pipe is dripping water into the pool...\nThat's new.\nYou don't pay any mind to it and go back to the hallway, with nothing left to do here.")
            continue
        elif current_index == 2 and choice == "no":
            print("You turn back to the hallway")
            continue
        elif current_index == 3 and choice == "yes":
            print("You notice a door that hides in the walls perfectly.")
            choice = choose.two_options("Do you open it?", "yes", "no")
            if choice == "yes":
                print("You notice the door is locked.")
                if "Old Key" in inventory and not door_open:
                    choice = choose.two_options("Use your key to unlock it?", "yes", "no")
                    door_open = True
                    if choice == "yes":
                        inventory.remove("Old Key")
                        print(f"You open the door, but in the process, the key gets stuck in the lock.\nYou now have {inventory}\nYou walk through the door and see wooden boards blocking your path.")
                        if "Rusted Axe" in inventory:
                            choice = choose.two_options("Break down the boards?", "yes", "no")
                            if choice == "yes":
                                print("You break down the boards, breaking the axe from how old it was.\nYou go through the gap and see something odd\nIt looks just like the hallways from before, but you sense that it's different somehow.\nYou enter the 'floor two', determining which way to go next.")
                                inventory.remove("Rusted Axe")
                                inventory.append("Broken Axe")
                                return inventory
                            if choice == "no":
                                print("You turn back, going to the hallways again.\nYou feel you should come back later when you have something to break the boards.")
                                continue
                        elif "Rusted Axe" not in inventory:
                            print("You have nothing to break the doors.\nYou turn back, going to the hallways\nYou take mental note of the door.")
                            continue
                    elif choice == "no":
                        print("You keep your key and turn around\nYou take note of this door though, having a feeling it's important.")
                        continue
                elif door_open:
                    print("You go back through the door, but the boards still block your path.")
                    if "Rusted Axe" in inventory:
                            choice = choose.two_options("Break down the boards?", "yes", "no")
                            if choice == "yes":
                                print("You break down the boards, breaking the axe from how old it was.\nYou go through the gap and see something odd\nIt looks just like the hallways from before, but you sense that it's different somehow.\nYou enter the 'floor two', determining which way to go next.")
                                inventory.remove("Rusted Axe")
                                return inventory
                            if choice == "no":
                                print("You turn back, going to the hallways again.\nYou feel you should come back later when you have something to break the boards.")
                                continue
                            elif "Rusted Axe" not in inventory:
                                print("You have nothing to break the doors.\nYou turn back, going to the hallways\nYou take mental note of the door.")
                                continue
                elif "Old Key" not in inventory:
                    print("You don't have anything to unlock the door.\nYou leave, knowing to come back with a key.")
                    continue
            elif current_index == 3 and choice == "no":
                print("You go back to the hall\nYou have a feeling that door was important.")
                continue
# why are you reading this? there isnt anything interesting here.