import os
import json
from rich import print
import importlib
import sys
import game.functions.splash as splash
from game.functions.choices import two_options

splashes = []

def scan():
    mods = []
    for i in os.listdir('mods'):
        if os.path.isdir(f'mods/{i}'):
            if not os.path.basename(f"mods/{i}") == "__pycache__":
                mods.append(mods.append(i))
    for i in mods:
        if not os.path.exists(f"mods/{i}/main.py"):
            mods.remove(i)
    return mods

def info(mod):
    try:
        with open(f"mods/{mod}/info.json", 'r') as f:
            global splashes
            data = json.load(f)
            name = data["name"]
            creator = data["creator"]
            description = data['description'] if 'description' in data else "No description provided."
            dependancies = data["requirements"]
            try:
                with open(f'mods/{mod}/splashes.txt', "r") as sf:
                    splashes = sf.readlines()
            except FileNotFoundError:
                splashes = None
            missingRequirements = []
            if not dependancies == []:
                for i in dependancies:
                    try:
                        importlib.import_module(i)
                    except:
                        missingRequirements.append(i)
            if not missingRequirements == []:
                choice = two_options("The mod was successfully found, but could not be loaded due to missing dependancies listed by the creator.\nWould you like to try and install these?", "yes", "no")
                if choice == "yes":
                    pip_cmd = input("What does your system use for pip? Default: \"pip\"\n")
                    if pip_cmd == "":
                        pip_cmd = "pip"
                    reqString = " ".join(missingRequirements)
                    os.system(f"{pip_cmd} install {reqString}")
                    print("All installs attempted. Restarting...")
                    from main import start
                    start()
            print(f"{name}\n-----------------------\n[blue]Developer: {creator}\n\n[yellow]Description:\n[white]{description}\n\n[green]ID: {mod}\n\nPackages used:\n")
            for i, dependency in enumerate(dependancies, 1):
                print(f"[blue]{i}. {dependency}")
    except FileNotFoundError:
        print("There was an error loading this mods's information, so we will choose not to load it")

def load(mod):
    print("Attempting to load mod...")
    try:
        modimport = importlib.import_module(f"mods.{mod}.main")
        if not splashes == None:
            splash.displaySplash(splashes)
        else:
            splash.displaySplash()
        modimport.main()
    except Exception as e:
        print(f"Failed to load mod: {e}")