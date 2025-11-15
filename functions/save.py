import json
import os

# Get the base directory of the project (parent of functions folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAVES_DIR = os.path.join(BASE_DIR, 'saves')
SAVE_FILE = os.path.join(SAVES_DIR, 'save.json')

def save(data):
    if not os.path.exists(SAVES_DIR):
        os.makedirs(SAVES_DIR)
    with open(SAVE_FILE, 'w') as f:
        json.dump(data, f)

def load():
    try:
        with open(SAVE_FILE, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        # Return default save data structure
        return {
            'inventory': [],
            'bought_key': False,
            'door_open': False
        }
def read():
    with open(SAVE_FILE, 'r') as f:
        data = json.load(f)
        print(data)