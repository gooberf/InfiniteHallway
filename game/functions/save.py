import json
import os
import game.functions.playtimetracker as playtimetracker
from colorama import Fore, Style
import pickle

# Get the base directory of the project (parent of functions folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SAVES_DIR = os.path.join(BASE_DIR, 'data/saves')
SAVES_DIR = 'data/saves'
SAVE_FILE = os.path.join(SAVES_DIR, '01.infsav')

def getinfo(peram):
    """Retrieve information from game/info.json"""
    info_file = os.path.join(BASE_DIR, 'game', 'info.json')
    try:
        with open(info_file, 'r') as f:
            info = json.load(f)
        return info.get(peram, None)
    except Exception:
        return None


def save(data):
    if not os.path.exists(SAVES_DIR):
        os.makedirs(SAVES_DIR)
    with open(SAVE_FILE, 'wb') as f:
        # Build header bytes safely: ensure iteration is string and encoded to bytes
        iteration = getinfo("saveIteration")
        iteration_bytes = str(iteration if iteration is not None else "").encode('utf-8')
        f.write(b"InfiniteHallway Save Iteration" + iteration_bytes)  # magic header
        pickle.dump(data, f)

def load():
    try:
        with open(SAVE_FILE, 'rb') as f:
            # Read the same number of bytes as written for the header
            iteration = getinfo("saveIteration")
            iteration_bytes = str(iteration if iteration is not None else "").encode('utf-8')
            header_len = len(b"InfiniteHallway Save Iteration") + len(iteration_bytes)
            header = f.read(header_len)
            if header != b"InfiniteHallway Save Iteration" + iteration_bytes:
                raise ValueError("Invalid save file")
            data = pickle.load(f)
        return data
    except FileNotFoundError:
        return {
            'inventory': [],
            'bought_key': False,
            'door_open': False,
            'floor': 1
        }
    
def display_stats(inventory=None):
    """
    Display formatted player statistics.
    If inventory is provided, it will be included in the stats and saved.
    """
    # Load save data
    try:
        saveData = load()
    except Exception:
        saveData = {'inventory': [], 'bought_key': False, 'door_open': False}
    
    # Update inventory if provided
    if inventory is not None:
        saveData['inventory'] = inventory
    
    # Get playtime - try live tracker first, then saved values
    try:
        minutes, seconds = playtimetracker.tracker.get()
    except Exception:
        try:
            minutes = int(saveData.get('playtime_minutes', 0))
            seconds = int(saveData.get('playtime_seconds', 0))
        except Exception:
            minutes = 0
            seconds = 0
    
    # Update save data with current playtime
    saveData['playtime_minutes'] = minutes
    saveData['playtime_seconds'] = seconds
    
    # Save updated data
    try:
        save(saveData)
    except Exception:
        pass
    
    # Format and display stats
    print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}PLAYER STATISTICS{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
    
    # Inventory display
    inv = saveData.get('inventory', [])
    if inv:
        print(f"{Fore.YELLOW}Inventory ({len(inv)} items):{Style.RESET_ALL}")
        for i, item in enumerate(inv, 1):
            print(f"  {Fore.GREEN}{i}. {item}{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}Inventory: {Fore.RED}Empty{Style.RESET_ALL}")
    
    print()
    
    # Progress display
    if saveData["floor"] == 1:
        bought_key = saveData.get('bought_key', False)
        door_open = saveData.get('door_open', False)
        print(f"{Fore.YELLOW}Progress:{Style.RESET_ALL}")
        print(f"  Key purchased: {Fore.GREEN if bought_key else Fore.RED}{'Yes' if bought_key else 'No'}{Style.RESET_ALL}")
        print(f"  Door opened: {Fore.GREEN if door_open else Fore.RED}{'Yes' if door_open else 'No'}{Style.RESET_ALL}")
    
    # Floor 2 progress (if exists)
    if saveData['floor'] == 2:
        print(f"{Fore.YELLOW}  Floor 2 Items:{Style.RESET_ALL}")
        if saveData.get('A_echo_taken'):
            print(f"    {Fore.GREEN}- Echo (taken){Style.RESET_ALL}")
        if saveData.get('B_frag_Taken'):
            print(f"    {Fore.GREEN}- Fragment (taken){Style.RESET_ALL}")
        if saveData.get('C_hollow_Taken'):
            print(f"    {Fore.GREEN}- Hollow (taken){Style.RESET_ALL}")
        if saveData.get('d_tone_Created'):
            print(f"    {Fore.GREEN}- Tone (created){Style.RESET_ALL}")
    
    print()
    
    # Playtime display
    total_seconds = minutes * 60 + seconds
    hours = total_seconds // 3600
    mins = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    
    if hours > 0:
        print(f"{Fore.CYAN}Playtime: {Fore.WHITE}{hours}h {mins}m {secs}s{Style.RESET_ALL}")
    else:
        print(f"{Fore.CYAN}Playtime: {Fore.WHITE}{mins}m {secs}s{Style.RESET_ALL}")
    
    print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
    
def migrate_save():
    """Migrate old JSON save to new pickle format."""
    old_save_file = os.path.join(SAVES_DIR, 'save.json')
    if os.path.exists(old_save_file):
        with open(old_save_file, 'r') as f:
            data = json.load(f)
        save(data)
        os.remove(old_save_file)