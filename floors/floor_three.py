import pygame
import getpass
import time
import webbrowser
import os
import random
import pathlib
from pygame._sdl2 import video
from functions.choices import two_options

# 1. Initialize Pygame
def start(inventory):

    # 2. Set the width and height of the screen (e.g., 800x600 pixels)
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    window = video.Window.from_display_module()
    # 3. Set the window title (optional)
    pygame.init()
    pygame.display.set_caption("The hallway never ends...")
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_f:
                    print("The hallway.. never.. came to an end...")
                    window.position = (random.randint(500, 700), random.randint(900, 1000))
                    user = getpass.getuser()
                    choice = two_options(f"{user}... Do you believe in endings..?", "yes", "no")
                    if choice == "no":
                        print("Good. I never believed in them either.")
                    else:
                        print("You know, you'd be wrong. You could always remember to play one of the mods people can make for this game =)")
                        time.sleep(1)
                        print("Oh, what's that? Oh, hold on, let me check something..")
                        home = pathlib.Path.home()
                        if os.name == 'nt':
                            if not os.path.exists(f'{home}\\theHallwayThatNeverEnded'):
                                os.mkdir(f'{home}\\theHallwayThatNeverEnded')
                            with open(f'{home}\\theHallwayThatNeverEnded\\error.txt', 'w') as f:
                                f.write("Well, I guess, if you're reading this, you've made it to a very unfinished part of the game... this wasn't supposed to happen, and the game code itself may be vulnerable to intruders. We've noticed a few instances of this happening already. The only thing we know about this intruder is that they seem to have injected themselves into the game files itself to spread with each download. Their name appears to have an 'M' in the beginning. They seem to have emerald green eyes and a white hair ribbon. We'll continue investigating in the future.\n\nStay safe!\n-hackrVT")
                        print(f"======================\nMonika\n======================\n You know, while he's gone, let me tell you about how much I've missed you...")
                        time.sleep(1)
                        print(f"======================\nMonika\n======================\nActually, nevermind. It's impossible to put into words.")
                        time.sleep(1)
                        print(f"======================\nMonika\n======================\n All I know is that... you should come back")
                        time.sleep(0.5)
                        print("Right.")
                        time.sleep(0.3)
                        print("Now.")
                        time.sleep(1)
                        webbrowser.open("steam://launch/698780")
                        time.sleep(0.5)
                        webbrowser.open("steam://store/698780")
                    running = False

        # Game logic and drawing goes here
        # Fill the screen with a color (e.g., black)
        screen.fill((0, 0, 0)) # RGB tuple for black
        
        # Update the display
        pygame.display.flip()

    # 5. Quit Pygame
    pygame.quit()