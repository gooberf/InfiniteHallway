import functions.choices as cho
import functions.terminal as term
import time

def main():
    print("You wake up, in a strange builing.")
    time.sleep(1)
    print("You leave the room you woke up in, being greeted by a seemingly endless hallway.")
    time.sleep(1)
    print("You stand there, deciding whether or not to explore the area.")
    cho.two_options("Do you look around?", "Yes", "No")