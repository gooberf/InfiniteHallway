import time
import pygame

def start(inventory):
    player_inventory = inventory
    pygame.init()
    WIDTH, HEIGHT = 640, 480
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Red Square - WASD movement")
    clock = pygame.time.Clock()

    SQUARE_SIZE = 50
    player = pygame.Rect((WIDTH - SQUARE_SIZE) // 2, (HEIGHT - SQUARE_SIZE) // 2, SQUARE_SIZE, SQUARE_SIZE)
    SPEED = 300  # pixels per second

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
        if keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_s]:
            dy += 1
        if keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_i]:
            print("Using item")
            for item in player_inventory:
                if item == 'rusty_axe':
                    rusty_axe = Item('Rusty Axe', 'A rusty old axe, not very useful.', WIDTH, HEIGHT, SQUARE_SIZE)
                    rusty_axe.use()
                elif item == 'rusted_key':
                    rusted_key = Item('Rusted Key', 'A rusted key, might open something.', WIDTH, HEIGHT, SQUARE_SIZE)
                    rusted_key.use()
        if keys[pygame.K_e] and pygame.Rect.colliderect(player, pygame.Rect((WIDTH - SQUARE_SIZE) // 2, (HEIGHT - SQUARE_SIZE) // 2, SQUARE_SIZE, SQUARE_SIZE)):
            # NOTE / TODO make this when the player is near an item/chest on the floor and E is pressed, it will interact/open it.
            pass
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
        pygame.display.flip()

    pygame.quit()

start(['rusty_axe', 'rusted_key'])