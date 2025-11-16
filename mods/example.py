import functions.choices as cho
import functions.terminal as term
import functions.splash as splash
import time

splashes = [
    "Oh, so we're playing the example mod now?",
    "Why not play the actual main game, it's better than this mod",
    "You're here to figure out what each function looks like, aren't ya?"
]

def main():
    splash.displaySplash(splashes)
    print("You wake up, in a strange builing.")
    time.sleep(1)
    print("You leave the room you woke up in, being greeted by a seemingly endless hallway.")
    time.sleep(1)
    print("You stand there, deciding whether or not to explore the area.")
    cho.two_options("Do you look around?", "Yes", "No")