import random
import functions.terminal as terminal
import time
import datetime
from datetime import datetime
import os
import traceback
import rich
from rich.console import Console
from colorama import Fore, Style
import colorama

# Initialize colorama
colorama.init(autoreset=True)

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
            "Please back up floor_one.py, you'll never know when you'll need it ;)",
            "This game was tested on actual humans. Results may vary.",
            "Floor three coming soon... maybe.",
            "Breaking news: Hallways still infinite.",
            "Warning: May contain traces of code.",
            "Powered by hopes and dreams (and Python).",
            "In case of emergency, press Ctrl+C repeatedly.",
            "This game has been rated E for 'Endless Hallways'.",
            "This game was made by pressing buttons until something happened.",
            "Infinite Hallway: More hallway than you can shake a stick at.",
            "Please rate this game 5 stars... wait, where do you rate games?",
            "The merchant's real name is Bob. Bob the Python script.",
            "This splash text is self-aware. Send help.",
            "Infinite Hallway: The game that answers 'What if hallways?'"
            ]

def displaySplash(splashes=[]):
    terminal.clear()
    if splashes == []:
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
                try: terminal.print_traceback("hackr broke something again")
                except:
                        console.print_exception(show_locals=True)
              else:
                    print(f"{Fore.MAGENTA}{Style.BRIGHT}{splash}{Style.RESET_ALL}")
    else:
        splash = random.choice(splashes)
        print(f"{Fore.MAGENTA}{Style.BRIGHT}{splash}{Style.RESET_ALL}")
    time.sleep(3)
    terminal.clear()
