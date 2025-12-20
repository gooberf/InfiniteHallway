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
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Game logic and drawing goes here
        # Fill the screen with a color (e.g., black)
        screen.fill((0, 0, 0)) # RGB tuple for black
        
        # Update the display
        pygame.display.flip()

    # 5. Quit Pygame
    pygame.quit()