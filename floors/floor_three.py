import pygame

# 1. Initialize Pygame
def start(inventory):
    pygame.init()

    # 2. Set the width and height of the screen (e.g., 800x600 pixels)
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))

    # 3. Set the window title (optional)
    pygame.display.set_caption("???")

    # 4. Game loop
    running = True
    while running:
        print("???")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_f:
                    print("HAHA DEVELOPED WITH PYGAME COULDN'T HAVE SEEN THIS COMING!!!")
                    running = False

        # Game logic and drawing goes here
        # Fill the screen with a color (e.g., black)
        screen.fill((0, 0, 0)) # RGB tuple for black
        
        # Update the display
        pygame.display.flip()

    # 5. Quit Pygame
    pygame.quit()
