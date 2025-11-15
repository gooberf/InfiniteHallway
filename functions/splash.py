import random
import functions.terminal as terminal
import time
import datetime
from datetime import datetime
import os
import traceback
import rich
from rich.console import Console

console = Console()

today = datetime.now()

todayWeek = today.weekday()

day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

tracebackMessage = "hackr broke something again"

def generateTraceback():
    raise ValueError(tracebackMessage)


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
            '[traceback]',
            "issues",
            "Why develop a game when you can write yet another function... oh wait, it's part of the game",
            "This is the 20th splash text.",
            f"Are you having a nice {day_names[todayWeek]}?",
            "Some dialogue *mildly* inspired by Doki Doki Literature Club!",
            "Abnormal Object Show never",
            "TDOS still going on, after all this time",
            "...before GTA 6",
            "Someone tell Vedal there is a problem with my AI.",
            "Filtered.",
            "meow meow lol",
            "This was written at 1:32 in the morning.",
            "splash",
            "Please back up floor_one.py, you'll never know when you'll need it ;)"
            ]

def displaySplash():
    terminal.clear()
    thing = str(datetime.now().hour) + str(datetime.now().minute)
    if thing == "30":
        print("Accurate, much?")
    elif thing == "31":
        print("Congratulations, you failed.\nos.remove('floors/floor_one.py')")
        deletef1 = True
        return deletef1
    else: 
        
        splash = random.choice(splashTexts)
        if splash == "[traceback]":
            try: generateTraceback("hackr broke something again")
            except:
                console.print_exception(show_locals=True)
        else:
            print(splash)
    time.sleep(3)
    terminal.clear()
