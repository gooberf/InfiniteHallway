import json
import os
import inspect
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


def _detect_mod_from_stack():
    # Inspect the call stack to determine if caller is inside a mod folder
    for frame_info in inspect.stack():
        fn = frame_info.filename
        parts = fn.replace('\\', '/').split('/')
        if 'mods' in parts:
            idx = parts.index('mods')
            if idx + 1 < len(parts):
                return parts[idx + 1]
    return None


def save(data, mod=None, slot=1):
    """Save data. If `mod` is provided or detected, save under that mod's folder."""
    target_mod = mod if mod is not None else _detect_mod_from_stack()
    if target_mod:
        saves_dir = os.path.join('mods', target_mod, 'saves')
        # format slot as two-digit number
        # save_file = os.path.join(saves_dir, '01.infsav')
        save_file = os.path.join(saves_dir, "01.infsav")
    else:
        saves_dir = SAVES_DIR
        save_file = SAVE_FILE

    if not os.path.exists(saves_dir):
        os.makedirs(saves_dir)
    with open(save_file, 'wb') as f:
        # Build header bytes safely: ensure iteration is string and encoded to bytes
        iteration = getinfo("saveIteration")
        iteration_bytes = str(iteration if iteration is not None else "").encode('utf-8')
        f.write(b"InfiniteHallway Save Iteration" + iteration_bytes)  # magic header
        pickle.dump(data, f)

def load(mod=None, slot=1):
    """Load save data. If `mod` provided or detected, loads that mod's save."""
    target_mod = mod if mod is not None else _detect_mod_from_stack()
    if target_mod:
        save_file = os.path.join('mods', target_mod, 'saves', '01.infsav')
    else:
        save_file = SAVE_FILE

    try:
        with open(save_file, 'rb') as f:
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
    
def convert_save_to_json(mod=None, slot=1):
    try:
        target_mod = mod if mod is not None else _detect_mod_from_stack()
        if target_mod:
            save_file = os.path.join('mods', target_mod, 'saves', '01.infsav')
            json_save_file = os.path.join('mods', target_mod, 'saves', 'save.json')
        else:
            save_file = SAVE_FILE
            json_save_file = os.path.join(SAVES_DIR, 'save.json')

        with open(save_file, 'rb') as f:
            # Read header
            iteration = getinfo("saveIteration")
            iteration_bytes = str(iteration if iteration is not None else "").encode('utf-8')
            header_len = len(b"InfiniteHallway Save Iteration") + len(iteration_bytes)
            f.read(header_len)
            data = pickle.load(f)

        with open(json_save_file, 'w') as jf:
            json.dump(data, jf, indent=4)
        print(f"Save converted to JSON format at {json_save_file}")
    except Exception as e:
        print(f"Failed to convert save: {e}")
    
def load_legacy(mod=None):
    """Load an old JSON save.

    If `mod` is provided, look inside that mod's folder. Otherwise check project root then mod folders.
    Returns the legacy inventory list (for compatibility with callers) or an empty list.
    """
    # Determine project root (parent of the directory that contains this module's parent)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Helper to try a path and return inventory if found
    def _try_load(path):
        try:
            with open(path, 'r') as f:
                data = json.load(f)
            # If legacy save is a dict with inventory, return that list; if it's a list, return it
            if isinstance(data, dict) and 'inventory' in data:
                return data['inventory']
            if isinstance(data, list):
                return data
            return []
        except Exception:
            return None

    # If a specific mod requested, check mod-specific save locations
    if mod:
        candidates = [
            os.path.join('mods', mod, 'save.json'),
            os.path.join('mods', mod, 'saves', 'save.json'),
        ]
        for c in candidates:
            inv = _try_load(c)
            if inv is not None:
                return inv
        return []

    # Check project root first
    root_candidate = os.path.join(project_root, 'save.json')
    inv = _try_load(root_candidate)
    if inv is not None:
        return inv

    # Scan mods for legacy save.json
    mods_dir = os.path.join(project_root, 'mods')
    if os.path.isdir(mods_dir):
        for entry in os.listdir(mods_dir):
            mod_path = os.path.join(mods_dir, entry)
            if os.path.isdir(mod_path):
                for candidate in ('save.json', os.path.join('saves', 'save.json')):
                    c = os.path.join(mod_path, candidate)
                    inv = _try_load(c)
                    if inv is not None:
                        return inv

    # Not found
    return []

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