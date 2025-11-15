import json
import os
import functions.choices as choose

def save(data):
    jsonData = {
        'inventory': data['inventory'],
        'bought_key': data['bought_key'],
        'door_open': data['door_open']
    }
    
    #if not os.path.exists('saves'):
    #    os.makedirs('saves')
    while True:
        try:
            with open('saves/save.json', 'w') as f:
                if not os.path.exists('saves/save.json'):
                    os.mkdir('saves')
                json.dump(data, f)
        except KeyboardInterrupt:
            choose.two_options("You're still saving! Are you sure you want to quit?", "yes", "no")

def load():
    try:
        with open('saves/save.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        # Return default save data structure
        return {
            'inventory': [],
            'bought_key': False,
            'door_open': False
        }