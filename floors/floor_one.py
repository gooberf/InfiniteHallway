import random
import functions.inventory as inv
import functions.choices as choose

inventory = []

possible_rooms = [  
    "The room is dark and smells faintly of rust.",
    "It looks like a birthday party. Balloons are everywhere.",
    "There is a soft hum from exposed wires on the ground.",
    "It's bright. The room is loud aswell. It overwhelms you."
]

bought_key = False

def floor_one():
    global bought_key
    while True:
        choice = choose.two_options("Do you want to go left or right?", "left", "right", "you go left", )
        current_index = random.randint(0, len(possible_rooms) - 1)
        current_room = possible_rooms[current_index]
        print(current_room)
        choice = choose.two_options("Would you like to look around?", "yes", "no")
        if choice == "yes" and current_index == 0 and "Rusted Axe" not in inventory:
            print(f"You find an axe lying on the floor.\nIt's covered in rust\nYou now have {inventory} in your inventory :)")
            print("You leave the room")
            continue
        elif choice == "yes" and current_index == 0 and "Rusted Axe" in inventory:
            print("You enter again.\nThe room looks just like it did when you left it.\nYou check around the room again, the axe that was there didn't magically reappear.")
        elif choice =="yes" and current_index == 1 and not bought_key:
            print("You look around the room and see... someone\n-----Merchant-----\nOh, hello wanderer! I didn't think another unfortunate soul would end up here...")
            choice = choose.two_options("-----Merchant-----\nWould you like to look at my wares?", "yes", "no")
            if choice == "yes":
                print("-----Merchant-----\nItem: Old Key\nCost: Ladder\n-----Merchant-----\nThis is all I have as of now, wanderer.")
                choice = choose.two_options("-----Merchant-----\nBuy the Key?")
                if choice == "yes" and "Ladder" in inventory:
                    inventory.remove("Ladder")
                    inventory.append("Old Key")
                    print(f"You bought an old key!\n You now have {inventory} in your inventory!")
                    bought_key = True
                    continue
                elif choice == "yes" and "Ladder" not in inventory:
                    print("-----Merchant-----\nThis isn't a charity! Leave!\nThe merchant swiftly kicks you out. Maybe return when you have what they want.")
                    continue
                elif choice =="no":
                    print("-----Merchant-----\nAlright then, wanderer. Safe travels.\n You leave the room, heading back to the hallway")
                    continue
        elif choice == "yes" and current_index == 1 and bought_key:
            print("You walk into the room, but the merchant isn't here.\n You wonder where they went before heading back to the hallway.")
            continue
        elif current_index == 2:
            pass # not worked on yet