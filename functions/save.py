import json
import os
import functions.choices as choose

def save(data):
    jsonData = {
        'inventory': data['inventory'],
        'current_room': data['current_room'],
        'floor': data['floor']
    }
    
    #if not os.path.exists('saves'):
    #    os.makedirs('saves')
    while True:
        try:
            with open('saves/save.json', 'w') as f:
                json.dump(data, f)
        except KeyboardInterrupt:
            choose.two_options("You're still saving! Are you sure you want to quit?", "yes", "no")

def load():
    try:
        with open('saves/save.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return None