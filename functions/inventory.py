import os
current_file_path = os.path.abspath(__file__)

def cha(item, add_or_remove, lose_message, inventory_list="inventory"):
    if add_or_remove == "add":
        print(f"You got {item}")
        inventory_list.append(item)
        return inventory_list
    elif add_or_remove == "rem":
        print(f"{lose_message} {item}")
        inventory_list.remove(item)
        return inventory_list
    else:
        print("Well fuck you for inputting something wrong, me.")
        os.remove("choices.py")