import time
import pygame

def start(inventory, dev):
    if dev == "true":
        print("hello. I don't know what hackr did to make the dev thing work, but uhh... im just gonna make this if anyway. tehe :3")

    player_inventory = inventory
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_i:
                    print("Inventory:", player_inventory)
                elif event.key == pygame.K_a:
                    # move a player to the left
                    pass
                elif event.key == pygame.K_d:
                    # move a player to the right
                    pass
                elif event.key == pygame.K_w:
                    # move a player up
                    pass
                elif event.key == pygame.K_s:
                    # move a player down
                    pass
                elif event.key == pygame.K_e:
                    # interact with things
                    pass


        # Your game logic here

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()