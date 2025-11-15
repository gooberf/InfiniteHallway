import random
import functions.clear_terminal as terminal
import time
import datetime
from datetime import datetime

today = datetime.now()

todayWeek = today.weekday()

day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


splashTexts = [
            "The hallway fills you with DETERMINATION", 
            "is that a suspiCiously human shaped ceiLing DDecoration", 
            "One of these splash texts have a secret...", 
            "This code is actually really unoptimized.",
            "hackr was here",
            "I gently open the door.",
            "developed by two idiots making a game",
            "https://twitch.tv/hackrxd",
            "Ren'Py version coming never",
            "Developed with anything but pygame",
            "An entire file was made for these splash texts",
            "null",
            "The door was gently opened.",
            "Why did I add artificial waiting to start.py",
            "Developed with way too many functions",
            "Saving was a little complicated",
            'Traceback (most recent call last):\n  File "main.py", line 126, in <module>\n    inventory = f2.floor_two(inventory)\nNameError: name \'f2\' is not defined\n\nRuntimeError: hackr broke something again\n',
            "issues",
            "Why develop a game when you can write yet another function... oh wait, it's part of the game",
            "This is the 20th splash text.",
            f"Are you having a nice {day_names[todayWeek]}?"
            ]

def displaySplash():
    terminal.clear()
    splash = random.choice(splashTexts)
    print(splash)
    time.sleep(3)