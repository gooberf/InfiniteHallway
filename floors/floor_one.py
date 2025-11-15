import random
import functions.choices as choose
import functions.save as gameSave
import functions.playtimetracker as playtimetracker
import os
import time
import functions.terminal as terminal

def _ask_load_save():
        """Ask whether to load an existing save or start fresh and return saveData."""
        if os.path.exists(gameSave.SAVE_FILE):
            while True:
                choice = input("Do you want to load your save? (yes/no): ").strip().lower()
                if choice == "yes":
                    return gameSave.load()
                if choice == "no":
                    print("Starting fresh :)")
                    return {"inventory": [], "bought_key": False, "door_open": False}
                print("Choices are 'yes' or 'no'. Please answer correctly.")
        else:
            return {"inventory": [], "bought_key": False, "door_open": False}


possible_rooms = [  
    "The room is dark and smells faintly of rust.",
    "It looks like a birthday party. Balloons are everywhere.",
    "There is a soft hum from exposed wires on the ground.",
    "It's bright. The room is loud aswell. It overwhelms you."
]

def floor_one():
    try:
        
        while True:
            try:
                saveData = _ask_load_save()
                break
            except KeyboardInterrupt:
                print("just answer the damn question")
                

        inventory = saveData['inventory']
        bought_key = saveData['bought_key']
        door_open = saveData['door_open']

        #global bought_key
        #global door_open
        #global inventory
        #global saveData
        
        while True:
                choice = choose.two_options("Do you want to go left or right?", "left", "right")
                current_index = random.randint(0, len(possible_rooms) - 1)
                current_room = possible_rooms[current_index]
                print(current_room)
                choice = choose.three_options("Would you like to look around? You can also view your stats", "yes", "no", "stats")
                if choice == "yes" and current_index == 0 and "Rusted Axe" not in inventory:
                    inventory.append("Rusted Axe")
                    saveData['inventory'] = inventory
                    print(f"You find an axe lying on the floor.\nIt's covered in rust\nYou now have {inventory} in your inventory :)")
                    print("You leave the room")
                    continue
                elif choice == 'stats':
                    try:
                        minutes, seconds = playtimetracker.tracker.get()
                    except Exception:
                        # If the live tracker isn't available, fall back to saved values
                        try:
                            saved = gameSave.load()
                            minutes = int(saved.get('playtime_minutes', 0))
                            seconds = int(saved.get('playtime_seconds', 0))
                        except Exception:
                            minutes = 0
                            seconds = 0

                    # Update saveData with current state
                    saveData['inventory'] = inventory
                    saveData['bought_key'] = bought_key
                    saveData['door_open'] = door_open
                    saveData['playtime_minutes'] = minutes
                    saveData['playtime_seconds'] = seconds

                    # Save the updated data
                    gameSave.save(saveData)
                    
                    # Read and display the saved data to the player
                    gameSave.read()
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
                            saveData['inventory'] = inventory
                            saveData['bought_key'] = True
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
                            saveData['inventory'] = inventory
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
                            saveData['door_open'] = True
                            if choice == "yes":
                                inventory.remove("Old Key")
                                saveData['inventory'] = inventory
                                print(f"You open the door, but in the process, the key gets stuck in the lock.\nYou now have {inventory}\nYou walk through the door and see wooden boards blocking your path.")
                                if "Rusted Axe" in inventory:
                                    choice = choose.two_options("Break down the boards?", "yes", "no")
                                    if choice == "yes":
                                        print("You break down the boards, breaking the axe from how old it was.\nYou go through the gap and see something odd\nIt looks just like the hallways from before, but you sense that it's different somehow.\nYou enter the 'floor two', determining which way to go next.")
                                        inventory.remove("Rusted Axe")
                                        saveData['inventory'] = inventory
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
                                        saveData['inventory'] = inventory
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
    except KeyboardInterrupt:
        print("Game interrupted by user.")
        saveChoice = choose.two_options("Would you like to save?", 'yes', 'no')
        if saveChoice == 'yes':
            # Load existing save to preserve any additional fields (eg. playtime)
            try:
                existing = gameSave.load()
            except Exception:
                existing = {}

            existing['inventory'] = inventory
            existing['bought_key'] = bought_key
            existing['door_open'] = door_open
            try:
                gameSave.save(existing)
            except Exception as e:
                print(f"Failed to save game: {e}")
            print("Game saved successfully. Goodbye!")
            exit()
        else:
            print("okay i'm just gonna waste a minute of your time")
            time.sleep(60)
            exit()
            

"""
try:
    floor_one()
except KeyboardInterrupt:
    print("Game interrupted by user. Exiting gracefully.")
    saveData['inventory'] = inventory
    saveData['bought_key'] = bought_key
    saveData['door_open'] = door_open
    gameSave.save(saveData)
    print("Game saved successfully. Goodbye!")
    exit()
except Exception as exception:
    print(f"An error occurred: {exception}")
    save = choose.two_options("An unexpected exception occured! You can choose to save, but it may result in a corrupted save. Would you like to save your data?", "yes", "no")
    if save == "yes":
        try:
            saveData['inventory'] = inventory
            saveData['bought_key'] = bought_key
            saveData['door_open'] = door_open
            gameSave.save(saveData)
            print("Game saved successfully.")
            restartChoice = choose.two_options("Would you like to restart the game?", "yes", "no")
            if restartChoice == "yes":
                print("Restarting the game...")
                import os
                os.execv(__file__, [''])
            else:
                print("Exiting the game. Goodbye!")
                exit()
        except Exception as save_exception:
            print(f"Failed to save the game: {save_exception}")
            exit()
    else:
        print("You chose not to save your data.")
        exit()
"""