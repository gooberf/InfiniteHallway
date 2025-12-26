import time
import pygame
import random
import game.functions.is_colliding as is_colliding
import getpass

def start(inventory):
    possible_names = ["the hallway never ends", 'there has to be an end', f'goodluck, {getpass.getuser()}', 'heh... youre not escaping']
    print(inventory) if len(inventory) > 0 else print("Inventory is empty.")
    pygame.init()
    WIDTH, HEIGHT = 640, 480
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(random.choice(possible_names))
    clock = pygame.time.Clock()
    chest_opened = False
    SQUARE_SIZE = 50
    player = pygame.Rect((WIDTH - SQUARE_SIZE) // 2, (HEIGHT - SQUARE_SIZE) // 2, SQUARE_SIZE, SQUARE_SIZE)
    SPEED = 500  # pixels per second
    chest = pygame.Rect(100, 100, 40, 40)
    wall_1 = pygame.Rect(200, 150, 300, 20)
    walls = [wall_1]

    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()
        dx = dy = 0

        ## COLLISION DETECTION ##
        colliding_with_chest = player.colliderect(chest)
        
        colliding_with_wall_bottom = is_colliding.bottom(walls, player)
        colliding_with_wall_top = is_colliding.top(walls, player)
        colliding_with_wall_left = is_colliding.left(walls, player)
        colliding_with_wall_right = is_colliding.right()
        #########################
        speed = 1
        
        if keys[pygame.K_w]:
            dy -= 1 if not colliding_with_wall_bottom else 0
        if keys[pygame.K_s]:
            dy += 1 if not colliding_with_wall_top else 0
        if keys[pygame.K_a]:
            dx -= 1 if not colliding_with_wall_right else 0
        if keys[pygame.K_d]:
            dx += 1 if not colliding_with_wall_left else 0
        if keys[pygame.K_e] and colliding_with_chest and not chest_opened:
            inventory.append("Gold Coin")
            chest_opened = True
            print("You got a golden coin!")
        # Normalize diagonal speed
        if dx != 0 and dy != 0:
            inv = 0.70710678
            dx *= inv
            dy *= inv

        player.x += int(dx * SPEED * dt)
        player.y += int(dy * SPEED * dt)

        # Keep inside screen
        player.clamp_ip(screen.get_rect())
        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, (255, 0, 0), player)
        pygame.draw.rect(screen, (255, 255, 0), chest) if not chest_opened else pygame.draw.rect(screen, (100, 100, 0), chest)
        pygame.draw.rect(screen, (100, 100, 100), wall_1)
        pygame.display.flip()
    pygame.quit()

