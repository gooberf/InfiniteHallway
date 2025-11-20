import functions.choices as cho
import functions.terminal as term
import functions.splash as splashFunc
import time

splashes = [
    "Oh, so we're playing the example mod now?",
    "Why not play the actual main game, it's better than this mod",
    "You're here to figure out what each function looks like, aren't ya?"
]

def splash():
    splashFunc.displaySplash(splashes)

def main():
    print("You wake up, in a strange builing.")
    time.sleep(1)
    print("You leave the room you woke up in, being greeted by a seemingly endless hallway.")
    time.sleep(1)
    print("You stand there, deciding whether or not to explore the area.")
    look = cho.two_options("Do you look around?", "Yes", "No")
    if look == "Yes":
        print("You decide to look around and explore more.")
    if look == "No":
        print("You decide not to look around, returning back to the room.")
        time.sleep(1)
        print("After a few hours, you left the room in a need for food.")
    time.sleep(1)
    print("You begin walking down the hallway, it never seems to end.")
    time.sleep(1)
    print("You walk up to one of the many doors.")
    opendr = cho.two_options("Do you open the door?", "yes", "no")
    if opendr == "yes":
        print("You carefully reach for the doorknob.")
        time.sleep(1)
        print("You open the door, revealing a-")
        term.logTraceback("Hm.. how do I fix this..? Do I continue writing the example mod, or am I too tired from writing modding docs? We will never know. If you were actually interested in learing the modding for this game, just read modding.md")
        exit()