import json
import os

def save(data):
    if not os.path.exists('saves'):
        os.makedirs('saves')
    with open('saves/save.json', 'w') as f:
        json.dump(data, f)

def load():
    try:
        with open('saves/save.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return None