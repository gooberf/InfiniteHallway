import functions.choices as cho
import functions.save as save
import functions.playtimetracker as playtimetracker

possible_rooms = [
    "The room seems to stretch forever, yet also folds in on itself. Every time you blink, the walls are closer.",#index 0
    "There's grass beneath you, soft and cold. The ceiling above is a perfect blue sky... until you notice clouds moving underneath it.",
    "Everything here glows faintly, like it's sunlight but not. Furniture floats a few inches off the floor, gently spinning in slow circles.",
    "Mirrors line the walls, but none show your reflection. Instead, you see the rooms you entered on the first floor in them."#index 4
]

roomA_echo_available = False
roomA_echo_taken = False

roomB_fragment_taken = False

roomC_hollow_taken = False

roomD_tone_created = False
ver_pos = 0


def _show_stats(inventory):
    """Save current inventory and show the player's stats from the save file."""
    try:
        saveData = save.load()
    except Exception:
        saveData = {'inventory': [], 'bought_key': False, 'door_open': False}

    # Keep previously saved bought_key/door_open if present
    bought_key = saveData.get('bought_key', False)
    door_open = saveData.get('door_open', False)

    # Try to get live playtime from the tracker; fall back to saved values
    try:
        minutes, seconds = playtimetracker.tracker.get()
    except Exception:
        try:
            minutes = int(saveData.get('playtime_minutes', 0))
            seconds = int(saveData.get('playtime_seconds', 0))
        except Exception:
            minutes = 0
            seconds = 0

    # Update and persist save data
    saveData['inventory'] = inventory
    saveData['A_echo_taken'] = roomA_echo_taken
    saveData['a_echo_Available'] = roomA_echo_available
    saveData['playtime_minutes'] = minutes
    saveData['playtime_seconds'] = seconds
    saveData['B_frag_Taken'] = roomB_fragment_taken
    saveData['C_hollow_Taken'] = roomC_hollow_taken
    saveData['d_tone_Created'] = roomD_tone_created

    try:
        save.save(saveData)
    except Exception:
        pass

    # Print the saved data for the player
    try:
        save.read()
    except Exception:
        print(saveData)

def floor_two(inventory):
    global ver_pos
    while True:
        if ver_pos == 0:
            choice = cho.four_options(f"{inventory}\nMove up the hall, into the room on your right, or into the room on your left? You can also view your stats", "up", "left", "right", "stats")
            if choice == "up":
                ver_pos += 1
                print("You go up the hall")
                continue
            elif choice == "left":
                print(f"You enter the room on your left.\n{possible_rooms[0]}\n--------------------\nThe walls close in again, and go back out. You feel a pulse as they do.\nIt's as if the room is breathing.")
                if roomA_echo_available and not roomA_echo_taken:
                    pass
                elif not roomA_echo_available:
                    print("You look around the room, it seem squelchy as you walk around. Nothing is here now though.")
                    choice = cho.two_options('Leave?', 'yes', 'no')
                    if choice == 'yes':
                        print('you leave the room')
                        continue
                    else:
                        print("You look around a bit more, still finding nothing.")
                        print('you leave the room')
                        continue
                elif roomA_echo_taken and roomA_echo_available:
                    pass # this will be what happens when the player has the item and still comes back
            elif choice == "right":
                print(f"You enter the room on your right. \n{possible_rooms[3]}")
                continue # work on this one second
            elif choice == 'stats':
                _show_stats(inventory)
                continue
        elif ver_pos == 1:
            choice = cho.four_options("Move down the hall, into the room on your right, or into the room on your left? You can also view your stats", "down", "left", "right", "stats")
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
            elif choice == "stats":
                _show_stats(inventory)
                continue
    