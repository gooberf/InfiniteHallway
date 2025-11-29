import pygame
import getpass
import time
import webbrowser
import os
import random
import pathlib
from pygame._sdl2 import video
import functions.choices as cho

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
                run = False
            if event.type == pygame.KEYDOWN:
                pass
                    

        screen.fill((0, 0, 0))  # Fill the screen with black color
        pygame.display.flip()  # Update the display