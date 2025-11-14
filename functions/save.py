import json
import os

def save(data):
    if not os.path.exists('saves'):
        os.makedirs('saves')
    with open('saves/save.json', 'w') as f:
        json.dump(data, f)