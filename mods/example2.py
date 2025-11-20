import functions.choices as cho
import functions.terminal as term
import functions.save as save
import functions.splash as splash
import time

def main():
    # Display intro splash
    custom_splashes = [
        "Welcome to the Example Adventure!",
        "Your journey begins now...",
        "Prepare yourself!"
    ]
    splash.displaySplash(custom_splashes)
    
    # Load or initialize save data
    saveData = save.load()
    mod_inventory = saveData.get('example_mod_inventory', [])
    mod_visited = saveData.get('example_mod_visited', False)
    
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