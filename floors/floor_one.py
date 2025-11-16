import random
import functions.choices as choose
import functions.save as gameSave
import functions.playtimetracker as playtimetracker
import os
import time
import functions.terminal as terminal
from colorama import Fore, Style

def _ask_load_save():
        """Ask whether to load an existing save or start fresh and return saveData."""
        if os.path.exists(gameSave.SAVE_FILE):
            while True:
                choice = input("Do you want to load your save? (yes/no): ").strip().lower()
                if choice == "yes":
                    return gameSave.load()
                if choice == "no":
                    print("Starting fresh :)")
                    return {"inventory": [], "bought_key": False, "door_open": False, "floor": 1}
                print("Choices are 'yes' or 'no'. Please answer correctly.")
        else:
            return {"inventory": [], "bought_key": False, "door_open": False, "floor": 1}


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
                terminal.clear()
                print("just answer the damn question")
                

        inventory = saveData['inventory']
        bought_key = saveData['bought_key']
        door_open = saveData['door_open']
        floor = saveData['floor']
        if not floor == 1:
            return inventory
        #global bought_key
        #global door_open
        #global inventory
        #global saveData
        
        while True:
                choice = choose.two_options("Do you want to go left or right?", "left", "right")
                current_index = random.randint(0, len(possible_rooms) - 1)
                current_room = possible_rooms[current_index]
                print(f"{Fore.BLUE}{current_room}{Style.RESET_ALL}")
                choice = choose.three_options("Would you like to look around? You can also view your stats", "yes", "no", "stats")
                if choice == "yes" and current_index == 0 and "Rusted Axe" not in inventory:
                    inventory.append("Rusted Axe")
                    saveData['inventory'] = inventory
                    print(f"{Fore.YELLOW}You find an axe lying on the floor.{Style.RESET_ALL}")
                    print(f"{Fore.WHITE}It's covered in rust{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}You now have {inventory} in your inventory :){Style.RESET_ALL}")
                    print(f"{Fore.CYAN}You leave the room{Style.RESET_ALL}")
                    continue
                elif choice == 'stats':
                    # Update saveData with current state before displaying stats
                    saveData['inventory'] = inventory
                    saveData['bought_key'] = bought_key
                    saveData['door_open'] = door_open
                    saveData['floor'] = 1
                    gameSave.save(saveData)
                    
                    # Display formatted statistics
                    gameSave.display_stats(inventory)
                    continue
                elif choice == "yes" and current_index == 0 and "Rusted Axe" in inventory:
                    print(f"{Fore.WHITE}You enter again.{Style.RESET_ALL}")
                    print(f"{Fore.BLUE}The room looks just like it did when you left it.{Style.RESET_ALL}")
                    print(f"{Fore.WHITE}You check around the room again, the axe that was there didn't magically reappear.{Style.RESET_ALL}")
                elif choice == "yes" and current_index == 1 and not bought_key:
                    print(f"{Fore.WHITE}You look around the room and see... someone{Style.RESET_ALL}")
                    print(f"{Fore.MAGENTA}{Style.BRIGHT}-----Merchant-----{Style.RESET_ALL}")
                    print(f"{Fore.CYAN}Oh, hello wanderer! I didn't think another unfortunate soul would end up here...{Style.RESET_ALL}")
                    choice = choose.two_options(f"{Fore.MAGENTA}-----Merchant-----\nWould you like to look at my wares?{Style.RESET_ALL}", "yes", "no")
                    if choice == "yes":
                        print(f"{Fore.MAGENTA}{Style.BRIGHT}-----Merchant-----{Style.RESET_ALL}")
                        print(f"{Fore.YELLOW}Item: {Fore.GREEN}Old Key{Style.RESET_ALL}")
                        print(f"{Fore.YELLOW}Cost: {Fore.RED}Ladder{Style.RESET_ALL}")
                        print(f"{Fore.MAGENTA}{Style.BRIGHT}-----Merchant-----{Style.RESET_ALL}")
                        print(f"{Fore.CYAN}This is all I have as of now, wanderer.{Style.RESET_ALL}")
                        choice = choose.two_options(f"{Fore.MAGENTA}-----Merchant-----\nBuy the Key?{Style.RESET_ALL}", "yes", "no")
                        if choice == "yes" and "Ladder" in inventory:
                            inventory.remove("Ladder")
                            inventory.append("Old Key")
                            saveData['inventory'] = inventory
                            saveData['bought_key'] = True
                            print(f"{Fore.GREEN}You bought an old key!{Style.RESET_ALL}")
                            print(f"{Fore.GREEN}You now have {inventory} in your inventory!{Style.RESET_ALL}")
                            bought_key = True
                            continue
                        elif choice == "yes" and "Ladder" not in inventory:
                            print(f"{Fore.MAGENTA}{Style.BRIGHT}-----Merchant-----{Style.RESET_ALL}")
                            print(f"{Fore.RED}This isn't a charity! Leave!{Style.RESET_ALL}")
                            print(f"{Fore.WHITE}The merchant swiftly kicks you out. Maybe return when you have what they want.{Style.RESET_ALL}")
                            continue
                        elif choice == "no":
                            print(f"{Fore.MAGENTA}{Style.BRIGHT}-----Merchant-----{Style.RESET_ALL}")
                            print(f"{Fore.CYAN}Alright then, wanderer. Safe travels.{Style.RESET_ALL}")
                            print(f"{Fore.WHITE}You leave the room, heading back to the hallway{Style.RESET_ALL}")
                            continue
                    elif choice == "no":
                        print(f"{Fore.MAGENTA}{Style.BRIGHT}-----Merchant-----{Style.RESET_ALL}")
                        print(f"{Fore.CYAN}Alright then, wanderer. Safe travels.{Style.RESET_ALL}")
                        print(f"{Fore.WHITE}You leave the room, heading back to the hallway{Style.RESET_ALL}")
                        continue
                elif choice == "yes" and current_index == 1 and bought_key:
                    print(f"{Fore.WHITE}You walk into the room, but the merchant isn't here.{Style.RESET_ALL}")
                    print(f"{Fore.BLUE}You wonder where they went before heading back to the hallway.{Style.RESET_ALL}")
                    continue
                elif current_index == 2 and "Ladder" not in inventory and not bought_key:
                    print(f"{Fore.YELLOW}There is a ladder in a pool of water...{Style.RESET_ALL}")
                    print(f"{Fore.RED}The exposed wires are right next to the water.{Style.RESET_ALL}")
                    choice = choose.two_options("Risk getting shocked to get the ladder?", "yes", "no")
                    if choice == "yes":
                        ran_num = random.randint(1,2)
                        if ran_num == 1:
                            inventory.append("Ladder")
                            saveData['inventory'] = inventory
                            print(f"{Fore.GREEN}You got the ladder!{Style.RESET_ALL}")
                            print(f"{Fore.GREEN}You now have {inventory} in your inventory.{Style.RESET_ALL}")
                            print(f"{Fore.WHITE}After getting back out of the pool of water, you leave the room.{Style.RESET_ALL}")
                            continue
                        else:
                            print(f"{Fore.RED}You get shocked and fall unconscious!{Style.RESET_ALL}")
                            print(f"{Fore.WHITE}When you awaken, you are in the hallway again.{Style.RESET_ALL}")
                            continue
                    elif choice == "no":
                        print(f"{Fore.WHITE}You leave the ladder where it is, deciding not to try and grab it.{Style.RESET_ALL}")
                        print(f"{Fore.CYAN}You leave the room.{Style.RESET_ALL}")
                        continue
                elif current_index == 2 and "Ladder" in inventory and choice == "yes" or current_index == 2 and bought_key and choice == "yes":
                    print(f"{Fore.WHITE}You enter the room, the pool of water still on the floor.{Style.RESET_ALL}")
                    print(f"{Fore.BLUE}This time, you notice that a pipe is dripping water into the pool...{Style.RESET_ALL}")
                    print(f"{Fore.BLUE}That's new.{Style.RESET_ALL}")
                    print(f"{Fore.WHITE}You don't pay any mind to it and go back to the hallway, with nothing left to do here.{Style.RESET_ALL}")
                    continue
                elif current_index == 2 and choice == "no":
                    print(f"{Fore.CYAN}You turn back to the hallway{Style.RESET_ALL}")
                    continue
                elif current_index == 3 and choice == "yes":
                    print(f"{Fore.YELLOW}You notice a door that hides in the walls perfectly.{Style.RESET_ALL}")
                    choice = choose.two_options("Do you open it?", "yes", "no")
                    if choice == "yes":
                        print(f"{Fore.RED}You notice the door is locked.{Style.RESET_ALL}")
                        if "Old Key" in inventory and not door_open:
                            choice = choose.two_options("Use your key to unlock it?", "yes", "no")
                            door_open = True
                            saveData['door_open'] = True
                            if choice == "yes":
                                inventory.remove("Old Key")
                                saveData['inventory'] = inventory
                                print(f"{Fore.GREEN}You open the door, but in the process, the key gets stuck in the lock.{Style.RESET_ALL}")
                                print(f"{Fore.GREEN}You now have {inventory}{Style.RESET_ALL}")
                                print(f"{Fore.WHITE}You walk through the door and see wooden boards blocking your path.{Style.RESET_ALL}")
                                if "Rusted Axe" in inventory:
                                    choice = choose.two_options("Break down the boards?", "yes", "no")
                                    if choice == "yes":
                                        print(f"{Fore.GREEN}You break down the boards, breaking the axe from how old it was.{Style.RESET_ALL}")
                                        print(f"{Fore.CYAN}You go through the gap and see something odd{Style.RESET_ALL}")
                                        print(f"{Fore.BLUE}It looks just like the hallways from before, but you sense that it's different somehow.{Style.RESET_ALL}")
                                        print(f"{Fore.MAGENTA}{Style.BRIGHT}You enter the 'floor two', determining which way to go next.{Style.RESET_ALL}")
                                        inventory.remove("Rusted Axe")
                                        saveData['inventory'] = inventory
                                        return inventory
                                    if choice == "no":
                                        print(f"{Fore.WHITE}You turn back, going to the hallways again.{Style.RESET_ALL}")
                                        print(f"{Fore.BLUE}You feel you should come back later when you have something to break the boards.{Style.RESET_ALL}")
                                        continue
                                elif "Rusted Axe" not in inventory:
                                    print(f"{Fore.RED}You have nothing to break the doors.{Style.RESET_ALL}")
                                    print(f"{Fore.WHITE}You turn back, going to the hallways{Style.RESET_ALL}")
                                    print(f"{Fore.BLUE}You take mental note of the door.{Style.RESET_ALL}")
                                    continue
                            elif choice == "no":
                                print(f"{Fore.WHITE}You keep your key and turn around{Style.RESET_ALL}")
                                print(f"{Fore.BLUE}You take note of this door though, having a feeling it's important.{Style.RESET_ALL}")
                                continue
                        elif door_open:
                            print(f"{Fore.WHITE}You go back through the door, but the boards still block your path.{Style.RESET_ALL}")
                            if "Rusted Axe" in inventory:
                                    choice = choose.two_options("Break down the boards?", "yes", "no")
                                    if choice == "yes":
                                        print(f"{Fore.GREEN}You break down the boards, breaking the axe from how old it was.{Style.RESET_ALL}")
                                        print(f"{Fore.CYAN}You go through the gap and see something odd{Style.RESET_ALL}")
                                        print(f"{Fore.BLUE}It looks just like the hallways from before, but you sense that it's different somehow.{Style.RESET_ALL}")
                                        print(f"{Fore.MAGENTA}{Style.BRIGHT}You enter the 'floor two', determining which way to go next.{Style.RESET_ALL}")
                                        inventory.remove("Rusted Axe")
                                        saveData['inventory'] = inventory
                                        return inventory
                                    if choice == "no":
                                        print(f"{Fore.WHITE}You turn back, going to the hallways again.{Style.RESET_ALL}")
                                        print(f"{Fore.BLUE}You feel you should come back later when you have something to break the boards.{Style.RESET_ALL}")
                                        continue
                                    elif "Rusted Axe" not in inventory:
                                        print(f"{Fore.RED}You have nothing to break the doors.{Style.RESET_ALL}")
                                        print(f"{Fore.WHITE}You turn back, going to the hallways{Style.RESET_ALL}")
                                        print(f"{Fore.BLUE}You take mental note of the door.{Style.RESET_ALL}")
                                        continue
                        elif "Old Key" not in inventory:
                            print(f"{Fore.RED}You don't have anything to unlock the door.{Style.RESET_ALL}")
                            print(f"{Fore.WHITE}You leave, knowing to come back with a key.{Style.RESET_ALL}")
                            continue
                    elif current_index == 3 and choice == "no":
                        print(f"{Fore.CYAN}You go back to the hall{Style.RESET_ALL}")
                        print(f"{Fore.BLUE}You have a feeling that door was important.{Style.RESET_ALL}")
                        continue
    except KeyboardInterrupt:
        print("Game interrupted by user.")
        saveChoice = choose.two_options("Would you like to save?", 'yes', 'no')
        if saveChoice == 'yes':
            # Load existing save to preserve any additional fields (eg. playtime)
            try:
                saveData = gameSave.load()
            except Exception:
                saveData = {}

            saveData['inventory'] = inventory
            saveData['bought_key'] = bought_key
            saveData['door_open'] = door_open
            saveData['floor'] = 1
            try:
                gameSave.save(saveData)
            except Exception as e:
                print(f"Failed to save game: {e}")
            print("Game saved successfully. Goodbye!")
            exit()
        else:
            print("okay i'm just gonna waste a minute of your time")
            time.sleep(60)
            terminal.clear()
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