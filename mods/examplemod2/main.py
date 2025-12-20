import functions.choices as cho
import functions.terminal as term
import functions.save as save
import time

def main():
    saveData = save.load()
    mod_inventory = saveData['example_mod_inventory'] if 'example_mod_inventory' in saveData else []
    mod_visited = saveData['example_mod_visited'] if 'example_mod_visited' in saveData else False
    
    term.clear()
    print("You find yourself in a mysterious room.")
    time.sleep(1)
    
    if not mod_visited:
        print("This is your first time here.")
    else:
        print("You've been here before.")
    
    # First choice
    choice1 = cho.two_options(
        "What do you do?",
        "Examine the room",
        "Leave immediately"
    )
    
    if choice1 == "Examine the room":
        print("You find a glowing key on the floor.")
        mod_inventory.append("Glowing Key")
        
        # Second choice
        choice2 = cho.three_options(
            "What next?",
            "Take the key",
            "Leave it",
            "Examine the key closer"
        )
        
        if choice2 == "Take the key":
            print("You pick up the key. It feels warm to the touch.")
        elif choice2 == "Leave it":
            print("You decide to leave the key where it is.")
            mod_inventory.remove("Glowing Key")
        else:
            print("The key seems to pulse with an inner light.")
    
    # Save progress
    saveData['example_mod_inventory'] = mod_inventory
    saveData['example_mod_visited'] = True
    save.save(saveData)
    
    print("\nYour adventure ends here... for now.")
    time.sleep(2)